def is_winner(pile):
    return pile == 0

# Minimax with Alpha-Beta Pruning
def minimax(pile, is_max, alpha, beta):
    if is_winner(pile):
        return -1 if is_max else 1

    if is_max:
        max_eval = -float('inf')
        for move in range(1, 4):
            if pile - move >= 0:
                eval = minimax(pile - move, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for move in range(1, 4):
            if pile - move >= 0:
                eval = minimax(pile - move, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# AI chooses best move
def best_move(pile):
    for move in range(1, 4):
        if pile - move >= 0:
            result = minimax(pile - move, False, -float('inf'), float('inf'))
            if result == 1:
                return move
    return 1  # fallback if no optimal move found

# Game loop
def play_nim():
    pile = int(input("Enter starting number of stones (e.g., 15): "))
    player_turn = input("Do you want to play first? (y/n): ").lower() == 'y'

    while pile > 0:
        print(f"\nCurrent pile: {pile}")
        if player_turn:
            try:
                move = int(input("Your turn - remove 1, 2, or 3 stones: "))
                if move not in [1, 2, 3] or move > pile:
                    print("Invalid move! Try again.")
                    continue
            except:
                print("Enter a number.")
                continue
        else:
            move = best_move(pile)
            print(f"AI removes {move} stone(s).")

        pile -= move
        if pile == 0:
            winner = "You" if player_turn else "AI"
            print(f"\n{winner} won the game!")
            break

        player_turn = not player_turn

# Start the game
play_nim()
