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

    def getAllTeamNames(self):
        return self.teams.TeamName.as_matrix()

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

    def normalizeGameData(self, teamName, data):
        teamId = self.getTeamId(teamName)
        result = data.copy()
        for i in range(data.shape[0]):
            if not np.equal(data[i,2], teamId):
                # Flip the winning and losing data so the matrix turns out correct
                result[i,3] = data[i,5]
                result[i,5] = data[i,3]
                result[i,8:20] = data[i,21:33]
                result[i,21:33] = data[i,8:20]
        return result

    def getDataMatrix(self, teamName, year):
        ''' matrix will follow the format
        Total Score, OTs, FG%, 3%, ft%, OR, DR, Ast, TO, Stl, Blk, Fouls, same for other team'''
        data = self.getData(teamName, year).as_matrix()
        data = self.normalizeGameData(teamName, data)
        totalScore = data[:,3] + data[:,5]
        wTwoPerc = (data[:,8]-data[:,10])/(data[:,9]-data[:,11])
        wThreePerc = data[:,10]/data[:,11]
        wFtPerc = data[:,12]/data[:,13]
        lTwoPerc = (data[:,21]-data[:,23])/(data[:,22]-data[:,24])
        lThreePerc = data[:,23]/data[:,24]
        lFtPerc = data[:,25]/data[:,26]
        result = [totalScore, data[:,7], wTwoPerc, wThreePerc, wFtPerc, data[:,14], data[:,15], data[:,16], data[:,17], data[:,18], data[:,19], data[:,20],
                                         lTwoPerc, lThreePerc, lFtPerc, data[:,27], data[:,28], data[:,29], data[:,30], data[:,31], data[:,32], data[:,33]]
        return result, data[:,3], data[:,5]

        
    def getAllDataMatrix(self, teamName):
        ''' matrix will follow the format
        Total Score, OTs, FG%, 3%, ft%, OR, DR, Ast, TO, Stl, Blk, Fouls, same for other team'''
        data = self.getAllData(teamName).as_matrix()
        data = self.normalizeGameData(teamName, data)
        totalScore = data[:,3] + data[:,5]
        wTwoPerc = (data[:,8]-data[:,10])/(data[:,9]-data[:,11])
        wThreePerc = data[:,10]/data[:,11]
        wFtPerc = data[:,12]/data[:,13]
        lTwoPerc = (data[:,21]-data[:,23])/(data[:,22]-data[:,24])
        lThreePerc = data[:,23]/data[:,24]
        lFtPerc = data[:,25]/data[:,26]
        result = [totalScore, data[:,7], wTwoPerc, wThreePerc, wFtPerc, data[:,14], data[:,15], data[:,16], data[:,17], data[:,18], data[:,19], data[:,20],
                                         lTwoPerc, lThreePerc, lFtPerc, data[:,27], data[:,28], data[:,29], data[:,30], data[:,31], data[:,32], data[:,33]]
        # result - teamName's full data
        # data[:,3] - teamName's score
        # data[:,5] - scores from every team that teamName played
        return result, data[:,3], data[:,5]

        