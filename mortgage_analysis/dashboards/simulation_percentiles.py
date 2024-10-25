from squirrels import DashboardArgs, dashboards as d
from matplotlib import pyplot as plt, figure as f, axes as a
import pandas as pd


def add_quartile_labels(ax: a.Axes, df: pd.DataFrame):
    for i, column in enumerate(df.columns):
        quartiles = df[column].quantile([0, 0.25, 0.5, 0.75, 1])
        for j, q in enumerate(['Min', 'Q1', 'Median', 'Q3', 'Max']):
            ax.text(
                i+1, quartiles.iloc[j], f'{q}: {quartiles.iloc[j]:.3f}', 
                horizontalalignment='center', verticalalignment='center',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7)
            )


async def main(sqrl: DashboardArgs) -> d.PngDashboard:
    """
    Create a dashboard by retrieving datasets using "sqrl.dataset" method and transform the datasets to return as a PngDashboard or a HtmlDashboard.
    - The PngDashboard constructor takes a single argument for either a matplotlib.figure.Figure or io.BytesIO/bytes of PNG data
    - The HtmlDashboard constructor takes a single argument for a io.StringIO/string of HTML data

    It is imperative to set the correct return type in the function signature for "main" above! It allows Squirrels to provide the correct format to 
    the data catalog without having to run this function.
    """
    df = await sqrl.dataset("simulations")

    # Create a figure with two subplots
    fig, (ax0, ax1) = plt.subplots(2, figsize=(6, 8))
    fig: f.Figure; ax0: a.Axes; ax1: a.Axes
    fig.tight_layout(pad=4, h_pad=6)

    # Create a box plot comparing simulations side by side
    df[["value_if_renew_mortgage", "value_if_pay_down_house"]].boxplot(ax=ax0)

    add_quartile_labels(ax0, df[["value_if_renew_mortgage", "value_if_pay_down_house"]])

    ax0.set_yscale('log')
    ax0.set_ylabel("Value of Stocks (in $1000's, log scale)")

    # Create a box plot for distribution of percentage differences
    df[["perc_diff"]].boxplot(ax=ax1)

    add_quartile_labels(ax1, df[["perc_diff"]])

    ax1.set_title('Renew vs Pay Down Mortgage - Percent Diff in Stock Value')
    ax1.set_ylabel('Percentage Difference')

    # Mark the percentile where the percentage difference is zero
    zero_percentile = (df['perc_diff'] < 0).mean() * 100
    ax1.text(0.51, 0, f'Percentile of 0:\n{zero_percentile:.1f}%', color='b', verticalalignment='baseline')
    
    return d.PngDashboard(fig)
