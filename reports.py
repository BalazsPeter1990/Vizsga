import os,costs

class report:
   def __init__(self,cathegorys): 
        self.cathegorys = cathegorys
        self.found = False
        self.max = None
        self.min = None

   def choise_report(self):
    while True:
                try:
                    print("Kérem válaszon egy jelentés típust: \n\t1: Dátum szerint\n\t2: Név szerint\n\t3: Kategória szerint\n\t4: Az egyes kategóriák maximális fogyasztásának megjelenítése\n\t5: Az adott időszak maximális fogyasztásának megjelenítése\n\t6: Az egyes kategóriák minimális fogyasztásának megjelenítése\n\t7: Az adott időszak minimális fogyasztásának megjelenítése\n\t8: Kilépés".expandtabs(35))
                    choise= int(input(""))
                    if choise <1 or choise>8:
                         print("Nem jó számot adott meg. Próbálja újra.")
                         continue
                    
                except ValueError: 
                        os.system("CLS")
                        print("Nem számot adott meg. Próbálja újra.")
                        continue
                
                match choise:
                        case 1: 
                            self.date_report()
                        case 2: 
                            self.name_report()
                        case 3: 
                            self.cathegory_report()
                        case 4: 
                            self.maxcathegory_report()
                        case 5: 
                            self.maxtime_report()
                        case 6: 
                            self.mincathegory_report()
                        case 7: 
                            self.mintime_report()
                        case 8: break
         
   def date_report(self):
            self.found = False
            os.system("CLS")
            while True:
                        try:
                            self.x = costs.date(input("Kérem adjon meg egy dátumot: \n"))
                            if self.x.error: raise ValueError
                            else: break
                        except ValueError: continue
            print("*"*100)
            for key in self.cathegorys.keys():
                for i in self.cathegorys[key]:
                    self.y = i['Költség dátuma']
                    if str(self.y) == str(self.x):
                        self.found = True   
                        for key1,value in i.items():
                               if key1 != "Költség értéke": print(f"{key1}: {value}")
                               else: print(f"{key1}: {value} Ft")
                        print()
            if self.found == False: print("Nincs ilyen dátumú költség.")
            print("*"*100)
            x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
            if x == "": os.system('CLS')
        
           

   def name_report(self):
            self.found = False 
            os.system("CLS")
            self.x = input("Kérem adjon meg egy költségnevet: \n")
            print("*"*100)
            for key in self.cathegorys.keys():
                for i in self.cathegorys[key]:
                    if i['Költség megnevezése'] == self.x:
                        self.found = True     
                        for key1,value in i.items():
                                if key1 != "Költség értéke": print(f"{key1}: {value}")
                                else: print(f"{key1}: {value} Ft")
                        print()
            if self.found == False: print("Nincs ilyen nevű költség.")
            print("*"*100)
            x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
            if x == "": os.system('CLS')

   def cathegory_report(self): 
            self.found = False 
            os.system("CLS")
            self.x = input("Kérem adjon meg egy költségkategóriát: \n")
            print("*"*100)
            for key in self.cathegorys.keys():
                for i in self.cathegorys[key]:
                    if i['Költség kategóriája'] == self.x:
                        self.found = True     
                        for key1,value in i.items():
                                if key1 != "Költség értéke": print(f"{key1}: {value}")
                                else: print(f"{key1}: {value} Ft")
                        print()
            if self.found == False: print("Nincs ilyen költségkategória.")
            print("*"*100)
            x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
            if x == "": os.system('CLS')

   def maxcathegory_report(self): 
            os.system("CLS")
            x = 0
            y = None
            print("*"*100)
            for key in self.cathegorys.keys():
                if self.cathegorys[key]:
                    for i in self.cathegorys[key]:
                        if x < i["Költség értéke"]: 
                                x = i["Költség értéke"]
                                y = i['Költség megnevezése']
                    if y: print(f"A(z){key} kategória maximális fogyasztása:\n {x} Ft")
                    x = 0
                    y = None
                else: print(f"A(z){key} kategória még üres.")

            print("*"*100)
            x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
            if x == "": os.system('CLS')


   def mincathegory_report(self): 
            os.system("CLS")
            x = None
            y = None
            print("*"*100)
            for key in self.cathegorys.keys():
                if self.cathegorys[key]:
                    for i in self.cathegorys[key]:
                        if x == None: 
                                x = i["Költség értéke"]
                                y = i['Költség megnevezése']
                        elif x > i["Költség értéke"]: 
                                x = i["Költség értéke"]
                                y = i['Költség megnevezése']
                    if y: print(f"A(z){key} kategória minimális fogyasztása:\n {x} Ft")
                    x = 0
                    y = None
                else: print(f"A(z){key} kategória még üres.")

            print("*"*100)
            x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
            if x == "": os.system('CLS')

   def maxtime_report(self):
        os.system("CLS")
        while True:
                start = costs.date(input("Kérem adja meg a kezdő dátumot: \n"))
                if start.error: continue
                while True:
                        end = costs.date(input("Kérem adja meg a befejező dátumot: \n"))
                        if int(str(start).replace(".", ""))>int(str(end).replace(".", "")) : 
                              print("A kezdő dátum nem lehet nagyobb a vége dátumnál.")
                              continue
                        if end.error == False: break 
                break  
        start = int(str(start).replace(".", ""))
        end = int(str(end).replace(".", ""))
            
        for key in self.cathegorys.keys():
            for i in self.cathegorys[key]:
                     x = int(str(i['Költség dátuma']).replace(".", ""))
                     if x in range(start,end+1):
                          if self.max == None: self.max = i['Költség értéke']
                          elif i['Költség értéke']>self.max: self.max = i['Költség értéke']
        print("*"*100)
        if self.max == None: print("A megadott időszakban nincs megadva fogyasztás.")
        else: print(f"A megadott időszakban a maximális fogyasztás: {self.max} Ft")
        print("*"*100)
        x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
        if x == "": os.system('CLS')
            
   def mintime_report(self): 
        os.system("CLS")
        while True:
                start = costs.date(input("Kérem adja meg a kezdő dátumot: \n"))
                if start.error: continue
                while True:
                        end = costs.date(input("Kérem adja meg a befejező dátumot: \n"))
                        if int(str(start).replace(".", ""))>int(str(end).replace(".", "")) : 
                              print("A kezdő dátum nem lehet nagyobb a vége dátumnál.")
                              continue
                        if end.error == False: break 
                break  
        start = int(str(start).replace(".", ""))
        end = int(str(end).replace(".", ""))
            
        for key in self.cathegorys.keys():
            for i in self.cathegorys[key]:
                     x = int(str(i['Költség dátuma']).replace(".", ""))
                     if x in range(start,end+1):
                          if self.min == None: self.min = i['Költség értéke']
                          elif i['Költség értéke']<self.min: self.min = i['Költség értéke']
        print("*"*100)
        if self.min == None: print("A megadott időszakban nincs megadva fogyasztás.")
        else: print(f"A megadott időszakban a minimális fogyasztás: {self.min} Ft")
        print("*"*100)
        x = input("A jelentések menühöz való visszatéréshez nyomjon egy entert.")
        if x == "": os.system('CLS')