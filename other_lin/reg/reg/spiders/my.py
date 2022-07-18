import scrapy
import json
import time
from scrapy.http import FormRequest
from reg.items import RegItem

class MySpider(scrapy.Spider):
    name = 'my'
    allowed_domains = ['zrsr.sk','registeruz.sk' ]
    start_urls = ['https://www.registeruz.sk/cruz-public/api/uctovne-jednotky?zmenene-od=2000-01-01&pravna-forma=101&pokracovat-za-id=0']

    def parse(self, response):     
         for p in response.json()['id']:
             url_ = 'https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id='+str(p)
             yield scrapy.Request(url = url_, callback=self.parse1) 
         if response.json()['existujeDalsieId']:
               urls = 'https://www.registeruz.sk/cruz-public/api/uctovne-jednotky?zmenene-od=2000-01-01&pravna-forma=101&pokracovat-za-id='+str(max(response.json()['id']))               
               yield scrapy.Request(url = urls, callback=self.parse) 
               
    def parse1(self, response):
        item = RegItem()
        if 'stav' not in response.json():
            if 'datumZrusenia' not in response.json():
                item['ico'] = response.json()['ico']
                item['nazovUJ'] = response.json()['nazovUJ']
                
                try:
                   idUctovnychZavierok =response.json()["idUctovnychZavierok"]
                   item['idUctovnychZavierok'] = response.json()['idUctovnychZavierok']
                   

                except KeyError:
                  idUctovnychZavierok = None
                
 
                try:
                  dic =response.json()["dic"]
                except KeyError:
                  dic = None
                  
                try:
                  ulica =response.json()["ulica"]
                except KeyError:
                  ulica = None
                  
                try:
                  mesto =response.json()["mesto"]
                except KeyError:
                  mesto = None
                  
                try:
                  psc =response.json()["psc"]
                except KeyError:
                  psc = None
                  

                yield {
                        'ico': response.json()['ico'],
                        'skNace': response.json()['skNace'],
                        'nazovUJ': response.json()['nazovUJ'],
                        'idUctovnychZavierok': idUctovnychZavierok,
                        'velkostOrganizacie': response.json()['velkostOrganizacie'],
                        'dic': dic,
                        'ulica': ulica,
                        'mesto': mesto,
                        'psc': psc,
                        'druhVlastnictva': response.json()['druhVlastnictva'],
                        'kraj': response.json()['kraj'],
                        'okres': response.json()['okres'],
                        'sidlo': response.json()['sidlo'],
                        'id_': response.json()['id']
                       
                       }
                
                


