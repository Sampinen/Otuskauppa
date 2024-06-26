# Otustarha
Nettipeli jossa keräillään fantasiaotuksia.

Tämän hetkiset ominaisuudet:
- Luo käyttäjä
- Kirjaudu sisään
- Osta otus, otus tallentuu omaan tietokantaan
- Peliraha, joka laskee otuksen hinnan verran kun ostat otuksen
-  Omat otukset sivu
-  Jokaisella pelin otuksella on nyt oma sivu
- Foorumi, jolle voi kirjoittaa palautetta ja jutella muiden sovelluksen käyttäjien kanssa
- Kertakäyttöiset/monikäyttöiset "lahjakoodit"

Muut parannukset:
- Uudet commit tägit ovat kuvaavampia (ei pelkkä default teksti) ja niitä on tehty tiheämpään tahtiin
- Nimi vaihdettu osuvammaksi, koska kyseessä ei ole varsinaisesti kauppa vaikka siinä voi ostaa asioita
- Koodia paranneltu siistimmäksi ja enemmän materiaalia vastaavaksi
- Sivu näytää nyt paremmalta visuaalisesti

Kesken:

- Otuksen nimeä voi vaihtaa
  
Mahdolliset tulevat ominaisuudet (saatan lisätä ominaisuuksia myöhemmin kurssin jälkeen):
- Valitettavasti SQL komennot eivät ole yhtä monipuolisia kuin olisi vaadittu, joten monipuolisemmin niitä :)
- Lisää taidetta
- Visuaalista parantelua
- Salasanan tulee sisätää sekä kirjaimia, että numeroita
- Luo toimiva osoite (niin että sovellusta ei tarvitse ajaa terminaalista)
- Ruokapalkki, joka laskee 10% päivässä
- Sivu jolta voi "ostaa" pelirahaa
- Sivu jolla voit myydä ja ostaa toisten pelaajien myynnissä olevia otuksia
- Mahdollisesti jokin minipeli, josta saa myös rahaa

Miten saan sovelluksen Toimimaan?

- Varmista, että Python3 on asennettuna
Linkki pythonin asennukseen https://www.python.org/downloads/
- Luo Otuskauppa kansioon .env tiedosto ja lisää sinne seuraavat rivit:
  ![image](https://github.com/Sampinen/Otuskauppa/assets/149503786/405b4c88-ed26-48b0-8b9b-897479c1a30c)
Asenna psql seuraavan linkin avulla: https://github.com/hy-tsoha/local-pg
- Siirry terminaaliin
- tarkista, että olet oikeassa kansiossa esim. /git/Otuskauppa
- Suorita seuraavat komennot terminaalissa:
python3 -m venv venv
source venv/bin/activate
- lataa tarvittavat lisäosat komennolla pip install -r requirements.txt
- Koita ajaa komento psql < schema.sql
Jos tämä ei toimi:
- Avaa uusi terminaali ja aja start-pg.sh
- Avaa vielä toinen uusi terminaali kirjoittamalla psql
- Aja psql < schema.sql uudestaan
- Palaa takaisin ensimmäiseen terminaaliin ja aja komento: flask run

Lahjakoodeja voi luoda ajamalla giftcodegenerator.py ennen kuin ohjelman ajaa Flashillä terminaalissa! Se luo myös automaattisesti giftcodes.txt nimisen tiedoston, josta voit helposti kopioida ja testata niitä sovelluksessa. Turvallisuuden kannalta kannattaa kenties siirtää sekä .text että .py tiedostot toiseen paikkaan sen jälkeen kun koodit on luotu, mutta tällä tuskin on suurempaa merkitystä, kun sovellusta testaa omalla koneella.




