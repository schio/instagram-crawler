import pymysql
import DataBaseInfo
import json 


def food(items):
    db_info = DataBaseInfo.getDBInfo()
    connection = pymysql.connect(host = db_info['host'],
    port = db_info['port'], user = db_info['user'], password = db_info['password'],
    db = db_info['db'], charset = db_info['charset'])
    
    curs = connection.cursor(pymysql.cursors.DictCursor)

    sourceFoodName = items['sourceFoodName']
    targetFoodName = items['targetFoodName']
    sourceLang = items['sourceLang']
    targetLang = items['targetLang']
    summary1 = items['summary1']
    about = items['about']
    summary2 = items['summary2']
    urls = json.loads(items['urls'])
    urls = urls['urls']
    # sql = """INSERT INTO `Menu`(`sourceFoodName`, `sourceLang`, `targetLang`, `targetFoodName`, `summary1`, `about`, `summary2`) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    sql = """INSERT INTO Menu(sourceFoodName, sourceLang, targetLang, targetFoodName, summary1, about, summary2) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    curs.execute(sql, (sourceFoodName,sourceLang,targetLang,targetFoodName,summary1,about,summary2))

    connection.commit()
    sql = """select foodID from Menu where `sourceFoodName` = %s;"""
    curs.execute(sql, (sourceFoodName))
    rows = curs.fetchall()

    food_id = rows[0]['foodID']
    sql = """INSERT INTO Urls(url, foodID) VALUES (%s, %s)"""
    
    for url in urls:
        curs.execute(sql, (url, food_id))
    connection.commit()
    
    connection.close() # Closing a cursor just exhausts all remaining data.
