# 📈 CodeAlpha Python Internship — Stock Portfolio Tracker

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Internship](https://img.shields.io/badge/CodeAlpha-Internship-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## 📌 Project Overview

The **Stock Portfolio Tracker** is a console-based portfolio management application developed in Python as part of the **CodeAlpha Python Programming Internship**.

It empowers users to track stock holdings, dynamically compute individual asset investments and percentage allocations, identify key portfolio metrics (such as the highest-priced stock and the asset with the largest capital commitment), and automatically export structured portfolio reports to CSV format.

🔗 **GitHub Repository:** [https://github.com/itsSonam01/CodeAlpha-Projects.git](https://github.com/itsSonam01/CodeAlpha-Projects.git)

---

## ✨ Features & Capabilities

- 📊 **Curated Stock Registry**: Includes 10 premier publicly traded companies (AAPL, TSLA, GOOGL, AMZN, MSFT, META, NFLX, NVDA, UBER, PYPL) with baseline market prices.
- ➕ **Dynamic Position Aggregation**: Automatically accumulates quantities if existing ticker symbols are purchased repeatedly during a single session.
- 💰 **Comprehensive Portfolio Analytics**:
  - Calculates total investment capital.
  - Dynamically computes individual portfolio percentage weights ($(\text{Asset Value} / \text{Grand Total}) \times 100$).
  - Automatically identifies the **Highest-Priced Stock** and **Most Invested Position**.
- 💾 **Persistent CSV Export**: Writes transaction logs and grand total summaries out to a cleanly formatted `portfolio.csv` upon exit.
- 🛡️ **Defensive Input Validation**: Validates ticker existence, rejects negative or zero quantities, and safeguards against non-numeric inputs.

---

## 🛠️ Technologies & Concepts Used

| Concept / Module | Implementation Purpose |
| :--- | :--- |
| **Language** | Python 3.x |
| **Standard Libraries** | `csv` (structured data persistence), `os` (terminal clearing) |
| **Data Structures** | Python `dict` for price mappings and user holdings, `lambda` functions for max value aggregations |
| **Input Validation** | `try-except` blocks handling `ValueError` |
| **File I/O** | `csv.writer` writing header rows, line items, and cumulative totals |

---

## 📂 Project Directory Structure

```text
CodeAlpha_StockTracker/
│
├── output/
│   └── sample_output.txt     # Terminal execution logs
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python environment info (standard library only)
├── stock_tracker.py          # Main application source code
└── README.md                 # Project documentation
```

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.x installed. No third-party packages need to be installed via `pip`.

### Execution
Run the script using:

```bash
python stock_tracker.py
```

---

## 📊 Supported Stock Tickers

| Symbol | Company Name | Base Price (USD) |
| :---: | :--- | :---: |
| **AAPL** | Apple Inc. | $180 |
| **TSLA** | Tesla Inc. | $250 |
| **GOOGL** | Alphabet Inc. (Google) | $140 |
| **AMZN** | Amazon.com Inc. | $175 |
| **MSFT** | Microsoft Corp. | $380 |
| **META** | Meta Platforms Inc. | $300 |
| **NFLX** | Netflix Inc. | $450 |
| **NVDA** | NVIDIA Corp. | $500 |
| **UBER** | Uber Technologies | $60 |
| **PYPL** | PayPal Holdings | $65 |

---

## 🎮 Step-by-Step Usage Guide

1. **Option 1 (Add Stock)**:
   - Enter ticker symbol (e.g., `AAPL` or `NVDA` — case insensitive).
   - Enter whole share quantity.
2. **Option 2 (View Portfolio)**:
   - Displays real-time breakdown with share weights and key insights.
3. **Option 3 (Save & Exit)**:
   - Displays the final summary, exports all records to `portfolio.csv`, and terminates cleanly.

---

## 🖥️ Sample Terminal Output

```text
=============================================
   📈 STOCK PORTFOLIO TRACKER | CodeAlpha
=============================================
  Stock    Company            Price
  -----------------------------------
  AAPL     Apple               $180
  TSLA     Tesla               $250
  NVDA     Nvidia              $500
=============================================

  OPTIONS:
  1 → Add Stock
  2 → View Portfolio
  3 → Save & Exit

=============================================
   💼 YOUR PORTFOLIO SUMMARY
=============================================
  Stock    Price      Qty    Total      Share
  ----------------------------------------
  AAPL     $180       5      $900       32.1%
  TSLA     $250       3      $750       26.8%
  NVDA     $500       2      $1000      35.7%
  ----------------------------------------

  💰 Total Investment: $2650
  📈 Highest Price Stock: NVDA
  💹 Most Invested: NVDA
=============================================

  ✅ Portfolio saved to portfolio.csv!
  Thanks! CodeAlpha Internship
```

---

## 🔮 Future Roadmap
- [ ] Connect with live financial APIs (`yfinance`, Alpha Vantage) for real-time market data.
- [ ] Add profit/loss calculation against buy-in prices.
- [ ] Plot portfolio asset allocation charts using `matplotlib` or `seaborn`.

---

## 👩‍💻 Author & Internship Details
- **Author:** **Sonam Thakur**
- **GitHub:** [@itsSonam01](https://github.com/itsSonam01)
- **Repository:** [CodeAlpha-Projects](https://github.com/itsSonam01/CodeAlpha-Projects.git)
- **Company:** [CodeAlpha](https://codealpha.tech/)
- **Domain:** Python Programming Internship
- **Task:** Task 2 — Stock Portfolio Tracker
- **License:** MIT License © 2026 Sonam Thakur
