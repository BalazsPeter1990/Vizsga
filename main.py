import sys,cathegory_s,costs,os,exportimporttxt,reports

def main(): 
    cathegorys = {}
    letters=["A","B","C","D","E","F","G"]
    while True:
        try:
            print("Kérem válaszon egy műveletett: \n\tA: Költségkategória hozzáadása\n\tB: Költségkategória törlése\n\tC: Költség megadása\n\tD: Költségek kiírása koltsegek.txt fájlba\n\tE: Költségek beolvasás koltsegek.txt fájlból\n\tF: Jelentések készítése\n\tG: Kilépés".expandtabs(30))
            choise = input()
            choise=choise.upper()
            if choise not in letters: raise IndexError
            match choise:
                case "A":
                    a = cathegory_s.cathegory(cathegorys)
                    continue

                case "B":
                    if cathegorys: a.dell_cathegory(cathegorys)
                    else: 
                        os.system("CLS")
                        print("Töltsön fel elöbb költségkategóriát.\n")
                    continue

                case "C":
                    if cathegorys: 
                        os.system("CLS")
                        b = costs.cost(cathegorys)
                        b.input_cost(cathegorys)
                    else: 
                        os.system("CLS")
                        print("Töltsön fel elöbb költségkategóriát.\n")
                    continue

                case "D":
                    find = False
                    for i in cathegorys.values():
                        for j in i:
                            if i: 
                                find = True
                                os.system("CLS")
                                c = exportimporttxt.file(cathegorys)
                                c.import_txt()
                    if find == False: 
                        os.system("CLS")
                        print("Töltsön fel elöbb költséget.\n")
                    continue
  
                case "E":
                    if cathegorys:
                                os.system("CLS")
                                c = exportimporttxt.file(cathegorys)
                                c.export_txt()
                    else: 
                        os.system("CLS")
                        print("Töltsön fel elöbb költségkategóriát.\n")
                    continue
                 
                case "F":
                    find = False
                    for i in cathegorys.values():
                        for j in i:
                            if i: 
                                find = True
                                os.system("CLS")
                                d = reports.report(cathegorys)
                                d.choise_report()
                                os.system('CLS')
                    if find == False: 
                        os.system("CLS")
                        print("Töltsön fel elöbb költséget.\n")
                    continue

                case "G":
                    os.system('CLS')
                    print('Viszontlátásra.')
                    break

        except IndexError:
            os.system("CLS")
            print("Nincs ilyen művelet.Kérem válaszon újat vagy lépjen ki.")
            continue

if __name__ == "__main__": sys.exit(main())