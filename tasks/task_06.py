class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError("Должно быть ровно 2 игрока")
    
    player1, move1 = players[0]
    player2, move2 = players[1]
    
    valid_moves = ['R', 'P', 'S']
    if move1 not in valid_moves or move2 not in valid_moves:
        raise NoSuchStrategyError("Ход должен быть R, P или S")
    
    if move1 == move2:
        return f"{player1} {move1}"
    
    if (move1 == 'R' and move2 == 'S') or \
       (move1 == 'S' and move2 == 'P') or \
       (move1 == 'P' and move2 == 'R'):
        return f"{player1} {move1}"
    else:
        return f"{player2} {move2}"

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
except WrongNumberOfPlayersError:
    print("WrongNumberOfPlayersError")

try:
    print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
except NoSuchStrategyError:
    print("NoSuchStrategyError")

print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) 
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))  