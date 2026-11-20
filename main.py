#!/usr/bin/env python3
"""Report per-function cyclomatic complexity using Python AST only."""
import argparse
import ast
import json
from pathlib import Path

class FunctionCollector(ast.NodeVisitor):
    def __init__(self):
        self.functions = []
    def visit_FunctionDef(self, node):
        self.functions.append(node)
        self.generic_visit(node)
    def visit_AsyncFunctionDef(self, node):
        self.functions.append(node)
        self.generic_visit(node)

class BranchCounter(ast.NodeVisitor):
    def __init__(self):
        self.branches = 0
    def visit_FunctionDef(self, node):
        return
    def visit_AsyncFunctionDef(self, node):
        return
    def visit_Lambda(self, node):
        return
    def visit_If(self, node):
        self.branches += 1
        self.generic_visit(node)
    def visit_For(self, node):
        self.branches += 1
        self.generic_visit(node)
    def visit_AsyncFor(self, node):
        self.branches += 1
        self.generic_visit(node)
    def visit_While(self, node):
        self.branches += 1
        self.generic_visit(node)
    def visit_ExceptHandler(self, node):
        self.branches += 1
        self.generic_visit(node)
    def visit_IfExp(self, node):
        self.branches += 1
        self.generic_visit(node)
    def visit_BoolOp(self, node):
        self.branches += max(0, len(node.values) - 1)
        self.generic_visit(node)
    def visit_Match(self, node):
        self.branches += len(node.cases)
        self.generic_visit(node)

def analyze_source(source, filename="<string>"):
    tree = ast.parse(source, filename=filename)
    collector = FunctionCollector()
    collector.visit(tree)
    results = []
    for function in collector.functions:
        counter = BranchCounter()
        for statement in function.body:
            counter.visit(statement)
        complexity = 1 + counter.branches
        results.append({
            "name": function.name,
            "line": function.lineno,
            "end_line": getattr(function, "end_lineno", function.lineno),
            "complexity": complexity,
            "level": "low" if complexity <= 5 else "moderate" if complexity <= 10 else "high",
        })
    return sorted(results, key=lambda item: (-item["complexity"], item["line"]))

def analyze_path(path):
    files = [path] if path.is_file() else sorted(path.rglob("*.py"))
    reports = []
    for file in files:
        try:
            reports.append({"file": str(file), "functions": analyze_source(file.read_text(encoding="utf-8"), str(file))})
        except (SyntaxError, UnicodeDecodeError) as exc:
            reports.append({"file": str(file), "error": str(exc), "functions": []})
    return reports

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Python file or directory")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()
    if not args.path.exists():
        parser.error(f"path does not exist: {args.path}")
    reports = analyze_path(args.path)
    if args.json:
        print(json.dumps(reports, indent=2))
    else:
        for report in reports:
            print(report["file"])
            if "error" in report:
                print("  ERROR: " + report["error"])
            for item in report["functions"]:
                print(f"  {item['line']:>4}  {item['level']:<8} complexity={item['complexity']:<3} {item['name']}")
    if any("error" in report for report in reports):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
