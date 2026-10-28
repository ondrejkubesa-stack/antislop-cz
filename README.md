# antislop-cz

Find and replace AI slop in Czech and English texts. A Claude Code plugin, a dependency-free detector, and paste-in rule files for ChatGPT and claude.ai.

[Česky](README.cs.md)

Slop is text that takes up space and says nothing: "It's not about tools. It's about people.", "In today's fast-paced world", three punchy sentences in a row, bold labels on every bullet, em dashes, a closing "Thoughts?". Antislop finds these and, for every finding, says what to put in its place. Deleting the phrase is not enough: the gap has to be filled with something specific (a number, a name, a tool, a situation).

## What it covers

- Phrases and constructions in Czech and English: false contrasts, filler openers, announced points, hype verbs, chatbot leftovers ("Certainly! Here is…").
- Rhythm and structure: staccato, a question followed by a fragment, flat sentence length, habitual triplets.
- Calques in both directions (Czech phrases translated into English word for word and vice versa), kept as their own category because people write them too.
- Punctuation, emoji and formatting: em dashes, arrows, emoji, bold-label bullets, heavy bold, Title Case headings.
- Profiles for posts, emails, offers and presentations, and feedback.
- Emptiness test (done by the model, not the detector): swap, opposite, new, concrete.

## Install (Claude Code)

```bash
/plugin marketplace add ondrejkubesa-stack/antislop-cz
/plugin install antislop-cz@antislop-cz
```

Then ask: "Check this post with antislop" or "make this email sound less like AI".

## Detector (CLI)

Python 3.9+, no dependencies.

```bash
python3 -m detector.antislop text.md --lang en --profile email
python3 -m detector.antislop text.md --json
cat text.md | python3 -m detector.antislop - --lang cs
```

Exit code 0 means no `zero` or `rewrite` findings, 1 means there are some, 2 is an input error. Severity: `zero` fails the text, `rewrite` should be rewritten, `watch` is a warning.

## ChatGPT and claude.ai

Paste `portable/antislop-en.md` (or `portable/antislop-cs.md`) into your project instructions and ask for a review. In ChatGPT you can also upload the `detector/` and `patterns/` folders to data analysis and run the detector there.

## Personal exceptions

If you use a phrase on purpose as your signature, list it in `antislop.local.md` in your project root. The skill reads it and stops flagging it. The file is ignored by git in this repo, so your exceptions stay yours.

## What it is not

- Not an AI detector. Antislop looks for empty text, not for who wrote it. Detectors that guess authorship flagged on average 61 % of TOEFL essays by non-native writers as AI-generated, while scoring near-perfect on essays by US 8th graders [Liang 2023]. People write slop too.
- Weak on short texts. Statistical signals (rhythm, density of overused words) need at least 150 words and are reported only as warnings.
- Czech research is thin. There is no measured list of words that Czech LLM output overuses. Czech rules come from practice and are marked `praxe` or `author` in the data; that Czech calques overlap with Czech LLM slop is a hypothesis.
- Lists age. Overused words change with model generations. The English vocabulary list is dated 2026-10 and should be reviewed twice a year [Kobak 2024].

## Contributing

Patterns live in `patterns/*.json`; `rules/*.md` and `portable/*.md` are generated from them:

```bash
python3 -m detector.build          # regenerate
python3 -m detector.build --check  # fails if generated files are stale
python3 -m unittest discover -s tests -t .
```

Every pattern needs a reason, a replacement and a before/after example. Calibration numbers are in `docs/calibration.md`, sources in `SOURCES.md`.

## Licence

MIT © 2026 Ondřej Kubesa. Parts adapted from nowork-ai/anti-ai-slop-cz (MIT © 2026 Filip Dřímalka); see `SOURCES.md`.
