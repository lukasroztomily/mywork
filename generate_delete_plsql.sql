/*Procedura maže data v nastaveném intervalu pro vybrané tabulky*/
DECLARE
  TYPE tab_t IS TABLE OF VARCHAR2(35);
  tabsezn tab_t := tab_t('TABLE1', 'TABLE2'); --seznam tabulek, ve kterých se data budou mazat.
  table_nam VARCHAR2(34);
   NULL_STRING EXCEPTION;
    PRAGMA
      EXCEPTION_INIT(NULL_STRING, -00936); 
  PROCEDURE gen_delete(p_tab_jmeno VARCHAR2) IS
    maz_sez    VARCHAR2(16096);
    cur_sez  VARCHAR2(16000);
    ref_vys VARCHAR2(16000) := null;
    refcur           sys_refcursor;
    inter            integer := null;
  BEGIN
    inter := 3; --nastavení intervalu pro mazání dat.
    maz_sez   := 'DELETE FROM ' || p_tab_jmeno ||' WHERE load_date <= (sysdate-'||inter||')';
    cur_sez := 'SELECT DISTINCT load_date FROM ' || p_tab_jmeno ||' WHERE load_date <= (sysdate-'||inter||')';
   OPEN refcur FOR cur_sez;
    LOOP
      FETCH refcur
        INTO ref_vys;
             IF refcur%rowcount = 0 THEN EXIT;
             ELSIF refcur%rowcount >= 1 THEN
           EXECUTE IMMEDIATE (maz_sez);
           DBMS_OUTPUT.PUT_LINE(maz_sez || ';');
           COMMIT;
           EXIT;
           END IF;
    END LOOP;
    Exception --ošetření chyb, které vznikly v rámci běhu procedůry
		when NULL_STRING then DBMS_OUTPUT.PUT_LINE( 'Tabulka  neexistuje!!'); 
       When others then DBMS_OUTPUT.PUT_LINE('Error=' || sqlerrm);
  
  END gen_delete;
  -----------------------------------------------------------------------
BEGIN

  FOR i IN tabsezn.FIRST .. tabsezn.LAST LOOP
    gen_delete(tabsezn(i));
  END LOOP;

END;
