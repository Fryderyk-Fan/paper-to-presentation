"""Check a PPTX and its Markdown narration file."""

import argparse
import posixpath
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
from zipfile import BadZipFile, ZipFile


TIMESTAMP = r"[ \t]+([0-9]{2}):([0-5][0-9])[ \t]*$"
MAX_SECONDS = 15 * 60
NARRATION_FORMATS = {
    "en": (r"^## Slide ([1-9][0-9]*) · \S[^\n]*$", "Estimated total duration", "Estimated duration"),
    "zh-CN": (r"^## 第 ([1-9][0-9]*) 页 · \S[^\n]*$", "预计总时长", "预计用时"),
}


def check_deck(path):
    with ZipFile(path) as package:
        presentation = ET.fromstring(package.read("ppt/presentation.xml"))
        pages = presentation.findall("./{*}sldIdLst/{*}sldId")
        if not 1 <= len(pages) <= 8:
            raise ValueError(f"expected 1–8 slides, found {len(pages)}")

        size = presentation.find("./{*}sldSz")
        if size is None:
            raise ValueError("slide dimensions are missing")
        width = int(size.attrib["cx"])
        height = int(size.attrib["cy"])
        # Allow rounding when an authoring tool stores 13.333 inches.
        if width <= 0 or height <= 0 or abs(9 * width - 16 * height) > 0.001 * 16 * height:
            raise ValueError(f"expected 16:9 slides, found dimensions {width}×{height}")

        relationships = ET.fromstring(package.read("ppt/_rels/presentation.xml.rels"))
        slides_by_id = {
            rel.attrib["Id"]: rel.attrib["Target"]
            for rel in relationships.findall("./{*}Relationship")
            if rel.attrib["Type"].endswith("/slide") and rel.get("TargetMode") != "External"
        }
        for number, page in enumerate(pages, start=1):
            relationship_id = next((value for key, value in page.attrib.items() if key.endswith("}id")), None)
            target = slides_by_id.get(relationship_id)
            if target is None:
                raise ValueError(f"slide {number} is missing from the PPTX package")
            part = unquote(target)
            part = part[1:] if part.startswith("/") else posixpath.normpath(posixpath.join("ppt", part))
            slide = ET.fromstring(package.read(part))
            if not slide.tag.endswith("}sld"):
                raise ValueError(f"slide {number} points to an invalid slide part")
            if slide.get("show") in {"0", "false"}:
                raise ValueError(f"slide {number} is hidden")
        return len(pages)


def timing(text, label):
    matches = list(re.finditer(r"^" + re.escape(label) + TIMESTAMP, text, re.MULTILINE))
    if len(matches) != 1:
        raise ValueError(f"expected one '{label} MM:SS' line")
    match = matches[0]
    minutes, seconds = map(int, match.groups())
    return minutes * 60 + seconds, match


def check_narration(path, slide_count, heading, total_label, page_label):
    text = path.read_text(encoding="utf-8-sig")
    sections = list(re.finditer(heading, text, re.MULTILINE))
    numbers = [int(section.group(1)) for section in sections]
    if numbers != list(range(1, slide_count + 1)):
        raise ValueError(f"expected headings for slides 1–{slide_count} in order, found {numbers}")

    declared_total, _ = timing(text[:sections[0].start()], total_label)
    page_sum = 0
    for index, section in enumerate(sections):
        start = section.end()
        end = sections[index + 1].start() if index + 1 < slide_count else len(text)
        passage = text[start:end]
        try:
            duration, marker = timing(passage, page_label)
            if duration <= 0:
                raise ValueError("the page duration must be positive")
            if not passage[marker.end():].strip():
                raise ValueError("the spoken passage is missing")
        except ValueError as error:
            raise ValueError(f"slide {index + 1}: {error}") from error
        page_sum += duration

    if declared_total != page_sum:
        raise ValueError(f"declared total {as_time(declared_total)} differs from page sum {as_time(page_sum)}")
    if declared_total > MAX_SECONDS:
        raise ValueError(f"declared total {as_time(declared_total)} exceeds 15:00")
    return declared_total


def as_time(seconds):
    minutes, remaining = divmod(seconds, 60)
    return f"{minutes:02d}:{remaining:02d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("presentation", type=Path)
    parser.add_argument("narration", type=Path)
    parser.add_argument("--language", choices=NARRATION_FORMATS, default="en", help="narration format (default: en)")
    args = parser.parse_args()

    try:
        slide_count = check_deck(args.presentation)
    except (BadZipFile, ET.ParseError, KeyError, OSError, ValueError) as error:
        parser.exit(1, f"{args.presentation}: {error}\n")

    try:
        total = check_narration(args.narration, slide_count, *NARRATION_FORMATS[args.language])
    except (OSError, ValueError) as error:
        parser.exit(1, f"{args.narration}: {error}\n")

    print(f"{slide_count} visible slides at 16:9. Declared {args.language} narration duration {as_time(total)}.")


if __name__ == "__main__":
    main()
