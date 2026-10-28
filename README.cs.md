# antislop-cz

Najde a nahradí AI slop v českých a anglických textech. Plugin pro Claude Code, detektor bez závislostí a soubory pravidel ke vložení do ChatGPT a claude.ai.

[English](README.md)

Slop je text, který zabírá místo a nic neříká: „Nejde o nástroje. Jde o lidi.“, „V dnešní uspěchané době“, tři úderné věty za sebou, tučné štítky v každé odrážce, dlouhé pomlčky, na konci „A co vy?“. Antislop je najde a ke každému nálezu řekne, co dát místo něj. Smazat obrat nestačí: na jeho místo patří něco konkrétního (číslo, jméno, nástroj, situace).

## Co hlídá

- Obraty a konstrukce v češtině a angličtině: falešné protiklady, vata na začátku, ohlašování pointy, nafouknutá slovesa, zbytky chatbota („Jistě! Zde je…“).
- Rytmus a strukturu: staccato, otázka a útržek místo věty, monotónní délka vět, trojice ze zvyku.
- Kalky v obou směrech (české obraty přeložené do angličtiny slovo od slova a naopak). Vede je zvlášť, protože je píšou i lidé.
- Interpunkci, emoji a formátování: dlouhé pomlčky, šipky, emoji, odrážky s tučnými štítky, moc tučného, nadpisy s velkými písmeny.
- Profily pro posty, e-maily, nabídky a prezentace a feedback.
- Test prázdnoty (dělá ho model, ne detektor): záměna, opak, nové, konkrétno.

## Instalace (Claude Code)

```bash
/plugin marketplace add ondrejkubesa-stack/antislop-cz
/plugin install antislop-cz@antislop-cz
```

Pak stačí napsat: „Zkontroluj ten post antislopem“ nebo „ať ten e-mail nezní jako AI“.

## Detektor (CLI)

Python 3.9+, bez závislostí.

```bash
python3 -m detector.antislop text.md --lang cs --profile post
python3 -m detector.antislop text.md --json
```

Návratový kód 0 = žádný nález `zero` ani `rewrite`, 1 = nějaký je, 2 = chyba vstupu. Závažnost: `zero` vyhazuje text, `rewrite` se přepisuje, `watch` je upozornění.

Spojovník s mezerami („a – b“) je správná česká pomlčka, proto je jen upozornění. Nulovou tolerancí je dlouhá pomlčka „—“.

## ChatGPT a claude.ai

Vlož `portable/antislop-cs.md` (nebo `portable/antislop-en.md`) do instrukcí projektu a požádej o kontrolu textu. V ChatGPT můžeš nahrát i složky `detector/` a `patterns/` do analýzy dat a detektor spustit tam.

## Osobní výjimky

Pokud nějaký obrat používáš schválně jako svůj podpis, zapiš ho do `antislop.local.md` v kořeni projektu. Skill ho načte a přestane ho hlásit.

## Co to není

- Není to detektor AI. Antislop hledá prázdný text, ne autora. Detektory, které hádají autora, označily v průměru 61 % esejí nerodilých mluvčích z testu TOEFL za text od AI, zatímco u esejí amerických osmáků byly téměř bezchybné [Liang 2023]. Slop píšou i lidé.
- U krátkých textů je slabší. Statistické signály (rytmus, hustota nadužívaných slov) potřebují aspoň 150 slov a hlásí se jen jako upozornění.
- Český výzkum chybí. Neexistuje změřený seznam slov, která český výstup modelů nadužívá. Česká pravidla vycházejí z praxe (v datech `praxe` a `author`). Že se české kalky kryjí s českým slopem z modelů, je hypotéza.
- Seznamy stárnou. Nadužívaná slova se mění s generacemi modelů; anglický seznam má datum 2026-10 a revizi dvakrát ročně [Kobak 2024].

## Jak přispět

Vzory jsou v `patterns/*.json`, z nich se generují `rules/*.md` a `portable/*.md`:

```bash
python3 -m detector.build
python3 -m detector.build --check
python3 -m unittest discover -s tests -t .
```

Každý vzor potřebuje důvod, náhradu a ukázku před a po. Kalibrace je v `docs/calibration.md`, zdroje v `SOURCES.md`.

## Licence

MIT © 2026 Ondřej Kubesa. Části převzaté z nowork-ai/anti-ai-slop-cz (MIT © 2026 Filip Dřímalka), viz `SOURCES.md`.
