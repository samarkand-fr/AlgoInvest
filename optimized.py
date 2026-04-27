import time
from data_loader import read_actions

def get_best_optimized(actions, max_budget):
    """
    Finds the most profitable combination of actions within a given budget
    using Dynamic Programming (0/1 Knapsack problem approach).

    Args:
        actions (list): List of dictionaries containing action details.
        max_budget (float): The maximum allowed budget.

    Returns:
        tuple: (best_combo, best_cost, best_profit)
                best_combo (list): The list of chosen actions.
                best_cost (float): Total cost of the chosen actions.
                best_profit (float): Total profit of the chosen actions.
    """
    scale = 100
    # Convert budget to cents to use as an integer array index
    budget_cents = int(max_budget * scale)
    
    # Pre-filter actions that are too expensive right from the start
    items = [action for action in actions if int(round(action['cost'] * scale)) <= budget_cents]
    num_items = len(items)
    
    # 1D array to store the maximum profit for each budget cent
    max_profit_at_budget = [0.0] * (budget_cents + 1)
    
    # 2D boolean matrix to track choices for backtracking the optimal combination
    history = [[False] * (budget_cents + 1) for _ in range(num_items)]

    for item_index in range(num_items):
        item_cost_cents = int(round(items[item_index]['cost'] * scale))
        item_profit = items[item_index]['profit']
        
        # Traverse the budget backward to guarantee 0/1 rule (use each item at most once)
        for current_budget_cents in range(budget_cents, item_cost_cents - 1, -1):
            if max_profit_at_budget[current_budget_cents - item_cost_cents] + item_profit > max_profit_at_budget[current_budget_cents]:
                max_profit_at_budget[current_budget_cents] = max_profit_at_budget[current_budget_cents - item_cost_cents] + item_profit
                history[item_index][current_budget_cents] = True

    # Retrieve the chosen actions by backtracking through the history matrix
    best_combo = []
    remaining_budget_cents = budget_cents
    for item_index in range(num_items - 1, -1, -1):
        if history[item_index][remaining_budget_cents]:
            best_combo.append(items[item_index])
            # Subtract the weight of the chosen item to trace back
            remaining_budget_cents -= int(round(items[item_index]['cost'] * scale))

    return best_combo, sum(action['cost'] for action in best_combo), max_profit_at_budget[budget_cents]


if __name__ == "__main__":
    datasets = [
        'actions.csv',   # 20 actions originales
        'dataset1.csv',  # Dataset 1 historique
        'dataset2.csv',  # Dataset 2 historique
    ]

    for filepath in datasets:
        actions = read_actions(filepath)
        start_time = time.time()
        combo, cost, profit = get_best_optimized(actions, 500)
        elapsed = time.time() - start_time
        print(f"[{filepath}] Actions valides: {len(actions)} | "
              f"Time: {elapsed:.4f}s | Cost: {cost:.2f}€ | Profit: {profit:.2f}€")