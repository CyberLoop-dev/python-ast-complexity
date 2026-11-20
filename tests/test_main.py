import unittest
from main import analyze_source

class Tests(unittest.TestCase):
    def test_simple_function(self):
        result = analyze_source("def greet(name):\n    return name\n")
        self.assertEqual(result[0]["complexity"], 1)
        self.assertEqual(result[0]["level"], "low")
    def test_branches_and_boolean_operators(self):
        source = "def check(a, b):\n    if a and b:\n        return True\n    return False\n"
        self.assertEqual(analyze_source(source)[0]["complexity"], 3)
    def test_nested_function_is_reported_separately(self):
        source = "def outer():\n    def inner(x):\n        if x:\n            return 1\n        return 0\n    return inner(1)\n"
        result = analyze_source(source)
        self.assertEqual(len(result), 2)
        outer = next(item for item in result if item["name"] == "outer")
        inner = next(item for item in result if item["name"] == "inner")
        self.assertEqual(outer["complexity"], 1)
        self.assertEqual(inner["complexity"], 2)
    def test_syntax_error_is_not_silently_ignored(self):
        with self.assertRaises(SyntaxError):
            analyze_source("def broken(:\n")

if __name__ == "__main__":
    unittest.main()
