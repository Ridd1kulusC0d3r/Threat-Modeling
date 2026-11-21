import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common  # noqa: E402
import ingest_feeds  # noqa: E402
import validate  # noqa: E402

OPML = """<?xml version="1.0"?><opml version="2.0"><body>
<outline text="osint"><outline type="rss" xmlUrl="https://blog.example.org/feed.xml" text="x"/></outline>
<outline text="cti"><outline type="rss" xmlUrl="https://attack.mitre.org/feed.xml" text="y"/></outline>
</body></opml>"""

NOW = datetime.now(timezone.utc)


def rss(items):
    body = "".join(
        f"<item><title>{t}</title><link>{u}</link><description>{d}</description><pubDate>{p}</pubDate></item>"
        for t, u, d, p in items
    )
    return f"<rss><channel><title>Blog Exemplo</title>{body}</channel></rss>".encode()


def stamp(days_ago):
    from email.utils import format_datetime

    return format_datetime(NOW - timedelta(days=days_ago))


class IngestTests(unittest.TestCase):
    def test_opml_categories_and_new_domains(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "f.opml"
            path.write_text(OPML, encoding="utf-8")
            feeds = ingest_feeds.read_opml(path)
        self.assertEqual([(f["category"], f["url"]) for f in feeds][0], ("osint", "https://blog.example.org/feed.xml"))
        fresh = ingest_feeds.new_domains(feeds, {"https://attack.mitre.org/x"})
        self.assertEqual(list(fresh), ["blog.example.org"])

    def test_candidates_are_valid_filtered_and_deduplicated(self):
        data = rss(
            [
                ("OSINT geolocation: um estudo", "https://blog.example.org/a", "<p>passo a passo</p>", stamp(3)),
                ("Receita de bolo", "https://blog.example.org/b", "nada a ver", stamp(3)),
                ("OSINT antigo", "https://blog.example.org/c", "osint", stamp(400)),
                ("OSINT sem https", "http://blog.example.org/d", "osint", stamp(1)),
            ]
        )
        feeds = [{"url": "https://blog.example.org/feed.xml", "category": "osint", "title": ""}]
        with mock.patch.object(ingest_feeds, "fetch", return_value=data):
            out = ingest_feeds.collect(feeds, ["osint"], [], 30, date.today(), common.resources())
        self.assertEqual([c["url"] for c in out], ["https://blog.example.org/a"])
        self.assertEqual(out[0]["grade"], "D")
        self.assertFalse(out[0]["featured"])
        self.assertEqual(validate.check_resources(out), [])
        self.assertEqual(out[0]["authors"], "Blog Exemplo")

    def test_existing_url_is_skipped(self):
        known = common.resources()[0]
        data = rss([("OSINT algo", known["url"], "osint", stamp(1))])
        feeds = [{"url": "https://blog.example.org/feed.xml", "category": "", "title": ""}]
        with mock.patch.object(ingest_feeds, "fetch", return_value=data):
            out = ingest_feeds.collect(feeds, ["osint"], [], 30, date.today(), common.resources())
        self.assertEqual(out, [])

    def test_slug(self):
        self.assertEqual(ingest_feeds.slug("Ameaças: O Que é APT?"), "ameacas-o-que-e-apt")


if __name__ == "__main__":
    unittest.main()
