import pickle
import random

filename = 'betalinger.pk'

fodboldtur = {}

personbeløb = 4500


def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")


# TODONE: Gør det printede layout federe og mere overskueligt.
# TODONE: Gør så funktionen først kalder menu(), når brugeren skriver '1', for at bevare brugerens overblik.
# TODONE: Tilføj mere information for indbetalingerne - indbetalt beløb, det fulde beløb der skal
#  indbetales, manglende indbetalte beløb, alt sammen for hver person og for summen af alle.
# TODONE: fortæl hvilke 3 medlemmer der mangler at betale mest.
def printliste():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print("LISTE OVER INDBETALT SUM\n")

    indbetaltsum = 0
    medlemmer = 0
    indbetalingliste = []
    sejliste = []
    for item in fodboldtur.items():
        print(f'{item[0]}s indbetalings-data:')
        print(f'Indbetalt beløb: {fodboldtur[item[0]]}/{personbeløb},-. Manglende indbetaling: {personbeløb - fodboldtur[item[0]]},-\n')
        indbetaltsum += fodboldtur[item[0]]
        medlemmer += 1
        indbetalingliste.append(fodboldtur[item[0]])
        sejliste.append((item[0], fodboldtur[item[0]]))

    print(f'Summen af indbetalinger på holdet:')
    print(f'Indbetalt beløb: {indbetaltsum}/{personbeløb * medlemmer},-. Manglende indbetaling: {personbeløb * medlemmer - indbetaltsum},-')

    # CHATGPT gav mig denne seje linje kode der ses under :)
    sorteretsejliste = sorted(sejliste, key=lambda x: x[1])
    print('\nDe 3 personer der skylder mest:')
    nummer = 0
    for item in range(3):
        print(f'{item}: {sorteretsejliste[item][0]} - har indbetalt {sorteretsejliste[item][1]},- og mangler dermed at betale {personbeløb - sorteretsejliste[item][1]},-')
        nummer += 1
        if nummer == 4:
            break

    valg = input('\nSkriv 1 for at gå tilbage til MENU')
    if valg == '1':
        menu()
    else:
        print('Du har skrevet en ikke defineret kommando og sendes tilbage til menuen, prøv igen')
        menu()


# TODONE: Gør det printede layout federe og mere overskueligt.
# TODONE: Tilføj mulighed for at kalde en funktion for at lave indbetalinger.
def menu():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print("MENU\n")
    print("1: Print liste over betalinger")
    print("2: Lav indbetalinger")
    print("3: Administration")
    print("4: Afslut program")
    valg = input("\nIndtast dit valg:")
    if valg == '1':
        printliste()
    if valg == '2':
        make_deposit()
    if valg == '3':
        administration()
    if valg == '4':
        afslut()
    else:
        print('Du har skrevet en ikke defineret kommando, prøv igen')
        menu()



# TODONE: Lav en funktion til indbetalinger hvori man skal vælge mellem individuelle indbetalinger eller
# random indbetalinger eller om man vil gå tilbage til menuen.
def make_deposit():
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print("INDBETALING\n")
    print("1: Lav individuelle indbetalinger")
    print("2: Lav random (300-500) indbetalinger for alle personer")
    print("3: Gå tilbage til menu")
    valg = input("\nIndtast dit valg:")
    if valg == '1':
        print('_"1"_blev_valgt_så_nu_skal_der_laves_individuelle_indbetalinger_for_hver_person__________________________________________________________________')
        print("-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-V-")

        for item in fodboldtur.items():
            while True:
                try:
                    deposit = int(input(f'\nHvilket beløb skal indbetales for {item[0]}?'))
                    fodboldtur[item[0]] += deposit
                except ValueError:
                    print('Du har skrevet en ikke defineret kommando, prøv igen')
                    continue
                break
        menu()

    if valg == '2':
        for item in fodboldtur.items():
            deposit = random.randint(300, 500)
            fodboldtur[item[0]] += deposit
        menu()

    if valg == '3':
        menu()

    else:
        print('Du har skrevet en ikke defineret kommando og sendes tilbage til menuen, prøv igen')
        menu()


# TODO: Administrations funktion, for justering af ønskede indbetalte beløbe og tilføjelse af personer.
def administration():
    global personbeløb
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
    print("ADMINISTRATION\n")
    print(f"1: Vil du ændre den samlede pris pr person ({personbeløb})?")
    print("2: Tilføj ny person")
    print("3: Gå tilbage til menu")
    valg = input("\nIndtast dit valg:")
    if valg == '1':
        while True:
            try:
                personbeløb = int(input('\nIndtast den nye samlede pris:'))
            except ValueError:
                print('Du har skrevet en ikke defineret kommando, prøv igen')
                continue
            break
        menu()
    if valg == '2':
        # TODO: Tilføj person-tingeling
        menu()
    if valg == '3':
        menu()
    else:
        print('Du har skrevet en ikke defineret kommando og sendes tilbage til menuen, prøv igen')
        menu()


infile = open(filename, 'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()
