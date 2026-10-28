# Antislop (čeština)

Vlož tento soubor do instrukcí projektu (ChatGPT, claude.ai) a požádej o kontrolu textu. Zdroj: plugin antislop, licence MIT.

## Principy antislopu

Slop je text, který zabírá místo a nic neříká. Nepoznáš ho podle jednoho slova, ale podle toho, že po přečtení nevíš nic nového. Antislop proto nehledá autora (člověk, nebo model), ale prázdná místa v textu. Píšou je lidé i modely a detektory, které hádají autora, křivdí hlavně lidem, kteří píšou v cizím jazyce [Liang 2023].

Každé pravidlo má náhradu. Smazat obrat nestačí: na jeho místo patří konkrétní informace (číslo, jméno, nástroj, situace, mechanismus). Když ji pisatel nemá, je to signál, že text ještě není hotový. Náhrada se nevymýšlí.

### Pět příznaků

1. Opakující se rytmus. Věty a odstavce stejné délky a stejné stavby (tvrzení, vysvětlení, příklad, přechod). Čtenář přestane vnímat obsah a slyší jen takt.
2. Umělé kontrasty. „Nejde o X, jde o Y“, „Není to X, ale Y“, „Dříve X, dnes Y“. Popírají něco, co nikdo netvrdil, a vypadají jako pointa. Test: zakryj první půlku. Když druhá funguje sama, první byla vata.
3. Dovysvětlování pointy. „A v tom je ten rozdíl.“, „Co to znamená v praxi?“, „Pokud si máte odnést jednu věc…“ Text ohlašuje, co řekne, místo aby to řekl.
4. Doslovné překlady. Anglické obraty přeložené slovo od slova („dělá to smysl“, „na konci dne“) a česká stavba vět přenesená do angličtiny. Kalky píšou i lidé při překladu, proto je antislop vede zvlášť a nehlásí je jako znak AI.
5. Úderné věty na povel. Krátké věty za sebou, otázka a útržek („Výsledek? Rychlejší práce.“), jednoslovné odpovědi („Rozhodně.“). Působí energicky, ale nesou málo.

### Dva tvary slopu

- Nabubřelá vata: dlouhá spojení, která obalují jednoduchou věc („hraje klíčovou roli“, „v dnešní uspěchané době“).
- Kulometné staccato: samé krátké úderné věty. Opak vaty, stejně prázdný.

Dobrý text střídá plynulé souvětí s krátkou větou, kterou si šetří na pointu.

### Test kombinace

Jedna fráze slop nedělá. Spolehlivý signál je kombinace: umělý kontrast, trojice, velký závěr a nula čísel a jmen. Když se v textu sejdou dvě z toho, přepiš úhel, ne slova.

### Testy prázdnoty (na každé hodnotící tvrzení)

1. Záměna. Nahraď klíčové slovo jiným ze stejné kategorie. Platí věta pořád? Pak nic neříká.
2. Opak. Dá se obhájit opak? Když zní absurdně, věta je prázdná.
3. Nové. Dozví se to čtenář poprvé?
4. Konkrétno. Nese věta číslo, mechanismus, situaci nebo příklad?

A na celý text:

5. Kdokoli. Mohl by text stát pod jménem jakékoli firmy? Pak chybí autorovo konkrétno.
6. První dva odstavce. Je v nich konkrétní situace, úkol nebo výsledek?
7. Tření. Tvrdí text, že je všechno snadné? Přiznat, kde to drhne, působí věrohodněji.

### Interpunkce, emoji a formátování

- Dlouhá pomlčka „—“ se nahrazuje čárkou, dvojtečkou, závorkou nebo novou větou. Je to stylová volba antislopu: modely ji přenášejí z angličtiny, česká typografie má pomlčku s mezerami „ – “ (ta je jen upozornění, když jí je moc). Pomlčka zůstává v rozsazích (5–10 minut).
- Šipky (`→`, `->`) místo vět nepatří do textu. Buď věta, nebo číslovaný seznam.
- Emoji nepatří do pracovních a publikovaných textů.
- Odrážky, které všechny začínají tučným štítkem, a hodně tučného písma jsou typické pro výstup chatovacích modelů [Sun 2025]. AI to samo nedokazuje, ale z textu to dělá osnovu. Odrážky jen tam, kde jde opravdu o výčet; jinak souvislý text.
- Nadpisy s velkým písmenem u každého slova jsou v češtině chyba a v angličtině prozrazují šablonu.
- Markdown nepatří do polí, která ho nevykreslí (e-mail, zpráva, post).

