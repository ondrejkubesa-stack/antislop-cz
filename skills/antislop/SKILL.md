---
name: antislop
description: >
  Use when checking or rewriting a Czech, Slovak or English text for AI slop or
  template writing before it is published or sent: posts, emails, offers,
  presentations, feedback, articles. Also when someone asks to make a text sound
  less like AI or less generic ("antislop", "zní to jako AI", "make it sound
  human"). Finds filler phrases, false contrasts, staccato rhythm, calques, em
  dashes, arrows, emoji and chatbot formatting, and replaces each with specific
  information.
---

# Antislop

Najde v textu slop a ke každému nálezu dá náhradu s konkrétní informací. Hledá prázdná místa, ne autora: nerozhoduje, jestli text psal člověk, nebo model.

Finds slop in a text and gives a specific replacement for every finding. It looks for empty places, not for the author.

## Postup / Procedure

1. Jazyk a profil. Urči jazyk (cs, en; slovenštinu kontroluj českými pravidly) a profil: `post`, `email`, `offer` (nabídka, prezentace), `feedback`. Když profil z kontextu nevyplývá, zeptej se jednou větou.
2. Detektor. Ulož text do dočasného souboru a spusť:
   ```bash
   cd "${CLAUDE_PLUGIN_ROOT}" && python3 -m detector.antislop /cesta/k/textu.md --lang cs --profile post --json
   ```
   Nálezy jsou vstup, ne verdikt. Detektor najde přesné obraty a strukturu (pomlčky, šipky, emoji, staccato, tučné štítky, nadpisy). Statistické signály počítá až od 150 slov a hlásí je jen jako `watch`.
3. Osobní výjimky. Pokud v kořeni projektu existuje `antislop.local.md`, načti ho. Výjimky v něm (obraty, které autor používá schválně) mají přednost před pravidly; nálezy, které pokrývají, nehlas.
4. Pravidla. Načti `rules/principy.md` a `rules/postup.md` (EN: `rules/principles-en.md` a `rules/procedure-en.md`), pak seznam pro jazyk: `rules/cs.md` nebo `rules/en.md`, kalky v `rules/kalky.md` a profil v `rules/profily/`. Načítej jen to, co text potřebuje.
5. Průchody A až D podle postupu. Průchod C (test prázdnoty) dělej vždy sám, detektor ho neumí.
6. Náhrady. U každého nálezu napiš náhradu s konkrétní informací. Číslo, jméno ani příklad nevymýšlej: když chybí, zeptej se autora.
7. Výstup ve formátu `ANTISLOP` z postupu. Když jde o přepis, nejdřív přepsaný text, pod ním blok `ANTISLOP`. Nejvýš dvě kola.

## Bez Claude Code / Without Claude Code

V ChatGPT nebo claude.ai použij soubory `portable/antislop-cs.md` a `portable/antislop-en.md` jako instrukce projektu. Detektor jde v ChatGPT spustit přes analýzu dat (nahraj složku `detector/` a `patterns/`).
