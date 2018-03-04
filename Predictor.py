from sklearn import linear_model as lm
import DataImporter as di

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
        teamOne2017Model = linear.fit(teamOne2017, teamOne2017Score)
        teamOne2017OppModel = linear.fit(teamOne2017, teamOne2017Opponent)
        teamOneAllModel = linear.fit(teamOneAll, teamOneAllScore)
        teamOneAllOppModel = linear.fit(teamOneAll, teamOneAllOpponent)
        teamTwo2017Model = linear.fit(teamTwo2017, teamTwo2017Score)
        teamTwo2017OppModel = linear.fit(teamTwo2017, teamTwo2017Opponent)
        teamTwoAllModel = linear.fit(teamTwoAll, teamTwoAllScore)
        teamTwoAllOppModel = linear.fit(teamTwoAll, teamTwoAllOpponent)

        t1 = averageStat()
        t2 = averageStat()

        # Predict
        teamOne2017Model.predict(t1)
        teamOne2017OppModel.predict(t1)
        teamOneAllModel.predict(t1)
        teamOneAllOppModel.predict(t1)
        teamTwo2017Model.predict(t1)
        teamTwo2017OppModel.predict(t1)
        teamTwoAllModel.predict(t1)
        teamTwoAllOppModel.predict(t1)

        


