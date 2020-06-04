from django.shortcuts import render
from django.http import HttpResponse
from backend.matchdetails import MatchDetails
from backend.racedetails import RaceDetails, info, winner_list
from backend.rankings import Rankings
# Create your views here.
def home(request):
        return render(request,"home.html",{'races': info})
    
          
def rankings(request):
    rankings=Rankings(winner_list)
    rank_list=dict(rankings.show_ranks())
    
    return render(request, "ranking.html",{'rank_list_dict':rank_list})

def filtering(request):
    filter_data=request.GET['filterings1']
    filter_data_by_name=request.GET['filterings2']
    if filter_data.isnumeric():
        number=int(filter_data)
        if number>0 and number<=len(info):
            return render(request,"filtered.html",{'races':info,'num':number,'name':filter_data_by_name})
        else:
            return render(request,"filtered.html",{'races':info,'num':-1,'name':filter_data_by_name})
    else:
        return render(request,"filtered.html",{'races':info,'num':-1,'name':filter_data_by_name})
            
          

    
    
