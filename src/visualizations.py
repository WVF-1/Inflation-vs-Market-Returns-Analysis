"""
Visualization Module
Creates publication-quality charts for the inflation vs returns analysis.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10


class FinancialVisualizer:
    """Creates visualizations for financial analysis."""
    
    @staticmethod
    def plot_inflation_vs_nominal_returns(df, save_path=None):
        """
        Create dual-axis plot showing inflation rate and nominal returns over time.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with Inflation_Rate and Nominal_Return columns
        save_path : str, optional
            Path to save the figure
        """
        fig, ax1 = plt.subplots(figsize=(14, 7))
        
        # Plot inflation rate
        color1 = '#e74c3c'
        ax1.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Inflation Rate (YoY %)', color=color1, fontsize=12, fontweight='bold')
        ax1.plot(df.index, df['Inflation_Rate'] * 100, color=color1, linewidth=2, label='Inflation Rate')
        ax1.tick_params(axis='y', labelcolor=color1)
        ax1.grid(True, alpha=0.3)
        
        # Create second y-axis for returns
        ax2 = ax1.twinx()
        color2 = '#3498db'
        ax2.set_ylabel('Monthly Return (%)', color=color2, fontsize=12, fontweight='bold')
        ax2.plot(df.index, df['Nominal_Return'] * 100, color=color2, linewidth=1.5, alpha=0.7, label='Nominal Return')
        ax2.tick_params(axis='y', labelcolor=color2)
        ax2.axhline(y=0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
        
        # Title and layout
        plt.title('Inflation Rate vs S&P 500 Nominal Returns (2012-2023)', 
                  fontsize=14, fontweight='bold', pad=20)
        
        # Add legends
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=10)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved: {save_path}")
        
        plt.show()
    
    @staticmethod
    def plot_real_vs_nominal_returns(df, save_path=None):
        """
        Plot cumulative nominal vs real returns over time.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with Cumulative_Nominal and Cumulative_Real columns
        save_path : str, optional
            Path to save the figure
        """
        fig, ax = plt.subplots(figsize=(14, 7))
        
        # Plot cumulative returns
        ax.plot(df.index, df['Cumulative_Nominal'] * 100, 
                color='#2ecc71', linewidth=2.5, label='Nominal Returns')
        ax.plot(df.index, df['Cumulative_Real'] * 100, 
                color='#9b59b6', linewidth=2.5, label='Real Returns (Inflation-Adjusted)')
        
        # Fill the area between
        ax.fill_between(df.index, df['Cumulative_Nominal'] * 100, df['Cumulative_Real'] * 100,
                        alpha=0.2, color='#e74c3c', label='Inflation Impact')
        
        # Formatting
        ax.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax.set_ylabel('Cumulative Return (%)', fontsize=12, fontweight='bold')
        ax.set_title('Cumulative Nominal vs Real Returns: The Inflation Effect',
                     fontsize=14, fontweight='bold', pad=20)
        ax.legend(loc='upper left', fontsize=11)
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved: {save_path}")
        
        plt.show()
    
    @staticmethod
    def plot_rolling_correlation(df, correlation_series, window=60, save_path=None):
        """
        Plot rolling correlation between inflation and returns.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with the data
        correlation_series : pd.Series
            Rolling correlation values
        window : int
            Window size used for rolling correlation
        save_path : str, optional
            Path to save the figure
        """
        fig, ax = plt.subplots(figsize=(14, 7))
        
        # Plot rolling correlation
        ax.plot(correlation_series.index, correlation_series, 
                color='#16a085', linewidth=2.5, label=f'{window}-Month Rolling Correlation')
        
        # Add horizontal reference lines
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
        ax.axhline(y=0.5, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Strong Positive')
        ax.axhline(y=-0.5, color='blue', linestyle='--', linewidth=1, alpha=0.5, label='Strong Negative')
        
        # Shading for correlation strength
        ax.fill_between(correlation_series.index, 0, correlation_series, 
                        where=(correlation_series > 0), alpha=0.2, color='red', interpolate=True)
        ax.fill_between(correlation_series.index, 0, correlation_series, 
                        where=(correlation_series < 0), alpha=0.2, color='blue', interpolate=True)
        
        # Formatting
        ax.set_xlabel('Date', fontsize=12, fontweight='bold')
        ax.set_ylabel('Correlation Coefficient', fontsize=12, fontweight='bold')
        ax.set_title(f'Rolling {window}-Month Correlation: Inflation vs Stock Returns',
                     fontsize=14, fontweight='bold', pad=20)
        ax.set_ylim(-1, 1)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved: {save_path}")
        
        plt.show()
    
    @staticmethod
    def plot_inflation_regimes(df, regime_stats, save_path=None):
        """
        Create visualization comparing returns across inflation regimes.
        
        Parameters:
        -----------
        df : pd.DataFrame
            DataFrame with regime data
        regime_stats : pd.DataFrame
            Regime statistics
        save_path : str, optional
            Path to save the figure
        """
        fig, axes = plt.subplots(1, 2, figsize=(16, 7))
        
        # Define regime order and colors
        regime_order = ['Low (<1%)', 'Moderate (1-3%)', 'High (>3%)']
        colors = ['#3498db', '#f39c12', '#e74c3c']
        
        # Plot 1: Box plot of returns by regime
        ax1 = axes[0]
        df_plot = df[df['Inflation_Regime'].isin(regime_order)]
        
        box_parts = ax1.boxplot(
            [df_plot[df_plot['Inflation_Regime'] == regime]['Nominal_Return'] * 100 
             for regime in regime_order],
            labels=regime_order,
            patch_artist=True,
            widths=0.6
        )
        
        # Color the boxes
        for patch, color in zip(box_parts['boxes'], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)
        
        ax1.set_ylabel('Monthly Nominal Return (%)', fontsize=11, fontweight='bold')
        ax1.set_xlabel('Inflation Regime', fontsize=11, fontweight='bold')
        ax1.set_title('Return Distribution by Inflation Regime', fontsize=12, fontweight='bold')
        ax1.axhline(y=0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Plot 2: Bar chart comparing average returns
        ax2 = axes[1]
        
        # Extract mean returns for plotting
        nominal_means = []
        real_means = []
        for regime in regime_order:
            if regime in regime_stats.index:
                nominal_means.append(regime_stats.loc[regime, ('Nominal_Return', 'mean')] * 100)
                real_means.append(regime_stats.loc[regime, ('Real_Return', 'mean')] * 100)
            else:
                nominal_means.append(0)
                real_means.append(0)
        
        x = np.arange(len(regime_order))
        width = 0.35
        
        bars1 = ax2.bar(x - width/2, nominal_means, width, label='Nominal Return', 
                       color='#2ecc71', alpha=0.8)
        bars2 = ax2.bar(x + width/2, real_means, width, label='Real Return', 
                       color='#9b59b6', alpha=0.8)
        
        ax2.set_xlabel('Inflation Regime', fontsize=11, fontweight='bold')
        ax2.set_ylabel('Average Monthly Return (%)', fontsize=11, fontweight='bold')
        ax2.set_title('Average Returns by Inflation Regime', fontsize=12, fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(regime_order)
        ax2.legend(fontsize=10)
        ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
        ax2.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.2f}%',
                        ha='center', va='bottom' if height > 0 else 'top', 
                        fontsize=9)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Saved: {save_path}")
        
        plt.show()


if __name__ == "__main__":
    print("Visualization Module")
    print("Ready for use in analysis notebooks")