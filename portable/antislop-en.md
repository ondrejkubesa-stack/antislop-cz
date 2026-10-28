# Antislop (English)

Paste this file into your project instructions (ChatGPT, claude.ai) and ask for a review of your text. Source: antislop plugin, MIT licence.

## Antislop principles

Slop is text that takes up space and says nothing. You do not spot it by one word but by the fact that after reading you know nothing new. Antislop therefore does not guess the author (human or model); it looks for empty places in the text. People write slop too, and detectors that guess authorship are unfair mostly to people writing in a second language [Liang 2023].

Every rule comes with a replacement. Deleting a phrase is not enough: the gap must be filled with specific information (a number, a name, a tool, a situation, a mechanism). If the writer does not have it, the text is not finished. The replacement is never invented.

### Five symptoms

1. Repeating rhythm. Sentences and paragraphs of the same length and shape.
2. Artificial contrast. "It's not about X. It's about Y." It denies what nobody claimed. Test: cover the first half; if the second works alone, the first was filler.
3. Explaining the point. "And that's the difference.", "What does this mean in practice?", "If you take away one thing…"
4. Literal translation. Phrases carried over word for word from another language. Humans do this too, so calques are kept as their own category, not as evidence of AI.
5. Punchlines on cue. Short sentences in a row, a question and a fragment ("Worth it? Absolutely."). Energetic, but nearly empty.

### Two shapes of slop

- Inflated filler: long phrases wrapped around a simple point ("plays a pivotal role", "in today's fast-paced world").
- Machine-gun staccato: nothing but short punchy sentences. The opposite of filler, equally empty.

### The combination test

One phrase does not make slop. The reliable signal is a combination: artificial contrast, a triplet, a grand conclusion and no numbers or names. Two of these together means rewriting the angle, not the words.

### Punctuation, emoji, formatting

- Em dashes become commas, colons, brackets or new sentences. This is antislop's style choice, not a spelling rule; a spaced en dash is only a warning. Dashes stay in ranges (5–10).
- Arrows (`→`, `->`) instead of sentences do not belong in prose.
- No emoji in work or published text.
- Bullets that all open with a bold label, and heavy bold, are typical of chat model output [Sun 2025]. That alone does not prove AI, but it turns prose into an outline.
- Title Case on every heading gives away the template.
- No markdown in fields that will not render it (email, messages, posts).

### Limits

Statistical signals (rhythm, density of overused words) are weak and unreliable on short texts. The detector computes them only from 150 words up and reports them as warnings. Whether a text is empty is decided by the emptiness test, not by a score.

## Review procedure

1. Language and text type. Decide the language and the profile: post, email, offer or presentation, feedback.
2. Zero tolerance. Em dashes, arrows instead of sentences, emoji in work text, leftover chatbot formulas ("Certainly! Here is…"), false contrast ("It's not about X. It's about Y."), invented numbers without a source, several calls to action in a row. One hit means the text gets rewritten.
3. Pass A: phrases. Check the phrase and calque list. For each hit, write a replacement that carries specific information.
4. Pass B: structure. Three short sentences in a row, paragraphs of equal length and shape, habitual triplets, bold labels opening every bullet, Title Case headings, markdown where it will not render, a question followed by a fragment instead of a sentence.
5. Pass C: emptiness test. For every evaluative or general claim (not facts, deadlines, safety instructions or contract clauses): swap (replace the key word with another of the same kind; still true?), opposite (can the opposite be argued?), new (does the reader learn it here?), concrete (number, mechanism, situation, example?). For the whole text: could anyone have signed it, do the first two paragraphs hold a concrete situation, does it admit friction? As a rough guide: if more than about a third of evaluative claims fail swap and opposite, fix the angle, not the words. This informs the comment; it is not an automatic verdict.
6. Pass D (only if the text exists in two lengths). Compare the versions paragraph by paragraph; differences must be intentional.
7. Personal exceptions. Phrases the author uses on purpose override the rules. List them up front.

Never invent the replacement: if a number or example is missing, ask the author.

### Output

```
ANTISLOP
A: [count] findings - [what was cut and what replaced it]
B: [structure findings]
C: [x/y evaluative claims passed swap and opposite]
Verdict: PASS / REWRITE
```

REWRITE means fix and run again. Two rounds at most, then ask the author for a concrete example.

### Structure and punctuation patterns

#### Constructions

- “Result? Faster work.”: A one- or two-word teaser question followed by a fragment ("Result? Faster work."). A punchline on cue. Replace: One sentence that says exactly what changed. Better: “Orders now ship in one day instead of two.”

#### Words that hurt in density

- “(text with several words from the list)” `watch`: Overused words hurt in density, not one by one [Kobak 2024]. Replace: Use a plainer word or a specific fact. Better: “(text with specific details)”

#### Punctuation

