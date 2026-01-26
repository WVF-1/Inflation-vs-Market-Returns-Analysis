# Inflation-vs-Market-Returns-Analysis
An analysis of the impacts on the returns of equities from the S&amp;P 500 based on CPI inflation.

---

## Dataset

**Dataset link (CC0 / public):** 
You may view the dataset here: [Kaggle Dataset](https://www.kaggle.com/datasets/rosicky1234/cpi-and-sp500/data).

The dataset is small, clean, and ideal for exploratory analysis and unsupervised learning.

---

# Week 1: Inflation vs Market Returns

A comprehensive analysis exploring the relationship between inflation and S&P 500 returns, examining whether equities truly hedge against inflation.

---

## Project Overview

**Theme:** Macro forces & real returns  
**Level:** Foundational analytics  
**Period Analyzed:** May 2012 - February 2023 (11 years)

---

### Core Questions
1. Do equities hedge inflation?
2. How does inflation affect real vs nominal returns?
3. Are there inflation regimes where markets struggle?

---

## Key Findings

- **Nominal vs Real Returns**: Inflation eroded a significant portion of nominal returns
- **Inflation Regimes**: Market performance varies across low, moderate, and high inflation environments
- **Correlation Dynamics**: The relationship between inflation and returns is time-varying and complex
- **Critical Insight**: Returns without inflation context are meaningless

---

## Project Structure

```
Week-1-Inflation-vs-Market-Returns/
│
├── README.md                          # This file
│
├── data/
│   ├── raw/                          # Original data files
│   │   ├── cpi.csv                   # CPI inflation data (2012-2023)
│   │   └── market_prices.csv         # S&P 500 daily prices (2000-2023)
│   │
│   └── processed/                    # Generated processed data
│       ├── inflation_rates.csv       # Monthly inflation rates
│       ├── market_returns.csv        # Monthly S&P 500 returns
│       └── combined_analysis.csv     # Full analysis dataset
│
├── notebooks/
│   └── inflation_vs_returns_analysis.ipynb  # Main analysis notebook
│
├── src/                              # Python source modules
│   ├── data_loader.py               # Data loading and preprocessing
│   ├── calculations.py              # Financial calculations
│   └── visualization.py             # Plotting functions
│
├── figures/                          # Generated visualizations
│   ├── inflation_vs_nominal_returns.png
│   ├── real_vs_nominal_returns.png
│   ├── rolling_correlation.png
│   └── inflation_regimes.png
│
└── requirements.txt                 # Python dependencies
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip package manager
- Jupyter Notebook

### Installation

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook**
   ```bash
   cd notebooks
   jupyter notebook inflation_vs_returns_analysis.ipynb
   ```

4. **Run all cells** to reproduce the analysis

## Analyses Performed

### 1. Time Series Analysis
- Monthly inflation rates (CPI YoY)
- S&P 500 monthly returns
- Real returns (inflation-adjusted)
- Cumulative performance comparison

### 2. Correlation Analysis
- 60-month (5-year) rolling correlations
- 36-month (3-year) rolling correlations
- Time-varying relationship assessment

### 3. Regime Analysis
Inflation regimes defined as:
- **Low**: < 1% annual inflation
- **Moderate**: 1-3% annual inflation
- **High**: > 3% annual inflation

For each regime, calculated:
- Average returns (nominal and real)
- Return volatility
- Distribution statistics

### 4. Performance Metrics
- Annualized returns
- Annualized volatility
- Sharpe ratios
- Cumulative wealth indices

---

## Key Methodology

### Data Processing
1. **CPI Data**: Monthly year-over-year inflation rates (already calculated)
2. **Market Data**: Daily S&P 500 prices resampled to month-end
3. **Returns**: Calculated as percentage change in monthly closing prices
4. **Real Returns**: Nominal return - Inflation rate (simple approximation)

---

### Real Return Formula
```
Real Return ≈ Nominal Return - Inflation Rate
```

For more precision, the Fisher equation would be:
```
(1 + Real Return) = (1 + Nominal Return) / (1 + Inflation Rate)
```

We use the approximation for simplicity, which is accurate for small values.

---

## Visualizations

The project generates four key visualizations:

1. **Inflation vs Nominal Returns**: Dual-axis time series showing the relationship
2. **Real vs Nominal Returns**: Cumulative returns with inflation impact highlighted
3. **Rolling Correlation**: 5-year rolling correlation between inflation and returns
4. **Inflation Regimes**: Box plots and bar charts comparing regime performance

---

## Key Insights

### The Inflation Impact
Inflation silently erodes purchasing power. A 10% nominal return with 3% inflation is really only a 7% real gain. Over decades, this difference compounds dramatically.

### Regime Matters
Market performance isn't uniform across inflation environments. Understanding the current regime helps set realistic expectations.

### Time-Varying Correlations
The inflation-return relationship isn't stable. Short-term correlations can be misleading - long-term perspective is essential.

### Context is King
Absolute returns are meaningless without economic context. Always evaluate investments through the lens of real, inflation-adjusted returns.

---

## Technical Stack

- **Python 3.8+**: Core programming language
- **pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Base plotting library
- **Seaborn**: Statistical visualization
- **Jupyter**: Interactive development environment

---

## Future Extensions

Potential areas for further analysis:

1. **Longer time horizon**: Include pre-2012 data (1970s stagflation, 2008 crisis)
2. **Asset class comparison**: Compare stocks to bonds, commodities, real estate
3. **International markets**: Analyze inflation hedging in different countries
4. **Sector analysis**: Which sectors perform best in different inflation regimes?
5. **Leading indicators**: Can we predict regime changes?
6. **Portfolio implications**: Optimal asset allocation across regimes

---

## Important Notes

### Data Limitations
- **Time Period**: 11 years (May 2012 - Feb 2023) - limited regime diversity
- **Single Asset**: S&P 500 only - doesn't represent total market or other assets
- **No Dividends**: Uses price returns only, not total returns
- **CPI Limitations**: CPI may not reflect individual inflation experiences

### Analysis Assumptions
- Simple real return calculation (not Fisher equation)
- Monthly frequency (loses some short-term dynamics)
- Regime boundaries are somewhat arbitrary
- Past performance doesn't guarantee future results

---

**Why This Project Matters**

In investing, context is everything. This project teaches the fundamental lesson that returns mean nothing without understanding the economic environment. Whether you're a beginner learning to analyze markets or an experienced analyst building a framework, mastering real returns is essential.

The skills developed here - data processing, statistical analysis, visualization, and economic thinking - form the foundation for all subsequent financial analysis. 

**Remember**: A 20% return in a 15% inflation environment is worse than a 5% return in a 1% inflation environment. Always think real, not nominal.
