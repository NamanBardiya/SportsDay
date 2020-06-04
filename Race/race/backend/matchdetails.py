from backend.racedetails import RaceDetails

class MatchDetails:
    def __init__(self, match_number, player_a, player_b, winner):
        self.match_number=match_number
        self.player_a=player_a
        self.player_b=player_b
        self.winner=winner

if __name__=='__main__':
    match_number=0
    for i in range(2):
        match_number+=1
        player_a="Naman"
        player_b="Bardiya"
        winner ="Bardiya"
        match_details=MatchDetails(match_number, player_a, player_b, winner)
        race_details=RaceDetails(match_details)

    print(race_details.show_details())
