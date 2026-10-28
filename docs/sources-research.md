# Zdroje výzkumu pro antislop

Notebook NotebookLM: "Antislop research 2026-10", ID `2273526a-eda2-4193-b571-abf5eae53ddc` (soukromý, nesdílený).
Ověřeno 2026-10-28 přes arxiv.org/abs a aclanthology.org: existence, první autoři, rok prvního zveřejnění, licence.
Rok v citacích je rok prvního zveřejnění (arXiv). U autorů uvádím prvního a "et al.", plné seznamy jsou na odkazu.
Licence "arXiv non-exclusive" znamená, že arXiv smí text distribuovat, autoři si drží práva. Nic z toho se nekopíruje, pravidla jsou extrakce.

Okruhy: A = jazykové rysy LLM textu, B = detekce a její limity, C = stylometrie, translationese, čeština.

| # | Autoři | Rok | Název | URL | Licence | Okruh | Co se použilo |
|---|---|---|---|---|---|---|---|
| 1 | Kobak, González-Márquez et al. | 2024 | Delving into LLM-assisted writing in biomedical publications through excess vocabulary | https://arxiv.org/abs/2406.07016 | CC BY-SA 4.0 | A | slovník "excess style words", posun z obsahových podstatných jmen na stylová slovesa, stárnutí seznamů |
| 2 | Reinhart, Markey et al. | 2024 | Do LLMs write like humans? Variation in grammatical and rhetorical styles | https://arxiv.org/abs/2410.16107 | CC BY-NC-ND 4.0 | A | násobky užití slov a konstrukcí (participia, nominalizace, that-věty), rozdíl base vs. instruct |
| 3 | Liang, Zhang et al. | 2024 | Mapping the Increasing Use of LLMs in Scientific Papers | https://arxiv.org/abs/2404.01268 | CC BY-NC-ND 4.0 | A | slova nejvíc nadužívaná v CS abstraktech (realm, intricate, showcasing, pivotal) |
| 4 | Muñoz-Ortiz, Gómez-Rodríguez et al. | 2023 | Contrasting Linguistic Patterns in Human and LLM-Generated News Text | https://arxiv.org/abs/2308.09067 | CC BY 4.0 | A | délka a rozptyl vět, POS, závislosti, lexikální diverzita, emoce |
| 5 | Padmakumar, He | 2023 | Does Writing with Language Models Reduce Content Diversity? | https://arxiv.org/abs/2309.05196 | arXiv non-exclusive | A | homogenizace obsahu a stylu při psaní s LLM, hloubka syntaktického stromu |
| 6 | Guo, Zhang et al. | 2023 | How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection (HC3) | https://arxiv.org/abs/2301.07597 | arXiv non-exclusive | A, B | šablona odpovědi ChatGPT (definice, kroky, shrnutí), perplexita |
| 7 | Sun, Yin et al. | 2025 | Idiosyncrasies in Large Language Models | https://arxiv.org/abs/2502.12150 | arXiv non-exclusive | A | markdown prvky a první slovo odpovědi jako otisk modelu |
| 8 | Liang, Yuksekgonul et al. | 2023 | GPT detectors are biased against non-native English writers | https://arxiv.org/abs/2304.02819 | arXiv non-exclusive | B | falešné obvinění nerodilých mluvčích (FPR), mechanismus přes perplexitu |
| 9 | Mitchell, Lee et al. | 2023 | DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature | https://arxiv.org/abs/2301.11305 | CC BY 4.0 | B | křivost log-pravděpodobnosti, zhoršení u krátkých textů a parafráze |
| 10 | Hans, Schwarzschild et al. | 2024 | Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text | https://arxiv.org/abs/2401.12070 | arXiv non-exclusive | B | poměr perplexity a cross-perplexity, "capybara problem", délka textu |
| 11 | Verma, Fleisig et al. | 2023 | Ghostbuster: Detecting Text Ghostwritten by Large Language Models | https://arxiv.org/abs/2305.15047 | CC BY 4.0 | B | pokles výkonu u krátkých dokumentů, nerodilé eseje |
| 12 | Sadasivan, Kumar et al. | 2023 | Can AI-Generated Text be Reliably Detected? | https://arxiv.org/abs/2303.11156 | CC BY 4.0 | B | parafrázovací útoky, spoofing, teoretické meze |
| 13 | Dugan, Hwang et al. | 2024 | RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors | https://arxiv.org/abs/2405.07940 | arXiv non-exclusive | B | robustnost detektorů, dekódování, útoky, česká zpravodajská sada |
| 14 | Wang, Mansurov et al. | 2023 | M4: Multi-generator, Multi-domain, and Multi-lingual Black-Box Machine-Generated Text Detection | https://arxiv.org/abs/2305.14902 | CC BY 4.0 | B | přenos mezi doménami, generátory a jazyky |
| 15 | Macko, Moro et al. | 2023 | MULTITuDE: Large-Scale Multilingual Machine-Generated Text Detection Benchmark | https://arxiv.org/abs/2310.13606 | CC BY 4.0 | B, C | 11 jazyků včetně češtiny, přenos mezi jazyky, selhání zero-shot detektorů |
| 16 | Schuster, Schuster et al. | 2019 | The Limitations of Stylometry for Detecting Machine-Generated Fake News | https://arxiv.org/abs/1908.09805 | arXiv non-exclusive | B, C | stylometrie sama o sobě nerozliší strojový text od lidského |
| 17 | Jungmannová, Plecháč | 2022 | Unsigned Play by Milan Kundera? An Authorship Attribution Study | https://arxiv.org/abs/2212.09879 | CC BY-SA 4.0 | C | stylometrie češtiny: lemmata + znakové trigramy, UDPipe, Cosine Delta, SVM |
| 18 | Evert, Proisl et al. | 2015 | Towards a better understanding of Burrows's Delta in literary authorship attribution | https://aclanthology.org/W15-0709/ | ACL Anthology, texty před 2016 CC BY-NC-SA 3.0 (dle poznámky Anthology) | C | základy Delta metod, normalizace frekvencí |
| 19 | Koppel, Ordan | 2011 | Translationese and Its Dialects | https://aclanthology.org/P11-1132/ | ACL Anthology, před 2016 CC BY-NC-SA 3.0 (dle poznámky Anthology) | C | rysy translationese (the, zájmena, spojky), interference zdrojového jazyka |
| 20 | Zhang, Toral | 2019 | The Effect of Translationese in Machine Translation Test Sets | https://arxiv.org/abs/1906.08069 | arXiv non-exclusive | C | translationese zkresluje hodnocení, jsou tam směry cs-en a en-cs |
| 21 | Chlumská | 2017 | Překladová čeština a její charakteristiky (disertace, UK, ÚČNK) | https://dspace.cuni.cz/handle/20.500.11956/80423 | neověřeno (repozitář UK, pouze abstrakt použit) | C | česká překladová čeština: zjednodušení, konvergence, frekvence slovních druhů a n-gramů. Do notebooku přidána jen stránka s abstraktem, tvrzení z ní jsou z abstraktu |

## Vynecháno nebo neověřeno

- Práce, které nešlo ověřit (Volanský et al. o translationese, Baroni a Bernardini): uzavřené časopisy, nepřidáno.
- Konkrétní data k rozdílu 1:1 mezi českým LLM textem a lidským: nenalezena (viz sekce D v `research.md`).
- Čísla v `research.md` pocházejí z extrakce NotebookLM nad těmito zdroji. Před převzetím čísla do README nebo do pravidla s tvrdým prahem ověřit v PDF.
