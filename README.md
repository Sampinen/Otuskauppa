# Otuskauppa
Nettipeli jossa voi ostaa (ja myydä) fantasiaotuksia. Ajatuksena oli, että olisin voinut piirtää ainakin osan otuksista itse. Valitettavasti sovellus on vielä kovin vaiheessa sillä muut kurssit ovat vieneet paljon aikaa, mutta koitan parhaani mukaan kiriä aikataulua.

Tämän hetkiset ominaisuudet:
- Luo käyttäjä
- Kirjaudu sisään
- Osta otus, otus tallentuu omaan tietokantaan
- Peliraha, joka laskee otuksen hinnan verran kun ostat otuksen
-  Omat otukset sivu
-  Jokaisella pelin otuksella on nyt oma sivu

  
Mahdolliset tulevat ominaisuudet:
- Foorumi, jolle voi kirjoittaa palautetta ja jutella muiden sovelluksen käyttäjien kanssa
- Lisää taidetta
- Visuaalista parantelua
- Otuksen nimeä voi vaihtaa
- Parempi nimi sovellukselle ja pelinsisäiselle valuutalle.
- Koodin parantelua (ainakin /buy osuus niin, että jokaiselle otukselle ei tarvitse kopioida samaa koodia uudestaan)
- Salasanan tulee sisätää sekä kirjaimia, että numeroita
- Luo toimiva osoite (niin että sovellusta ei tarvitse ajaa terminaalista)
- Ruokapalkki, joka laskee 10% päivässä
- Sivu jolta voi "ostaa" pelirahaa
- Kertakäyttöiset/monikäyttöiset "lahjakoodit"
- Sivu jolla voit myydä ja ostaa toisten pelaajien myynnissä olevia otuksia
- Mahdollisesti jokin minipeli, josta saa myös rahaa

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






