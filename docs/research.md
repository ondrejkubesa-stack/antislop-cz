# Výzkumné podklady pro antislop

Stav: 2026-10-28. Zdroje a licence: `sources-research.md`. Extrakce proběhla v NotebookLM (notebook "Antislop research 2026-10") nad 21 zdroji. Tvrzení jsou přeformulovaná, citace ve tvaru [autor rok] odkazují do tabulky zdrojů. Čísla jsou z extrakce a před použitím jako tvrdý práh je nutné ověřit v PDF.

Zásada plynoucí z výzkumu: detektor má hledat **slop (vzorce v textu)**, ne **autora**. Zdroje shodně ukazují, že autorství z textu spolehlivě určit nejde a že pokus o to křivdí nerodilým mluvčím (sekce B).

Zkratky: **R** = regex, **H** = heuristika (počty, poměry, POS), **J** = jen úsudek (LLM nebo člověk), **EN/CZ** = jazyk, pro který je pravidlo doloženo.

## A. Rysy a kandidátní pravidla

Pozn.: tabulka níže používá slovo "kandidát", ne hotové pravidlo. Žádný rys nestačí sám o sobě, doporučuje se skórování a hustota na 1000 slov.

### A1. Slovní zásoba (EN doloženo, CZ nedoloženo)

- Po nástupu ChatGPT vyskočil na PubMed seznam "stylových" slov, většinou sloves (např. delve, underscore, showcase) a několika adjektiv, zatímco dřívější skoky v slovníku byly obsahové (ebola, zika, covid) [Kobak 2024]. Odhad: aspoň 13,5 % abstraktů z roku 2024 prošlo LLM, v některých podoborech až 40 % [Kobak 2024].
- Na arXiv CS abstraktech byla nejvíc nadužívaná slova realm, intricate, showcasing a pivotal [Liang 2024].
- Instruktážně doladěné modely (GPT-4o, Llama 3 Instruct) používají některá slova mnohonásobně častěji než lidé, např. tapestry, camaraderie, intricate, palpable, amidst; pořadí se liší model od modelu a základní modely se lidem blíží [Reinhart 2024].
- Hrubé porovnání: obsahová slova stárnou s tématy, stylová s generacemi modelů a s tím, že lidé se slovům začnou vyhýbat nebo je naopak převezmou [Kobak 2024].

Kandidáti:

| ID | Pravidlo | Typ | Závažnost | Jazyk | Zdroj |
|---|---|---|---|---|---|
| L1 | Seznam "excess" slov (delve, intricate, pivotal, showcase, underscore, tapestry, realm, palpable...) s váhou a **hustotou** na 1000 slov, ne jednotlivým výskytem | R + H | střední (jednotlivě), vysoká při hustotě | EN | Kobak 2024, Liang 2024, Reinhart 2024 |
| L2 | Seznam má mít datum a verzi, revize aspoň každého půl roku; slova s ověřenou migrací do lidského psaní snižovat | H (správa dat) | metapravidlo | EN, CZ | Kobak 2024 |
| L3 | Sumarizační vata v závěrech (tapestry, testament, "in the ever-evolving landscape" a podobně) ve **větách na konci textu** | R | střední | EN | Reinhart 2024 (slovník), vlastní praxe |

Česká verze L1 nemá oporu ve výzkumu, viz D1. Český seznam proto vychází z autorova vlastního antislopu a sbírky nowork-ai, ne z tohoto výzkumu.

### A2. Gramatika a syntax (EN)

- Participiální vazby (present participial clauses) jsou u GPT-4o asi 5krát častější než u lidí, instruct modely 2 až 5krát [Reinhart 2024].
- Nominalizace jsou asi 2krát častější (1,5 až 2krát u instruct modelů) [Reinhart 2024].
- Věty se podmětem v podobě "that" klauze a frázová koordinace jsou u GPT-4o častější (zhruba 2,6 a 1,9krát); naopak agentless pasiv GPT-4o používá zhruba poloviční oproti lidem [Reinhart 2024]. Pozor: tento efekt se mezi rodinami modelů liší (Llama vs. GPT), takže pravidlo na "méně pasivu" je křehké.
- V novinovém textu mají LLM víc pomocných sloves, zájmen a spon, méně podstatných jmen, přídavných jmen a přívlastků; lidské texty mají vyšší optimalizaci délky závislostí [Muñoz-Ortiz 2023].
- Při psaní s InstructGPT bylo nepatrně nižší syntaktické zanoření a kratší průměrná věta [Padmakumar 2023]; efekt je malý.

