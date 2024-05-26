


PLAYER_FILE = "player_short.csv"
GAME_FILE = "games_short.csv"
RESULT_FILE = "result_short.csv"

# Data type of result can be a list of dictionaries:
"""
result = [
    {"player A": "player_1", "player B": "player_2", "result": "1-0"},
]
"""

playerA = "player A"
playerB = "player B"
result_key = "result"


def load_results(file_name:str) -> list:
    results = []
    with open(file_name, "r") as file:

        lines_data = file.readlines()[1:]
        for line in lines_data:
            result = dict()
            result_data = line.strip().split(",")
            result[playerA] = result_data[0]
            result[playerB] = result_data[1]
            result[result_key] = result_data[2]
            results.append(result)

    return results


# by default we can build a list of dictionaries
# but better approach is to build a dictionary with key -> name and value -> SELO score

def load_players(file_name:str) -> dict:
    players = dict()

    with open(file_name, "r") as file:
        lines_data = file.readlines()[1:]
        for line in lines_data:
            player_data = line.strip().split(",")
            players[player_data[0]] = int(player_data[1])

    return players


def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))


def calculate_scores(players: dict, results: list[dict[str, any]]) -> dict:

    for result in results:
        player_a = result[playerA]
        player_b = result[playerB]
        scoring = result[result_key]

        if player_a not in players:
            players[player_a] = 1500
        if player_b not in players:
            players[player_b] = 1500

        player_a_score = players[player_a]
        player_b_score = players[player_b]

        
        if scoring == "1-0":
            delta_score = 200 * delta(player_a_score, player_b_score)
            players[player_a] = round(players[player_a] + delta_score)
            players[player_b] =  round(players[player_b] - delta_score)
        elif scoring == "0-1":
            delta_score = int(200 * delta(player_b_score, player_a_score))
            players[player_a] = round(players[player_a] - delta_score)
            players[player_b] = round( players[player_b] + delta_score)
        else:
            pass

    return players


def print_results(file_name:str, players: dict)-> None:
    players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))

    with open(file_name, "w") as file:
        file.write("Name,Score\n")
        for player, score in players.items():
            file.write(f"{player},{score}\n")


if __name__ == "__main__":
    players = load_players(PLAYER_FILE)
    print(f"player: {players}")
    results = load_results(GAME_FILE)
    print(f"results: {results}")
    players = calculate_scores(players, results)
    print("----------AFter calculating scores----------")
    print(f"players: {players}")
    print_results(RESULT_FILE, players)
