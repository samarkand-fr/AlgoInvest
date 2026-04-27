import numpy as np

def read_actions(filepath):
    """
    Reads a CSV file containing stock actions data using NumPy.
    
    Args:
        filepath (str): The path to the CSV file.
        
    Returns:
        list: A list of dictionaries, where each dictionary represents an action
              with 'name' (str), 'cost' (float), and 'profit' (float in euros).
    """
    try:
        # Use delimiter=',' explicitly.
        # skip_header=1 ignores the title line to avoid type conflicts.
        data = np.genfromtxt(
            filepath, 
            delimiter=',', 
            dtype=None, 
            encoding='utf-8', 
            skip_header=1, 
            invalid_raise=False
        )
        
        actions = []
        for row in data:
            # row[0] = Name, row[1] = Cost, row[2] = Profit percentage
            name = str(row[0])
            cost = float(row[1])
            
            # Clean up the profit string by removing the '%' sign and convert to float
            profit_raw = str(row[2]).replace('%', '')
            profit_pct = float(profit_raw)
            
            # Filter out free or negative cost actions
            if cost > 0:
                actions.append({
                    'name': name,
                    'cost': cost,
                    # Calculate absolute profit in euros
                    'profit': cost * (profit_pct / 100)
                })
        return actions
    except Exception as e:
        print(f"Error while loading data with NumPy: {e}")
        return []