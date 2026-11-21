import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import lab  # noqa: E402


class ConditionTests(unittest.TestCase):
    def test_precedence_and_not(self):
        r = {"a": True, "b": False, "c": True}
        self.assertTrue(lab.evaluate_condition("a and not b", r))
        self.assertFalse(lab.evaluate_condition("a and not (b or c)", r))
        self.assertTrue(lab.evaluate_condition("b or a and c", r))

    def test_rejects_unknown_selection_and_garbage(self):
        with self.assertRaises(ValueError):
            lab.evaluate_condition("a and zzz", {"a": True})
        with self.assertRaises(ValueError):
            lab.evaluate_condition("a and", {"a": True})
        with self.assertRaises(ValueError):
            lab.evaluate_condition("(a", {"a": True})

    def test_operators(self):
        self.assertTrue(lab.selection_matches({"x|contains": "ab"}, {"x": "xABy"}))
        self.assertTrue(lab.selection_matches({"x|endswith": "$"}, {"x": "DC1$"}))
        self.assertTrue(lab.selection_matches({"x": ["a", "b"]}, {"x": "B"}))
        self.assertFalse(lab.selection_matches({"x": "a"}, {}))
        self.assertTrue(lab.selection_matches({"x|exists": False}, {}))
        self.assertTrue(lab.selection_matches({"x|contains": "m"}, {"x": ["mail", "z"]}))


class RuleContract(unittest.TestCase):
    def test_missing_required_field_is_degraded_not_no_match(self):
        rule = {"required_fields": ["a"], "selections": {"s": {"a": "1"}}, "condition": "s"}
        self.assertEqual(lab.evaluate(rule, {}), "degraded")
        self.assertEqual(lab.evaluate(rule, {"a": "1"}), "match")
        self.assertEqual(lab.evaluate(rule, {"a": "2"}), "no_match")

    def test_check_rule_requires_telemetry_contract(self):
        rule = {"id": "x", "title": "t", "case": "c", "required_fields": [], "selections": {"s": {"a": 1}}, "condition": "s"}
        self.assertTrue(any("required_fields" in e for e in lab.check_rule(rule)))


class LabCases(unittest.TestCase):
    def test_there_are_cases(self):
        self.assertGreaterEqual(len(lab.cases()), 3)

    def test_every_case_has_all_fixture_classes(self):
        for name in lab.cases():
            rule, fixtures = lab.load_case(name)
            self.assertEqual(lab.check_rule(rule), [], name)
            self.assertTrue((ROOT / rule["case"]).exists(), f"{name}: case documental ausente")
            classes = {f["class"] for f in fixtures}
            self.assertEqual(classes, {"positive", "variant", "benign", "degraded"}, name)
            for f in fixtures:
                self.assertIn(f["expect"], lab.OUTCOMES)

    def test_every_fixture_behaves_as_declared(self):
        for name in lab.cases():
            report = lab.run_case(name)
            self.assertEqual(report["failures"], [], name)
            self.assertEqual(report["fn"], 0, name)
            self.assertEqual(report["fp"], 0, name)


if __name__ == "__main__":
    unittest.main()
