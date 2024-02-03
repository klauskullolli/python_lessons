from datetime import datetime

INPUT_FILE = "sportivi.csv"
# relative path related to the file that is currently executing
INPUT_FILE_ZODIAC = "zodiaco.csv"
# EX_File = "../armstrong/number.txt"
NAME = 'name'
GOALS = "goals"
COUNTRY = "country"
BIRTHDATE = "birthdate"

date_format = "%d/%m/%Y"


def read_players_data(fileName):
    players = []

    try:
        f = open(fileName, "r")
        # player = {1, 3} # touple
        for line in f:
            # string is converted into a list of strings splitted by a comma
            line_elements = line.split(",")
            # print(line_elements)
            player = {}
            player[NAME] = line_elements[0]
            player[GOALS] = int(line_elements[1])
            player[COUNTRY] = line_elements[2]
            player[BIRTHDATE] = datetime.strptime(
                line_elements[3].strip(), date_format)
            players.append(player)

    except Exception as e:
        print(e)
        print("Can not read the file")

    return players


def read_zodiac_data(fileName):
    zoidac = dict()
    
    date_format = "%d/%m"
    try:
        file = open(fileName, "r")
        for line in file:
            line_splited = line.strip().split(",")
            zoidac[line_splited[0]] = {
                "start": datetime.strptime(line_splited[1], date_format),
                "end": datetime.strptime(line_splited[2], date_format)
            }

    except Exception as e:
        print(e)

    return zoidac


'''
player parameter is a player dict example -> {"name" : "Abe Lenstra", "goals" : 710, "country" : "Netherland", "birthdate": "27/11/1920" }
zodiac parameter is a zodiac dict that is created from reading the file from zodiaco.csv
hint:  should be taken into consideration only the day and month for checking which zodiac it belongs to:


'''

# name of zodiac is the key
def getZodiacOfPlayer(player:dict, zodiac:dict):
    birthday = player[BIRTHDATE]
    birthday =  birthday.replace(year=1900)
  
    zodiac_name = "" 
    for name_zod  in zodiac.keys(): 
        values = zodiac[name_zod]
        if ( values["start"] <= birthday <= values["end"]) : 
            zodiac_name = name_zod 
            break
 


    return zodiac_name


'''
players param is a list of player dictionary 
procedure: 
1 - create a new dictionary with zodiac 
1 - iterate for each player
2 - use the player object to return the zodiac sign 
3 - sum only player that belong to the same sign 
4 -  assign to specific zodiac sign 
5 - return the dict of new zodiac created
'''

''' zodiac_goals  = {"Aries": 0}'''


def total_goals_per_sign(players:list, zodiac:dict):
    zodiac_goals = dict()  

    # initializing the zodiac_goals with 0 goals first each 
    for k in  zodiac: 
        zodiac_goals[k] = 0 

    zod_names  = zodiac_goals.keys()

    for player in players : 
        zod =  getZodiacOfPlayer(player, zodiac)

        if(zod in zod_names ):
            zodiac_goals[zod]  += player[GOALS]  
    
       
    return zodiac_goals

#  (20 , 3) (17, 4)  --> (24 , 3) --> (20<=24<=17 or 20>=24>=17) and 3 <= 3<=4
'''
new data created from total_goals_per_sign 
format according to the exercise requirements and print it to the console 
'''
def printing_result(zodiac): 
    pass


''' zodiac =  {"Aries": {
                  "start" : "21/03" ,
                  "end": "20/04" 
                }, 
    "Taurus": {
                  "start" : "21/03" ,
                  "end": "20/04" 
                }

}

zoidac2 = [
{
"sign": "Aries", 
 "start" : "21/03" ,
"end": "20/04" }, 
{
"sign": "Taurus", 
 "start" : "21/03" ,
"end": "20/04" }, 
] 

firt proposition accessed directly by key
zoidac["Aries"]

for zod in zoidac2: 
    if zod["sign"] == "Taurus": 
        return  zod 
 '''


def main():
    players = read_players_data(INPUT_FILE)
   
    zodiacs = read_zodiac_data(INPUT_FILE_ZODIAC)
    zodiac_goals =  total_goals_per_sign(players, zodiacs)
    sorted_zod  = sorted(zodiac_goals.items(), key= lambda x : x[1], reverse=True )  # [(name , goal-value for each zodiac)]
    # [("Aquarius", "5283"), ("Cancer", "3593")]
    biggest_number  = sorted_zod[0][1]
    for name_zod , goals  in sorted_zod: 
        asterix = 0 
        if (goals == biggest_number) : asterix = 50
        else: asterix  = (50* goals) //biggest_number
        print(f"{name_zod:20s} ({goals}) {asterix*'*':60s}") # this is a sting formatting
    # dict1 = {"name":"Klaus" , "goals": 42}
    # dict2 = {"name":"John" , "goals": 22}
    # dict3 = {"name":"Donny" , "goals": 72}


    #  sorted is a build function used to sort list object according to specified/defined keys keys, descending or ascending  
    # ls =  [dict1,  dict2, dict3 ]
    # values = sorted(ls, key= lambda x : x["goals"] , reverse=True) 
    # print(values)


# main()

# if this script is executing so call the main function
if __name__ == "__main__":
    main()






#  futboll player (27/09/2001)
#  (27/09)

# Aries,21/03,20/04                 
# Taurus,21/04,20/05
# Gemini,21/05,21/06
# Cancer,22/06,22/07
# Leone,23/07,23/08
# Virgo,24/08,22/09
# Libra,23/09,22/10  --> Libra
# Scorpio,23/10,22/11
# Sagittarius,23/11,21/12
# Capricorn,22/12,20/01
# Aquarius,21/01,19/02
# Pisces,20/02,20/03 