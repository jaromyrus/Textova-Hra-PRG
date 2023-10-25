import time
import random
print("Vítej v mé textové hře! Tvůj úkol je se dostat z šatny 3A do učebny měření! Tak honem ať nedostaneš 5 od Loserta!")

time.sleep(1)

šatna=input("Nacházíš se v šatně. Vidíš mřížové dveře chceš jít dál? \nANO \nNE \n ")

if šatna == "ano":
    chodbamezisatnami=input("Nacházíš se na chodbě mezi ostatními šatnami. Kam chceš jít? \nVLEVO \nVPRAVO \n ")
else:
    print("Nikam jsi nešel a dostal jsi 5.")

if chodbamezisatnami == "VLEVO":
    time.sleep(1)
    Laf=input("Jsi u LAFu vidíš schody a dveře na dvůr. Kam chceš jít? \nSCHODY \nDVEŘE \n ")
    if Laf == "SCHODY":
        time.sleep(1)
        patro=input("Nacházíš se v prvním patře, nalevo vidíš jazykové učebny a na pravo vidíš hodně učeben a na konci schody dolů. Kam chceš jít? \nJU \nSCHODY \n ")
        if patro == "SCHODY":
            time.sleep(1)
            schodydolu=input("Nacházíš se u schodů, chceš je sejít a přejít do druhé budovy kde se nachází automat a cesta k ELM1? \nANO \nNE \n ")
            if schodydolu == "ANO":
                time.sleep(1)
                automat=input("Nacházíš se u automatu, chceš zkusit štěstí a vydělat na automatu že dostaneš 2x KitKat za cenu 1? Nebo chceš jít dál na rozcestí u jídelny? \nAUTOMAT \nJIDELNA \n ")
                if automat == "AUTOMAT":
                    while True:
                        input("Stiskni Enter aby jsi koupil KitKat a padli ti 2 za cenu jednoho, musí ti padnout 3 stejná čísla!")

                        cislo1 = random.randint(1, 5)
                        cislo2 = random.randint(1, 5)
                        cislo3 = random.randint(1, 5)

                        print(f"Padla čísla: {cislo1}, {cislo2}, {cislo3}")

                        if cislo1 == cislo2 == cislo3:
                            print("Gratuluji! Získal jsi 2x KitKat za cenu jednoho!")
                            break
                        else:
                            print("Bohužel to nevyšlo, zkus to znova xd")
                    time.sleep(1)
                    jidelna = input("Po automatu ses vydal k jídelně. Vidíš před sebou 2 možnosti (jídelna je zavřená). Jít po schodech nahoru, nebo do laboratoří. Kam chceš jít? \nSCHODY \nLABORATOŘ \n ")
                    if jidelna == "SCHODY":
                        time.sleep(1)
                        chodbapredelmapavem = input("UŽ JSI SKORO TAM. Nyní máš na výběr 2 místnosti. PAV a ELM1. Kam chceš jít? \nPAV \nELM \n ")
                        if chodbapredelmapavem == "ELM":
                            time.sleep(1)
                            print("GRATULUJI došel jsi do ELM1 a nemáš 5 ta teprve přijde :)")
                        else:
                            time.sleep(1)
                            print("Těsně vedle, došel jsi do PAVU a ne jenom že jsi dostal 5 z ELM ale dostal jsi 5 z automatizace. GRATULUJI!")
                else: 
                    time.sleep(1)
                    jidelna = input("Vydal ses k jídelně. Vidíš před sebou 2 možnosti (jídelna je zavřená). Jít po schodech nahoru, nebo do laboratoří. Kam chceš jít? \nSCHODY \nLABORATOŘ \n ")
                    if jidelna == "SCHODY":
                        time.sleep(1)
                        chodbapredelmapavem = input("UŽ JSI SKORO TAM. Nyní máš na výběr 2 místnosti. PAV a ELM1. Kam chceš jít? \nPAV \nELM \n ")
                        if chodbapredelmapavem == "ELM":
                            time.sleep(1)
                            print("GRATULUJI došel jsi do ELM1 a nemáš 5 ta teprve přijde :)")
                        else:
                            time.sleep(1)
                            print("Těsně vedle, došel jsi do PAVU a ne jenom že jsi dostal 5 z ELM ale dostal jsi 5 z automatizace. GRATULUJI!")
                    else:
                        time.sleep(1)
                        print("Došel jsi do laboratoře, ale nic tam není, bohužel máš smůlu a dostal jsi 5. GRATULUJI!")
            else:
                time.sleep(1)
                ("Nesešel jsi schody a zůstal jsi tam do konce vyučovacího dne, dostal jsi 5 ze všech předmětů. GRATULUJI!")
        else:
            time.sleep(1)
            print("Došel jsi do JU, ale co tady sakra děláš, chytla tě Procházková a máš za 5 jak z ELM tak aji z angličtiny GRATULUJI!")
    else:
        time.sleep(1)
        print("O né dveře jsou zamčené a chytl tě Milan jak to zkoušíš otevřít, dostal jsi přes hubu a máš 5 GRATULUJI!")
