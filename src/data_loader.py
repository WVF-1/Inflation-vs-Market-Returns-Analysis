"""
Data Loader Module
Handles loading and initial processing of CPI and market price data.
"""

import pandas as pd
import numpy as np
from pathlib import Path


class DataLoader:
    """Loads and performs initial processing of financial data."""
    
    def __init__(self, data_dir='../data/raw'):
        """
        Initialize DataLoader with path to raw data directory.
        
        Parameters:
        -----------
        data_dir : str
            Path to directory containing raw data files
        """
        self.data_dir = Path(data_dir)
        
    def load_cpi(self, filename='CPI.csv'):
        """
        Load CPI data from CSV file.
        
        Parameters:
        -----------
        filename : str
            Name of CPI data file
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with datetime index and inflation rate column
        """
        filepath = self.data_dir / filename
        
        # Read the CSV
        df = pd.read_csv(filepath)
        
        # Create datetime from Year, Month, Day columns
        df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
        
        # Set datetime as index
        df.set_index('Date', inplace=True)
        
        # Keep only the Actual column (YoY inflation rate)
        df = df[['Actual']].copy()
        df.rename(columns={'Actual': 'Inflation_Rate'}, inplace=True)
        
        # Sort by date
        df.sort_index(inplace=True)
        
        return df
    
    def load_market_prices(self, filename='SP500.csv'):
        """
        Load S&P 500 market price data from CSV file.
        
        Parameters:
        -----------
        filename : str
            Name of market prices data file
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with datetime index and OHLC columns
        """
        filepath = self.data_dir / filename
        
        # Read the CSV
        df = pd.read_csv(filepath)
        
        # Convert Date column to datetime with flexible format
        df['Date'] = pd.to_datetime(df['Date'], format='mixed')
        
        # Set datetime as index
        df.set_index('Date', inplace=True)
        
        # Convert column names to lowercase for consistency
        df.columns = df.columns.str.lower()
        
        # Sort by date
        df.sort_index(inplace=True)
        
        return df
    
    def resample_to_monthly(self, df, price_col='close'):
        """
        Resample daily data to monthly frequency (month-end).
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with daily data
        price_col : str
            Column name to use for monthly price
            
        Returns:
        --------
        pd.DataFrame
            DataFrame with monthly frequency
        """
        # Resample to month-end, taking the last available value
        monthly_df = df[[price_col]].resample('ME').last()
        
        return monthly_df
    
    def load_all_data(self):
        """
        Load all data and return as a tuple.
        
        Returns:
        --------
        tuple
            (cpi_df, daily_prices_df, monthly_prices_df)
        """
        # Load raw data
        cpi_df = self.load_cpi()
        daily_prices_df = self.load_market_prices()
        
        # Create monthly version of prices
        monthly_prices_df = self.resample_to_monthly(daily_prices_df)
        
        return cpi_df, daily_prices_df, monthly_prices_df


if __name__ == "__main__":
    # Test the data loader
    loader = DataLoader()
    cpi, daily, monthly = loader.load_all_data()
    
    print("CPI Data:")
    print(cpi.head())
    print(f"\nShape: {cpi.shape}")
    print(f"Date range: {cpi.index.min()} to {cpi.index.max()}")
    
    print("\n" + "="*50)
    print("\nMonthly Market Prices:")
    print(monthly.head())
    print(f"\nShape: {monthly.shape}")
    print(f"Date range: {monthly.index.min()} to {monthly.index.max()}")