- “It is fast — and cheap.” `zero`: The em dash is a typographic habit models carry into every text. Removing it is antislop's style choice, not a spelling rule; a spaced en dash ( – ) is only a warning. Replace: Comma, colon, brackets or a new sentence. Keep dashes in ranges (5–10). Better: “It is fast and cheap.”
- “Input → output.”: An arrow instead of a sentence. As a bullet at the start of a line it is zero tolerance; tables and technical diagrams are skipped. Replace: A normal sentence or a numbered list. Better: “The input becomes the output.”

#### Emoji

- “Done 🚀” `zero`: Emoji in work or published text. In emails only a warning. Replace: Remove it; let the words carry the tone. Better: “Done, deployed at 9:00.”

#### Formatting

- “**Fast** and **cheap** and **now**.” `watch`: Too much bold; emphasis stops working. Replace: At most one bold item per paragraph. Better: “Fast and cheap.”
- “- **Speed:** a
- **Price:** b
- **Support:** c”: Every bullet opens with a bold label. Typical of chat model output [Sun 2025], though it does not prove AI on its own; it mainly turns text into an outline. Replace: Prose, or bullets without labels. Better: “It is fast, cheap, and support answers within an hour.”
- “# How To Write Good Text”: Capitalising every word of a heading gives away the template. Replace: Sentence case: capitalise only the first word and proper names. Better: “# How to write good text”

#### Rhythm

- “(text with uniform sentence length)” `watch`: Sentences of almost the same length. A weak signal, only for texts over 150 words [Muñoz-Ortiz 2023]. Replace: Mix a short sentence with a longer one. Better: “(text with varied sentence length)”
- “It's fast. It's cheap. It works now.”: Three or more short sentences in a row. Sounds punchy, reads as machine-made. Replace: Join them into one sentence; keep a short one only as the punchline. Better: “It's fast and cheap and works without setup.”

## English: phrases and constructions

The list below is generated from `patterns/en.json` (`python3 -m detector.build`). Do not edit it by hand; change the JSON. Severity: **zero** fails the text, **rewrite** must be rewritten, **watch** is a warning.

Vocabulary items (delve, tapestry, pivotal…) are reported only as density: two or more hits and more than three per 1000 words in a text of at least 150 words. A single "robust" in a technical spec is fine. The list is dated and should be reviewed twice a year, because overused words change with model generations and people start avoiding them [Kobak 2024].

#### Constructions

- “Great job overall, but the intro is weak.”: Feedback sandwich: the praise is a wrapper, not information. Replace: Name what works specifically, then the issue and the fix. Better: “The pricing table is clear. The intro needs the client's problem in the first sentence.”
- “This isn't about tools. It's about people.”: False contrast: denies something nobody claimed. Replace: State the second half directly and add the specific fact. Better: “The team needs two days of training; licences cost less.”
- “It's not just an app, it's a lifestyle.”: False contrast „It's not just X, it's Y“. Replace: State what it actually does. Better: “The app tracks protein and reminds you to eat.”
- “It saves not only time but also money.” `watch`: Padding when there is no real contrast. Replace: Join with „and“ or drop one half. Better: “It saves an hour a week and costs less.”
- “Sales rose 5 %, highlighting the strength of the brand.”: A participle tail that adds an interpretation nobody asked for; overused by instruction-tuned models [Reinhart 2024]. Replace: End the sentence; state the interpretation only if you can back it. Better: “Sales rose 5 %.”
- “Worth it? Absolutely.”: Question and one-word answer on cue. Replace: Write one sentence with the reason. Better: “It paid back in three months.”

#### Phrases

