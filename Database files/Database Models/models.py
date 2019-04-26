from __future__ import unicode_literals

from django.db import models
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# Create your models here.
class Card(models.Model):

	gameId = models.CharField(max_length=3,blank=False)
	teamId = models.CharField(max_length=2,blank=False)
	playerId = models.IntegerField(max_length=11,blank=False)
	color_card = models.CharField(max_length=6,blank=False)
	time_of_card = models.IntegerField(max_length=11,blank=False)


	def __str__(self): 
		return ('GameId : {0} PlayerID :{1} Time_of_card :{2}'.format(self.gameId,self.playerId,self.time_of_card))

class Game(models.Model):

	gameId = models.CharField(max_length=3,blank=False)
	matchType = models.CharField(max_length=1,blank=False)
	matchDate = models.CharField(max_length=9,blank=False)
	sId = models.CharField(max_length=3,blank=False)
	teamId1 = models.CharField(max_length=2,blank=False)
	teamId2 = models.CharField(max_length=2,blank=False)
	team1Score = models.IntegerField(max_length=11,blank=False)
	team2Score = models.IntegerField(max_length=3,blank=False)

	def __str__(self): 
		return ('GameId : {0} TeamId1 :{1} TeamId2 :{2}'.format(self.gameId,self.teamId1,self.teamId2))



class Goal(models.Model):

	gameId = models.CharField(max_length=3,blank=False)
	teamId = models.CharField(max_length=2,blank=False)
	playerId = models.IntegerField(max_length=11,blank=False)
	time_of_goal = models.IntegerField(max_length=11,blank=False)
	pen = models.CharField(max_length=1,blank=False)

	def __str__(self): 
		return ('GameId : {0} playerId :{1} time_of_goal :{2}'.format(self.gameId,self.playerId,self.teamId))


class OwnGoal(models.Model):

	gameId = models.CharField(max_length=3,blank=False)
	teamId = models.CharField(max_length=2,blank=False)
	playerId = models.IntegerField(max_length=11,blank=False)
	time_of_og = models.IntegerField(max_length=11,blank=False)
	for_teamId = models.CharField(max_length=2,blank=False)


	def __str__(self): 
		return ('GameId : {0} teamId :{1} playerId :{2}'.format(self.gameId,self.teamId,self.playerId))




class Player(models.Model):

	team = models.CharField(max_length=15,blank=False)
	teamId = models.CharField(max_length=2,blank=False)
	playerId = models.IntegerField(max_length=2,blank=False)
	position = models.CharField(max_length=2,blank=False)
	fifa = models.CharField(max_length=20,blank=False)
	bday = models.CharField(max_length=10,blank=False)


	shirt_name = models.CharField(max_length=15,blank=False)
	club = models.CharField(max_length=25,blank=False)
	height = models.IntegerField(max_length=3,blank=False)
	weight = models.IntegerField(max_length=3,blank=False)

	def __str__(self): 
		return ('PLayerID : {0} teamId :{1}'.format(self.playerId,self.teamId))


class Stadium(models.Model):

	sId = models.CharField(max_length=3,blank=False)
	sName = models.CharField(max_length=25,blank=False)
	sCity = models.CharField(max_length=15,blank=False)
	scap = models.IntegerField(max_length=11,blank=False)

	def __str__(self): 
		return ('SID : {0} sName :{1}'.format(self.sId,self.sName))



class Line(models.Model):
	gameId = models.CharField(max_length=3,blank=False)
	teamId = models.CharField(max_length=2,blank=False)
	playerId = models.IntegerField(max_length=11,blank=False)

	def __str__(self): 
		return ('gameId : {0} teamId :{1} playerId:{2}'.format(self.gameId,self.teamId,self.playerId))




class Subs(models.Model):

	gameId = models.CharField(max_length=3,blank=False)
	teamId = models.CharField(max_length=2,blank=False)
	sub_playerId = models.IntegerField(max_length=11,blank=False)

	position = models.CharField(max_length=2,blank=False)
	replace_playerId = models.IntegerField(max_length=11,blank=False)
	time_of_sub = models.IntegerField(max_length=11,blank=False)


	def __str__(self): 
		return ('gameId : {0} subId :{1} time_of_sub:{2} teamId{3}'.format(self.gameId,self.sub_playerId,self.time_of_sub,self.teamId))


class Team(models.Model):

	teamId = models.CharField(max_length=2,blank=False)
	team = models.CharField(max_length=20,blank=False)
	conti = models.CharField(max_length=10,blank=False)
	league = models.CharField(max_length=10,blank=False)

	pop = models.IntegerField(max_length=20,blank=False)


	def __str__(self): 
		return ('teamId : {0} team :{1} Continent:{2}'.format(self.teamId,self.team,self.conti))
















