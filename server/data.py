import pandas as pd

def conectDB():
    # Connect to the database
    import sqlite3
    conn = sqlite3.connect('./database/participants.db')
    return conn

def generateResults():
    survey = pd.read_csv("./Data - csvToDB.Survey.csv")
    task = pd.read_csv("./Data - csvToDB.Tasks.csv")

    task.drop(columns=['E-mail', 'Description', 'MainFlow', 'AltFlow'], inplace=True)

    result = task.merge(survey, on='Code')

    result.to_csv('Result')