#Problem-1
import random
import numpy as np


def utility_function(max_str, min_str):
    random_number = random.choice([0, 1])
    utility = (strength_function(max_str) - strength_function(min_str) + ((-1) ** random_number) * random.randint(1, 10)) / 10
    return utility


def strength_function(value):
    strength = (np.log2(value + 1) + (value / 10))
    return strength


def alpha_beta_function(depth, idx, is_maximum, leaf_val, alpha, beta):
    if depth == 5:  #Last level a pouchaye gese
        return leaf_val[idx]

    if is_maximum:  #For max, alpha update
        best_val = float('-inf')
        for i in range(2):
            x = alpha_beta_function(depth + 1, idx * 2 + i, False, leaf_val, alpha, beta)
            best_val = max(best_val, x)
            alpha = max(alpha, best_val)
            if alpha >= beta:
                break  #Prune
        return best_val
    else:
        best_val = float('inf')   #For min, beta update
        for i in range(2):
            x = alpha_beta_function(depth + 1, idx * 2 + i, True, leaf_val, alpha, beta)
            best_val = min(best_val, x)
            beta = min(beta, best_val)
            if beta <= alpha:
                break  #Prune
        return best_val


def simulation(player_01, carlsen_str, caruana_str):
    results = {"Carlsen": 0, "Caruana": 0, "Draws": 0}

    for game in range(4):
        if game % 2 == player_01:
            max_value, min_value = carlsen_str, caruana_str

        else:
            max_value, min_value = caruana_str, carlsen_str

        nodes = []

        for y in range(32):   # Since 2^5 = 32
            nodes.append(utility_function(max_value, min_value))

        game_result = alpha_beta_function(0, 0, True, nodes, float('-inf'), float('inf'))

        if game_result > 0:
            if game % 2 == player_01:
                winner = "Carlsen"
            else:
                winner = "Caruana"
        elif game_result < 0:
            if game % 2 == player_01:
                winner = "Caruana"
            else:
                winner = "Carlsen"
        else:
            winner = "Draw"

        print(f"Game {game + 1} Winner: {winner} (Utility: {game_result:.2f})")
        results[winner] += 1

    print(
        f"\nOverall Results:\n"
        f"Magnus Carlsen Wins: {results['Carlsen']}\n"
        f"Fabiano Caruana Wins: {results['Caruana']}\n"
        f"Draws: {results['Draws']}")

    if results["Carlsen"] > results["Caruana"]:
        print(f"Champion: Magnus Carlsen")
    elif results["Carlsen"] < results["Caruana"]:
        print(f"Overall Winner: Fabiano Caruana")
    else:
        print(f"Overall Result: Draw")


#Driver Codes
player_01 = int(input("Enter starting player (0 for Carlsen, 1 for Caruana): "))
carlsen_str = float(input("Enter base strength for Carlsen: "))
caruana_str = float(input("Enter base strength for Caruana: "))

simulation(player_01, carlsen_str, caruana_str)

#=====================================================================================================================
# #Problem-02
# import numpy as np
# import random
#
#
# def utility_function(max_str, min_str):
#     random_number = random.choice([0, 1])
#     utility = (find_strength(max_str) - find_strength(min_str) + ((-1) ** random_number) * random.randint(1, 10)) / 10
#     return utility
#
#
# def find_strength(value):
#     strength = np.log2(value + 1) + value / 10
#     return strength
#
#
# def minimax_function(depth, maximizing, values, alpha, beta):
#     if depth == 5:
#         return values.pop(0)  #Last level a chole ashche
#
#     if maximizing:
#         max_val = float('-inf')
#         for i in range(2):
#             val = minimax_function(depth + 1, False, values, alpha, beta)
#             max_val = max(max_val, val)
#             alpha = max(alpha, max_val)
#             if beta <= alpha:
#                 break         #Prune
#         return max_val
#     else:
#         min_val = float('inf')
#         for j in range(2):
#             val = minimax_function(depth + 1, True, values, alpha, beta)
#             min_val = min(min_val, val)
#             beta = min(beta, min_val)
#             if beta <= alpha:
#                 break        #Prune
#         return min_val
#
#
# def minimax_with_mind_control_power(depth, maximizing, values, alpha, beta):
#     if depth == 5:
#         return values.pop(0)
#
#     if maximizing:
#         max_val = float('-inf')
#         for i in range(2):
#             val = minimax_with_mind_control_power(depth + 1, False, values, alpha, beta)
#             max_val = max(max_val, val)
#             alpha = max(alpha, max_val)
#             if beta <= alpha:
#                 break
#         return max_val
#     else:
#         worst_move = float('-inf')
#         for j in range(2):
#             val = minimax_with_mind_control_power(depth + 1, True, values, alpha, beta)
#             worst_move = max(worst_move, val)
#             beta = min(beta, worst_move)
#             if beta <= alpha:
#                 break
#         return worst_move
#
#
# def simulation(initial_player, cost_mind_control, light_strg, l_strg):
#     if initial_player == 0:
#         maxV, minV = light_strg, l_strg
#
#     else:
#         maxV, minV = l_strg, light_strg
#
#     val1 = []    # utility values store kore
#     for i in range(32):  # 2^5 = 32 leaf nodes
#         value = utility_function(maxV, minV)
#         val1.append(value)
#
#     val2 = []   #Val1 er ta copy kore
#     for item in val1:
#         val2.append(item)
#
#     minimax_normal = minimax_function(0, True, val1, float('-inf'), float('inf'))
#     minimax_mind_control = minimax_with_mind_control_power(0, True, val2, float('-inf'), float('inf'))
#     minimax_with_mind_control = minimax_mind_control - cost_mind_control
#
#     print(
#         f"Minimax value without Mind Control: {minimax_normal:.2f}\n"
#         f"Minimax value with Mind Control: {minimax_mind_control:.2f}\n"
#         f"Minimax value with Mind Control after incurring the cost: {minimax_with_mind_control:.2f}")
#
#     print("")
#
#     if minimax_with_mind_control > minimax_normal:
#         print("Light should use Mind Control.")
#     else:
#         print("Light should NOT use Mind Control as the position is already winning..")
#
#
#
# #Driver Codes
# initial_player = int(input("Enter who goes first (0 for Light, 1 for L): "))
# cost_mind_control = float(input("Enter the cost_mind_control of using Mind Control: "))
# light_strg = float(input("Enter base strength for Light: "))
# l_strg = float(input("Enter base strength for L: "))
#
# simulation(initial_player, cost_mind_control, light_strg, l_strg)

