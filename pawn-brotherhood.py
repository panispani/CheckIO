def safe_pawns(pawns):
    safe =  0
    for pawn in list(set(pawns)):
        left  = chr(ord(pawn[0]) - 1) + chr(ord(pawn[1]) - 1)
        right = chr(ord(pawn[0]) + 1) + chr(ord(pawn[1]) - 1)
        if (left in pawns) or (right in pawns):
            safe += 1
    return safe
