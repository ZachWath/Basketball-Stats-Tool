import constants
import copy 


player_list = copy.deepcopy(constants.PLAYERS)
teams_list = copy.deepcopy(constants.TEAMS)
Panthers = []
Bandits = []
Warriors = []

def clean_data ():
    for person in player_list:
        height = person ['height'].split()
        person ['height'] = int(height [0])
        if person['experience'] == "YES":
            person['experience'] = True
        if person['experience']== "NO":
            person['experience']= False

def balance_teams (team_mates):
    no_exp = []
    exp = []

    for person in team_mates:
        if person ['experience'] == False :
            no_exp.append(person)
        elif person ['experience'] == True:
            exp.append(person)


    Panthers = no_exp[:len(no_exp):3] + exp[:len(exp):3]
    Bandits = no_exp[1:len(no_exp):3] + exp [1:len(exp):3]
    Warriors = no_exp[2:len(no_exp):3] + exp [2:len(exp):3]
    
    return ([Panthers,Bandits,Warriors])

clean_data()

teams_list2 = balance_teams (player_list)
Panthers = teams_list2[0]
Bandits = teams_list2[1]
Warriors = teams_list2[2]
print(Panthers)