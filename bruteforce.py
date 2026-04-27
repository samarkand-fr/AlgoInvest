import time
from data_loader import read_actions

def get_best_bruteforce(actions, max_budget):
    """
    Finds the most profitable combination of actions within a given budget
    by evaluating all possible combinations (O(2^n) time complexity).

    Args:
        actions (list): List of dictionaries containing action details.
        max_budget (float): The maximum allowed budget.

    Returns:
        tuple: (best_combo, best_cost, best_profit)
                best_combo (list): The list of chosen actions.
                best_cost (float): Total cost of the chosen actions.
                best_profit (float): Total profit of the chosen actions.
    """
    num_actions = len(actions)
    best_profit = 0
    best_combo = []

    # Iterate through all 2^num_actions possible combinations using bitwise shift
    for combo_index in range(1 << num_actions):
        current_combo = []
        total_cost = 0
        total_profit = 0
        
        for action_index in range(num_actions):
            # Check if the action_index-th bit is set in the current combination integer combo_index
            if (combo_index >> action_index) & 1:
                current_combo.append(actions[action_index])
                total_cost += actions[action_index]['cost']
                total_profit += actions[action_index]['profit']
        
        # Update the best combination if it fits the budget and yields higher profit
        if total_cost <= max_budget and total_profit > best_profit:
            best_profit = total_profit
            best_combo = current_combo
            
    return best_combo, sum(action['cost'] for action in best_combo), best_profit

if __name__ == "__main__":
    datasets = [
        'actions.csv',   # 20 actions originales
        'dataset1.csv',  # Dataset 1 historique
        'dataset2.csv',  # Dataset 2 historique
    ]

    for filepath in datasets:
        actions = read_actions(filepath)
        start_time = time.time()
        combo, cost, profit = get_best_bruteforce(actions, 500)
        elapsed = time.time() - start_time
        print(f"[{filepath}] Actions valides: {len(actions)} | "
              f"Time: {elapsed:.2f}s | Cost: {cost:.2f}€ | Profit: {profit:.2f}€")