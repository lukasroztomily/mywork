    /*Účelem procedůry je generovat created statement v SQL pro existující tabulky. 
     Kód se může používat pro export, zalohování či duplikování existujících tabulek. */
    DECLARE
      TYPE tab_t IS TABLE OF VARCHAR2(35);
      tabsezn tab_t := tab_t('TABLE1',
                               'TABLE2',
                               'TABLE3',
                               'TABLE4'); --seznam objektů pro které vytváříme created statement
    
      tab_jmeno VARCHAR2(34);
    NULL_STRING EXCEPTION;
    PRAGMA
      EXCEPTION_INIT(NULL_STRING, -00936); 
      PROCEDURE gen_created(p_tab_jmeno VARCHAR2) IS
        slou_sez     VARCHAR2(4096) := null;
        created_sez     VARCHAR2(16096);
        ref_sloupec VARCHAR2(16096) := null;
        cur_sez   VARCHAR2(16000);
        cur_vystup  VARCHAR2(16000) := null;
        sloupec_jmeno     VARCHAR2(256);
        CURSOR c1 IS
        --********************************************************
          select i.column_name,
                 i.data_type,
                 i.data_length,
                 i.data_scale,
                 i.nullable,
                 i.column_id,
                 case
                   when cols.column_name is not null then
                    'P'
                   else
                    cols.column_name
                 end as PRIM_KEY
            from all_tab_columns i
          ----------------------------------------
            left join (select *
                         from all_constraints
                        where constraint_type = 'P') cons
              on i.table_name = cons.table_name
             and i.owner = cons.owner
          ----------------------------------------
            left join all_cons_columns cols
              on cons.constraint_name = cols.constraint_name
             and cols.owner = cons.owner
             and i.owner = cols.owner
             and i.column_name = cols.column_name
            where i.owner = 'SQL5' --nastavuje se schéma, ve kterém se nachází objekty pro které vytváříme created statement
             and i.table_name = UPPER(p_tab_jmeno)
          ----------------------------------------
           order by i.COLUMN_ID;
        --*********************************************************
        refcur sys_refcursor;
      BEGIN
        FOR i IN c1 LOOP
          sloupec_jmeno := i.column_name;
        /*Z metedatových tabulek se do created statementu kopiruje nastavení k jednotlivým tabulkám*/
          IF i.data_type in ('DATE', 'CLOB') AND i.nullable = 'N' THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || ' NOT NULL';
          
          ELSIF i.data_type in ('DATE', 'CLOB') AND I.PRIM_KEY is null THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type;
          
          ELSIF i.data_type in ('DATE', 'CLOB') AND I.PRIM_KEY is not null THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || ' NOT NULL PRIMARY KEY';
      
      ------------------------------------------------------------------------------------------------------------
          
          ELSIF i.data_type = 'NUMBER' AND i.data_scale is not null AND
                i.nullable = 'N' AND i.prim_key is not null THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || '(' || i.data_length || ',' ||
                             i.data_scale || ') NOT NULL PRIMARY KEY';
          
          ELSIF i.data_type = 'NUMBER' AND i.data_scale is not null AND
                i.nullable = 'N' AND i.prim_key is null THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || '(' || i.data_length || ',' ||
                             i.data_scale || ') NOT NULL ';
          
          ELSIF i.data_type = 'NUMBER' AND i.data_scale is not null AND
                i.nullable = 'Y' THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || '(' || i.data_length || ',' ||
                             i.data_scale || ')';
          
      ------------------------------------------------------------------------------------------------------------
           
          ELSIF i.nullable = 'N' AND i.PRIM_KEY is not null THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || '(' || i.data_length || ') ' ||
                             'NOT NULL PRIMARY KEY';
          
          ELSIF i.nullable = 'N' THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || '(' || i.data_length || ') ' ||
                             'NOT NULL';
          
          ELSIF i.nullable = 'Y' THEN
            slou_sez := slou_sez || ',' || sloupec_jmeno || ' ' ||
                             i.data_type || '(' || i.data_length || ')';
         
 
          END IF;
     
      
     ------------------------------------------------------------------------------------------------------------- 
        
        ref_sloupec := ref_sloupec || '||' || chr(39) || ',' ||
                             chr(39) || '||' || sloupec_jmeno;
        
        END LOOP;
       
   /***********************************************************************************************************************/
      slou_sez     := LTRIM(slou_sez, ',');
      ref_sloupec := SUBSTR(ref_sloupec, 8);
      created_sez   := 'CREATE TABLE DUPL_' || p_tab_jmeno || ' (' || slou_sez || ')'; --K původnímu názvu objetku je možné přidat prefix např.: "DUPL_"
        cur_sez := 'SELECT ' || ref_sloupec || ' FROM ' ||p_tab_jmeno;
        --DBMS_OUTPUT.PUT_LINE(ref_sloupec);
        --DBMS_OUTPUT.PUT_LINE(cur_sez);
        OPEN refcur FOR cur_sez;
        LOOP
          FETCH refcur
            INTO cur_vystup;
          IF refcur%rowcount <= 1 THEN
            cur_vystup := created_sez;
            DBMS_OUTPUT.PUT_LINE(cur_vystup || ';');
            --EXECUTE IMMEDIATE (cur_vystup); /*Zde se vykoná created statement, který je vygenerován procedurou*/
            EXIT;
          END IF;
          
     
      END LOOP;
       
        -- commit;
    /***********************************************************************************************************************/  
      Exception --ošetření chyb, které vznikly v rámci běhu procedůry
    when NULL_STRING then DBMS_OUTPUT.PUT_LINE( 'Tabulka ' ||p_tab_jmeno||' neexistuje!!'); 
       When others then
          DBMS_OUTPUT.PUT_LINE('Error=' || sqlerrm);
        
      END gen_created;
   ----------------------------------------------------------------------------------------------------------
   
    BEGIN                               
    
      FOR i IN tabsezn.FIRST .. tabsezn.LAST LOOP
        gen_created(tabsezn(i));
      END LOOP;
    
    END;
    /
