from sklearn import linear_model as lm
import DataImporter as di
import numpy as np

class Predictor:    
    def analyze(self, teamOne, teamTwo):
        # Acquire data from DataImporter
        dataImp = di.DataImporter()
        teamOne2017, teamOne2017Score, teamOne2017Opponent = dataImp.getDataMatrix(teamOne, 2017)
        teamOneAll, teamOneAllScore, teamOneAllOpponent = dataImp.getAllDataMatrix(teamOne)
        teamTwo2017, teamTwo2017Score, teamTwo2017Opponent = dataImp.getDataMatrix(teamTwo, 2017)
        teamTwoAll, teamTwoAllScore, teamTwoAllOpponent = dataImp.getAllDataMatrix(teamTwo)
        # AllTeams
        
        # Generate models
        linear = lm.LinearRegression()
        teamOne2017 = np.matrix(teamOne2017).transpose()
        teamOneAll = np.matrix(teamOneAll).transpose()
        teamTwo2017 = np.matrix(teamTwo2017).transpose()
        teamTwoAll = np.matrix(teamTwoAll).transpose()
        teamOne2017Model = linear.fit(teamOne2017, teamOne2017Score)
        teamOne2017OppModel = linear.fit(teamOne2017, teamOne2017Opponent)
        teamOneAllModel = linear.fit(teamOneAll, teamOneAllScore)
        teamOneAllOppModel = linear.fit(teamOneAll, teamOneAllOpponent)
        teamTwo2017Model = linear.fit(teamTwo2017, teamTwo2017Score)
        teamTwo2017OppModel = linear.fit(teamTwo2017, teamTwo2017Opponent)
        teamTwoAllModel = linear.fit(teamTwoAll, teamTwoAllScore)
        teamTwoAllOppModel = linear.fit(teamTwoAll, teamTwoAllOpponent)

        t1 = dataImp.getTeamEstimate(teamOne, 2017)
        t2 = dataImp.getTeamEstimate(teamTwo, 2017)
        t1 = np.matrix(t1).transpose()
        t2 = np.matrix(t2).transpose()

        # Predict
        t1Score1 = teamOne2017Model.predict(t1)
        t1Score2 = teamOne2017OppModel.predict(t1)
        t1Score3 = teamOneAllModel.predict(t1)
        t1Score4 = teamOneAllOppModel.predict(t1)
        t2Score1 = teamTwo2017Model.predict(t2)
        t2Score2 = teamTwo2017OppModel.predict(t2)
        t2Score3 = teamTwoAllModel.predict(t2)
        t2Score4 = teamTwoAllOppModel.predict(t2)

        t1Score = np.mean([t1Score1, t1Score2, t1Score3, t1Score4])
        t2Score = np.mean([t2Score1, t2Score2, t2Score3, t2Score4])

        return t1Score, t2Score


        


