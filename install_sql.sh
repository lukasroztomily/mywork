#Provádí exekuci sql skriptů.
#Kopiruje vstupní soubory do temp adresáře a vkládá do každého sql souboru prompt text.
ECHO Checkout files of sql
mkdir temp
chmod 777 temp
for a in SQL/*.sql; do cp $a temp; done
for a in temp/*.sql; do echo -e "prompt Start processing of object:" "$a\n$(cat $a)"> $a; done
for a in temp/*.sql; do echo "prompt Finished processing of object:" $a | sed -e "s/temp[/]//" -e "s/.sql//" >> $a; done
for a in temp/*.sql; do sed -i -e "s/temp[/]//"  $a; done
for a in temp/*.sql; do sed  -i -e "s/.sql//" $a; done


ECHO Created installfile
#Vytváří instalační soubor pro sqlplus, ve kterém se vypíše seznam instalovaných sql souborů.
echo -e "spool logdb.log\n" >> tst.txt 
for a in temp/*.sql; do printf '%s\n'  @"$a" >> tst.txt; done
echo -e "\nspool off" >> tst.txt



#Připojování do databáze a vykonání instalačního souboru.
user="uživatel"
 
sqlplus $user/heslo@localhost:1521 <<! @tst.txt>>sqllog.log
whenever sqlerror exit 1;
exit
!

if [ $? = 0 ]; then
    echo Connect to database $user
else
    echo "Failed connect"
fi
#Výstupem skriptu je log o průběhu instalace: sqllog.log 
echo Compiliete process $user >> sqllog.log 
DATE=`date '+%m.%d.%Y %H:%M:%S'`
ECHO ******************************************END PROCESS $DATE "******************************************" >> sqllog.log  
ECHO "*******************************************************************************************************************************" >> sqllog.log
ECHO "*******************************************************************************************************************************" >> sqllog.log
ECHO "*******************************************************************************************************************************" >> sqllog.log
ECHO Remove installfile
rm -f -r tst.txt

rm -r temp
