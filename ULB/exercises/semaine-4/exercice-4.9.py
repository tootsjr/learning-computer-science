def bat(player_1: int, player_2: int) -> bool:
    game = (player_2 + 1) % 3
    if game == player_1:
        return True
    else:
        return False
