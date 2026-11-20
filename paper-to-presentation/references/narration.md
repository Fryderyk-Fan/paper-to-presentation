# Narration

Write one complete script in the deck's selected language. Use natural spoken English in English mode and natural spoken Standard Mandarin in Chinese mode. Preserve the deck's claims, data, causal qualifications, and conclusion. Use terminology consistent with the slides. In Chinese, give the English name or acronym on first mention when it helps the listener recognize a term or an original figure label.

## Write for the final deck

- Give each slide one spoken passage with a clear role. Add information that helps the audience follow the argument, such as what to notice in a figure, how a mechanism works, why a comparison matters, or which caveat affects the interpretation. Use each passage to advance the argument and connect naturally to adjacent slides. Check the final slide before referring to any visible position, color, or label.
- Ground every factual claim in the paper, including context that appears only in the script. Check values, comparisons, and scope against the source. Keep hypotheses, reported findings, and author-proposed implications distinct. Avoid unsupported results, uses, novelty claims, and promotional wording.
- Use full, speakable sentences. Introduce the essential context and expand unfamiliar acronyms when it helps comprehension. Explain equations or dense figures in plain academic language, preserving the meanings of the symbols and the direction of comparisons. Avoid reading slide bullets, long citations, equations verbatim, or passages copied from the abstract.
- End with the strongest supported takeaway and any limitation that affects its meaning. A contribution, method property, or scope statement can close the talk when the paper reports no demonstrated outcome.

## Timing

- Use approximately 6–10 minutes as the default planning range. Short papers and simple arguments may need less time. Allow up to 15 minutes for dense work. Use a shorter ceiling when the user supplies one.
- Budget time according to the content of each slide. Let setup, figures, comparisons, and equations take the time they need. Include pauses and transitions. A starting pace for technical narration is about 120–145 English words per minute or 200–240 spoken Chinese characters per minute. Estimate mixed-language terminology, symbols, and numbers by how they are pronounced. Treat these rates as estimates and leave time for figures and pauses.
- Write the anticipated duration for each page, then sum those durations for the full script. Check dense or near-limit passages by reading them aloud or estimating their spoken forms at a conservative pace. Shorten the script if it exceeds its budget. Mark the total as an estimate unless timed delivery was actually measured.

## File format

Use the matching format below for the default UTF-8 Markdown file. Page numbers start at 1 and match the final deck. Use each slide's title or a recognizable equivalent. Timing lines and headings are for the speaker's reference.

### Chinese script (`narration.zh-CN.md`)

```markdown
# 中文口播稿

预计总时长 06:40

## 第 1 页 · 研究问题

预计用时 00:45

本页实际口播内容。
```

### English script (`narration.en.md`)

```markdown
# English narration

Estimated total duration 07:15

## Slide 1 · Research question

Estimated duration 00:50

The spoken passage for this slide.
```

The duration examples show the format. The delivered script covers all slides, and the sum of its page timings equals the total. Include the spoken passages and essential recording labels. Keep planning notes, prompts, and file paths out of the script. If the user requests a different script format, preserve the page correspondence and timing information in that format.
