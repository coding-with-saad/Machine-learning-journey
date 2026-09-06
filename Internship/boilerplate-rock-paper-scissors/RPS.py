my_history = []


def player(prev_play, opponent_history=[]):

    global my_history

    # Reset when a new match starts
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
    else:
        opponent_history.append(prev_play)

    # First move
    if len(my_history) == 0:
        move = "R"

    else:
        # -------------------------
        # Quincy strategy
        # -------------------------

        if len(opponent_history) >= 5:

            quincy_pattern = ["R", "R", "P", "P", "S"]

            # Check the position in Quincy's repeating pattern
            position = (len(opponent_history) - 1) % 5

            prediction = quincy_pattern[position]

            # Counter the prediction
            if prediction == "R":
                move = "P"
            elif prediction == "P":
                move = "S"
            else:
                move = "R"

        else:
            # -------------------------
            # Kris strategy
            # -------------------------

            previous_move = my_history[-1]

            if previous_move == "R":
                prediction = "P"
            elif previous_move == "P":
                prediction = "S"
            else:
                prediction = "R"

            # Counter the prediction
            if prediction == "R":
                move = "P"
            elif prediction == "P":
                move = "S"
            else:
                move = "R"

    # Remember our move
    my_history.append(move)

    return move