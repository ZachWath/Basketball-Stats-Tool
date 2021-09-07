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
    try:
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
    except TypeError:
        team_selection()

def select_option ():
    
        print("""\n\n BASKETBALL TEAM STATS TOOL!!!\n\n
        ****MENU****\n\n
        Here are your choices:\n
        A) Display Team Stats\n
        B) Quit\n
        \n
        """)
        selection = input("   Enter an option:   ")
        
        if selection.upper() == "A":
            print("""
            Which team would you like to view?\n
            A) Panthers\n
            B) Bandits\n
            C) Warriors\n\n
            """)
        elif selection.upper() == "B":
            exit()
        else:
            print('please choose from the provided options...')
            select_option()
            

def team_selection():

    while True:
        team_selection = input("  Enter an opption:   ")
        if team_selection.upper() == "A":
                print("\nTeam: Panthers...")
                return(Panthers)
                


        elif team_selection.upper() == "B":
                print("\nTeam: Bandits...")
                return(Bandits)

        elif team_selection.upper() == "C":
                print("\nTeam: Warriors...")
                return(Warriors)  
        else:
            print ('please chooose from the provided options...')
            continue


def continue_question():
    while True:
        continue_selection = input ("Would you like to view another teams stats? (Y/N):    ")    
        if continue_selection.upper() == 'Y':
            break 
        elif continue_selection.upper() == 'N':
            quit_question = input ("Would you like to exit the program? (Y/N)?:    ")
            if quit_question.upper() == 'Y':
                exit() 
            elif quit_question.upper()== 'N':
                break
            else:
                print("please choose from the provided options....")  
                continue              
        else:
            print("please choose from the provided options....")  
            continue              

        

        

                
                
        
            
    
            







if __name__ == "__main__":
    clean_data()

    teams_list2 = balance_teams (player_list)
    Panthers = teams_list2[0]
    Bandits = teams_list2[1]
    Warriors = teams_list2[2]



    while True:
        select_option()
        selected_team = team_selection()
        display_stats(selected_team)
        continue_question()
