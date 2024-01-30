import os,costs
class file:
    def __init__(self,cathegorys):
        self.cathegorys = cathegorys
        self.dictvalue = {}
        self.strvalue = ""
        self.found = False
        self.x = ""
    
    def export_txt(self):
            y = 0
            try:
                with open('koltsegek.txt', encoding="utf-8") as file:
                    self.input_lines = [line.strip().split(';') for line in file]
                    
                for i in self.input_lines:
                    for j in range(0,len(i)):
                        match j:
                            case 0: 
                                    self.dictvalue["Költség megnevezése"] = i[j]
                            case 1: 
                                    self.dictvalue["Költség dátuma"] = costs.date(i[j])
                            case 2: 
                                    self.dictvalue["Költség értéke"] = int(i[j])
                            case 3:  
                                    self.dictvalue["Költség kategóriája"] = i[j]
                                    self.x =i[j] 

                    if self.x in self.cathegorys.keys():                                  
                                os.system("CLS")          
                                self.cathegorys[self.x].append({})
                                for key,value in self.dictvalue.items(): self.cathegorys[self.x][-1][key] = value
                                print(f"A(z) {self.x} kategória frissitve.")
                    else: print(f"A(z) {self.x} kategória nem létezik. A feltöltéshez hozza létre.")


            except FileNotFoundError:
                                os.system("CLS")
                                print("Nem található koltsegek.txt nevű fájl. Kérem hozzon létre a beolvasáshoz.\n")
            except ValueError :
                            os.system("CLS")
                            print("Megadott érték nem szám.Kérem modósítsa a txt fájlt.")
    def import_txt(self):
            for key in self.cathegorys.keys():
                       for i in self.cathegorys[key]:
                            for value in i.values():
                                     self.strvalue+=str(value)+";"
                            self.strvalue = self.strvalue[:-1]+"\n"
            with open('koltsegek.txt','w', encoding="utf-8") as file: file.write(self.strvalue)
            os.system("CLS")
            print(f"A koltsegek.txt fájl frissitve.")