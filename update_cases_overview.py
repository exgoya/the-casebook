
import os
import re
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OVERVIEW_FILE = BASE_DIR / "cases-overview.md"
DOCS_INDEX_FILE = BASE_DIR / "docs/index.md"

def parse_front_matter(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if match:
            return yaml.safe_load(match.group(1))
    except Exception:
        return {}
    return {}

def collect_cases(folder: Path):
    cases = []
    if not folder.exists():
        return cases

    for item in sorted(folder.iterdir()):
        if item.is_file() and item.suffix == ".md":
            meta = parse_front_matter(item)
            cases.append({"name": item.name, "path": item, "meta": meta})
        elif item.is_dir():
            summary = item / "summary.md"
            meta = parse_front_matter(summary) if summary.exists() else {}
            cases.append({"name": item.name, "path": summary if summary.exists() else item, "meta": meta})
    return cases

def normalize_products(meta):
    p = meta.get("product", "unspecified")
    if isinstance(p, list):
        return p
    elif isinstance(p, str):
        return [p]
    else:
        return ["unspecified"]

def update_cases_overview():
    content = ["# Cases Overview\n"]

    # High Priority
    content.append("## High Priority Cases")
    high_priority = collect_cases(BASE_DIR / "high-priority-cases")
    if high_priority:
        for c in high_priority:
            products = ", ".join(normalize_products(c["meta"]))
            content.append(f"- {c['name']} ({products})")
    else:
        content.append("- (없음)")
    content.append("")

    # Open Cases
    content.append("## Open Cases")
    open_cases = collect_cases(BASE_DIR / "open-cases")
    if open_cases:
        for c in open_cases:
            products = ", ".join(normalize_products(c["meta"]))
            content.append(f"- {c['name']} ({products})")
    else:
        content.append("- (없음)")
    content.append("")

    # Resolved Cases
    content.append("## Resolved Cases")
    resolved_root = BASE_DIR / "resolved-cases"
    resolved_cases_all = []
    if resolved_root.exists():
        for year_dir in sorted(resolved_root.iterdir()):
            if year_dir.is_dir():
                content.append(f"### {year_dir.name}")
                resolved_cases = collect_cases(year_dir)
                if resolved_cases:
                    for c in resolved_cases:
                        resolved_cases_all.append(c)
                        products = ", ".join(normalize_products(c["meta"]))
                        content.append(f"- {c['name']} ({products})")
                else:
                    content.append("- (없음)")
                content.append("")
    else:
        content.append("- (없음)")

    # Product-wise Index
    content.append("## Cases by Product")
    product_map = {}
    for section in [high_priority, open_cases, resolved_cases_all]:
        for c in section:
            for p in normalize_products(c["meta"]):
                product_map.setdefault(p, []).append(c["name"])

    for product, cases in sorted(product_map.items()):
        content.append(f"### {product}")
        for c in cases:
            content.append(f"- {c}")
        content.append("")

    OVERVIEW_FILE.write_text("\n".join(content), encoding="utf-8")
    print(f"✅ {OVERVIEW_FILE} updated successfully with multi-product support!")

    # Update docs/index.md with sample cases
    docs_index = [
        "# The Casebook",
        "",
        "GitHub Pages에서 열람할 수 있는 Casebook 문서 페이지입니다.",
        "",
        "## 📂 Case Overview",
        "- [Cases Overview](./cases-overview.md)",
        "",
        "## 📚 Guide",
        "- [Casebook 사용 가이드](./guide.md)",
        "",
        "## 📝 Sample Cases",
    ]

    # Add samples if available
    if high_priority:
        docs_index.append("### High Priority")
        for c in high_priority[:3]:  # 최대 3개
            rel = os.path.relpath(c["path"], BASE_DIR)
            docs_index.append(f"- [{c['name']}](../{rel})")
        docs_index.append("")

    if open_cases:
        docs_index.append("### Open Cases")
        for c in open_cases[:3]:
            rel = os.path.relpath(c["path"], BASE_DIR)
            docs_index.append(f"- [{c['name']}](../{rel})")
        docs_index.append("")

    if resolved_cases_all:
        docs_index.append("### Resolved Cases")
        for c in resolved_cases_all[:3]:
            rel = os.path.relpath(c["path"], BASE_DIR)
            docs_index.append(f"- [{c['name']}](../{rel})")
        docs_index.append("")

    DOCS_INDEX_FILE.write_text("\n".join(docs_index), encoding="utf-8")
    print(f"✅ {DOCS_INDEX_FILE} updated with sample case links!")

if __name__ == "__main__":
    update_cases_overview()
