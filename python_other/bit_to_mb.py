def bit_to_mb (invar):
    
    helpvar = []
    #vzroc pro prevod bitu na MB a
    MB_ = 1024.0**-2

    #provadi se konroly datovych typu, pro int a float se nic nemeni    
    if type(invar) is int: 
        return (MB_ * invar)
    
    elif type(invar) is float: 
        return (MB_ * invar)
    
    else:    
            #pokud vstupni hodnotou je string, prevede se na int, provede se vypocet a vysledek se zpatky prevede na string 
            if type(invar) is str:
                
                v = invar.split('_')
                f =''
                
                for i in v:    
                    MB = (MB_) * int(i)
                    f +=  str(MB) +"_"
                return f[:-1]
            
            
            else:
            
                #pokud datovy typ neodpovida stringu, int a ani float, potom se kontroluje, jestli se jedna o list a nebo tupple
                for i in invar:
                    MB = (MB_) * i
                    helpvar.append(MB)

                if type(invar) is list:
                  return helpvar
                
                elif type(invar) is tuple:
                  return tuple(helpvar)
                

        
mbinput = "1545465_454312"

print(bit_to_mb(mbinput))

mbinput = [1545465, 454312]

print(bit_to_mb(mbinput))


mbinput = (1545465, 454312)

print(bit_to_mb(mbinput))
