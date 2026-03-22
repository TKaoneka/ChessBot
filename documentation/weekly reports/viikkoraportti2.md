# Viikkoraportti 2

Tällä viikolla loin harjoitustyön pohja, eli kehitin minimax-algoritmin alpha-beta-karsinnalla. Kyseinen funktio joko yrittää maksimoida (tai minimoida) arvionnin tietystä asemasta.

Tässä ohjelman tämänhetkinen tilanne:

Valkeat nappulat yrittää maksimoida arviointia, ensiksi käymällä kaikki mahdolliset asemat eli solmun lapset tietyyn syvyyteen asti. Koodi toimii seuraavasti:

```python
def minimax(position, max_depth, maximizing_player, alpha, beta):
    if not position.children or max_depth == 0:
        return evaluate(position)

    if maximizing_player:
        value = float("-inf")

        for child in position.children:
            value = max(value, minimax(child, max_depth - 1, False, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
```
Funktio toimii samanlaisesti mustien nappuloiden kanssa; arvo mitä etsitään mielummin minimiarvo.

Funktio tutkii jos ollaa maksimisyvyydellä tai jos kyseinen asema on viimeinen mahdollinen liike (shakkimatti). Kyseinen funktio muuten jatkaa arvojen tutkimista jos ei ole maksimisyvyys tai viimeinen liike, muuten jatkaa minimax-algoritmin toteuttamista aseman mahdollisiin lopputuloksiin:

```python
def evaluate(position): 
    piece_values = {
        "white_pawn": 100,
        "white_rook": 500,
        "white_knight": 320,
       "white_bishop": 330,
        "white_queen": 900,
        "white_king": 20000,
        "black_pawn": -100,
        "black_rook": -500,
        "black_knight": -320,
       "black_bishop": -330,
        "black_queen": -900,
        "black_king": -20000
    }
    
    material_score = 0

    for row in position:
        for piece in row:
            material_score += piece_values.get(piece, 0)

    return material_score
```
Kyseinen arviointi funktio, sekä funktio parhaimman liikkeen etsimiseen eivät ole vielä valmiita.

Ohjelma on tällä viikolla hitaasti edistynyt. Yksikkötestit ja testikattavuus varsinkin puuttuvat sekä main-funktio, jolla saa ohjelman kokeiltua

Opin aseman arvioinnista sekä liikkeiden tekemistä (vaikka funktio liikkeiden toteuttamiseen eivät vielä ole toteutettu). 

Epäselväksi vielä jäi shakkilaudan alustamisesta. Liikkeiden tekeminen vaikuttaa haastavalta (varsinkin jos harkitaan erikoissäännöt kuten linnoitus). Myös kurssilla käytetty tekoälyalusta ei toimi; kysyn ensi viikon loppuun mennessä apua tarvittaessa.

Seuraavaksi kehitän yksikkötestit ja testikattavuuden tutkimista sekä tekoälyalustalla sopiva komento. Lisäksi kehitän loppuun funktion, joka palauttaa parhaimman liikkeen, sekä yritän saada suhteellisen toimivan shakkipelin. Jos nämä onnistuvat, aloitan heurestiikan ja erikoissääntöjen käyttöönottoa.