### Co antislop neumí

Statistické signály (rytmus, hustota nadužívaných slov) jsou slabé a u krátkých textů nespolehlivé. Detektor je proto počítá až od 150 slov a hlásí je jen jako upozornění. O tom, jestli je text prázdný, nakonec rozhoduje test prázdnoty, ne skóre.

## Postup kontroly

1. Jazyk a typ textu. Urči jazyk (CZ, EN, SK jede českými pravidly) a profil: post, e-mail, nabídka a prezentace, feedback.
2. Nulová tolerance. Dlouhá pomlčka, šipky místo vět, emoji v pracovním textu, zbytky chatbota, falešný protiklad „Nejde o X, jde o Y“, vymyšlené číslo bez zdroje, víc výzev k akci za sebou. Jeden nález = text k přepsání.
3. Průchod A: obraty. Projdi seznam obratů a kalků. U každého nálezu napiš náhradu s konkrétní informací.
4. Průchod B: struktura. Tři krátké věty za sebou, odstavce stejné délky a stavby, trojice ze zvyku, tučné štítky v odrážkách, nadpisy s velkými písmeny, markdown tam, kde se nevykreslí, otázka a útržek místo věty.
5. Průchod C: test prázdnoty. Na každé hodnotící nebo obecné tvrzení záměna, opak, nové, konkrétno. Fakta, termíny, bezpečnostní pokyny a smluvní ustanovení se netestují. Na celý text kdokoli, první dva odstavce, tření. Orientačně: když záměnou a opakem neprojde víc než zhruba třetina hodnotících tvrzení, problém je v úhlu, ne ve slovech. Je to vodítko pro komentář, ne automatický verdikt.
6. Průchod D (jen když text existuje ve dvou délkách). Porovnej verze po odstavcích. Rozdíl je v pořádku jen tam, kde je záměrný.
7. Osobní výjimky. Obraty, které autor používá schválně (jeho podpis), mají přednost před pravidly. Uveď je předem.

Náhrada se nevymýšlí: když chybí číslo nebo příklad, zeptej se autora.

### Výstup

```
ANTISLOP
A: [počet] nálezů - [co se vyhodilo a čím se nahradilo]
B: [nálezy struktury]
C: [x/y hodnotících tvrzení prošlo záměnou a opakem]
Verdikt: PROŠLO / K PŘEPSÁNÍ
```

K PŘEPSÁNÍ znamená opravit a pustit znovu. Nejvýš dvě kola, pak se zeptat autora na konkrétní příklad z praxe.

### Strukturní a interpunkční vzory

#### Konstrukce

- „Výsledek? Rychlejší práce.“: Otázka a útržek místo věty („Výsledek? Rychlejší práce.“). Úderná věta na povel. Náhrada: Jedna plynulá věta s tím, v čem přesně. Lépe: „Objednávku teď vyřídíme za den místo za dva.“

#### Slova, která vadí v hustotě

- „(text s několika slovy ze seznamu)“ `watch`: Nadužívaná slova vadí v hustotě, ne jednotlivě [Kobak 2024]. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „(text s konkrétními údaji)“

#### Interpunkce

- „Je to rychlé — a levné.“ `zero`: Dlouhá pomlčka „—“ je anglický typografický zvyk, který modely přenášejí do češtiny. V češtině se pomlčka píše jako „ – “ s mezerami (ta je jen upozornění). Vyhazovat dlouhou pomlčku je stylová volba antislopu, ne pravidlo pravopisu. Náhrada: Čárka, dvojtečka, závorka nebo nová věta. Pomlčka jen v rozsazích (5–10). Lépe: „Je to rychlé a levné.“
- „Vstup → výstup.“: Šipka místo věty. Jako odrážka na začátku řádku je to nulová tolerance; v tabulkách a technických schématech se nehlásí. Náhrada: Normální věta, nebo číslovaný seznam. Lépe: „Ze vstupu vznikne výstup.“

#### Emoji

- „Hotovo 🚀“ `zero`: Emoji v publikovaném nebo pracovním textu. V e-mailu jen upozornění. Náhrada: Vypusť; tón nes slovy. Lépe: „Hotovo, nasazeno v 9:00.“

