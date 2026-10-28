# Kalibrace detektoru (2026-10-28, po oponentuře)

Korpus jsou veřejné texty psané lidmi, staženo 2026-10-28 (`defuddle parse <url> --md`) do `tests/private/` (není v repu). Wikipedie, licence CC BY-SA 4.0.

- CZ: https://cs.wikipedia.org/wiki/ + Praha, Pivo, Účetnictví, Faktura, Daň_z_přidané_hodnoty, Brno, Železnice, Jan_Amos_Komenský
- EN: https://en.wikipedia.org/wiki/ + Accounting, Invoice, Brewing, Railway, Prague, Value-added_tax

Omezení: encyklopedický text není cílový žánr (posty, e-maily, nabídky, feedback). Výsledek ukazuje, že detektor nestřílí do běžného spisovného textu, ne že je kalibrovaný pro jednotlivé profily. Další kalibrace má být po profilech na textech psaných lidmi.

| Jazyk | Slov | zero / 1000 slov | rewrite / 1000 slov | watch / 1000 slov |
|---|---|---|---|---|
| CZ | 122 824 | 0,10 | 0,13 | 2,59 |
| EN | 99 357 | 0,33 | 0,03 | 0,68 |
| CZ, autorovy zápisky 2022 až 2024 (182 souborů, soukromé, jen čísla) | 40 166 | 0,12 | 0,55 | 0,72 |

Cíl: `zero` ≤ 1 a `rewrite` ≤ 5 na 1000 slov. Splněno.

## Co kalibrace změnila

- **Nadpisy:** text VELKÝMI PÍSMENY, jména osob a wiki odkazy se nepočítají jako Title Case; hlásí se až 3 a víc delších slov s velkým písmenem (na autorových zápiscích bylo 103 falešných nálezů, teď 0).

- **Spojovník s mezerami ` – ` je jen `watch`.** V češtině je to správná pomlčka (a v britské angličtině běžná). Zero zůstává jen dlouhá pomlčka `—`. Před změnou vycházelo CZ zero 2,69 na 1000 slov.
- **Poznámky pod čarou (`[^n]:`) nejsou próza.** Citace se rozpadaly na krátké „věty“ a dělaly falešné staccato (EN rewrite 2,6 před změnou).
- **Zkratky a iniciály nedělí věty** (př. n. l., J. A., pp.).

## Zbylé nálezy v lidských textech

- `x-em-dash` (zero): dlouhá pomlčka v EN Wikipedii. Je to záměr pravidla, ne chyba detektoru: v textu, který má projít antislopem, se dlouhá pomlčka nahrazuje.
- `cs-nejen-ale-i` (watch, 5×), `x-staccato` (6×), `x-arrow` (6×).
- `x-title-case-heading` (EN watch, 16×): anglické nadpisy Wikipedie. V EN je to jen upozornění.
