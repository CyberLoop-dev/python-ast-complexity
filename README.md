<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=145&section=header&text=Python%20AST%20Complexity&fontColor=ffffff&fontSize=34" alt="Animated header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=Python%20AST%20Complexity;Measure%20branching%20per%20function" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/python-ast-complexity?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/python-ast-complexity)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/python-ast-complexity?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/python-ast-complexity)

<img src="./assets/mark.svg" width="145" alt="Custom SVG illustration"/>

**Measure per-function cyclomatic complexity in Python without importing or executing project code.**

</div>

## ✨ Overview

A lightweight static analyzer that parses Python syntax trees and counts common decision points inside each function.

## 🚀 Features

- 🌳 Uses Python AST parsing; analyzed files are never executed.
- 🧮 Counts branches, loops, exception handlers, boolean operators, and match cases.
- 📊 Labels functions low, moderate, or high complexity.
- 📁 Scans one file or a directory recursively.

## 🧪 Demo

```bash
python main.py src/ --json
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/python-ast-complexity.git
cd python-ast-complexity
python main.py .
```

## 🧰 Tech Stack

Python 3.10+ · ast · pathlib · Standard library only.

## 🗂️ Folder Structure

```text
python-ast-complexity/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Per-function branch counts
- [x] Nested function handling and tests
- [ ] Configurable complexity weights
- [ ] Markdown and SARIF exports

## 🤝 Contributing

Add a small Python snippet and an expected complexity result for each new counting rule.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer"/></div>
