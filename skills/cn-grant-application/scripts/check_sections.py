#!/usr/bin/env python3
"""Conservative non-whitespace character checks; no Word or funder word-count claim."""

import argparse
import json
from pathlib import Path
import sys


def check_sections(data):
    if not isinstance(data, dict) or not isinstance(data.get("sections"), list):
        raise ValueError("输入须为含 sections 数组的 JSON 对象")
    if not data["sections"]:
        raise ValueError("sections 不能为空")
    results, seen = [], set()
    for index, item in enumerate(data["sections"], 1):
        if not isinstance(item, dict):
            raise ValueError(f"第{index}项须为对象")
        name, texts, limit = item.get("name"), item.get("texts"), item.get("limit")
        if not isinstance(name, str) or not name.strip() or name in seen:
            raise ValueError(f"第{index}项需有非空且不重复的 name")
        if not isinstance(texts, list) or not texts or any(not isinstance(t, str) for t in texts):
            raise ValueError(f"{name}: texts 须为非空字符串数组")
        if limit is not None and (type(limit) is not int or limit < 0):
            raise ValueError(f"{name}: limit 须为非负整数或 null")
        seen.add(name)
        count = sum(not char.isspace() for text in texts for char in text)
        results.append({"name": name, "characters": count, "limit": limit,
                        "over_limit": limit is not None and count > limit,
                        "remaining": None if limit is None else limit - count})
    return {"count_method": "Unicode非空白字符，包含标点、引文及传入的表格文字；不是Word字数",
            "sections": results, "passed": not any(r["over_limit"] for r in results)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 JSON with sections/name/texts/limit")
    args = parser.parse_args()
    try:
        report = check_sections(json.loads(args.input.read_text(encoding="utf-8-sig")))
    except (OSError, UnicodeError, ValueError) as error:
        print(f"输入错误：{error}", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
