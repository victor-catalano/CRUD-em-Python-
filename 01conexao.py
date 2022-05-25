import mysql.connector

class conexao:
    def __init__(self):
        self.conexao =  mysql.connector.connect(host='localhost', database='login',user='root',password='')