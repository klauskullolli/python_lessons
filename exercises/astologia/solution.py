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
        player = dict()
        for line in f:
            # string is converted into a list of strings splitted by a comma
            line_elements = line.split(",")
            # print(line_elements)
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


def getZodiacOfPlayer(player, zodiac):
    pass


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


def total_goals_per_sign(players, zodiac):
    zodiac_goals = {}
    # initializing the zodiac_goals with 0 goals first each 
    for k in  zodiac: 
        zodiac_goals[k] = 0 
    pass

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
    # players = read_players_data(INPUT_FILE)
    # print(players)
    read_zodiac_data(INPUT_FILE_ZODIAC)


# main()

# if this script is executing so call the main function
if __name__ == "__main__":
    main()
