import time

from time import gmtime, strftime

def parsertext (inputdatadef):
    splitstring1 = "{"
    splitstring = "' "+chr(92)+"                '"

    
    #vstupni hodnota se rozsplituje
    splitinputdata = inputdatadef.split(splitstring)
    
    arraytemp = [] 
    outputtuple = ()
    for ele in splitinputdata: 
          
        #splitovani v prvnim kroku nebylo dokonale, proto musime splitovat jeste jednou
        #timto splitovanim dosahneme, ze vstupni text jeste rozdelime na mensi prvky, se kterymi se da snadno pracovat 
        
        arraytemp.append(ele.split(splitstring1)) 

    
    i = 0
    
    #iterace v poli
    while len(arraytemp) > i:
        tr = arraytemp[i][1]
        i += 1
        
        #dosahli jsme toho, ze kazda veta je realizovana jako prvek v poli, ktery iterujeme
        #ted musime kazdy prvek rozdelit podle carek, abychom mohli efektivne pracovat s textem.
        help_ = tr.split(",")
    
        pohlavi = help_[0].replace('"','' )
        
        #cisteni textu od nezadoucich vyskytu
        jmeno1 = help_[1].split(" ")
        jmeno = str(jmeno1[1]).replace('"','' ) + ' '+str(jmeno1[0]).replace('"','' )
        rok = help_[2].replace('"','' ).replace(' ','' )
        byt = help_[3].replace('"','' ).replace('}','' ).replace(']','' )
        
        #zjistuji aktualni rok, abych mohl vypocitat vek
        year = time.strftime("%Y")
        
        osloveni = ''
        
        #pokud neni vyplnen rok narozeni nastavi se hodnota XXX, 
        #pokud rok narozeni je dostupny, odecte se od aktualniho roku
        
        if rok == '':
           rok = 0
           narozeni = 'XXX'
        
        if int(rok) > 0:
            narozeni = int(year) - int(rok)
     
        #nastavuje se hodnota osloveni dle pohlavi
        if str(pohlavi) == "Zena":
            osloveni = 'Paní '
        elif str(pohlavi) == 'Muz':
          osloveni = 'Pan '
        
        if byt == ' ':
           byt = ' neznámým'
        
        #upraveny vstupni text se radi do vety.
        text = osloveni+ jmeno+ ', ' +'bytem' +str(byt)+ ', '+ 've veku ' + str(narozeni) + ' let.'
        outputtuple = outputtuple + (text,)
    return outputtuple



inputdata = """[{"Muz","Novy Karel","1950" , "Praha"},' \                '{"Zena","Hladova Jana", "1992", ""},' \                '{"Muz","Roztomily Lukas", "", "Praha"},' \                '{"Muz","Janek Jan", "", "Ostrava"}]"""


print(parsertext(inputdata))
