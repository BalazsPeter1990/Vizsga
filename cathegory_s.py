import os

class cathegory:
    def __init__(self,cathegory_list):
        os.system("CLS")
        if cathegory_list:
            print("Már megadott költségkategóriák:")
            for key in cathegory_list.keys():
                print(f"\t{key}".expandtabs(31))
        else: print("Nincs megadva költségkategória.\n")
        self.cathegory = input("Kérem adjon meg egy új költségkategóriát: \n")
        if self.cathegory not in cathegory_list.keys():
            cathegory_list[self.cathegory] = []
            os.system("CLS")
        else: 
            os.system("CLS")
            print("Ilyen költségkategória már létezik. Adjon meg másikat.")

    def dell_cathegory(self,cathegorys):
        os.system("CLS")
        while True:
            if cathegorys == {}:break
            i=0
            print("Kérem válasza ki a törölni kívánt költségkategória számát: \n\t0: Kilépés".expandtabs(58))
            for key in cathegorys.keys():
                i+=1 
                print(f"\t{i}: {key}".expandtabs(58))
            try:
                x = int(input())
                if x == 0:
                    os.system("CLS")
                    break
                elif x>len(cathegorys.keys()) or x<0: raise IndexError
                else:
                    i=1
                    for j in cathegorys.keys():
                        if i == x : 
                            cathegorys.pop(j)
                            os.system("CLS")
                            break
                        else: i+=1
            except IndexError: 
                os.system("CLS")
                print("A megadott számú kategória nem létezik. Adjon meg új számot vagy lépjen ki 0-val.")
                continue
            except ValueError:
                os.system("CLS")
                print("Nem számot adott meg. Adjon meg egy számot vagy lépjen ki 0-val.")
                continue