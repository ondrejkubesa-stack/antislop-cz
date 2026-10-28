# Jak jsme zkrátili fakturaci

Účetní kancelář v Brně měla v září sto čtyřicet klientů a každý měsíc přepisovala přibližně devět set faktur ručně z PDF do účetního programu. Jedna faktura zabrala v průměru dvě minuty, takže na přepis padlo zhruba třicet hodin práce měsíčně. Chyby se objevovaly hlavně u zahraničních dodavatelů, kde se plete datum splatnosti s datem vystavení.

V říjnu jsme zapojili čtení faktur přes rozhraní účetního programu. Program si sám načte dodavatele, částku, DPH a splatnost a účetní jen potvrdí, že údaje sedí. U faktur od stálých dodavatelů to jde rychle, u nových dodavatelů je potřeba první fakturu zkontrolovat celou.

Po čtyřech týdnech trvá zpracování jedné faktury kolem dvaceti sekund. Ruční kontrola zůstala u dokladů nad padesát tisíc korun, protože tam chceme mít jistotu. Dva klienti posílají faktury jako fotky z telefonu a ty se pořád čtou špatně, takže je zatím zadáváme postaru.

Co bychom příště udělali jinak: s dodavateli bychom se dřív domluvili na posílání faktur ve formátu ISDOC. Ten program načte bez chyb a odpadá i kontrola splatnosti. Zatím tak posílá faktury asi třetina dodavatelů.

Náklady na rozšíření byly čtyři tisíce korun měsíčně za licenci a jeden den nastavení. Úspora práce vychází na zhruba pětadvacet hodin měsíčně, které teď účetní věnují konzultacím s klienty. Největší přínos ale vidíme v tom, že se faktury dostanou do systému do druhého dne, takže klienti mají přehled o cash flow dřív než dosud.

Pokud zvažujete totéž, začněte dodavateli, od kterých chodí nejvíc faktur. U nás to bylo pět firem, které dohromady tvořily skoro polovinu všech dokladů.
