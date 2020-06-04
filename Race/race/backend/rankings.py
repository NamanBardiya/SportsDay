#from backend.racedetails import winner_list
class Rankings:
    def __init__(self, winner_list):
        self.participants = set(winner_list)
        self.rank={}
        
        for i in self.participants:
            self.rank[i]=winner_list.count(i)

        self.ranked_orders = sorted(self.rank.items(),key=lambda x: x[1],reverse=True)

    def show_ranks(self):
        return self.ranked_orders

if __name__=='__main__':
    winner_list=['a','a','a','b','c','c','d','e','e','e','e']
    rank_test = Rankings(winner_list)
    print(rank_test.show_ranks())
 
