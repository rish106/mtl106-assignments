import random

def win_probability(x, y):
    return x / (x + y)

def min_strategy(my_warriors, alice_warriors):
    return min(my_warriors)

def max_strategy(my_warriors, alice_warriors):
    return max(my_warriors)

def optimal_strategy(my_warriors, alice_warriors):
    # TODO
    return max(my_warriors)

def simulate_game(your_strength, alice_strength, pick_strategy):

    wins = 0
    num_iterations = 100000

    for _ in range(num_iterations):
        my_warriors = your_strength.copy()
        alice_warriors = alice_strength.copy()

        while my_warriors and alice_warriors:
            my_pick = pick_strategy(my_warriors, alice_warriors)
            alice_pick = random.choice(alice_warriors)
            prob_win = win_probability(my_pick, alice_pick)
            my_warriors.remove(my_pick)
            alice_warriors.remove(alice_pick)
            if random.random() < prob_win:
                my_warriors.append(my_pick + alice_pick)
            else:
                alice_warriors.append(my_pick + alice_pick)
        if my_warriors:
            wins += 1

    return wins / num_iterations

# Example strengths
your_strength = [5, 8, 1]
alice_strength = [3, 4, 6, 7]

# 1. Max strategy
max_strat_probability = simulate_game(your_strength, alice_strength, max_strategy)
print("Probability of winning with max strategy (Monte Carlo Simulation):", max_strat_probability)

# 2. Min strategy
min_strat_probability = simulate_game(your_strength, alice_strength, min_strategy)
print("Probability of winning with min strategy (Monte Carlo Simulation):", min_strat_probability)

# 3. Expected Gain is 0

# 4. Optimal strategy
optimal_strat_probability = simulate_game(your_strength, alice_strength, optimal_strategy)
print("Probability of winning with optimal strategy (Monte Carlo Simulation):", optimal_strat_probability)

