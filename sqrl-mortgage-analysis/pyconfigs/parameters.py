from squirrels import ParametersArgs, parameters as p, parameter_options as po


# Loan Amount Parameter
@p.TextParameter.create_simple(
    "loan_amount", "Loan Amount", default_text="500000", input_type="number", description="Loan amount principal remaining"
)
def loan_amount_options() -> None:
    pass


# Mortgage Rate Parameter
@p.NumberParameter.create_simple(
    "mortgage_rate", "Mortgage Rate (Percent)", min_value="0", max_value="20", increment="0.01", default_value="4.00", 
    description="Annual mortgage rate in percent"
)
def mortgage_rate_options() -> None:
    pass


# Compounding Periods per Year Parameter
@p.SingleSelectParameter.create_with_options(
    "compound_periods", "Compounding Periods per Year"
)
def compound_periods_options() -> list[po.SelectParameterOption]:
    return [
        po.SelectParameterOption("1", "1"), 
        po.SelectParameterOption("2", "2", is_default=True),
        po.SelectParameterOption("3", "3"), 
        po.SelectParameterOption("4", "4"),
        po.SelectParameterOption("6", "6"), 
        po.SelectParameterOption("12", "12")
    ]


# Number of Years Parameter
@p.NumberParameter.create_simple(
    "num_years", "Number Of Years", min_value=0, max_value=50, default_value=25
)
def num_years_options() -> None:
    pass


# Number of Additional Months Parameter
@p.NumberParameter.create_simple(
    "num_months", "Number Of Additional Months", min_value=0, max_value=11, default_value=0
)
def num_months_options() -> None:
    pass


# Start Date Parameter
@p.DateParameter.create_simple(
    "start_date", "Start Date", default_date="2026-01-01"
)
def start_date_options() -> None:
    pass


# Mortgage Payment Parameter
@p.TextParameter.create_simple(
    "mortgage_payment", "Monthly Mortgage Payment", default_text="3500", input_type="number"
)
def mortgage_payment_options() -> None:
    pass


# Number of Trials Parameter
@p.NumberParameter.create_simple(
    "num_trials", "Number Of Trials", min_value=100, max_value=10_000, increment=100, default_value=1000
)
def num_trials_options() -> None:
    pass
