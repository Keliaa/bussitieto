from sys import exit
import folitieto

#Menu ja koko ohjelman sydän.
def main():
    print("Mitä haluat tehdä?")
    print("1) Näytä bussitietoja")
    print("2) Selvitä pysäkin nimi")
    print("3) Selvitä pysäkin numero")
    print("4) Kerro tietoa tästä ohjelmasta")
    print("5) Poistu ohjelmasta")
    try:
        x = input("Anna vaihtoehto (1, 2, 3, 4, 5): ")
        numero = int(x)

        if numero == 1:
            folitieto.bussitieto()
        elif numero == 2:
            folitieto.pysakkitietoNimi()
        elif numero == 3:
            folitieto.pysakkitietoNumero()
        elif numero == 4:
            avaaTiedosto()
        else:
            exit(0)
    except:
        print("")
        print("Anna oikea numero.")
        print("")
        main()

#Syöttää dokumentti.txt -tiedoston sisällön näytölle.
def avaaTiedosto():
    try:
        print("")
        tiedosto = open("dokumentti.txt",'r')
        for rivi in tiedosto:
            print (rivi)
        print("")
        main()
    except:
        print("Tiedostoa dokumentti.txt ei löydy.")

main()
