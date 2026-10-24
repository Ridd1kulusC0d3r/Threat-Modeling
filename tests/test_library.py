import copy
import re
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_readme  # noqa: E402
import check_links  # noqa: E402
import common  # noqa: E402
import query  # noqa: E402
import validate  # noqa: E402

RES = common.resources()
METHODS = common.methods()
IDS = {r["id"] for r in RES}


def good() -> dict:
    return copy.deepcopy(next(r for r in RES if r["id"] == "holmes"))


class DataTests(unittest.TestCase):
    def test_resources_validate(self):
        self.assertEqual(validate.check_resources(RES), [])

    def test_methods_validate(self):
        self.assertEqual(validate.check_methods(METHODS, IDS), [])

    def test_schema_enums_match_code(self):
        import json

        schema = json.loads((ROOT / "schemas/resource.schema.json").read_text(encoding="utf-8"))["properties"]
        self.assertEqual(schema["type"]["enum"], list(common.TYPES))
        self.assertEqual(schema["grade"]["enum"], list(common.GRADES))
        self.assertEqual(schema["access"]["enum"], list(common.ACCESS))
        self.assertEqual(schema["topics"]["items"]["enum"], list(common.TOPICS))
        method = json.loads((ROOT / "schemas/method.schema.json").read_text(encoding="utf-8"))["properties"]
        self.assertEqual(method["status"]["enum"], list(common.METHOD_STATUS))

    def test_hand_written_docs_use_only_catalogued_urls(self):
        known = {r["url"] for r in RES}
        link = re.compile(r"^\|\s*\[[^\]]+\]\((https?://[^)]+)\)")
        for name in ("BIBLIOGRAFIA", "ENGENHARIA-DE-DETECCAO", "CONFERENCIAS", "CATALOGO"):
            for line in (ROOT / "docs" / f"{name}.md").read_text(encoding="utf-8").splitlines():
                m = link.match(line)
                if m:
                    self.assertIn(m.group(1), known, f"{name}: {m.group(1)} não está em data/resources.json")

    def test_legacy_items_never_featured(self):
        for r in RES:
            if r["grade"] in {"D", "E"}:
                self.assertFalse(r["featured"], r["id"])

    def test_checked_only_with_valid_date(self):
        for r in RES:
            if r.get("checked") is not None:
                self.assertTrue(validate.valid_date(r["checked"]), r["id"])


class ValidatorRejects(unittest.TestCase):
    def fails(self, mutate, needle):
        item = good()
        mutate(item)
        errors = validate.check_resources([item])
        self.assertTrue(any(needle in e for e in errors), errors)

    def test_missing_limit(self):
        self.fails(lambda i: i.__setitem__("limit", " "), "limit vazio")

    def test_bad_grade(self):
        self.fails(lambda i: i.__setitem__("grade", "Z"), "grade")

    def test_http_url(self):
        self.fails(lambda i: i.__setitem__("url", "http://example.com/x"), "https")

    def test_unknown_topic(self):
        self.fails(lambda i: i.__setitem__("topics", ["nope"]), "topics desconhecidos")

    def test_unknown_field(self):
        self.fails(lambda i: i.__setitem__("rating", 5), "campos desconhecidos")

    def test_featured_grade_e(self):
        self.fails(lambda i: i.update(grade="E", featured=True), "destaque")

    def test_bad_checked_date(self):
        self.fails(lambda i: i.__setitem__("checked", "ontem"), "checked")

    def test_duplicate_id_and_url(self):
        a, b = good(), good()
        errors = validate.check_resources([a, b])
        self.assertTrue(any("id duplicado" in e for e in errors))
        self.assertTrue(any("url repetida" in e for e in errors))

    def test_method_with_unknown_resource(self):
        method = copy.deepcopy(METHODS[0])
        method["resources"] = ["does-not-exist"]
        self.assertTrue(any("não existe" in e for e in validate.check_methods([method], IDS)))

    def test_method_without_sources(self):
        method = copy.deepcopy(METHODS[0])
        method["resources"] = []
        self.assertTrue(validate.check_methods([method], IDS))


class GeneratedFiles(unittest.TestCase):
    def test_generated_files_are_current(self):
        proc = mock.Mock()
        with mock.patch.object(sys, "argv", ["build_readme", "--check"]):
            self.assertEqual(build_readme.main(), 0, proc)

    def test_anchor_matches_github_style(self):
        self.assertEqual(build_readme.anchor("Inteligência de ameaças (CTI)"), "inteligência-de-ameaças-cti")
        self.assertEqual(build_readme.anchor("Métodos e modelos"), "métodos-e-modelos")

    def test_topic_links_point_to_real_headings(self):
        topics_md = (ROOT / "docs/TEMAS.md").read_text(encoding="utf-8")
        headings = {build_readme.anchor(h) for h in re.findall(r"^## (.+)$", topics_md, re.M)}
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for target in re.findall(r"\(docs/TEMAS\.md#([^)]+)\)", readme):
            self.assertIn(target, headings)

    def test_method_links_point_to_real_headings(self):
        methods_md = (ROOT / "docs/METODOS.md").read_text(encoding="utf-8")
        headings = {build_readme.anchor(h) for h in re.findall(r"^## (.+)$", methods_md, re.M)}
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for target in re.findall(r"\(docs/METODOS\.md#([^)]+)\)", readme):
            self.assertIn(target, headings)


class QueryTests(unittest.TestCase):
    def test_search_uses_word_prefixes_not_substrings(self):
        hits = query.search(RES, "apt")
        self.assertTrue(hits)
        for item in hits:
            self.assertRegex(query.haystack(item), r"\bapt")

    def test_search_requires_all_terms(self):
        self.assertTrue(query.search(RES, "apt provenance"))
        self.assertEqual(query.search(RES, "apt zzzznotaword"), [])


class LinkClassification(unittest.TestCase):
    def http_error(self, code):
        return urllib.error.HTTPError("https://x", code, "err", {}, None)

    def test_ok(self):
        response = mock.MagicMock()
        response.__enter__.return_value.status = 200
        with mock.patch("urllib.request.urlopen", return_value=response):
            self.assertEqual(check_links.probe("https://x", 1), ("ok", "200"))

    def test_blocked_is_not_broken(self):
        with mock.patch("urllib.request.urlopen", side_effect=self.http_error(403)):
            self.assertEqual(check_links.probe("https://x", 1)[0], "blocked")

    def test_404_is_broken(self):
        with mock.patch("urllib.request.urlopen", side_effect=self.http_error(404)):
            self.assertEqual(check_links.probe("https://x", 1)[0], "broken")

    def test_network_failure_is_unreachable_not_broken(self):
        with mock.patch("urllib.request.urlopen", side_effect=urllib.error.URLError("dns")):
            self.assertEqual(check_links.probe("https://x", 1)[0], "unreachable")


if __name__ == "__main__":
    unittest.main()
