# Otuskauppa
Nettipeli jossa voi ostaa (ja myydä) fantasiaotuksia. Ajatuksena oli, että olisin voinut piirtää ainakin osan otuksista itse. 

Tämän hetkiset ominaisuudet:
- Luo käyttäjä
- Kirjaudu sisään


Mahdolliset tulevat ominaisuudet:
- Korjaa evästeet (tällä hetkellä kirjautuu automaattisesti vanhoilla tunnuksilla)
- Luo toimiva osoite (niin että ei tarvitse ajaa terminaalista)
- Osta otus, otus tallentuu omaan tietokantaan
- Peliraha, joka laskee otuksen hinnan verran kun ostat otuksen
- Omat otukset sivu
- Ruokapalkki, joka laskee 10% päivässä
- Sivu jolta voi "ostaa" pelirahaa
- Kertakäyttöiset/monikäyttöiset "lahjakoodit"
- Sivu jolla voit myydä ja ostaa toisten pelaajien myynnissä olevia otuksia
- Mahdollisesti jokin minipeli, josta saa myös rahaa

Risuaidalla merityt osat koodia ovat vielä työn alla

Miten saan sovelluksen Toimimaan?

- Varmista, että Python3 on asennettuna
Linkki pythonin asennukseen https://www.python.org/downloads/
- Luo Otuskauppa kansioon .env tiedosto ja lisää sinne seuraavat rivit:
  ![image](https://github.com/Sampinen/Otuskauppa/assets/149503786/405b4c88-ed26-48b0-8b9b-897479c1a30c)
Asenna psql seuraavan linkin avulla: https://github.com/hy-tsoha/local-pg
- Siirry terminaaliin
- tarkista, että olet oikeassa kansiossa esim. cd ./Downloads/Otuskauppa/
- Suorita seuraavat komennot terminaalissa:
python3 -m venv venv
source venv/bin/activate
- Asenna tarvittavat lisäosat seuraavilla komennoilla:
pip install flask
pip install flask-sqlalchemy
pip install psycopg2
pip install python-dotenv
- Avaa uusi terminaali ja aja start-pg.sh
- Avaa vielä toinen uusi terminaali kirjoittamalla psql
- Palaa takaisin ensimmäiseen terminaaliin ja aja komento: flask run

Huom! Kirjautumisessa on vielä ongelmia ja saatat joutua tyhjentämään välimuistin aloittaessasi uuden istunnon.
Tyhjennä välimuisti painamalla kolmea pistettä oikeassa yläreunassa ja sitten paina "clear browsing data" (Chromium)