| ID | Pravidlo | Typ | Závažnost | Jazyk | Zdroj |
|---|---|---|---|---|---|
| G1 | Hustota participiálních vazeb ("..., leaning on X, he...") nad prahem | H (POS) | střední | EN | Reinhart 2024 |
| G2 | Hustota nominalizací (-tion, -ment, -ness...) nad prahem | H | nízká až střední | EN | Reinhart 2024 |
| G3 | Zvýšené spony a pomocná slovesa v kombinaci s nízkým podílem přívlastků | H | nízká | EN | Muñoz-Ortiz 2023 |

CZ ekvivalenty (přechodníky, slovesná podstatná jména na -ní, shluky genitivů) jsou v D2.

### A3. Rytmus: délka a rozptyl vět

- Věty z LLM jsou v novinovém textu soustředěné do pásma kolem 10 až 30 tokenů, málo je velmi dlouhých (nad 40 tokenů); lidský text má širší rozptyl [Muñoz-Ortiz 2023]. Autoři to označují jako vyrovnávání registru.
- Lexikální diverzita (STTR, MTLD) bývá u LLM nižší než u lidí; rozdíly jsou velké u některých modelů (Falcon) a malé u jiných [Muñoz-Ortiz 2023].

| ID | Pravidlo | Typ | Závažnost | Jazyk | Zdroj |
|---|---|---|---|---|---|
| R1 | Variační koeficient délky vět pod prahem u textu ≥ 150 slov (i beze slov typu "delve") | H | nízká až střední | EN, CZ k ověření | Muñoz-Ortiz 2023 |
| R2 | Chybějící dlouhé věty (nad 40 slov) a krátké úderné věty na povel, spolu s opakovaným schématem | H | nízká | EN | Muñoz-Ortiz 2023 |
| R3 | Nízká lexikální diverzita (MTLD) | H | nízká, jen jako příznak | EN | Muñoz-Ortiz 2023 |

Upozornění: R1 až R3 jsou přesně ty vlastnosti, které mívá i zjednodušený text nerodilého mluvčího (sekce B). Nikdy neoznačovat samostatně jako "AI".

### A4. Interpunkce

- LLM v novinovém textu užívají interpunkci mírně méně než lidé (zhruba 10,8 až 11,4 % vs. 11,9 % tokenů), s výjimkami podle modelu [Muñoz-Ortiz 2023]. Rozdíl je příliš malý a nekonzistentní na to, aby se z něj stavělo pravidlo.
- O pomlčce, vykřičnících, uvozovkách a emoji zdroje nic měřitelného neříkají (viz D3). Pravidla na em dash a emoji zůstávají založená na pozorování z praxe, ne na výzkumu.

### A5. Formátování, struktura odstavce, začátky a konce

- Klasifikátor, který viděl jen markdown prvky (tučné, kurzíva, nadpisy, číslované a odrážkové seznamy, kód) a všechna slova nahrazená, poznal rodinu modelu s 73 % přesností u chatovacích API [Sun 2025]. [ověřeno v PDF: 73,1 %] ChatGPT často tučně uvozuje body ve seznamech a používá hierarchické odrážky, Claude méně formátuje, Gemini víc kurzívy [Sun 2025].
- První slovo odpovědi samo prozrazuje model zhruba v polovině případů (u pěti modelů); typické jsou "Certainly!", "Here is", "Below is" [Sun 2025].
- ChatGPT v HC3 sleduje šablonu: nejdřív definice, potom kroky v odrážkách, nakonec shrnutí [Guo 2023].

| ID | Pravidlo | Typ | Závažnost | Jazyk | Zdroj |
|---|---|---|---|---|---|
| F1 | Úvodní formule chatu ("Certainly!", "Here is...", "Sure,") na začátku textu | R | vysoká (v publikovaném textu) | EN, CZ překlad formulí | Sun 2025, Guo 2023 |
| F2 | Tučné úvodní slovo v odrážce typu "**Klíčový bod:** vysvětlení" opakovaně v jednom textu | R | střední | EN, CZ | Sun 2025 |
| F3 | Šablona "definice - seznam - shrnutí", závěrečný odstavec začínající shrnutím | J | střední | EN, CZ | Guo 2023 |
| F4 | Hustota markdown prvků neobvyklá pro daný typ textu (např. nadpisy v e-mailu) | H | nízká až střední | EN, CZ | Sun 2025 |

### A6. Hedging a stanovisko

- GPT-4o a 4o mini používají zeslabovače (barely, nearly) víc než lidé, kdežto Llama 3 je naopak míjí; ChatGPT-4 má podle jedné z citovaných prací méně epistemických značek a odkazů na lidské subjekty [Reinhart 2024].
- Důsledek: neexistuje jediný "hedging" rys, který by platil pro všechny modely. Pravidlo na hedging nechat jako úsudek (J), ne jako regex.

### A7. Spojky a konektory