#### Formátování

- „**Rychle** a **levně** a **hned**.“ `watch`: Moc tučného písma; zvýraznění přestává fungovat. Náhrada: Nech tučně nejvýš jednu věc na odstavec. Lépe: „Rychle a levně.“
- „- **Rychlost:** a
- **Cena:** b
- **Podpora:** c“: Odrážky, které všechny začínají tučným štítkem. Je to formát typický pro výstup chatovacích modelů [Sun 2025], sám o sobě ale AI nedokazuje; vadí hlavně čitelnosti, protože z textu dělá osnovu. Náhrada: Plynulý text, nebo odrážky bez štítků. Lépe: „Je to rychlé, levné a podpora odpoví do hodiny.“
- „# Jak Napsat Dobrý Text“: Nadpis s velkými písmeny u každého slova. V češtině chyba, v angličtině styl, který prozrazuje šablonu. Náhrada: Velké jen první písmeno (a vlastní jména). Lépe: „# Jak napsat dobrý text“

#### Rytmus

- „(text s monotónní délkou vět)“ `watch`: Věty skoro stejně dlouhé; slabý signál, platí jen u textů nad 150 slov [Muñoz-Ortiz 2023]. Náhrada: Prostřídej krátkou větu a delší souvětí. Lépe: „(text, kde se délky vět střídají)“
- „Je to rychlé. Je to levné. Funguje to hned.“: Tři a víc krátkých vět za sebou. Působí úderně, čte se strojově. Náhrada: Spoj do souvětí, krátkou větu nech jen jako pointu. Lépe: „Je to rychlé a levné a funguje bez nastavování.“

## Čeština: obraty a konstrukce

Seznam níže se generuje z `patterns/cs.json` (`python3 -m detector.build`). Neupravuj ho ručně, změny patří do JSON. Závažnost: **zero** vyhazuje text okamžitě, **rewrite** se přepisuje, **watch** je upozornění.

Osobní výjimky (obraty, které někdo používá schválně jako podpis) patří do `antislop.local.md` v projektu, ne sem.

#### Konstrukce

- „Ulož si to, sdílej a napiš mi.“ `zero`: Víc CTA za sebou. Jedno CTA, konkrétní akce. Náhrada: Nech jednu výzvu s konkrétní akcí. Lépe: „Šablonu si stáhněte na odkazu v komentáři.“
- „Dříve jsme psali e-maily ručně. Dnes je píše AI.“: Šablonový kontrast „Dříve jsme dělali X. Dnes děláme Y.“ Náhrada: Popiš jednu konkrétní změnu a co přinesla. Lépe: „Odpovědi na reklamace teď připraví AI a člověk je jen schválí.“
- „Nejde o nástroje. Jde o lidi.“: Falešný protiklad: popírá něco, co nikdo netvrdil, a pointu jen otočí. Náhrada: Napiš rovnou druhou půlku a doplň, v čem přesně. Lépe: „Tým potřebuje dva dny zaškolení, licence stojí méně.“
- „Šetří nejen čas, ale i peníze.“ `watch`: „nejen…, ale i…“ jako vata. Smí zůstat jen s reálným protikladem. Náhrada: Spoj obě části prostým „a“, nebo jednu vypusť. Lépe: „Ušetří hodinu týdně a licence je levnější.“
- „Není to o penězích, ale o čase.“ `watch`: Umělý kontrast „Není to X, ale Y“; zní jako pointa, ale nic nepřidá. Náhrada: Ověř, jestli X někdo tvrdil. Když ne, napiš rovnou Y. Lépe: „Projekt zabral tři týdny navíc.“
- „Není to jen aplikace, je to životní styl.“: „Není to jen X, je to Y“ nafukuje význam. Náhrada: Řekni, co to konkrétně dělá navíc. Lépe: „Aplikace hlídá příjem bílkovin a připomene jídlo.“
- „Otázkou není, jestli AI nasadit, ale kdy.“: Falešný protiklad „Otázkou není X, ale Y“. Náhrada: Polož rovnou tu skutečnou otázku a odpověz na ni. Lépe: „AI nasadíme na zákaznickou podporu v březnu.“
- „To není zpravodajský server, to je e-shop.“: Falešný protiklad „To není X, to je Y“. Náhrada: Napiš jen Y a doplň konkrétní fakt. Lépe: „Takové články píšou e-shopy s doplňky stravy.“
- „Jenže je tu ještě něco třetího.“: Ohlášený třetí prvek. Náhrada: Třetí bod prostě napiš. Lépe: „Třetí jsou rozhodnutí.“
- „Je důležité najít rovnováhu.“: Umělé vyvažování bez názoru. Náhrada: Napiš svůj názor a riziko řeš konkrétním opatřením. Lépe: „Nasadíme to, ale nejdřív na jednom oddělení.“

