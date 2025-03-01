import pymysql
import os

def create_database():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root')
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS BDD")
        connection.commit()
        connection.close() 
    except Exception as e:
        print("Erreur lors de la creation de la base de données")
        print(e)

def create_table_professeur():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='BDD')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Professeur (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
        connection.commit()
        connection.close()
    except Exception as e:
        print("Erreur lors de la creation de la table Professeur")
        print(e)
def create_table_etudiant():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='root',
                                     db='BDD')
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Etudiant (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
        connection.commit()
        connection.close()
    except Exception as e:
        print("Erreur lors de la creation de la table Etudiant")
        print(e)

def main():
    create_database()
    create_table_professeur()
    create_table_etudiant()
    print("Base de données et tables créées avec succès")
if __name__ == "__main__":
    main()