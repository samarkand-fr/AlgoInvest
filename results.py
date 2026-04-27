from data_loader import read_actions
from optimized import get_best_optimized
import time

BUDGET = 500

for filepath in ['actions.csv','dataset1.csv', 'dataset2.csv']:
    actions = read_actions(filepath)
    t0 = time.time()
    combo, cost, profit = get_best_optimized(actions, BUDGET)
    elapsed = time.time() - t0

    print(f"\n{'─'*50}")
    print(f"  {filepath}  ({len(actions)} actions valides)")
    print(f"{'─'*50}")
    print(f"  Temps      : {elapsed:.4f}s")
    print(f"  Coût total : {cost:.2f}€")
    print(f"  Profit     : {profit:.2f}€")
    print(f"  Actions choisies ({len(combo)}) :")
    for a in sorted(combo, key=lambda x: -x['profit']):
        print(f"    {a['name']:20s}  {a['cost']:.2f}€  profit={a['profit']:.2f}€")

print(f"\n{'─'*50}")
print("  Décision 1 Sienna (à comparer avec dataset1) :")
print("    Share-GRUT — coût 498.76€ — profit 196.61€")
print()
print("  Décision 2 Sienna (à comparer avec dataset2) :")
print("    18 actions — coût 489.24€ — profit 193.78€")
print(f"{'─'*50}")