#### Obraty

- „Jsem tu pro vás.“ `zero`: Patetická sebeprezentace. Náhrada: Řekni, co nabízíš a pro koho. Lépe: „Ozvěte se, pokud máte víc než 100 faktur měsíčně.“
- „A co vy?“: Generická koncovka bez konkrétní otázky. Náhrada: Polož konkrétní otázku, na kterou jde odpovědět jednou větou. Lépe: „Kolik faktur měsíčně ještě přepisujete ručně?“
- „A teď pozor.“: Falešné napětí. Náhrada: Napiš rovnou riziko nebo vypusť. Lépe: „Pokud zapomenete na zálohu, data přijdou.“
- „A víte co? Fungovalo to.“: Falešné napětí. Náhrada: Smaž a napiš pointu. Lépe: „Fungovalo to na první pokus.“
- „AI je kopilot, ne autopilot.“: Přepálená metafora o AI. Náhrada: Napiš, co AI v té situaci udělá a co rozhoduje člověk. Lépe: „AI připraví návrh odpovědi, odesílá ji člověk.“
- „Ať už jste začátečník, nebo profík…“: Vata, která oslovuje všechny a nikoho. Náhrada: Oslov jednu konkrétní skupinu. Lépe: „Pro účetní, kteří mají víc než 50 klientů.“
- „Tohle je bod zlomu.“: Dramatizace. Náhrada: Řekni, co se od té chvíle změnilo. Lépe: „Od dubna platí nová pravidla pro DPH.“
- „Nástroj chápe váš byznys.“: Personifikace nástroje. Náhrada: Popiš, co nástroj konkrétně dělá. Lépe: „Nástroj si načte ceník a odpoví na dotaz k ceně.“
- „Co to znamená v praxi?“: Řečnická otázka jako přechod. Náhrada: Rovnou napiš, co se v praxi změní. Lépe: „Účetní dostane faktury o den dřív.“
- „Tady je to, co většina lidí nechápe:“: Háček bez obsahu. Náhrada: Řekni rovnou, co lidé dělají a proč to nefunguje. Lépe: „Lidé počítají kalorie, ale neváží jídlo.“
- „Posuňte svůj byznys na další úroveň.“: Marketingové klišé. Náhrada: Řekni, co konkrétně se zlepší. Lépe: „Zkraťte vyřízení objednávky ze dvou dnů na jeden.“
- „Data nám říkají, že lidé nečtou.“: Personifikace dat bez zdroje. Náhrada: Uveď číslo a jeho zdroj. Lépe: „Podle Google Analytics dočte článek 18 % návštěvníků.“
- „V dnešní uspěchané době je čas vzácný.“: Vata na začátku. Náhrada: Začni rovnou tvrzením. Lépe: „Na poradu máme dvacet minut.“
- „Doslova to změnilo všechno.“ `watch`: „doslova“ jako zesílení. Náhrada: Vypusť, pokud nejde o doslovný význam. Lépe: „Změnilo to cenu i dodací lhůtu.“
- „Doufám, že se máte dobře.“ `watch`: Výplň na začátku e-mailu. Náhrada: Rovnou k věci. Lépe: „Posílám nabídku na úterní schůzku.“
- „Doufám, že vám to pomohlo!“: Generická koncovka. Náhrada: Skonči posledním konkrétem. Lépe: „Šablonu najdete v příloze.“
- „Otevřelo mi to oči.“: Falešné prozření. Náhrada: Napiš konkrétní pozorování. Lépe: „Na třech workshopech se ptali na totéž: cenu tokenů.“
- „Jenže právě tady přichází háček.“: Ohlášený háček. Náhrada: Napiš rovnou, co nefunguje. Lépe: „Import ale neumí české znaky.“
- „Technologie sama o sobě nestačí.“: Falešně hluboký závěr. Náhrada: Skonči posledním konkrétem. Lépe: „Bez školení ji v prvním měsíci použili tři lidé z dvaceti.“
- „Komunikace hraje klíčovou roli.“ `watch`: Vata, pokud věta neřekne mechanismus nebo velikost vlivu. V odborném textu s mechanismem je v pořádku. Náhrada: Řekni, co přesně a o kolik pomůže. Lépe: „Odpověď do hodiny sníží počet vratek.“
- „Je důležité si uvědomit, že data jsou citlivá.“: Kazatelský přechod. Náhrada: Napiš rovnou tvrzení. Lépe: „Data obsahují rodná čísla.“
- „Jednoduše řečeno, funguje to.“: Prázdný přechod ke shrnutí. Náhrada: Smaž a nech jen obsah. Lépe: „Funguje to na 9 z 10 objednávek.“
- „Budoucnost klepe na dveře.“: Klišé. Náhrada: Napiš, co a kdy přijde. Lépe: „Od ledna musí e-shopy mít tlačítko pro odstoupení.“
- „Klíčem k úspěchu je rychlost.“: Marketingová vycpávka. Náhrada: Řekni, co přesně a o kolik pomůže. Lépe: „Zákazník, který dostane odpověď do hodiny, nevrací zboží.“
- „Text křičí, že ho psala AI.“: Personifikace obsahu. Náhrada: Popiš, co konkrétně na textu vadí. Lépe: „V textu jsou tři pomlčky a pět emoji.“
- „Nedávno mi jeden klient řekl…“: Generická LinkedIn anekdota. Náhrada: Konkrétní situace: obor, úkol, co se stalo. Lépe: „Účetní kancelář s 40 klienty chtěla zkrátit uzávěrku.“
- „Možná právě proto to nefunguje.“: Mlhavé ohlášení příčiny. Náhrada: Napiš příčinu přímo. Lépe: „Nefunguje to, protože formulář nikdo nečte.“
- „Značka si našla svůj hlas.“: Klišé o značce. Náhrada: Popiš, jak značka teď píše jinak. Lépe: „Značka teď píše v první osobě a bez anglicismů.“
- „Staň se nejlepší verzí sebe sama.“: Motivační kýč. Náhrada: Napiš jeden konkrétní krok. Lépe: „Přidej k obědu 30 g bílkovin.“
- „Objevte nekonečné možnosti AI.“: Marketingová vycpávka. Náhrada: Napiš jednu konkrétní možnost. Lépe: „AI vám připraví odpověď na reklamaci.“
- „Výzkumy ukazují, že lidé čtou méně.“: Nepodložená autorita: tvrzení se schovává za anonymní výzkum. Náhrada: Uveď konkrétní zdroj (autor, rok, odkaz), nebo tvrzení vypusť. Lépe: „Podle Google Analytics dočte článek 18 % návštěvníků.“
- „Neváhejte nás kontaktovat.“: Šablonová výzva. Náhrada: Napiš konkrétní další krok. Lépe: „Zavolejte na 777 000 000 do pátku.“
- „Pokud si z toho máte odnést jednu věc, tak…“: Ohlášený závěr. Náhrada: Napiš tu jednu věc rovnou, bez ohlášení. Lépe: „Fakturu posílejte do 14 dnů.“
- „A tady je to nejdůležitější:“: Ohlášení pointy. Náhrada: Buď to řekni, nebo vypusť. Lépe: „Faktura musí mít DIČ.“
- „Rychleji, levněji, efektivněji.“: Ohraná trojice. Náhrada: Vyber jednu položku a doložit ji. Lépe: „Faktury odcházejí o den dřív.“
- „Upřímně řečeno, nebylo to snadné.“: Plastová lidskost. Náhrada: Smaž a napiš obsah. Lépe: „Migrace trvala tři víkendy.“
- „Pojďme se podívat na tři chyby.“: Ohlášení obsahu místo obsahu. Náhrada: Začni prvním bodem. Lépe: „První chyba je cena v PDF.“
- „Pojďme si to rozebrat.“: Prázdné ohlášení. Náhrada: Začni rovnou prvním bodem. Lépe: „První chyba je v ceně.“
- „A právě tady nastává problém.“: Ukazování na vlastní text místo obsahu. Náhrada: Popiš, co se v tom bodě konkrétně stane. Lépe: „Po třetím kroku polovina lidí formulář zavře.“
- „Tohle mění pravidla hry.“: Klišé. Náhrada: Řekni, co konkrétně se mění. Lépe: „Smlouvu teď podepíšete v aplikaci za minutu.“
- „Samozřejmě, faktura dorazí.“: Prázdné první slovo věty. Náhrada: Smaž a začni obsahem. Lépe: „Faktura dorazí v pondělí.“
- „Znáte to? Ráno nestíháte.“: Řečnický úvod. Náhrada: Začni situací nebo faktem. Lépe: „Ráno v 7:40 ještě nemám odeslanou fakturu.“
- „Revoluce v zákaznické péči.“: Přepálené tvrzení. Náhrada: Popiš změnu a její velikost. Lépe: „Chatbot vyřeší třetinu dotazů bez operátora.“
- „Obsah se snaží tvářit odborně.“: Personifikace obsahu. Náhrada: Řekni, co text tvrdí a co chybí. Lépe: „Článek cituje jednu studii a tu špatně.“
- „Tichá revoluce v účetnictví.“: Módní dramatizace „tichý problém / posun / revoluce“. Náhrada: Pojmenuj, co se děje, a doplň číslo nebo příklad. Lépe: „Polovina našich klientů už posílá faktury přes API.“
- „A to je přesně ten důvod, proč to děláme.“: Prázdná spojka. Náhrada: Spoj příčinu a následek jednou větou. Lépe: „Děláme to, protože ruční přepis trvá dvě hodiny.“
- „Trh si žádá změnu.“: Personifikace trhu. Náhrada: Řekni, kdo konkrétně co chce. Lépe: „Tři ze čtyř zákazníků chtějí platit kartou.“
- „V jádru jde o důvěru.“: Nabubřelá fráze. Náhrada: Začni předmětem. Lépe: „Zákazník zaplatí, když vidí reference.“
- „V neposlední řadě je důležitá podpora.“: Šablonový výčet. Náhrada: Prostě napiš další bod. Lépe: „Podpora odpovídá do hodiny.“
- „A v tom je ten rozdíl.“: Ohlášení pointy místo pointy. Náhrada: Rozdíl řekni konkrétně. Lépe: „Druhá verze odpoví do minuty, první za den.“
- „Právě v tom spočívá síla automatizace.“: Ohlášení síly místo důkazu. Náhrada: Ukaž, co to konkrétně umí. Lépe: „Automatizace zpracuje 300 objednávek bez obsluhy.“
- „Zde je pár tipů, jak ušetřit.“: Šablonový úvod. Náhrada: Rovnou první tip. Lépe: „Zrušte nevyužívané licence.“

