from urllib.request import urlopen
import gzip
import json
import datetime

#busseihin liittyvä URL
bussiUrl = "http://data.foli.fi/siri/vm/"

#pysäkkeihin liittyvä URL
pysakkiUrl = "http://data.foli.fi/siri/sm/pretty"

#Hakee busseista tiedot
def bussitieto():
    data = urlopen(bussiUrl).read()
    data = gzip.decompress(data)
    data = data.decode('utf-8')
    obj = json.loads(data)

    vehicles = []
    monitored = {}
    item2 = ""
    try:
        numero = input("Anna bussinumero: ")
        oikeat = []
                
        for item in obj['result']['vehicles']:
            vehicles.append(item)

        for vehicle in vehicles:
            monitored[vehicle] = obj['result']['vehicles'][vehicle]['monitored']

        for item2 in vehicles:
            if monitored[item2] == True:
                if obj['result']['vehicles'][item2]['lineref'] == numero:
                    oikeat.append(item2)

        index = 1
        print("\nBussi numeroa", numero, "on olemassa", len(oikeat), "kappaletta.\nMinkä näistä valitset kun seuraava pysähdys on:\n")
            
        for oikeaBussi in oikeat:
            print(str(index) + ".", obj['result']['vehicles'][oikeaBussi]['next_stoppointname'], "")
            index += 1

        oikeaNumero = input("Anna haluamasi numero: ")
        oikeaNumero = int(oikeaNumero)
            
        aika = obj['result']['vehicles'][oikeat[oikeaNumero-1]]['next_expectedarrivaltime']
        aika2 = obj['result']['vehicles'][oikeat[oikeaNumero-1]]['next_aimedarrivaltime']

        muokattuAika = datetime.datetime.fromtimestamp(int(aika)).strftime('%M:%S')
        muokattuAika2 = datetime.datetime.fromtimestamp(int(aika2)).strftime('%M:%S')

        a1 = datetime.datetime.strptime(muokattuAika, "%M:%S")
        a2 = datetime.datetime.strptime(muokattuAika2, "%M:%S")

        diff = (a1 - a2)
            
        if a1 > a2:
            print("Linja", numero, "-", obj['result']['vehicles'][oikeat[oikeaNumero-1]]['destinationname'], "on myöhässä:", diff)
            print("Ja on kulkenut matkasta", str(obj['result']['vehicles'][oikeat[oikeaNumero-1]]['percentage']) + "%")
        elif a2 < a1:
            print("Linja", numero, "-", obj['result']['vehicles'][oikeat[oikeaNumero-1]]['destinationname'], "on etuajassa:", diff)
            print("Ja on kulkenut matkasta", str(obj['result']['vehicles'][oikeat[oikeaNumero-1]]['percentage']) + "%")
        elif a1 == a2:
            print("Linja", numero, "-", obj['result']['vehicles'][oikeat[oikeaNumero-1]]['destinationname'], "on normaalissa ajassa.")
            print("Ja on kulkenut matkasta", str(obj['result']['vehicles'][oikeat[oikeaNumero-1]]['percentage']) + "%")
            
    except:
        print("")
        print("Jokin meni vikaan.")

    print("")    
    import menu
    menu.main()

#Antaa pysäkin nimen
def pysakkitietoNimi():
    response = urlopen(pysakkiUrl).read().decode('utf8')
    obj = json.loads(response)
    try:
        numero = input("Anna pysäkkinumero: ")
        for item in obj:
            if item == numero:
                print("Pysäkin nimi on:", obj[item]['stop_name'])
    except:
        print("")
        print("Anna oikea numero.")
			 
    print("")
    import menu
    menu.main()

#Antaa pysäkin numeron
def pysakkitietoNumero():
    response = urlopen(pysakkiUrl).read().decode('utf8')
    obj = json.loads(response)
    try:
        nimi = input("Anna pysäkin nimi: ")
        nimi = nimi.capitalize()
        for item in obj:
            if obj[item]['stop_name'] == nimi:
                print("Pysäkkinumero on:", item)
    except:
        print("")
        print("Anna oikea numero.")

    print("")
    import menu
    menu.main()
