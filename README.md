# Investment Optimization Algorithm 📈

This project provides a software solution to maximize investment portfolio profits for **Sienna's** clients. It compares a Brute Force approach with an Optimized solution using Dynamic Programming.

## 🚀 Project Objective
Find the most profitable combination of stocks for a **€500** investment per client.
- Each stock can only be purchased once.
- No fractional shares allowed.
- Maximize total profit after a 2-year period.

## 🛠️ Project Structure
- `bruteforce.py`: Exhaustive solution exploring all possible combinations ($2^n$).
- `optimized.py`: High-performance solution based on the 0/1 Knapsack algorithm.
- `data_loader.py`: Module for ingestion and cleaning of CSV data (powered by NumPy).
- `results.py`: Main script to run benchmarks across all datasets.
- `dataset1.csv` & `dataset2.csv`: Historical test datasets (1000+ actions each).

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd p7-algorithm
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install numpy
   ```

## 💻 Usage

### Run comparative tests
The `results.py` script executes the algorithm on the three data files and displays profits and execution time:
```bash
python3 results.py
```

### Test a specific file
You can also run the optimized algorithm directly:
```bash
python3 optimized.py
```

## 📊 Performance and Results
The optimized algorithm utilizes **Dynamic Programming**.

| Characteristic | Brute Force | Optimized Algorithm |
| :--- | :--- | :--- |
| **Complexity** | $O(2^n)$ | $O(n \times W)$ |
| **Capacity** | < 25 actions | > 1000 actions |
| **Execution Time (1000 actions)** | Uncalculable | ~2 seconds |

### Data Audit
The program includes a safety filter that automatically discards corrupted data found in historical files (negative or zero prices), ensuring investment reliability.

## 🏆 Backtest Results
- **Dataset 1**: The algorithm outperforms Sienna's manual selection by **+€1.94**.
- **Dataset 2**: The algorithm outperforms Sienna's manual selection by **+€4.18**.

## ⚖️ License
This project was developed as part of an OpenClassrooms training program.
