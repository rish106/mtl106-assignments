import random

def win_probability(my_pick, alice_pick):
    return my_pick / (my_pick + alice_pick)

def min_strategy(my_warriors):
    return min(my_warriors)

def max_strategy(my_warriors):
    return max(my_warriors)

def optimal_strategy(my_warriors):
    # TODO
    if random.random() < 0.3333:
        return min(my_warriors)
    else:
        return max(my_warriors)

def simulate_game(pick_strategy):

    my_warriors = [5, 8, 1]
    alice_warriors = [3, 4, 6, 7]
    wins = 0
    num_iterations = 500000

    for _ in range(num_iterations):
        curr_my_warriors = my_warriors.copy()
        curr_alice_warriors = alice_warriors.copy()

        while curr_my_warriors and curr_alice_warriors:
            alice_pick = random.choice(curr_alice_warriors)
            my_pick = pick_strategy(curr_my_warriors)
            prob_win = win_probability(my_pick, alice_pick)
            curr_my_warriors.remove(my_pick)
            curr_alice_warriors.remove(alice_pick)
            if random.random() < prob_win:
                curr_my_warriors.append(my_pick + alice_pick)
            else:
                curr_alice_warriors.append(my_pick + alice_pick)
        if len(curr_my_warriors) > 0:
            wins += 1

    return wins / num_iterations


# 1. Max strategy
max_strat_probability = simulate_game(max_strategy)
print("With max strategy", max_strat_probability)

# 2. Min strategy
min_strat_probability = simulate_game(min_strategy)
print("With min strategy", min_strat_probability)

# 3. Expected Gain is 0

# 4. Optimal strategy
optimal_strat_probability = simulate_game(optimal_strategy)
print("With optimal strategy", optimal_strat_probability)

