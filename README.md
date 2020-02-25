# bussitieto
Lukiossa vuonna 2016 tehty python-projekti.

1. Kuvaus ja analysointi
Kyseinen ohjelma pystyy seuraamaan yksittäisten bussien ja pysäkkien tietoja Föli -API:a hyväksikäyttäen (http://data.foli.fi/doc/index). Mahdollinen laajennus voisi olla pysäkkien aikataulut ja niiden vertaaminen bussien aikatauluihin.

2. Ratkaisuperjaate
Ohjelma hakee netin kautta Föli API:sta tietoa, joka tulee Json -muodossa ja syöttää ne käyttäjälle ymmärrettyyn muotoon käyttäen json, urllib, time- ja date moduulia (löytyvät Pythonista). Föli API:n Vehicle Monitoring -osio palauttaa tiedot muodossa, josta ne on purettava ja dekoodattava.

3. Ohjelma ja sen osat
Ohjelma koostuu kahdesta moduuliista. Ensimmäinen toimii menuna, josta voi valita mieleisensä toiminnon. Toisessa moduulissa on monimutkaisempaa Föli API:in liittyvää koodia ja sen muokkaamista.
Föli API -moduulissa on kolme funktiota. Yksi niistä antaa tietoa busseista, toinen pysäkin nimesta ja kolmas pysäkin numerosta.
Menu -moduulissa on kaksi funktiota: itse menu funktio ja toinen, joka avaa tämän tiedoston.

4. Testaus
Föli API -osaa on testattu enemmän ja testausten aikana voi huomata, että ongelmia tulee jos Föli API ei toimi (esimerkiksi internet yhteys, päivitys) tai käyttäjän internet yhteydessä on ongelmia.
