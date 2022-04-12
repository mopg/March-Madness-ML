import numpy as np
import pandas as pd

teams_pd = pd.read_csv('Data/KaggleData/Teams.csv')

def predictGame(team_1_vector, team_2_vector, home, modelUsed):
    diff = [a - b for a, b in zip(team_1_vector, team_2_vector)]
    diff.append(home)
    if hasattr(modelUsed, 'predict_proba'):
        return modelUsed.predict_proba([diff])[0][1]
    elif hasattr(modelUsed, 'predict'):
        return modelUsed.predict([diff])[0]
    else:
        raise AttributeError("Model does not have expected prediction method")

def loadTeamVectors(years):
    listDictionaries = []
    for year in years:
        curVectors = np.load("Data/PrecomputedMatrices/TeamVectors/" + str(year) + "TeamVectors.npy", allow_pickle=True).item()
        listDictionaries.append(curVectors)
    return listDictionaries


def findWinner(team1, team2, modelUsed):
    year = [2022]
    teamVectors = loadTeamVectors(year)[0]
    values_1 = teams_pd[teams_pd['TeamName'] == team1]
    if len(values_1) == 0:
        print(f'Team {team1} not found')
        raise ValueError
    team1Vector = teamVectors[int(values_1.values[0][0])]

    values_2 = teams_pd[teams_pd['TeamName'] == team2]
    if len(values_2) == 0:
        print(f'Team {team2} not found')
        raise ValueError
    team2Vector = teamVectors[int(values_2.values[0][0])]

    prediction = predictGame(team1Vector, team2Vector, 0, modelUsed)
    if (prediction < 0.5):
        return team2, 1 - prediction
    else:
        return team1, prediction
