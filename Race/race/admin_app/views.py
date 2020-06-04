from django.shortcuts import render
from django.http import HttpResponse
from backend.matchdetails import MatchDetails
from backend.racedetails import RaceDetails, info, winner_list
from backend.rankings import Rankings

def Admin(request):
    return render(request, 'Admin.html')
    
def add(request):
    player_a=request.GET['playera']
    player_b=request.GET['playerb']
    winner=request.GET['winnerp']
    passw=request.GET['pc']
    if passw!="naman@07":
        return render(request,"success.html",{'status':'wrong password'})
    if player_a != "" and player_b !="" and winner !="":
        if winner==player_a or winner==player_b:
            match_number=len(info)+1
            match_details=MatchDetails(match_number, player_a, player_b, winner)
            race_details=RaceDetails(match_details)
    else:
        return render(request,"success.html",{'status':'fail'})
            
    if player_a != "" and player_b !="" and winner !="":
        if winner==player_a or winner==player_b:
            return render(request,"success.html",{'status':'success'})
        else:
            return render(request,"success.html",{'status':'fail'})
    else:
        return render(request,"success.html",{'status':'fail'})
    
    
    
    