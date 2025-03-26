import pymysql
from pymongo import MongoClient

class PlayerOperations:
   def addnewplayertodb(self,nm,age,country,team,price):
       con=pymysql.connect(host='mysql-python-adesh-python.c.aivencloud.com',port=18521,user='avnadmin',password='AVNS_dBnrUQNBCl6YJQKxI5X',database='Adeshdb')
       curs=con.cursor()
       curs.execute("insert into IPL_Players(name,age,country,ipl_team,price_in_2025) values('%s',%d,'%s','%s',%.1f)" %(nm,age,country,team,price))
       con.commit()
       con.close()
       return 'new player added successfully'

   def deleteplayer(self,pid):
           con=pymysql.connect(host='mysql-python-adesh-python.c.aivencloud.com',port=18521,user='avnadmin',password='AVNS_dBnrUQNBCl6YJQKxI5X',database='Adeshdb')
           curs=con.cursor()
           curs.execute("delete from IPL_Players where name='%s'" %pid)
           con.commit()
           con.close()
           return 'player deleted successfully'

   def searchplayerfromteam(self,team):
           dic={}
           con=pymysql.connect(host='mysql-python-adesh-python.c.aivencloud.com',port=18521,user='avnadmin',password='AVNS_dBnrUQNBCl6YJQKxI5X',database='Adeshdb')
           curs=con.cursor()
           curs.execute("select * from IPL_Players where ipl_team='%s'" %team)
           data=curs.fetchall()
           
           con.close()
           return data

   def allplayerlist(self):
        con=pymysql.connect(host='mysql-python-adesh-python.c.aivencloud.com',port=18521,user='avnadmin',password='AVNS_dBnrUQNBCl6YJQKxI5X',database='Adeshdb')
        curs=con.cursor()
        curs.execute("select * from IPL_Players")
        data=curs.fetchall()
        
        con.close()
        return data

        
   def playerhistry(self,nm):
        
           client=MongoClient("mongodb+srv://adesh:mongodb0212@adeshcluster.sbnbu.mongodb.net/?retryWrites=true&w=majority&appName=Adeshcluster")
           db=client.ipl_projectdb
           coll=db["playerhistry"]
           data=coll.find_one({"playernm":nm})
           return data

        
                




    



       