#### Slova, která vadí v hustotě

- „Doporučujeme best practice.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Zálohujte každý den v 18:00.“
- „Zajistíme bezešvou integraci.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Napojení na e-shop zabere jeden den.“
- „Zažíváme bezprecedentní růst.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Tržby vzrostly o 30 % proti loňsku.“
- „Máme inovativní přístup.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Faktury čteme přímo z e-mailu.“
- „Klíčový faktor je komunikace.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Rozhoduje, jestli zákazník dostane odpověď do hodiny.“
- „Nabízíme komplexní řešení.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Dodáme účetní software a jeho nastavení.“
- „Je to mnohovrstevnatý problém.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Problém má dvě příčiny: cenu a termín.“
- „Řešíme pain pointy klientů.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Klienti nestíhají párovat platby.“
- „Přinášíme průlomový nástroj.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Nástroj načte fakturu za dvacet sekund.“
- „Spokojenost klienta je prvořadá.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Na reklamaci odpovíme do 24 hodin.“
- „Postavili jsme robustní systém.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Systém zvládne 500 objednávek za hodinu.“
- „Pracujeme se špičkovými technologiemi.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Pracujeme v Pohodě a Money S3.“
- „Šlo o transformační projekt.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Projekt změnil způsob fakturace u 40 klientů.“
- „Nabízíme unikátní službu.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Jako jediní v kraji zpracujeme fakturu do druhého dne.“
- „Šlo o zásadní změnu procesu.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Změna zkrátila schvalování ze tří dnů na jeden.“
- „Pomůžeme vám zefektivnit procesy.“ `watch`: Slovo, které často nahrazuje konkrétní informaci; vadí v hustotě. Náhrada: Nahraď číslem, nástrojem nebo situací. Lépe: „Zkrátíme uzávěrku z pěti dnů na tři.“

