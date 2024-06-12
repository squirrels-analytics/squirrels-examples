import squirrels as sr


def main(sqrl: sr.ParametersArgs) -> None:

    ## Examples of Selection Parameters
    
    group_by_options = [
        sr.SelectParameterOption("g0", "Gender", columns=["gender"]),
        sr.SelectParameterOption("g1", "City", columns=["state", "city"]),
        sr.SelectParameterOption("g2", "Category", columns=["category"]),
        sr.SelectParameterOption("g3", "State", columns=["state"]),
        sr.SelectParameterOption("g4", "Month", columns=["STRFTIME('%Y-%m', date(trans_date_trans_time))"], aliases = ["Month"])
    ]
    sr.SingleSelectParameter.Create("group_by", "Group By", group_by_options)

    gender_options = [
        sr.SelectParameterOption("m", "M"),
        sr.SelectParameterOption("f", "F")
    ]
    sr.MultiSelectParameter.CreateSimple("gender", "Gender", gender_options)

    fraud_percent_count = [
        sr.SelectParameterOption("count", "Count"),
        sr.SelectParameterOption("perc", "Percentage")
    ]
    sr.SingleSelectParameter.CreateSimple("percent_toggle", "Percent/Count", fraud_percent_count)

    category_ds = sr.MultiSelectDataSource("SELECT DISTINCT Category FROM LU_JobCategories", "Category", "Category")
    sr.MultiSelectParameter.CreateFromSource("job_category", "Job Category Filter", category_ds)

    subcategory_ds = sr.MultiSelectDataSource("Lu_JobCategories", "JobTitle", "JobTitle", parent_id_col="Category")
    sr.MultiSelectParameter.CreateFromSource("job_subcategory", "Job Filter", subcategory_ds, parent_name="job_category")

    ## Example of creating parent parameter from source, and child parameter with options written in code

    is_online_options_ds =  sr.SingleSelectDataSource("select distinct isOnline from LU_Online", "isOnline", "isOnline")
    sr.SingleSelectParameter.CreateFromSource("is_online", "Online/In-Person", is_online_options_ds)

    parent_name = "is_online"
    trans_category_options = [
        sr.SelectParameterOption("personal_care", "Personal Care", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("health_fitness", "Health and Fitness", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("misc_pos", "Misc. (In-Person)", parent_option_ids = "In-Person"),
        sr.SelectParameterOption("travel", "Travel", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("kids_pets", "Kids and Pets", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("shopping_pos", "In-Person Shopping", parent_option_ids = "In-Person"),
        sr.SelectParameterOption("food_dining", "Food and Dining", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("home", "Home", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("entertainment", "Entertainment", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("shopping_net", "Online Shopping", parent_option_ids = "Online"),
        sr.SelectParameterOption("misc_net", "Misc. (Online)", parent_option_ids = "Online"),
        sr.SelectParameterOption("grocery_pos", "In-Person Groceries", parent_option_ids = "In-Person"),
        sr.SelectParameterOption("gas_transport", "Gas and Transport", parent_option_ids = "Uncertain"),
        sr.SelectParameterOption("grocery_net", "Online Groceries", parent_option_ids = "Online")
    ]
    sr.MultiSelectParameter.Create("transaction_category", "Transaction Category", trans_category_options, parent_name=parent_name)

    ## Examples of Date and DateRange Parameters
    
    sr.DateParameter.CreateSimple("start_date", "Start Date", "2020-06-01")

    end_date_option = [sr.DateParameterOption("2020-12-31")]
    sr.DateParameter.Create("end_date", "End Date", end_date_option)

    sr.DateRangeParameter.CreateSimple("date_range", "Date Range", "2020-06-01", "2020-12-31")

    dob_data_source = sr.DateRangeDataSource("select min(date(dob)) as min_dob, max(date(dob)) as max_dob from transactions", "min_dob", "max_dob")
    sr.DateRangeParameter.CreateFromSource("between_dob", "Date of Birth Between", dob_data_source)
    
    minimum_date_source = sr.DateDataSource("select min(date(trans_date_trans_time)) as oldest_date from transactions", "oldest_date")
    sr.DateParameter.CreateFromSource("min_date_source", "Minimum Transaction Date", minimum_date_source)

    max_date_source = sr.DateDataSource("select max(date(trans_date_trans_time)) as nearest_date from transactions", "nearest_date")
    sr.DateParameter.CreateFromSource("max_date_source", "Maximum Transaction Date", max_date_source)

    ## Examples of Number and NumberRange Parameters

    sr.NumberParameter.CreateSimple("min_filter", "Amounts Greater Than", min_value=0, max_value=1500, increment=10)

    ## SQLite "round" function doesn't work with negative arguments. Working around it by dividing 10 and multiplying after rounding
    query = "SELECT 0 as min_value, 1500 as max_value, 10 as increment"
    max_amount_ds = sr.NumberDataSource(query, "min_value", "max_value", increment_col="increment", default_value_col="max_value")
    sr.NumberParameter.CreateFromSource("max_filter", "Amounts Less Than", max_amount_ds)

    sr.NumberRangeParameter.CreateSimple("between_filter", "Amounts Between", 0, 1500, increment=10, default_lower_value=100, default_upper_value=1000)

    between_amt_source = sr.NumberRangeDataSource("select 0 as min_amt, 1500 as max_amt, 10 as incr", "min_amt", "max_amt", increment_col="incr")
    sr.NumberRangeParameter.CreateFromSource("between_filter2", "Amounts Between", between_amt_source)
