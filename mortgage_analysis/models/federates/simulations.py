from squirrels import ModelArgs
import pandas as pd, numpy as np


def main(sqrl: ModelArgs) -> pd.DataFrame:

    def run_single_simulation(stock_returns):
        assert len(stock_returns) == sqrl.ctx["total_num_months"]
        
        value_if_renew_mortgage = sqrl.ctx["loan_amount"]
        value_if_pay_down_house = 0
        for stock_return in stock_returns:
            value_if_renew_mortgage *= (1 + stock_return)
            value_if_pay_down_house *= (1 + stock_return)
            value_if_pay_down_house += sqrl.ctx["monthly_payment"]
        
        return value_if_renew_mortgage, value_if_pay_down_house
    
    ## Randomly generate n values of monthly stock returns for given number of months and number of trials
    num_trials = sqrl.ctx["num_trials"]
    mu, sigma = sqrl.connections["norm_dist_params"]
    data = np.random.normal(loc=mu, scale=sigma, size=sqrl.ctx["total_num_months"]*num_trials)

    ## Run simulations
    rows = []
    for idx in range(num_trials):
        value_if_renew_mortgage, value_if_pay_down_house = run_single_simulation(data[idx::num_trials])
        difference = value_if_renew_mortgage - value_if_pay_down_house
        rows.append({
            "trial_number": idx+1,
            "value_if_renew_mortgage": value_if_renew_mortgage / 1000,
            "value_if_pay_down_house": value_if_pay_down_house / 1000,
            "perc_diff": difference / value_if_pay_down_house * 100
        })

    df = pd.DataFrame(rows)
    return df.round(3)