## Kalky / Calques

Kalk je obrat přeložený z jiného jazyka slovo od slova. Antislop ho vede jako samostatnou kategorii, protože ho píšou lidé i modely: přeložený text je na kalky bohatý, i když ho žádný model nepsal [Koppel 2011]. Kalk proto není důkaz AI. Je to místo, kde text nezní jako čeština (nebo angličtina).

A calque is a word-for-word translation from another language. Antislop keeps calques separate because humans write them too, especially when translating [Koppel 2011]. A calque is not evidence of AI; it is a spot where the text stops sounding native.

To, že se české kalky z angličtiny kryjí s českým slopem z modelů, je zatím hypotéza: nikdo to neměřil.

### Z angličtiny do češtiny / English to Czech

#### Kalky

- „Musíme adresovat tento problém.“: Kalk z „address the issue“. Píšou ho i lidé. Náhrada: řešit, vyřešit, zabývat se Lépe: „Musíme ten problém vyřešit.“
- „Dělá to smysl.“: Kalk z „makes sense“; česky „dává smysl“. Píšou ho i lidé. Náhrada: „dává to smysl“, nebo řekni proč. Lépe: „Dává to smysl, protože ušetříme dva dny.“
- „Musíme si nastavit mindset.“ `watch`: Korporátní kalk. Náhrada: Řekni, co konkrétně udělat. Lépe: „Každý pátek projdeme chyby z týdne.“
- „Fascinující mozaika kultur.“: Kalk z „rich tapestry“. Náhrada: Vyjmenuj konkrétní prvky. Lépe: „Ve firmě pracují lidé z pěti zemí.“
- „Kontrolujeme to na denní bázi.“: Kalk z „on a daily basis“. Náhrada: denně, každý týden, pravidelně Lépe: „Kontrolujeme to denně.“
- „Na konci dne jde o zákazníka.“ `watch`: Kalk z „at the end of the day“ jako obrazné „nakonec“; doslovně o dni je v pořádku. Náhrada: „nakonec“, nebo vypustit. Lépe: „Rozhoduje, jestli zákazník zaplatí.“
- „Odemkněte potenciál svého týmu.“: Kalk z „unlock potential“. Náhrada: Řekni, co konkrétně získáte. Lépe: „Tým zvládne o deset zakázek měsíčně víc.“
- „Pojďme prozkoumat možnosti.“: Kalk z „let's explore“. Náhrada: Začni obsahem. Lépe: „Máme dvě možnosti: nájem, nebo koupě.“
- „Je to svědectvím toho, že to funguje.“: Kalk z „a testament to“. Náhrada: „ukazuje, že“, nebo rovnou fakt. Lépe: „Ukazuje to, že funguje.“
- „Musíme udělat rozhodnutí.“: Kalk z „make a decision“. Náhrada: rozhodnout se Lépe: „Musíme se rozhodnout.“
- „Je to celé o důvěře.“: Kalk z „it's all about“. Náhrada: Řekni rovnou, o co jde. Lépe: „Zákazník zaplatí, když vidí reference.“
- „V tento moment to nejde.“ `watch`: Kalk z „at this moment“. Náhrada: teď, v tuto chvíli Lépe: „Teď to nejde.“
- „Zůstaňte naladěni!“: Kalk z „stay in touch / stay tuned / deep dive / let's dive in“. Náhrada: Konkrétní další krok, nebo vypustit. Lépe: „Další díl vyjde ve čtvrtek.“