else:
    time.sleep(1)
    chodbaven = input("Nacházíš se na chodbě u vstupu, máš možnost jít ven, nebo jít na schody které vedou do školy. Kam chceš jít? \nVEN \nSCHODY \n ")
    if chodbaven == "SCHODY":
        time.sleep(1)
        schodydolu=input("Nacházíš se u schodů, chceš je sejít a přejít do druhé budovy kde se nachází automat a cesta k ELM1? \nANO \nNE \n ")
        if schodydolu == "ANO":
                time.sleep(1)
                automat=input("Nacházíš se u automatu, chceš zkusit štěstí a vydělat na automatu že dostaneš 2x KitKat za cenu 1? Nebo chceš jít dál na rozcestí u jídelny? \nAUTOMAT \nJIDELNA \n ")
                if automat == "AUTOMAT":
                    time.sleep(1)
                    while True:
                        input("Stiskni Enter aby jsi koupil KitKat a padli ti 2 za cenu jednoho, musí ti padnout 3 stejná čísla!")

                        cislo1 = random.randint(1, 5)
                        cislo2 = random.randint(1, 5)
                        cislo3 = random.randint(1, 5)

                        print(f"Padla čísla: {cislo1}, {cislo2}, {cislo3}")

                        if cislo1 == cislo2 == cislo3:
                            print("Gratuluji! Získal jsi 2x KitKat za cenu jednoho!")
                            break
                        else:
                            print("Bohužel to nevyšlo, zkus to znova xd")
                    time.sleep(1)
                    jidelna = input("Po automatu ses vydal k jídelně. Vidíš před sebou 2 možnosti (jídelna je zavřená). Jít po schodech nahoru, nebo do laboratoří. Kam chceš jít? \nSCHODY \nLABORATOŘ \n ")
                    if jidelna == "schody":
                        time.sleep(1)
                        chodbapredelmapavem = input("UŽ JSI SKORO TAM. Nyní máš na výběr 2 místnosti. PAV a ELM1. Kam chceš jít? \nPAV \nELM \n ")
                        if chodbapredelmapavem == "ELM":
                            time.sleep(1)
                            print("GRATULUJI došel jsi do ELM1 a nemáš 5 ta teprve přijde :)")
                        else:
                            time.sleep(1)
                            print("Těsně vedle, došel jsi do PAVU a ne jenom že jsi dostal 5 z ELM ale dostal jsi 5 z automatizace. GRATULUJI!")
                else: 
                    time.sleep(1)
                    jidelna = input("Vydal ses k jídelně. Vidíš před sebou 2 možnosti (jídelna je zavřená). Jít po schodech nahoru, nebo do laboratoří. Kam chceš jít? \nSCHODY \nLABORATOŘ \n ")
                    if jidelna == "SCHODY":
                        time.sleep(1)
                        chodbapredelmapavem = input("UŽ JSI SKORO TAM. Nyní máš na výběr 2 místnosti. PAV a ELM1. Kam chceš jít? \nPAV \nELM \n ")
                        if chodbapredelmapavem == "ELM":
                            time.sleep(1)
                            print("GRATULUJI došel jsi do ELM1 a nemáš 5 ta teprve přijde :)")
                        else:
                            time.sleep(1)
                            print("Těsně vedle, došel jsi do PAVU a ne jenom že jsi dostal 5 z ELM ale dostal jsi 5 z automatizace. GRATULUJI!")
                    else:
                        time.sleep(1)
                        print("Došel jsi do laboratoře, ale nic tam není, bohužel máš smůlu a dostal jsi 5. GRATULUJI!")
        else:
            time.sleep(1)
            ("Nesešel jsi schody a zůstal jsi tam do konce vyučovacího dne, dostal jsi 5 ze všech předmětů. GRATULUJI!")
    else:
        time.sleep(1)
        krizovatka = input("Nacházíš se venku a jsi na křižovatce, když půjdeš rovno, půjdeš do Kauflandu, ale když půjdeš do leva vrátíš se zpátky do školy. Kam chceš jít? \nKAUFLAND \nŠKOLA \n ")
        if krizovatka == "ŠKOLA":
                time.sleep(1)
                jidelna = input("Přes bránu venku ses vydal přes dvůr a dveře na chodbu před jídelnou. Vidíš před sebou 2 možnosti (jídelna je zavřená). Jít po schodech nahoru, nebo do laboratoří. Kam chceš jít? \nSCHODY \nLABORATOŘ \n ")
                if jidelna == "SCHODY":
                        time.sleep(1)
                        chodbapredelmapavem = input("UŽ JSI SKORO TAM. Nyní máš na výběr 2 místnosti. PAV a ELM1. Kam chceš jít? \nPAV \nELM \n ")
                        if chodbapredelmapavem == "ELM":
                            time.sleep(1)
                            print("GRATULUJI došel jsi do ELM1 a nemáš 5 ta teprve přijde :)")
                        else:
                            time.sleep(1)
                            print("Těsně vedle, došel jsi do PAVU a ne jenom že jsi dostal 5 z ELM ale dostal jsi 5 z automatizace. GRATULUJI!")
                else:
                    time.sleep(1)
                    print("Došel jsi do laboratoře, ale nic tam není, bohužel máš smůlu a dostal jsi 5. GRATULUJI!")
        else:
            time.sleep(1)
            kaufland = input("Nacházíš se v Kauflandu, sice dostaneš za 5, protože měření už nestíháš, ALE můžeš si zahrát tuhle luxusní hru a ta se jmenuje: ODHADNI CENU RADEGAST 12!")
            cislo = random.randint(10, 30)
            pokusy = 0

            print("Čau alkoholiku, vítám tě ve hře kde budeš hádat cenu RADEGAST 12, hodně štěstí!")

            while True:
                pokusy += 1
                tip = int(input("Zadej číslo mezi 10 a 30: "))

                if tip < cislo:
                    print("Takhle levný není.")
                elif tip > cislo:
                    print("Takhle drahý není.")
                else:
                    print(f"Super! Uhádl jsi cenu RADEGASTA 12, která činí {cislo} a zabralo ti to pouze {pokusy} pokusů xDD .")
                    break
            time.sleep(1)
            print("Jsi u konce školního dne dostal jsi za 5 z každého předmětu, ale hlavní je, že máš svoji vysněnou RADEGAST 12 :)))))")