from squirrels import DashboardArgs, dashboards as d
import matplotlib.pyplot as plt


async def main(sqrl: DashboardArgs) -> d.PngDashboard:
    # Retrieve the dataset
    ds = await sqrl.dataset("ice_cream_sales_trend")
    df = ds.to_pandas()
    
    # Sort by temperature for a cleaner expected profit line
    df = df.sort_values('temperature_c')
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Scatter plot for actual profits
    ax.scatter(df['temperature_c'], df['ice_cream_profits'], label='Actual Profit', alpha=0.5, s=10)
    
    # Line plot for expected profits
    ax.plot(df['temperature_c'], df['expected_profit'], label='Expected Profit (Model)', color='red', linewidth=2)
    
    ax.set_title('Ice Cream Profits vs. Temperature')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Profit ($)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    
    fig.tight_layout()
    
    return d.PngDashboard(fig)
