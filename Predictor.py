from sklearn import linear_model as lm
import DataImporter as di

class Predictor:    
    def doStuff(self, teamOne, teamTwo):
        # Acquire data from DataImporter
        teamOne2017, teamOne2017Score, teamOne2017Opponent = di.getDataMatrix(teamOne, 2017)
        teamOneAll, teamOneAllScore, teamOneAllOpponent = di.getAllDataMatrix(teamOne)
        teamTwo2017, teamTwo2017Score, teamTwo2017Opponent = di.getDataMatrix(teamTwo, 2017)
        teamTwoAll, teamTwoAllScore, teamTwoAllOpponent = di.getAllDataMatrix(teamTwo)
        # AllTeams
        
        # Generate models
        teamOne2017Model = lm.fit(teamOne2017, teamOne2017Score)
        teamOne2017OppModel = lm.fit(teamOne2017, teamOne2017Opponent)
        teamOneAllModel = lm.fit(teamOneAll, teamOneAllScore)
        teamOneAllOppModel = lm.fit(teamOneAll, teamOneAllOpponent)
        teamTwo2017Model = lm.fit(teamTwo2017, teamTwo2017Score)
        teamTwo2017OppModel = lm.fit(teamTwo2017, teamTwo2017Opponent)
        teamTwoAllModel = lm.fit(teamTwoAll, teamTwoAllScore)
        teamTwoAllOppModel = lm.fit(teamTwoAll, teamTwoAllOpponent)

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


