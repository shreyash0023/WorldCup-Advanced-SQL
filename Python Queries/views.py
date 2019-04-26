from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate 
from django.contrib.auth import get_user_model, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
import numpy


def queries(request):

	# FOR QUERY 1

	query = request.GET.get('qt') # Team Name
	type_query = request.GET.get('dropdown') # Query 1 or 2 
	team = Team.objects.all()
	player = Player.objects.all()
	game = Game.objects.all()
	line_up = Line.objects.all()
	leng = 0 
	for x in str(query):
		leng+=1

	query = str(query)


	s = ''

	upper = 0
	for x in query:
		if upper == 0:
			s+= x.upper()
		else:
			s+=x

	
	player = Player.objects.all().filter(Q(team__icontains=query) )

	counting = 0 
	for x in player:
		counting+=1



	# Query2 
	query2 = request.GET.get('qt') # Team Name
	type_query = request.GET.get('dropdown') # Query 1 or 2




	inputs = []

	query2 = str(query2)
	print(query2)

	if len(query2.split()) > 1:
		card_color = query2.split()[1]
		team_name= query2.split()[0]
		inputs.append(query2)

		teamids_q2 = 0
		team = Team.objects.all() #OBJECT

		for x in team:
			if (x.team == team_name):
				teamids_q2 = x.teamId

		game = Game.objects.all() # OBJECT

		gameids_q2 = []
		for x in game:
			if (x.teamId1 ==teamids_q2 ) or (x.teamId2 ==teamids_q2 ):
				gameids_q2.append(x.gameId)

		cards = Card.objects.all() # OBJECT


		info_final = []
		for x in cards:
			if (x.color_card == card_color) and (x.teamId == teamids_q2):
				for y in gameids_q2:
					if y == x.gameId:
						info_final.append([x.playerId,x.gameId,x.color_card])

		player = Player.objects.all()

		fifa_pop_name = []
		count = 0
		# for x in player:
		# 	if count >= len(inf)
		# 	if (x.playerId == info_final[count][0]) and (x.teamId ==  teamids_q2)
		# 		fifa_pop_name.append([x.fifa,info_final[count][1]])
		# 	count+=1

		for x in range(len(info_final)):
			info_pid = info_final[x][0]
			for y in player:
				if (y.teamId == teamids_q2) and (y.playerId == info_final[x][0]):
					fifa_pop_name.append([info_final[x][1],y.fifa])



	if leng > 2 and query!= None and player!= None and counting>1 and type_query == 'q1':
		# Select team Ids
		teamIds = []
		for x in team:
			if (query==x.team):
				teamIds.append(x.teamId)

		#teamIds = [str(r) for r in teamIds]

		# Select game ids
		gameIds = []
		for x in game:
			
			if (x.teamId1 in teamIds) or (x.teamId2 in teamIds):
				gameIds.append(x.gameId)


		# Get plyer id from line up
		playerids_fromlineup = []

		count=0
		for x in line_up:
			if ( (x.gameId in gameIds) and (x.teamId in teamIds) ):
				playerids_fromlineup.append(x.playerId)
				count+=1

		player_names = []

		# for x in player:
		# 	if (x.teamId in teamIds) and (x.playerId in playerids_fromlineup):
		# 		if (x.gameId in gameIds):

		info = []
		change = 0
		for y in range(len(gameIds)):
			for x in range(change,change+11):
				info.append([gameIds[y],playerids_fromlineup[x],teamIds[0]])
				change+=1
			change=0

		if len(teamIds) > 0:
			player = Player.objects.all().filter(Q(teamId__icontains=teamIds[0]) )

		ps = []
		for x in player:
			ps.append([x.playerId,x.fifa,x.teamId])

		# count = 0
		# for x in player:
		# 	if (x.playerId == info[count][1]) and (x.teamId == info[count][2]):
		# 		info[count].append(x.fifa)

		# 		count+=1

		for x in range(len(ps)):
			player__ = ps[x][0] # extacted a player id
			team__ = ps[x][2]
			fifa__ =ps[x][1]
			for y in range(len(playerids_fromlineup)):
				if (player__ == info[y][1]) and (team__ == info[y][2]):
					info[y].append(fifa__)
		count = 0
		
		for x in info:
			x = [str(r) for r in x]

		context = { 'playerids':playerids_fromlineup ,'count':count,'gameIds':gameIds,'player_names':player_names,
					'information':info,'test':ps,'qqq': 0, 'query1': 1
						}





	elif type_query == 'q2':

		context = { 'playerids':[] ,'count':10,'gameIds':[],'player_names':[],
					'information':[],'test':[], 'query2': 1, 'inp':fifa_pop_name
						}
					



	



	else:

		context = { 'playerids':[] ,'count':10,'gameIds':[],'player_names':[],
					'information':[],'test':[], 'query1': 0
						}


	return render(request,'databases/query.html',context)









