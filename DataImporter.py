import pandas as pd
import numpy as np

class DataImporter:
    def __init__(self):
        self.teams = pd.read_csv('Data/Teams.csv')
        self.regularSeasonStats = pd.read_csv('Data/RegularSeasonDetailedResults.csv')
        #print(self.teams.columns.values)
        #print(self.regularSeasonStats.columns.values)

    def getTeamId(self, teamName):
        ids = self.teams.loc[self.teams['TeamName'] == teamName].TeamID.values
        if len(ids) > 0:
            return ids[0]
        return False

    def getGameData(self, a, b, year):
        aId = self.getTeamId(a)
        bId = self.getTeamId(b)
        stats = self.regularSeasonStats.loc[(self.regularSeasonStats['WTeamID'] == aId) & (self.regularSeasonStats['Season'] == year) & (self.regularSeasonStats['LTeamID'] == bId)]
        if stats.shape[0] is 0:
            stats = self.regularSeasonStats.loc[(self.regularSeasonStats['WTeamID'] == bId) & (self.regularSeasonStats['Season'] == year) & (self.regularSeasonStats['LTeamID'] == aId)]
        if stats.shape[0] is 0:
            return False
        return stats

    def getAllData(self, teamName):
        teamId = self.getTeamId(teamName)
        dataWon = self.regularSeasonStats.loc[self.regularSeasonStats['WTeamID'] == teamId]
        dataLost = self.regularSeasonStats.loc[self.regularSeasonStats['LTeamID'] == teamId]
        data = pd.concat([dataWon, dataLost])
        return data

    def getData(self, teamName, year):
        teamId = self.getTeamId(teamName)
        dataWon = self.regularSeasonStats.loc[(self.regularSeasonStats['WTeamID'] == teamId) & (self.regularSeasonStats['Season'] == year)]
        dataLost = self.regularSeasonStats.loc[(self.regularSeasonStats['LTeamID'] == teamId) & (self.regularSeasonStats['Season'] == year)]
        data = pd.concat([dataWon, dataLost])
        return data

