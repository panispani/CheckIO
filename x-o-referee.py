def checkrows(game_result):
    rows = columns = len(game_result)
    for row in range(rows):
        player = game_result[row][0]
        if player != 'O' and player != 'X':
            continue
        win = True
        for col in range(columns):
            if game_result[row][col] != player:
                win = False
                break
        if win:
            return player
    return 'D'

def checkcolumns(game_result):
    rows = columns = len(game_result)
    for col in range(columns):
        player = game_result[0][col]
        if player != 'O' and player != 'X':
            continue
        win = True
        for row in range(rows):
            if game_result[row][col] != player:
                win = False
                break
        if win:
            return player
    return 'D'

def checkdiagonals(game_result):
    if game_result[0][0] == game_result[1][1] and\
       game_result[1][1] == game_result[2][2]:
           return game_result[1][1]
    if game_result[0][2] == game_result[1][1] and\
       game_result[1][1] == game_result[2][0]:
           return game_result[1][1]
    return 'D'

def checkio(game_result):
    winner = checkrows(game_result)
    if winner == 'O' or winner == 'X':
        return winner
    winner = checkcolumns(game_result)
    if winner == 'O' or winner == 'X':
        return winner
    winner = checkdiagonals(game_result)
    if winner == 'O' or winner == 'X':
        return winner
    return 'D'
