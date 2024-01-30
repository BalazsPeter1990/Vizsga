import os

class cost:

    def __init__(self,cathegorys):
        self.cathegorys = cathegorys
        self.error = False
        self.found = True

    def input_cost(self,cathegory):
        self.cost_type = input("Kérem adja meg a költség kategóriáját:\n")
        os.system("CLS")
        if self.cost_type in cathegory.keys():
            cathegory[self.cost_type]
            while True:
                try:
                        new_name = input("Kérem neveze meg a költséget: \n")
                        new_date = date(input("Kérem addja meg a költség dátumát(év.hónap.nap.): \n"))
                        if new_date.error: continue
                        new_value = int(input("Kérem adja meg a költség értékét: \n"))
                        for i in self.cathegorys[self.cost_type]:
                                if new_name == str(i["Költség megnevezése"]) and str(new_date) == str(i["Költség dátuma"]) and str(new_value) == str(i["Költség értéke"]) and str(self.cost_type) == str(i['Költség kategóriája']):                               
                                                 self.found = False
                                                 break
                        if self.found:
                                cathegory[self.cost_type].append({"Költség megnevezése" : new_name})
                                if new_date:cathegory[self.cost_type][-1]["Költség dátuma"] = new_date
                                cathegory[self.cost_type][-1]["Költség értéke"] = new_value
                                cathegory[self.cost_type][-1]["Költség kategóriája"] = self.cost_type
                                os.system('Cls')
                        else: 
                              os.system('Cls')
                              print("A megadott adatok már rögzitve lettek.")                     
                        break
                except ValueError:
                    os.system("CLS")
                    print("Megadott érték nem szám.Próbálja újra.")
                    continue
                
        else:
            os.system("CLS") 
            print("Ilyen kategória nem lett még megadva. Ha valós akkor adja meg az 1. pontban, ellenben próbálja újra.")

class date:
    def __str__(self): return f"{self.value}"
    def __repr__(self): return str(self)
    def error_mod(self):
          self.error = True

    def __init__(self,value):
        self.error = False
        try:
            self.value1 = ""
            self.point = 0
            if value[-1]!="." or value[-4]!="." or value[-7]!=".": raise ValueError
            x=0
            while x!=len(value):
                if value[x] == ".":
                    if self.point==0:self.year=int(self.value1)
                    if self.point==1:self.mounth=int(self.value1)
                    if self.point==2:self.day=int(self.value1)
                    self.point +=1
                    self.value1=""
                    x+=1
                    continue
                else:
                    self.value1 = self.value1+value[x]
                    x+=1
                    continue
            match self.mounth:
                case 1: 
                        if self.day>31 or self.day<1: raise ValueError
                case 2: 
                        if self.day>29 or self.day<1: raise ValueError
                case 3: 
                        if self.day>31 or self.day<1: raise ValueError
                case 4: 
                        if self.day>30 or self.day<1: raise ValueError
                case 5: 
                        if self.day>31 or self.day<1: raise ValueError
                case 6: 
                        if self.day>30 or self.day<1: raise ValueError
                case 7: 
                        if self.day>31 or self.day<1: raise ValueError
                case 8: 
                        if self.day>31 or self.day<1: raise ValueError
                case 9: 
                        if self.day>30 or self.day<1: raise ValueError
                case 10: 
                        if self.day>31 or self.day<1: raise ValueError
                case 11: 
                        if self.day>30 or self.day<1: raise ValueError
                case 12: 
                        if self.day>31 or self.day<1: raise ValueError
                case _: raise ValueError
        except ValueError:
              os.system("CLS")
              print("A megadott érték nem felel meg a szabványos dátum formátumnak.")
              self.error_mod()
        self.value = value