tab = [0, 0, 0, 0, 0, 0, 0, 0, 0]

t = tab

win_line = [[t[0], t[1], t[2]], [t[3], t[4], t[5]], [t[6], t[7], t[8]],
            [t[0], t[3], t[6]], [t[1], t[4], t[7]], [t[2], t[5], t[8]],
            [t[0], t[4], t[8]], [t[6], t[4], t[2]]]

depth = 9


def update(tab=tab, t=t, win_line=win_line):
    t = tab
    w = [[t[0], tab[1], t[2]], [t[3], tab[4], t[5]], [t[6], t[7], t[8]],
         [t[0], tab[3], t[6]], [t[1], tab[4], t[7]], [t[2], t[5], t[8]],
         [t[0], tab[4], t[8]], [t[6], tab[4], t[2]]]
    for i in range(8):
        for j in range(3):
            win_line[i][j] = w[i][j]


def init(tab=tab, n=1, win_line=win_line):
    for i in range(9):
        tab[i] = n
    update()


def get_moves(tab=tab):
    moves = []
    for i in range(9):
        if tab[i] == 0:
            moves.append(i)
    return moves


def game_end(tab=tab):
    cont = 0
    for i in tab:
        if i == 1 or i == 2:
            cont += 1
    if cont == 9:
        return 1
    else:
        return 0

# To note here it is set as the AI to be 1 and user to be 2
def evaluate(turn, win_line=win_line):
    score = 0
    cont = 0  # scans through the line to find if there is a pair of three
    for line in win_line:
        cont = 0
        for case in line:
            if case == 1:
                cont += 1
            if case == 2:
                cont -= 1
        if turn == "max":
            if cont == 2:
                cont *= 2
            elif cont == -2:
                cont *= 4
            elif cont == 3:
                cont *= 10
        if turn == "min":
            if cont == 2:
                cont *= 4
            elif cont == -2:
                cont *= 2
            elif cont == -3:
                cont *= 10
        score += cont
    return score

def win(win_line=win_line):
    """
    This function defines the condition for the AI to win
    """
    cont = 0
    for line in win_line:
        cont = 0
        for case in line:
            if case == 1:
                cont += 1
        if cont == 3:
            return 1


def lose(win_line=win_line):
    """
    This function defines the condition for the opponent to win
    """
    cont = 0
    for line in win_line:
        cont = 0
        for case in line:
            if case == 2:
                cont += 1
        if cont == 3:
            return 1


def draw():
    """
    This function continues the turns
    """
    if not win() and not lose() and game_end():
        return 1


tab_copy = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def copy_tab(tab=tab, tab_copy=tab_copy):
    for i in range(9):
        tab_copy[i] = tab[i]

copy_tab()


def copy(tab_copy=tab_copy, tab=tab):
    for i in range(9):
        tab[i] = tab_copy[i]


def count_tab(tab=tab):
    cont = 0
    for i in range(9):
        if tab[i] == 1 or tab[i] == 2:
            cont += 1
    return cont


def recursive_play(depth, turn, tab=tab):
    if turn == "max":
        if not win() and not lose() and not game_end() and depth != 0:
            moves = get_moves()
            score = -1000
            for move in moves:
                tab[move] = 1;
                update()
                if win(): tab[move] = 0; tab[move] = 1; update();cont = count_tab();copy();update();return +1000 - cont
                result = evaluate(turn=turn)
                tab[move] = 0;
                update()
                if result > score: score = result;best_move = move
            tab[best_move] = 1;
            update()

    if turn == "min":
        if not win() and not lose() and not game_end() and depth != 0:
            moves = get_moves()
            score = +1000
            for move in moves:
                tab[move] = 2;
                update()
                if lose(): tab[move] = 0; tab[move] = 2; update();cont = count_tab();copy();update();return -1000 + cont
                result = evaluate(turn=turn)
                tab[move] = 0;
                update()
                if result < score: score = result;best_move = move
            tab[best_move] = 2;
            update()

    if turn == "max":
        turn = "min"
    elif turn == "min":
        turn = "max"
    if not win() and not lose() and not game_end() and depth != 0: return recursive_play(depth - 1, turn)

    if win(): cont = count_tab();copy();update();return +1000 - cont
    if lose(): cont = count_tab();copy();update();return -1000 + cont
    if not win() and not lose() and game_end() or depth == 0: score = evaluate(turn="max");copy();update();return score
    if not win() and not lose(): score = evaluate(turn="max");copy();update();return score
    update()


def get_best_move(depth, turn="min", tab=tab):
    moves = get_moves()
    score = -1000
    for move in moves:
        tab[move] = 1;
        update()
        result = recursive_play(depth, turn)
        if result > score:
            score = result
            best_move = move
    return best_move
