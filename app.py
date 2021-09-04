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
        
def display_stats(team):
    player_list =''
    total_players = len(team)
    exp_players = 0
    non_exp_players = 0
    hieghts = 0
    average_height = ''
    guardians_list = ''
    for person in team:
        player_list = player_list + str(person ['name']) + ", "
        if person ['experience'] == False:
            non_exp_players += 1 
        elif person ['experience'] == True:
            exp_players += 1
        hieghts += int(person ['height'])
        guardians_list = guardians_list + str(person ['guardians']) + ', '
    average_height = hieghts / total_players

    print ("*****************************")
    print ("""
        Total Players: {}\n
        Total Expierenced Players: {}\n
        Total Un-Expierenced Players: {}\n
        Average Height: {}\n
        """ .format(total_players, exp_players, non_exp_players, average_height))
    print (""" 
        Players on Team:
            {}\n
        Guardians:
            {}
        """.format(player_list, guardians_list))








clean_data()

teams_list2 = balance_teams (player_list)
Panthers = teams_list2[0]
Bandits = teams_list2[1]
Warriors = teams_list2[2]


def select_option ():
    selection = input("   Enter an option:   ")
    while True:
        if selection == "A":
            print("""
                Which team would you like to view?\n
                A) Panthers\n
                B) Bandits\n
                C) Warriors\n\n
                """)
            team_selection = input("  Enter an opption:   ")
            if team_selection == "A":
                print("\nTeam: Panthers...")
                display_stats(Panthers)
                


            elif team_selection == "B":
                print("\nTeam: Bandits...")
                display_stats (Bandits)

            elif team_selection == "C":
                print("\nTeam: Warriors...")
                display_stats(Warriors)
        

        elif selection == "B":
            exit()
        continue_selection = input ("Would you like to view another teams stats? (Y/N):    ")
        if continue_selection == 'Y':
            print("""\n\n BASKETBALL TEAM STATS TOOL!!!\n\n
            ****MENU****\n\n
            Here are your choices:\n
            A) Display Team Stats\n
            B) Quit\n
             \n
             """)
            break 
        elif continue_selection == 'N':
            exit()

            
    
            


print("""\n\n BASKETBALL TEAM STATS TOOL!!!\n\n
   ****MENU****\n\n
   Here are your choices:\n
   A) Display Team Stats\n
   B) Quit\n
   \n
   """)

while True:
    select_option()
