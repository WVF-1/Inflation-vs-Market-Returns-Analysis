"""
Calculations Module
Performs financial calculations including returns, real returns, correlations, and regime analysis.
"""

import pandas as pd
import numpy as np


class FinancialCalculator:
    """Performs financial calculations on market and inflation data."""
    
    @staticmethod
    def calculate_returns(prices_df, price_col='close'):
        """
        Calculate monthly returns from prices.
        
        Parameters:
        -----------
        prices_df : pd.DataFrame
            DataFrame with price data
        price_col : str
            Column name containing prices
            
        Returns:
        --------
        pd.Series
            Monthly returns (as decimals, e.g., 0.05 = 5%)
        """
        returns = prices_df[price_col].pct_change()
        return returns.dropna()
    
    @staticmethod
    def align_data(cpi_df, returns_series):
        """
        Align CPI and returns data to have matching dates.
        
        Parameters:
        -----------
        cpi_df : pd.DataFrame
            DataFrame with inflation data (may have mid-month dates)
        returns_series : pd.Series
            Series with return data (month-end dates)
            
        Returns:
        --------
        pd.DataFrame
            Aligned DataFrame with both inflation and returns
        """
        # Normalize CPI dates to month-end to match returns
        cpi_normalized = cpi_df.copy()
        cpi_normalized.index = cpi_normalized.index.to_period('M').to_timestamp('M')
        
        # Normalize returns index to month-end as well
        returns_normalized = returns_series.copy()
        returns_normalized.index = returns_normalized.index.to_period('M').to_timestamp('M')
        
        # Create a combined dataframe
        combined = pd.DataFrame({
            'Inflation_Rate': cpi_normalized['Inflation_Rate'],
            'Nominal_Return': returns_normalized
        })
        
        # Drop any rows with missing data
        combined = combined.dropna()
        
        return combined
    
    @staticmethod
    def calculate_real_returns(combined_df):
        """
        Calculate real returns from nominal returns and inflation.
        
        Real Return ≈ Nominal Return - Inflation Rate
        
        Parameters:
        -----------
        combined_df : pd.DataFrame
            DataFrame with Nominal_Return and Inflation_Rate columns
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with added Real_Return column
        """
        # Simple approximation: real return = nominal return - inflation
        combined_df['Real_Return'] = combined_df['Nominal_Return'] - combined_df['Inflation_Rate']
        
        return combined_df
    
    @staticmethod
    def calculate_rolling_correlation(df, col1, col2, window=60):
        """
        Calculate rolling correlation between two columns.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame containing the data
        col1 : str
            First column name
        col2 : str
            Second column name
        window : int
            Rolling window size in months (default: 60 for 5 years)
            
        Returns:
        --------
        pd.Series
            Rolling correlation values
        """
        rolling_corr = df[col1].rolling(window=window).corr(df[col2])
        return rolling_corr
    
    @staticmethod
    def classify_inflation_regime(inflation_rate):
        """
        Classify inflation rate into regime categories.
        
        Parameters:
        -----------
        inflation_rate : float
            Inflation rate as decimal (e.g., 0.02 = 2%)
            
        Returns:
        --------
        str
            Regime classification
        """
        if inflation_rate < 0.01:
            return 'Low (<1%)'
        elif inflation_rate < 0.03:
            return 'Moderate (1-3%)'
        else:
            return 'High (>3%)'
    
    @staticmethod
    def add_inflation_regimes(df):
        """
        Add inflation regime classification to dataframe.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with Inflation_Rate column
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with added Inflation_Regime column
        """
        df['Inflation_Regime'] = df['Inflation_Rate'].apply(
            FinancialCalculator.classify_inflation_regime
        )
        return df
    
    @staticmethod
    def analyze_by_regime(df):
        """
        Calculate summary statistics by inflation regime.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with returns and Inflation_Regime column
            
        Returns:
        --------
        pd.DataFrame
            Summary statistics grouped by regime
        """
        regime_stats = df.groupby('Inflation_Regime').agg({
            'Nominal_Return': ['count', 'mean', 'std', 'min', 'max'],
            'Real_Return': ['mean', 'std', 'min', 'max'],
            'Inflation_Rate': ['mean', 'min', 'max']
        }).round(4)
        
        return regime_stats
    
    @staticmethod
    def calculate_cumulative_returns(df):
        """
        Calculate cumulative returns for nominal and real returns.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with Nominal_Return and Real_Return columns
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with cumulative return columns added
        """
        df['Cumulative_Nominal'] = (1 + df['Nominal_Return']).cumprod() - 1
        df['Cumulative_Real'] = (1 + df['Real_Return']).cumprod() - 1
        
        return df
    
    @staticmethod
    def calculate_annualized_metrics(returns_series):
        """
        Calculate annualized return and volatility.
        
        Parameters:
        -----------
        returns_series : pd.Series
            Series of monthly returns
            
        Returns:
        --------
        dict
            Dictionary with annualized metrics
        """
        # Annualized return (geometric mean)
        ann_return = (1 + returns_series.mean()) ** 12 - 1
        
        # Annualized volatility
        ann_vol = returns_series.std() * np.sqrt(12)
        
        return {
            'Annualized_Return': ann_return,
            'Annualized_Volatility': ann_vol,
            'Sharpe_Ratio': ann_return / ann_vol if ann_vol != 0 else 0
        }


if __name__ == "__main__":
    # Test the calculator
    print("Financial Calculator Module")
    print("Ready for use in analysis notebooks")