#převádí data z csv do sql insert statement
for a in *.csv; do echo "Generate:" $a  #prohledává v adresáři všechny soubory csv a název ukládá do proměnné
sed 's/\s*,*\s*$//g' $a> temp.csv # z csv (název je uložen $a) načte obsah do temporárního csv 
out=$(echo $a | cut -d"." -f 1) #z názvu csv souboru ořezává sufix .csv
outfil="$out.sql" 
columns=$(head -n 	1 temp.csv | sed 's/;/,/g' | tr -d "\r\n") #načtená hlavička a formátování oddělovače ";" na ","
tail -n +2 temp.csv | while read l ; do 
values=$(echo $l | sed "s/;/\'\,\'/g" | tr -d "\r\n") #načítá data od druhého řádků z temp.csv do proměnné
values=\'$values\'
echo "INSERT INTO $out ($columns) VALUES ($values);"
done > $outfil; done
rm temp.csv	
