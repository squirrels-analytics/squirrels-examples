from squirrels import ParametersArgs, parameters as p, parameter_options as po

def main(sqrl: ParametersArgs) -> None:
    ## Loan Amount Parameter
    p.TextParameter.CreateSimple(
        "loan_amount", "Loan Amount", default_text="500000", input_type="number", description="Loan amount principal remaining"
    )

    ## Mortgage Rate Parameter
    p.NumberParameter.CreateSimple(
        "mortgage_rate", "Mortgage Rate (Percent)", min_value="0", max_value="20", increment="0.01", default_value="4.34",
        description="Annual mortgage rate in percent"
    )

    ## Number of Compounding Periods per Year
    compound_periods_options = [
        po.SelectParameterOption("1", "1"), 
        po.SelectParameterOption("2", "2", is_default=True),
        po.SelectParameterOption("3", "3"), 
        po.SelectParameterOption("4", "4"),
        po.SelectParameterOption("6", "6"), 
        po.SelectParameterOption("12", "12")
    ]
    p.SingleSelectParameter.CreateWithOptions("compound_periods", "Compounding Periods per Year", compound_periods_options)

    ## Number of Years Parameter
    p.NumberParameter.CreateSimple("num_years", "Number Of Years", min_value=0, max_value=50, default_value=20)
    
    ## Number of Years Parameter
    p.NumberParameter.CreateSimple("num_months", "Number Of Additional Months", min_value=0, max_value=11, default_value=0)
    
    ## Start Date Parameter
    p.DateParameter.CreateSimple("start_date", "Start Date", default_date="2026-01-01")

    ## Mortgage Payment Parameter
    p.TextParameter.CreateSimple("mortgage_payment", "Monthly Mortgage Payment", default_text="3000", input_type="number")

    ## Number of Trials Parameter
    p.NumberParameter.CreateSimple("num_trials", "Number Of Trials", min_value=100, max_value=10_000, increment=100, default_value=1000)