### Z češtiny do angličtiny / Czech to English

#### Calques

- “Please send me the actual price list.” `watch`: False friend: „aktuální“ means current, „actual“ means real. Replace: current (if you mean aktuální) Better: “Please send me the current price list.”
- “In the attachment you find the offer.” `watch`: Czech email calque („v příloze“, „s pozdravem“). Replace: attached is / Kind regards, Better: “The offer is attached.”
- “In the frame of the project we tested it.”: Czech calque („v rámci“, „na základě“, „na denní bázi“). Replace: within / as part of / based on / daily Better: “As part of the project, we tested it.”
- “It is necessary to say that prices rose.” `watch`: Throat-clearing meta phrase, common in Czech-English („je nutné říct“, „dá se říct“). Replace: Just say it. Better: “Prices rose.”
- “We will control the invoices.” `watch`: Czech calque („udělat fotku“, „kontrolovat“ in the sense of check). Replace: take a photo / check Better: “We will check the invoices.”
- “On the other side, it is cheaper.”: Czech calque of „na druhé straně“; English says „on the other hand“. Replace: on the other hand Better: “On the other hand, it is cheaper.”

## Profil: post (LinkedIn, Instagram, sociální sítě)

Nejvíc slopu na jednom místě. Hlídej hlavně:

- Háček bez obsahu. První věta má nést situaci, číslo nebo tvrzení, ne „Většina lidí to dělá špatně.“ nebo „Tohle mění pravidla hry.“
- Umělé kontrasty a dovysvětlování. „Nejde o X, jde o Y“, „A v tom je ten rozdíl.“, „Co to znamená v praxi?“
- Staccato a řádkování. Každá věta na samostatném řádku s prázdným řádkem mezi nimi. Krátká věta jen jako pointa.
- Generická anekdota. „Nedávno mi jeden klient řekl…“ bez oboru, úkolu a toho, co se stalo.
- Koncovka. „A co vy?“, „Thoughts?“, „Agree?“ Polož konkrétní otázku, na kterou jde odpovědět jednou větou, nebo skonči posledním konkrétem.
- Emoji, šipky, hashtagové stěny.

