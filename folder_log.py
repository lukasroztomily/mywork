
import os
from time import gmtime, strftime
import time
    


def get_me_info (filein = '', sortedin = 'zmena'):
    
    #podle vstupnich hodnot se nastavuje beh funkce (napr. podle jakeho sloupce se bude sortovat)
    #sortovani se apk nastavuje podle cisla, ktere odpovida pozici daného sloupce v tabulce
	
    if sortedin.lower() =='zmena':
       sortedbycolumn = 3
       
    if sortedin.lower() =='jmeno':
       sortedbycolumn = 0 

    if sortedin.lower() =='sufix':
       sortedbycolumn = 1

    if sortedin.lower() =='velikost':
       sortedbycolumn = 2
    else:
        sortedbycolumn = 3

       
    printconsole = ''
    lookupdir = filein
    
    #pokud uzivatel na vstupu nezada cestu k adresari, pak se cesta nastavi na pracovni adresar
    if lookupdir == '':
       lookupdir = os.getcwd()
    
    

 
    
    #nacita se obsah zvoleneho adresare
    lookupdirfetch = os.listdir(lookupdir)
    
    sortedpreaper = []
    getmaxlen = []
    MB_ = 1024.0**-2
    
    for x in lookupdirfetch:
       #nacita se velikost k jednotlivym souborum
       size_ = os.stat(lookupdir+'/'+x).st_size
       
       #nactena velikost souboru se prevede z bitu na MB a zaokrouhli se.
       sizehelp = round((MB_) * size_,3)
       
       #nazvy a sufixy souboru
       resultlookup = os.path.splitext(x)
       
       #cas posledni zmeny ve dvou formatech: datumovy a ciselny format
       timechange = time.ctime(os.path.getmtime(lookupdir+'/'+x))
       timesortform = os.path.getmtime(lookupdir+'/'+x)
       
       #vybira se sufix
       sufixhelp = resultlookup[1][1:]
    
        #pokud soubor nema sufix, potom je vyhodnocen jako subfolder se sufix dir   
       if  sufixhelp == '':
           sufixhelp = "dir"
       else:
            sufixhelp ='.'+sufixhelp
       
        #uklada se textove delka souboru do seznamu
       getmaxlen.append(len(resultlookup[0]))
       
       #tvori se radek do vysledne tabulky, prebyva jenom ciselny format  last change
       #radek se provizorne prevede do seznamu, aby se mohl sortovat
       rows = resultlookup[0]+','+ sufixhelp+','+ str(sizehelp)+','+str(timechange)+','+str(timesortform)
       rowssplit = rows.split(",")
       sortedpreaper.append(rowssplit)
    
    #sortovani podle parametru, ktery jsme nastavili na vstupu    
    sorted_list = sorted(sortedpreaper, key = lambda x:x[sortedbycolumn])
    
    
    names = []
    suffix = []
    size = []
    change = []
    
    for x in sorted_list:
    
    #usporadane pole iterujeme a rozrazujeme do prislusnych sezanmu
        
        names.append(x[0])
        suffix.append(x[1])
        size.append(x[2])
        change.append(x[3])
    
    


     #podle textove delky nazvu souboru se nastavuje format tabulky
    setformattable = max(getmaxlen)
     
     #pokud nejdelsi nazev je mensi 24, potom se nastavi default hodnota pro formatovani tabulky
    if setformattable < 24:
       setformattable = 26
    elif setformattable >= 24:
        setformattable = setformattable +2
    
    
    #nazvy sloupcu
    titles = ['Jmeno', 'Sufix', 'Velikost v MB', 'Naposledy změněno']
    
    #k prislusnym sloupcum se nacitaji data, ktere jsme nacetli vyse.
    data = [titles] + list(zip(names, suffix, size, change))
    
    
        
    for positionrow, fetchdata in enumerate(data):
     
        #zde se nastavuje format, ohraniceni a obsah hlavicky tabulky.
        lines = '|'+'|'.join(str(x).rjust(setformattable)for x in fetchdata)+'|'
    setpositiontitle = len(lines)-2
    title = 'get_me_info'
    setpositiontitlehelp = setpositiontitle//2-(len(title)//2)
    setpositiontitlehelp1 = len(lines) - len('-'*setpositiontitlehelp+title) 
    printtitle = '|'+'-'*setpositiontitlehelp+title+'-'*(setpositiontitlehelp1-2)+'|'
    printconsole += '\n' + printtitle         
    printconsole += '\n' +'|'+('-' * setpositiontitle)+'|'
    printconsole += '\n' + '|'+('-' * setpositiontitle)+'|'            
    
    for i, d in enumerate(data):

    
        if i == 0:
             
         #zde se nastavuje format, ohraniceni a nazev sloupcu   
             line = '|'+'|'.join(str(x+' '*(setformattable//2 - len(x)//2)).rjust(setformattable) for x in d)+'|'
        
             printconsole += '\n' + line
  
    
        if i > 0:
            
                     #zde se nastavuje format, ohraniceni a obsah radku
            line = '|'+'|'.expandtabs(1).join(str(x).rjust(setformattable) for x in d)+'|'
            printconsole += '\n' + line
    
            
        if i == len(names):
            
            #po iteraci vsech radku (tj. celkovy pocet prvku v poli names se rovna iterovane pozici) dojde k nastaveni paticky.
             setpositionfooter = len(line)-2
             setpositionfooterhelp = len(line)-1
             printconsole += '\n' + '|'+('-' * setpositionfooter)+'|'
             printconsole += '\n' + '|'.ljust(setpositionfooterhelp)+'|'
             setpositiontime = setpositionfooter//2-10
             localtime = strftime("%H:%M:%S %Y-%m-%d", gmtime())
             setpositiontime = setpositiontitle//2-(len(localtime)//2)
 
             printconsole += '\n' + '|'+'-'*setpositiontime+localtime+'-'*(setpositiontime)+'|'
         

    return printconsole

ttt = []

    
print(get_me_info('','asdsad'))




  


  

