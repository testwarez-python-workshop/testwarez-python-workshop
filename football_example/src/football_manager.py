import requests

base_url = "http://api.football-data.org/v1"


class FootballManager:

    @staticmethod
    def get_competition_id(competition_code):
        competitions = requests.get(base_url + "/soccerseasons").json()
        for competition in competitions:
            if competition["league"] == competition_code:
                return competition["id"]

    def get_number_of_results(self, competition_code, winning_team):
        competition_id = self.get_competition_id(competition_code)
        res = requests.get(base_url + "/soccerseasons/{0}/fixtures".format(competition_id))
        results = res.json()["fixtures"]
        num_of_matches = 0
        for result in results:
            if str(winning_team) == "1" and result["result"]["goalsHomeTeam"] > result["result"]["goalsAwayTeam"]:
                num_of_matches += 1
            elif str(winning_team).upper() == "X" and result["result"]["goalsHomeTeam"] == result["result"]["goalsAwayTeam"]:
                num_of_matches += 1
            elif str(winning_team) == "2" and result["result"]["goalsHomeTeam"] < result["result"]["goalsAwayTeam"]:
                num_of_matches += 1
        return num_of_matches