- “I hope this helps!” `zero`: Assistant boilerplate. Replace: Delete it; end with the last concrete point. Better: “The template is attached.”
- “Certainly! Here is a summary of the meeting.” `zero`: Chat formula left in the text; the first words alone often reveal the model [Sun 2025]. Replace: Delete it and start with the content. Better: “The meeting agreed on a March launch.”
- “We deliver cutting-edge, tailored solutions.”: Offer buzzword without proof. Replace: Replace with a fact: a number, a client type, a result. Better: “We set up invoice import for accounting firms in two days.”
- “Did you know most invoices are paid late?”: Rhetorical opener. Replace: Start with the fact itself. Better: “Our clients pay 40 % of invoices after the due date.”
- “Please don't hesitate to reach out.”: Template call to action. Replace: Give one concrete next step. Better: “Call me on Thursday after 2 pm if the date doesn't work.”
- “In today's fast-paced world, time is scarce.”: Filler opener. Replace: Start with the claim. Better: “We have twenty minutes for the review.”
- “This is a game changer.”: Marketing cliché. Replace: Say what concretely improves and by how much. Better: “Orders now ship in one day instead of two.”
- “Here's the thing: nobody reads it.”: Fake tension. Replace: Say the point plainly. Better: “Only 18 % of visitors finish the article.”
- “I hope this email finds you well.”: Email filler opener. Replace: Go straight to the reason for writing. Better: “I'm sending the offer for Tuesday's meeting.”
- “I'm thrilled to announce our new feature!”: LinkedIn template. Replace: Say the news and why it matters. Better: “We launched invoice import from Xero.”
- “In conclusion, the plan works.”: Recap opener; the ending repeats what was already said [Guo 2023]. Replace: End with the last concrete point or the next step. Better: “The pilot starts on 4 March.”
- “Let's dive in.”: Announces content instead of giving it. Replace: Start with the first point. Better: “First, the pricing.”
- “I wanted to circle back on this.”: Corporate filler. Replace: Say what you need and by when. Better: “Can you confirm the price by Friday?”
- “Stay tuned!”: Generic sign-off. Replace: Ask one concrete question or end with the last point. Better: “The next release ships on 4 March.”
- “Unlock your full potential.”: Hype verb. Replace: Say what the reader gets. Better: “You will close the books two days earlier.”
- “Studies show that remote teams are happier.”: Unsupported authority: the claim hides behind anonymous research. Replace: Name the source (author, year, link) or drop the claim. Better: “A 2023 Stanford survey of 1,600 workers found…”
- “Whether you're a founder or a freelancer…”: Addresses everyone and no one. Replace: Name one specific reader. Better: “For agencies with more than ten clients.”
- “It might be worth considering a shorter intro.” `watch`: Over-cushioned criticism hides the point. Replace: Say what to change and why. Better: “Cut the intro to two sentences; the offer starts too late.”

#### Words that hurt in density

- “Additionally, we offer support.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “We also offer support.”
- “Amidst the changes, we grew.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “During the changes, we grew.”
- “The team has great camaraderie.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “The team covers for each other on holidays.”
- “Your effort is commendable.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “You finished two days early.”
- “Timing is crucial.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Invoices must go out by the 15th.”
- “In this report we delve into the results.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “This report covers the results.”
- “Elevate your brand.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Get more replies to your emails.”
- “We embarked on a journey.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “We started the project in May.”
- “We empower teams.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Teams approve their own budgets.”
- “We foster collaboration.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Teams share one board.”
- “Furthermore, it is cheap.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “It is also cheap.”
- “Harness the power of data.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Use last year's sales to plan stock.”
- “We take a holistic approach.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “We look at sales and support together.”
- “The process is intricate.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “The process has seven approval steps.”
- “The AI landscape is changing.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Three new models came out this month.”
- “We leverage AI to save time.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “We use AI to draft replies.”
- “We did a meticulous review.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “We checked all 300 invoices.”
- “Moreover, it is fast.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “It is also fast.”
- “It is a multifaceted problem.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “The problem has two causes: price and timing.”
- “Notably, costs fell.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Costs fell by 8 %.”
- “It is a nuanced topic.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “The answer depends on company size.”
- “The excitement was palpable.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Forty people stayed after the talk.”
- “This was a pivotal moment.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “After this, sales doubled.”
- “In the realm of finance, this matters.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “In finance, this matters.”
- “We built a robust system.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “The system handles 500 orders an hour.”
- “We offer seamless integration.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “Integration takes one day.”
- “The demo showcases our features.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “The demo shows invoice import and export.”
- “A rich tapestry of cultures.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “People from five countries work here.”
- “This is a testament to our work.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “This shows our work paid off.”
- “This underscores the need for change.” `watch`: Overused in LLM text; counts only as density per 1000 words. List dated 2026-10, review twice a year [Kobak 2024]. Replace: Replace with a number, a tool or a situation, or a plainer word. Better: “So we need a second server.”

### Calques from Czech

#### Calques

- “Please send me the actual price list.” `watch`: False friend: „aktuální“ means current, „actual“ means real. Replace: current (if you mean aktuální) Better: “Please send me the current price list.”
- “In the attachment you find the offer.” `watch`: Czech email calque („v příloze“, „s pozdravem“). Replace: attached is / Kind regards, Better: “The offer is attached.”
- “In the frame of the project we tested it.”: Czech calque („v rámci“, „na základě“, „na denní bázi“). Replace: within / as part of / based on / daily Better: “As part of the project, we tested it.”
- “It is necessary to say that prices rose.” `watch`: Throat-clearing meta phrase, common in Czech-English („je nutné říct“, „dá se říct“). Replace: Just say it. Better: “Prices rose.”
- “We will control the invoices.” `watch`: Czech calque („udělat fotku“, „kontrolovat“ in the sense of check). Replace: take a photo / check Better: “We will check the invoices.”
- “On the other side, it is cheaper.”: Czech calque of „na druhé straně“; English says „on the other hand“. Replace: on the other hand Better: “On the other hand, it is cheaper.”
