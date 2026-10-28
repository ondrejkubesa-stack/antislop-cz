# Čeština: obraty a konstrukce

Seznam níže se generuje z `patterns/cs.json` (`python3 -m detector.build`). Neupravuj ho ručně, změny patří do JSON. Závažnost: **zero** vyhazuje text okamžitě, **rewrite** se přepisuje, **watch** je upozornění.

Osobní výjimky (obraty, které někdo používá schválně jako podpis) patří do `antislop.local.md` v projektu, ne sem.

<!-- generated:patterns-cs -->
### Konstrukce

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

### Obraty

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

### Slova, která vadí v hustotě

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
<!-- /generated -->
