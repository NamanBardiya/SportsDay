winner_list=[]
info=[]
class RaceDetails:
    def __init__(self, match_details):
        info.append(match_details.__dict__)
        winner_list.append(match_details.winner)

    def show_details(self):
        return info

if __name__=='__main__':
    test=RaceDetails()
    test.show_details()