# =============================================================================
#     c = []
#     def start_requests(self):
#         f = open ('sample.json', "r")
#  
# 
#         data = json.loads(f.read())
#         f.close()
#         #for i in data['id']:
#         p = [1,2,3,6,7,8,10,11,12,13,16,17,19,21,23,25,26,27,29,30,31,35,36,37,39,41,45,46,47,48,50,51,52,53,54,55,58,59,60,61,64,66,68,70,73,75,76,78,79,80,81,82,84,87,88,89,90,91,92,93,94,96,97,99,101,102,103,104,106,107,109,110,111,112,118,119,122,123,124,127,128,129,130,131,132,134,135,136,138,139,140,141,145,146,147,148,149,150,151,154,156,159,160,162,163,164,165,167,168,169,170,171,172,174,175,176,177,178,179,181,183,187,188,189,190,191,192,193,194,196,197,198,199,201,202,203,204,205,207,208,214,217,219,221,222,223,225,226,227,228,230,231,232,233,234,235,236,238,241,242,243,244,246,249,250,251,255,256,257,258,259,260,262,264,265,268,269,270,271,272,273,274,275,278,279,280,282,283,285,287,289,291,292,294,298,300,301,302,304,306,308,310,311,313,314,316,317,318,319,320,322,323,325,327,329,330,331,332,333,335,336,338,339,342,344,348,349,350,352,353,355,356,357,358,359,360,361,363,366,367,369,371,373,375,377,378,380,381,382,383,384,385,386,388,389,390,391,392,393,394,398,400,401,403,404,405,407,408,409,410,413,416,417,418,419,423,426,428,430,432,436,437,438,439,440,445,446,449,455,456,457,459,460,462,463,465,467,468,471,473,474,475,477,478,481,483,485,486,487,489,490,492,493,494,495,496,497,500,502,503,504,505,506,507,508,509,511,513,514,515,516,517,518,520,522,525,526,527,529,530,532,534,535,536,538,539,540,542,543,545,547,551,553,555,557,558,559,561,562,564,566,568,569,570,571,572,576,577,578,580,581,582,584,585,588,589,590,591,593,594,595,596,598,599,600,601,603,604,605,607,608,611,614,616,617,618,620,621,625,629,630,634,635,637,638,639,640,641,642,643,644,645,646,647,650,652,654,656,657,660,662,665,666,667,671,673,676,677,680,681,683,686,688,690,693,694,696,698,701,702,703,704,705,706,708,709,712,714,715,716,719,720,721,723,725,727,730,731,733,734,735,736,738,739,740,741,745,746,748,749,750,752,754,755,757,760,762,763,764,767,768,769,770,773,774,776,779,781,783,784,786,787,793,794,798,799,800,801,802,803,804,805,806,807,808,810,811,812,815,816,819,821,822,823,824,828,829,830,832,833,835,837,838,839,840,842,848,849,852,854,855,856,857,858,861,863,866,867,870,872,874,876,878,879,880,881,882,884,885,886,887,888,893,894,896,898,899,900,901,902,906,907,910,911,912,914,916,917,919,921,923,924,925,926,927,928,931,932,933,934,935,936,938,939,941,942,943,945,948,949,950,951,952,954,955,957,961,962,965,966,967,968,969,970,974,977,978,979,982,983,984,985,986,989,990,991,992,993,997,1000,1002,1003,1004,1005,1006,1007,1008,1010,1014,1018,1019,1021,1025,1028,1030,1031,1033,1034,1035,1036,1037,1038,1039,1041,1043,1046,1048,1049,1051,1052,1053,1054,1057,1058,1059,1060,1062,1063,1064,1065,1066,1067,1068,1069,1070,1071,1072,1074,1077,1078,1081,1082,1084,1086,1087,1091,1093,1094,1097,1098,1099,1100,1101,1102,1104,1105,1106,1110,1111,1112,1115,1117,1118,1119,1120,1122,1124,1125,1126,1129,1130,1131,1134,1135,1137,1142,1143,1144,1145,1146,1147,1148,1149,1151,1153,1154,1155,1157,1158,1160,1161,1162,1164,1165,1166,1167,1168,1169,1170,1172,1174,1175,1176,1177,1178,1179,1180,1181,1182,1184,1185,1186,1192,1195,1196,1197,1198,1199,1203,1204,1205,1206,1207,1208,1211,1213,1214,1215,1216,1217,1220,1221,1224,1225,1226,1227,1230,1231,1232,1234,1236,1237,1238,1241,1242,1246,1248,1250,1252,1255,1256,1257,1258,1260,1261,1262,1263,1265,1266,1267,1268,1270,1271,1272,1275,1276,1278,1279,1281,1285,1288,1289,1294,1295,1296,1297,1300,1301,1302,1303,1306,1308,1311,1316,1318,1319,1320,1321,1322,1323,1324,1326,1327,1331,1332,1333,1335,1336,1337,1338,1339,1342,1343,1344,1348,1349,1350,1352,1354,1355,1357,1358,1359,1361,1362,1363,1364,1365,1367,1370,1372,1373,1376,1377,1379,1380,1381,1382,1386,1387,1389,1390,1391,1393,1394,1396,1397,1401,1402,1406,1407,1408,1409,1410,1411,1414,1415,1416,1420,1421,1422,1425,1428,1429,1431,1432,1433,1436,1438,1442,1444,1445,1449,1451,1452,1455,1457,1459,1460,1462,1463,1464,1465,1466,1468,1470,1472,1475,1476,1477,1478,1483,1484,1485,1487,1489,1490,1491,1492,1495,1496,1497,1499,1500,1501,1503,1504,1505,1506,1508,1510,1513,1514,1515,1516,1517,1520,1521,1524,1526,1529,1531,1533,1535,1538,1540,1541,1542,1543,1544,1546,1547,1551,1554,1555,1556,1558,1559,1560,1562,1563,1564,1566,1567,1568,1573,1574,1575,1578,1580,1581,1582,1584,1586,1587,1588,1589,1590,1592,1594,1595,1596,1597,1599,1600,1603,1604,1605,1606,1610,1611,1612,1616,1617,1619,1620,1621,1622,1624,1625]
#         #p = [1,2,3,6, 7, 8,10,11,12,13,16,17, 31,35,36,37,39,41,45,46 ]
#         for a in p:
#              urls = 'https://www.registeruz.sk/cruz-public/api/uctovna-jednotka?id='+str (a)
#              yield scrapy.Request(url = urls, callback=self.parse)
# 
#     def parse(self, response):
#         
#         if 'stav' not in response.json():
#             if 'datumZrusenia' not in response.json():
#                 self.c.append(response.json()['ico'])
#         yield {'ico': self.c}
# =============================================================================
            
# =============================================================================
#     def zrsr(self, response):
#         ico = response.meta['ico']
# 
#         set_forms ={
#             "__VIEWSTATE": response.css('#__VIEWSTATE::attr(value)').extract()[0],
#             "__VIEWSTATEGENERATOR": response.css('#__VIEWSTATEGENERATOR::attr(value)').extract()[0],
#             "__EVENTVALIDATION": response.css('#__EVENTVALIDATION::attr(value)').extract()[0],
#             "msg1": "IČO+musí+tvoriť+8+číslic!",
#             "tico":	ico,
#             "cmdVyhladat":"Vyhľadať"
#             }
#         yield FormRequest.from_response(response,
#                                 formdata=set_forms,
#                                 callback=self.parse1,  meta={'ico':ico}, method='POST')
#         
#     def parse1(self, response):
#         set_forms ={
#             "__VIEWSTATE": response.css('#__VIEWSTATE::attr(value)').extract()[0],
#             "__VIEWSTATEGENERATOR": response.css('#__VIEWSTATEGENERATOR::attr(value)').extract()[0]            
#             }  
#         #yield FormRequest.from_response('https://www.zrsr.sk/zr_vypis.aspx?ID=1&V=U', formdata=set_forms, method='POST', self.parse1)
#         yield FormRequest.from_response(response, formdata=set_forms, self.parse1,  meta={'ico':ico}, method='POST')
# =============================================================================
        
        
#    def parse2(self, response):    
#         yield {'response': response.body.decode("utf-8"), 'ico':response.meta['ico']}
