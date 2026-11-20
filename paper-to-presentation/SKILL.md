---
name: paper-to-presentation
description: Turn a research paper PDF from any discipline into a concise, evidence-grounded PowerPoint of up to eight slides and one matching narration script. Deliver both in English by default or both in Simplified Chinese on request. Use when asked to present, teach, or explain a research paper using slides and spoken narration.
---

# Paper to Presentation

Use the supplied research paper PDF as the source. Deliver one editable 16:9 `.pptx` with at most 8 total slides and one complete narration script. Resolve the delivery language from the user's request before planning. An explicit choice of English or Chinese applies to both files. When the user omits the choice, proceed in English. In Chinese mode, write slide text in Simplified Chinese and narration for spoken Standard Mandarin. By default, write for an academically literate audience unfamiliar with the paper. Honor a requested audience or shorter duration. The script must fit within 15 minutes, including pauses and transitions.

## Read the paper and plan the story

1. Read the abstract, main text, figures, tables, and relevant appendix. Identify the question, actual contribution, strongest supporting evidence, and limitations that affect the main claims. Check important numbers, definitions, and figure labels against their source. Use OCR or inspect the page image when PDF extraction loses text, columns, equations, or tables. If material evidence remains unreadable, qualify or omit the affected claim. If the main contribution cannot be established from the available file, request a readable copy.
2. Choose a narrative that fits the contribution and audience. Use fewer pages if the argument fits. Count any title, summary, or reference slide toward the eight-page limit. An opening slide can introduce the paper and frame the research question at the same time.
3. Make one shared outline before authoring. For each slide, record its main message, supporting paper page or section and figure or table when applicable, intended visual, and what the speaker should explain. Give experimental setup, results, algorithm steps, or assumptions their own space when they are essential to understanding the contribution.

## Produce the files

4. Read [slide design and evidence](references/slides.md) and produce `presentation.pptx` from the outline. Use available PowerPoint authoring and rendering tools. Keep authored text, tables, charts, and diagrams editable where practical. Use the paper's figures and results to support the explanation. Put the claim and its evidence on the slide and develop the explanation in the narration.
5. Read [narration](references/narration.md) and write `narration.en.md` in English mode or `narration.zh-CN.md` in Chinese mode. Align the script to the **final** slide count and order, with one section per slide and room for several sentences, figure guidance, and transitions. Check that facts, terminology, and caveats agree with the deck.
6. Reopen and render the finished PPTX. Inspect each page for legibility, alignment, margins, figure integrity, and text or object overflow. Recheck claims and source references against the PDF. Verify that both files use the selected language for authored content, the script follows the deck, and the estimated delivery time meets the budget. Optionally run `scripts/check_delivery.py` with the PPTX and narration paths to check the package and timing lines. For Chinese, add `--language zh-CN`. If a verification capability is unavailable, describe the specific check that remains unverified in the handoff.

Deliver the PowerPoint and its narration script as files. Include the slide count and estimated speaking time in the handoff. Keep drafts, extraction logs, and production instructions out of the deliverables.