Náhrada je skoro vždycky stejná: jedna konkrétní situace z praxe místo obecného tvrzení.

## Profil: e-mail / email

Pracovní e-mail má jeden účel: aby příjemce věděl, co se po něm chce a do kdy. Slop v e-mailu je hlavně obal kolem toho.

- Úvodní výplň. „Doufám, že se máte dobře.“, „I hope this email finds you well.“, „I just wanted to reach out.“ Začni důvodem, proč píšeš.
- Korporátní slovesa. circle back, touch base, leverage, align.
- Šablonová výzva. „Neváhejte se ozvat.“, „Please don't hesitate to reach out.“ Napiš jeden konkrétní další krok s termínem.
- Kalky v angličtině. „In the attachment I am sending you“, „With regards,“, „actual“ ve smyslu aktuální.
- Markdown v e-mailu. Nadpisy a tučné odrážky se v mnoha klientech nevykreslí a e-mail pak vypadá jako výstup chatbota.
- Zbytky asistenta. „Certainly! Here is…“, „I hope this helps!“

Emoji jsou v e-mailu jen upozornění, ne chyba: v osobní komunikaci můžou změkčit přímý soud.

## Profil: nabídka a prezentace / offer and presentation

Nabídka slibuje. Slop v nabídce slibuje obecně, takže nic.

- Buzzwordy bez důkazu. „best-in-class“, „cutting-edge“, „tailored solutions“, „inovativní“, „komplexní řešení“. Nahraď faktem: pro koho, co přesně, za kolik, do kdy.
- Vymyšlená čísla. Procento bez zdroje, „až o 300 % efektivnější“. Buď zdroj, nebo pryč.
- Ohraná trojice. „rychleji, levněji, efektivněji“, „lidé, procesy, technologie“.
- Slajdy ze samých kategorií. Když na slajdu není jediné jméno, číslo ani situace, je to osnova, ne obsah.
- Nadpisy. Ne „Pět chyb, které děláte“, ale co konkrétně slajd říká. V angličtině pozor na Title Case u každého nadpisu.
- Tučné štítky v odrážkách. „**Rychlost:** …, **Cena:** …“ Je to formát chatbota; tabulka nebo věta poslouží líp.

## Profil: feedback a posudek / feedback and review

Feedback má říct, co funguje, co ne a co s tím. Slop ho zabalí tak, že to příjemce nenajde.

- Sendvič. „Great job overall, but…“, „Celkově super, jen…“ Pochvala jako obal nic neříká. Pochval konkrétní věc, pak problém a návrh opravy.
- Přehnané změkčování. „It might be worth considering…“, „možná by stálo za zvážení…“ Řekni, co změnit a proč. Zjemnit smíš zobecnění o světě, ne svůj soud.
- Umělé vyvažování. „Má to silné i slabé stránky, je důležité najít rovnováhu.“ Napiš verdikt.
- Kategorie bez příkladů. „Komunikace by mohla být lepší.“ Kde, která věta, jak jinak.
- Ohlašování. „Tady je moje zpětná vazba:“, „Here's my feedback:“ a pak teprve obsah.