- Nadužívané jsou také souvislostní spojky a konektory (additionally, notably, furthermore...) [Kobak 2024]. Pozor: stejné konektory jsou přebyteční i v překladech (explicitace) [Koppel 2011]. To je zdroj falešných nálezů (sekce B, C).

| ID | Pravidlo | Typ | Závažnost | Jazyk | Zdroj |
|---|---|---|---|---|---|
| K1 | Hustota konektorů (additionally, furthermore, moreover, notably) | R + H | nízká až střední | EN | Kobak 2024, Koppel 2011 |

### A8. Statistické metriky

- Perplexita a její odvozeniny (DetectGPT, Binoculars) umí odlišit LLM text za vhodných podmínek (dlouhý anglický text, běžné modely) [Mitchell 2023, Hans 2024], ale selhávají mimo tyto podmínky (sekce B).
- antislop je **nepoužije jako rozhodující signál**. Perplexita vyžaduje model a poskytuje skóre pro autora, ne důkaz o frázi. Volitelný příznak lze doplnit pozdějc.

## B. Limity a falešné nálezy (podklad pro varování v README)

1. **Nerodilí mluvčí.** Sedm komerčních detektorů označilo asi 61 % TOEFL esejí nerodilých autorů za AI [ověřeno v PDF: průměr 61,22 %], kdežto u esejí rodilých osmáků byly téměř bezchybné [ověřeno v PDF; číslo ~5 % v článku není, opraveno]. Mechanismus: nižší perplexita jednodušší slovní zásoby [Liang 2023]. Po "obohacení" slovníku falešně pozitivních výrazně ubylo a po "zjednodušení" rodilých esejí jich naopak vzrostlo [Liang 2023]. Binoculars podle Hans 2024 je na tento posun odolnější, ale pro krátké texty to neplatí obecně [Hans 2024, Verma 2023].
2. **Krátké texty.** Výkon detektorů klesá pod zhruba 100 až 250 tokenů [Verma 2023, Hans 2024, Mitchell 2023]. antislop proto u krátkých vstupů skóre nepočítá a vrací jen přesné nálezy frází.
3. **Parafráze a úpravy.** Parafrázování omezí výkon zero-shot, trénovaných i retrieval detektorů; úprava promptu ("použij literární jazyk") snížila detekci u esejí z 100 % na 13 % [Sadasivan 2023, Liang 2023]. Zjednodušení: kdo ví, jak slop vypadá, ho snadno obejde.
4. **Doménový a modelový posun.** Detektory trénované v jedné doméně nebo na jednom generátoru dramaticky ztrácejí v jiné, někdy na úroveň náhody; dekódování (opakovací penalizace, sampling) výkon dále lámou [Wang 2023, Dugan 2024].
5. **Perplexita sama nestačí.** Neobvyklé zadání (příklad "capybara astrofyzik") vyrobí vysokou perplexitu i u LLM a zero-shot detektory selžou [Hans 2024].
6. **Stylometrie samotná** nestačí k rozlišení strojového textu od lidského [Schuster 2019].
7. **Seznamy slov stárnou.** Modely se mění, lidé se slovům vyhýbají, a lidský styl některé "AI" obraty převezme [Kobak 2024, Wang 2023]. Proto verzovat a datovat seznamy (L2).
8. **Zero-shot detektory ve více jazycích** selhávaly (blízko náhody) a komerční služby v ne-angličtině také [Macko 2023].
9. **Falešné obvinění je asymetrické.** Chybné označení člověka je horší než minutí AI textu. Odtud rozhodnutí: plugin hledá fráze s citací důvodu, ne verdikt "psal to AI".

Doporučené věty do README (vlastními slovy): nástroj hledá znaky prázdné, šablonovité prózy bez ohledu na autora; texty zjednodušené a přeložené mohou pár pravidel spustit i bez AI; nic z toho není důkaz o původu.

## C. Čeština a kalky

### C1. Co výzkum o češtině říká

- MULTITuDE obsahuje češtinu. Detektor doladěný jen na angličtině dává na češtině Macro F1 0,68, na ruštině 0,79, na všech jazycích dohromady 0,86 [Macko 2023]. Přenos funguje lépe z příbuzných jazyků, ale čeština je latinkou psaná slovanština, takže nezapadá ani do cyrilice, ani do románských jazyků [Macko 2023].
- V RAID na české zpravodajské sadě dosáhl Binoculars zhruba 67 % přesnosti při 5 % FPR, trénované detektory téměř náhodně [Dugan 2024]. Čísla bereme jako orientační.
- Čeština je morfologicky bohatá. Stylometrie češtiny pracuje s lemmaty a znakovými trigramy, což zachytí slovní zásobu i skloňování zároveň; autoři použili UDPipe 2.0 a Cosine Delta nebo SVM [Jungmannová 2022]. Pro antislop z toho plyne: počty slov bez lemmatizace jsou u češtiny nespolehlivé (jeden obrat má mnoho tvarů), regexy je třeba psát na kmen a tvary.
- Delta metody jsou vůči volbě normalizace citlivé [Evert 2015], takže ani frekvenční rozdíly "AI vs. člověk" není vhodné brát jako absolutní.

