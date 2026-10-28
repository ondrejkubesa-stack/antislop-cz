# Principy antislopu

Slop je text, který zabírá místo a nic neříká. Nepoznáš ho podle jednoho slova, ale podle toho, že po přečtení nevíš nic nového. Antislop proto nehledá autora (člověk, nebo model), ale prázdná místa v textu. Píšou je lidé i modely a detektory, které hádají autora, křivdí hlavně lidem, kteří píšou v cizím jazyce [Liang 2023].

Každé pravidlo má náhradu. Smazat obrat nestačí: na jeho místo patří konkrétní informace (číslo, jméno, nástroj, situace, mechanismus). Když ji pisatel nemá, je to signál, že text ještě není hotový. Náhrada se nevymýšlí.

## Pět příznaků

1. Opakující se rytmus. Věty a odstavce stejné délky a stejné stavby (tvrzení, vysvětlení, příklad, přechod). Čtenář přestane vnímat obsah a slyší jen takt.
2. Umělé kontrasty. „Nejde o X, jde o Y“, „Není to X, ale Y“, „Dříve X, dnes Y“. Popírají něco, co nikdo netvrdil, a vypadají jako pointa. Test: zakryj první půlku. Když druhá funguje sama, první byla vata.
3. Dovysvětlování pointy. „A v tom je ten rozdíl.“, „Co to znamená v praxi?“, „Pokud si máte odnést jednu věc…“ Text ohlašuje, co řekne, místo aby to řekl.
4. Doslovné překlady. Anglické obraty přeložené slovo od slova („dělá to smysl“, „na konci dne“) a česká stavba vět přenesená do angličtiny. Kalky píšou i lidé při překladu, proto je antislop vede zvlášť a nehlásí je jako znak AI.
5. Úderné věty na povel. Krátké věty za sebou, otázka a útržek („Výsledek? Rychlejší práce.“), jednoslovné odpovědi („Rozhodně.“). Působí energicky, ale nesou málo.

## Dva tvary slopu

- Nabubřelá vata: dlouhá spojení, která obalují jednoduchou věc („hraje klíčovou roli“, „v dnešní uspěchané době“).
- Kulometné staccato: samé krátké úderné věty. Opak vaty, stejně prázdný.

Dobrý text střídá plynulé souvětí s krátkou větou, kterou si šetří na pointu.

## Test kombinace

Jedna fráze slop nedělá. Spolehlivý signál je kombinace: umělý kontrast, trojice, velký závěr a nula čísel a jmen. Když se v textu sejdou dvě z toho, přepiš úhel, ne slova.

## Testy prázdnoty (na každé hodnotící tvrzení)

1. Záměna. Nahraď klíčové slovo jiným ze stejné kategorie. Platí věta pořád? Pak nic neříká.
2. Opak. Dá se obhájit opak? Když zní absurdně, věta je prázdná.
3. Nové. Dozví se to čtenář poprvé?
4. Konkrétno. Nese věta číslo, mechanismus, situaci nebo příklad?

A na celý text:

5. Kdokoli. Mohl by text stát pod jménem jakékoli firmy? Pak chybí autorovo konkrétno.
6. První dva odstavce. Je v nich konkrétní situace, úkol nebo výsledek?
7. Tření. Tvrdí text, že je všechno snadné? Přiznat, kde to drhne, působí věrohodněji.

## Interpunkce, emoji a formátování

- Dlouhá pomlčka „—“ se nahrazuje čárkou, dvojtečkou, závorkou nebo novou větou. Je to stylová volba antislopu: modely ji přenášejí z angličtiny, česká typografie má pomlčku s mezerami „ – “ (ta je jen upozornění, když jí je moc). Pomlčka zůstává v rozsazích (5–10 minut).
- Šipky (`→`, `->`) místo vět nepatří do textu. Buď věta, nebo číslovaný seznam.
- Emoji nepatří do pracovních a publikovaných textů.
- Odrážky, které všechny začínají tučným štítkem, a hodně tučného písma jsou typické pro výstup chatovacích modelů [Sun 2025]. AI to samo nedokazuje, ale z textu to dělá osnovu. Odrážky jen tam, kde jde opravdu o výčet; jinak souvislý text.
- Nadpisy s velkým písmenem u každého slova jsou v češtině chyba a v angličtině prozrazují šablonu.
- Markdown nepatří do polí, která ho nevykreslí (e-mail, zpráva, post).

## Co antislop neumí

Statistické signály (rytmus, hustota nadužívaných slov) jsou slabé a u krátkých textů nespolehlivé. Detektor je proto počítá až od 150 slov a hlásí je jen jako upozornění. O tom, jestli je text prázdný, nakonec rozhoduje test prázdnoty, ne skóre.
