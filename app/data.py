
import pandas as pd

def generateResults():
    survey = pd.read_csv("./Data - csvToDB.Survey.csv")
    task = pd.read_csv("./Data - csvToDB.Tasks.csv")

    task.drop(columns=['E-mail', 'Description', 'MainFlow', 'AltFlow'], inplace=True)

    result = task.merge(survey, on='Code')

    result.to_csv('Result')