# English: phrases and constructions

The list below is generated from `patterns/en.json` (`python3 -m detector.build`). Do not edit it by hand; change the JSON. Severity: **zero** fails the text, **rewrite** must be rewritten, **watch** is a warning.

Vocabulary items (delve, tapestry, pivotal…) are reported only as density: two or more hits and more than three per 1000 words in a text of at least 150 words. A single "robust" in a technical spec is fine. The list is dated and should be reviewed twice a year, because overused words change with model generations and people start avoiding them [Kobak 2024].

<!-- generated:patterns-en -->
### Constructions

- “Great job overall, but the intro is weak.”: Feedback sandwich: the praise is a wrapper, not information. Replace: Name what works specifically, then the issue and the fix. Better: “The pricing table is clear. The intro needs the client's problem in the first sentence.”
- “This isn't about tools. It's about people.”: False contrast: denies something nobody claimed. Replace: State the second half directly and add the specific fact. Better: “The team needs two days of training; licences cost less.”
- “It's not just an app, it's a lifestyle.”: False contrast „It's not just X, it's Y“. Replace: State what it actually does. Better: “The app tracks protein and reminds you to eat.”
- “It saves not only time but also money.” `watch`: Padding when there is no real contrast. Replace: Join with „and“ or drop one half. Better: “It saves an hour a week and costs less.”
- “Sales rose 5 %, highlighting the strength of the brand.”: A participle tail that adds an interpretation nobody asked for; overused by instruction-tuned models [Reinhart 2024]. Replace: End the sentence; state the interpretation only if you can back it. Better: “Sales rose 5 %.”
- “Worth it? Absolutely.”: Question and one-word answer on cue. Replace: Write one sentence with the reason. Better: “It paid back in three months.”

### Phrases

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

### Words that hurt in density

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
<!-- /generated -->
