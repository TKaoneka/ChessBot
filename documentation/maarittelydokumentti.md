# ChessBot - Määrittelydokumentti (TKT)

Harjoitustyöni perustuu shakkibottiini ChessBot, jonka tavoite on pelata realistisesti eri elo-tasoilla ja aikarajoilla. ChessBotin ydin on shakkibottiin perustuva tekoäly.

## Ohjelmointikieli

Botin logiikka sekä todennäköinen käyttöliittymä toteudetaan Python-kielellä. 

Osaan kattavasti lukea Javaa, JS, C# ja Scalaa, sekä ymmärrän C:tä melko hyvin.

## Toteutettavat tietorakenteet ja algoritmit
ChessBot pääsijaisesti käyttää minimax-algoritmia (alpha-beta-karsinnan avustuksella). Algoritmi toimii parhaiten pelipuu-tietorakenteen avulla. Pelipuu on suunnattu verkko joka edustaa kaikki mahdolliset asemat. Verkon solmut ovat asemat ja suunnatut kaaret ovat liikkeet.

## Ratkaistu ongelmia 
Shakkibotilla opin navigoimaan monimutkaisia laskennallisia rajoituksia, erityisesti shakin aiheuttamat ongelmat (esim. shakin suuri skaala, sillä mahdollisia pelejä on n. 10¹²⁰), sekä botin logiikan kehittäminen (esim. miten botti osaa päättää mikä on paras liike tietyssä asemassa).

## Syötteet ja niiden käyttötarkoitukset
Shakkibotti vaatii ainakin seuraavat syötteet:
- Pelin ajankohtainen tilanne (solmu),
- Maksimisyvyys (eli monta liikettä tulevaisuuteen tuomitaan)
- Alpha- sekä beta-arvot
- Boolean-arvo, joka kertoo meille jos kyseisen pelaajan vuoro on maksimi- tai minimi-pelaaja
- Heurestiikka

Myös funktio, joka osaa kertoa kaikki mahdolliset lailliset liikkeet tietyssä asemassa (varsinaisen kätevä silloin kun kuningas on uhattuna).

## Aika- ja tilavaativuudet 
Minimax-algoritmin aikavaativuus on O(b^d), missä b (branch/haara) on keskimmäärin shakkipelin haarojen määrä per vuoro ja d (depth) pelipuun syvyys, eli kuinka pitkälle katsotaan pelin tilannetta. Alpha-beta-karsinnan avulla voidaan saavuttaa O(b^(d/2)).

Algoritmin tilavaativuus on O(bd).

## Lähteet
- Shakkiohjelmoinnin wiki: https://www.chessprogramming.org/Main_Page
- Minimax-algoritmin ja alpha-beta-karsinnan selitykset: https://www.youtube.com/watch?v=l-hh51ncgDI, https://materiaalit.github.io/intro-to-ai/part2/
- Tutoriaali shakkibotin koodin rakentamiseen: https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
- Esimerkki toimivasta shakkibotista: https://github.com/thomasahle/sunfish