### C2. Translationese (obecné doloženo, CZ okrajově)

- Přeložený text se liší od původního: zjednodušení, normalizace, explicitace a interference zdrojového jazyka [Koppel 2011]. V angličtině z překladu je nadměrné "the", méně osobních zájmen (I, he, she) a víc kohezních konektorů (therefore, thus, moreover, furthermore) [Koppel 2011].
- Otisk zdrojového jazyka je rozlišitelný (francouzština, němčina, španělština) a vzdálenější jazyky se klasifikují hůř [Koppel 2011].
- Překladová čeština v disertaci Chlumské se zjednodušuje, konverguje a liší se frekvencí slovních druhů a n-gramů od původní češtiny; práce se opírá o korpus Jerome, v němž převažují překlady z angličtiny [Chlumská 2017, podle abstraktu].
- Překládané zdrojové texty zkreslují i hodnocení strojového překladu, včetně dvojice en-cs; efekt je větší tam, kde je strojový překlad horší [Zhang 2019].

### C3. Kalky: co je doložené a co je úsudek

- **Doložené:** explicitace konektorů v překladech [Koppel 2011]; LLM nadužívají podobnou sadu konektorů [Kobak 2024]; nerodilé psaní má nižší perplexitu [Liang 2023].
- **Úsudek (žádný zdroj to neměřil):** že doslovné překlady anglických frází do češtiny ("dává to smysl", "v konci dne", "pojďme se ponořit") se kryjí s českým LLM slopem a že text přeložený z angličtiny spustí tytéž detektory. Nikdo nezkoumal LLM detektor na české překladové češtině. V README to označit jako hypotézu.
- Důsledek pro pravidla: u českých kalků (typicky "v podstatě je to o tom", "není to jen X, je to Y", "hluboce se ponořit") hodnotit vždy jako **fráze/kalk**, ne jako důkaz AI; text přeložený z angličtiny je na kalky bohatý, aniž by ho psal model.

| ID | Pravidlo | Typ | Závažnost | Jazyk | Zdroj |
|---|---|---|---|---|---|
| C1 | Seznam doslovných překladů anglických frází (kalky) jako samostatná kategorie "kalk", oddělená od "AI" | R | střední | CZ | Koppel 2011 (mechanismus), vlastní praxe |
| C2 | Hustota explicitních konektorů v češtině ("navíc", "dále", "v neposlední řadě", "je třeba zdůraznit") | R + H | nízká až střední | CZ | Koppel 2011, Kobak 2024 (analogie, ne přímý důkaz) |
| C3 | Lemma-aware matching (UDPipe nebo ekvivalent) pro české frazémy místo prostých řetězců | H (nástroj) | metapravidlo | CZ | Jungmannová 2022 |

## D. Mezery

1. **D1. Žádný český seznam nadužívaných slov.** Všechny frekvenční násobky jsou z angličtiny. Český slovník je potřeba odvodit z vlastního korpusu (lidské vs. LLM české texty v obdobných žánrech); to je samostatný drobný experiment, ne citace.
2. **D2. Gramatika LLM češtiny.** Chybí studie přechodníků, nominalizací na -ní, slovosledu, shody či slovesného vidu v textech LLM. Nelze citovat.
3. **D3. Interpunkce a emoji.** Pomlčka, vykřičník, uvozovky, emoji a seznamy v češtině nemají měření. Pravidla na em dash a emoji jdou jen z pozorování; doporučuji označit v `SOURCES.md` jako "praxe", ne "výzkum".
4. **D4. Hedging a závěry** mají jen částečné (a modelově rozporuplné) doklady, viz A6.
5. **D5. Detektory na české překladové češtině** nikdo neměřil (viz C3). Falešné nálezy u přeložených textů neumíme kvantifikovat.
6. **D6. Novější modely.** Zdroje pracují s modely do 2024 (GPT-4o, Llama 3). Chování novějších modelů (včetně těch s min. markdownem) není pokryto; seznamy musí být datované.
7. **D7. Chlumská** byla do notebooku přidána jako web stránka s abstraktem, ne plný text. Případné čerpání konkrétních českých n-gramů vyžaduje PDF.
8. **D8. Ověření čísel.** Extrakce NotebookLM je mezistupeň; konkrétní číselné prahy (5,3krát, 61 %, 0,86) před použitím v pravidlech ověřit v PDF.
