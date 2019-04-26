# WorldCup-Advanced-SQL

Created the 9 tables for the WORLD CUP database:
```
  1. TEAM (TeamID, Team, Continent, League, Population)
  
  2. STADIUM (SID, SName, SCity, SCapacity)
  
  3. PLAYER (Team,TeamID,PNo,Position,PName,Birth Date,Shirt Name,Club,Height,Weight)
  (* PLAYER corresponds to the data in the “rosters” data file – Pno corresponds to PlayerID,
  And PName corresponds to FIFA Popular Name *)
  4. GAME(GameID,MatchType,MatchDate,SID,TeamID1,TeamID2,Team1_Score,Team2_Score)
  (* GAME corresponds to the data in the “matches” data file *)
  5. STARTING_LINEUPS(GameID,TeamID,PNo)
  6. SUBSTITUTIONS(GameID,TeamID,PNoIn,Position,PNoOut,Time)
  7. GOALS(GameID,TeamID,PNo,Time,Penalty)
  8. OWN_GOALS(GameID,TeamID,PNo,Time,For_TeamID)
  9. CARDS(GameID,TeamID,PNo,Color,Time)
  ```
  
  
  Queries Executed:
  
    1. Retrieve the country, height, and names of all the players who hail from the African continent
        and are taller than 190 cm. Sort the list by country and their height.
        
    2. Retrieve the scores of all games played in Group A or B where each team had at least one score.
    Each result should list team 1 name, team 1 score, team 2 name, and team 2 score. Sort the
    result by the match type.
    
    3. For all the players who received red card, retrieve their country, player name, height
    and weight
    
    4. What is the name of the player who received the maximum number of yellow cards? How
    many yellow cards did he receive, and which country does he come from?
    
    5. Retrieve the names of the teams that scored more than 1 own goals in 1 or more games. List the
    number of own goals that each of these teams scored
    Explanation: An own goal is an event in competitive 
    
    6. Create a view GAME_INFO that retrieves for each team all that team’s game scores. The view
    should have the following attributes: Team, and for each game that the team has participated
    in (either as TeamID1 or TeamID2) the following information: Match Type, MatchDate,
    StadiumName, SCity, Team1Name, Team1Score, Team2Name, Team2Score.
    
    7. 
    Retrieve all game information from game_info where France played
    Retrieve all game information from game_info where game type is A or X
    Retrieve all game information from game_info where team 1 scored more than 2 goals
    Retrieve all game information from game_info where the stadium name has Kazan in it.
    
    8.
    (i) Retrieve the name of the player and his country who received a yellow card
    during A game. Sort the list by country names
    (ii) Retrieve a sorted list of the names of each country/team that played at least one game
    in the city of Sochi.
    (iii) For each player who was substituted in the first 30 minutes of a game, retrieve the
    player name (PlayerOut) and the substitute player’s name (PlayerIn), and the minute of
    the substitution, as well as the team name.
    
    
    
    
    
    
    
    
    
    
