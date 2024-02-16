import squirrels as sr


def main(sqrl: sr.ParametersArgs) -> None:
    """
    Create all widget parameters in this file. If two or more datasets use a different set of parameters, define them all
    here, and specify the subset of parameters used for each dataset in the "squirrels.yml" file.

    Parameters are created by a factory method associated to some parameters class. For example (note the "Create"):
    > sr.SingleSelectParameter.Create(...)

    The parameter classes available are:
    - SingleSelectParameter, MultiSelectParameter, DateParameter, DateRangeParameter, NumberParameter, NumberRangeParameter
    
    The factory methods available are:
    - Create, CreateSimple, CreateFromSource
    """

    """ Example of creating SingleSelectParameter and specifying each option by code """
    group_by_options = [
        sr.SelectParameterOption("g0", "Gender", columns=["gender"]),
        sr.SelectParameterOption("g1", "City", columns=["state", "city"]),
        sr.SelectParameterOption("g2", "Category", columns=["category"]),
        sr.SelectParameterOption("g3", "State", columns=["state"]),
        sr.SelectParameterOption("g4", "Month", columns=["STRFTIME('%Y-%m', date(trans_date_trans_time))"], aliases = ["Month"])
    ]
    sr.SingleSelectParameter.Create("group_by", "Group By", group_by_options)

    # Not entirely the most comprehensive
    gender_options = [
        sr.SelectParameterOption("gen0", "M", columns=["M"]),
        sr.SelectParameterOption("gen1", "F", columns=["F"])
    ]
    sr.MultiSelectParameter.CreateSimple("gender", "Gender", gender_options)

    fraud_percent_count = [
        sr.SelectParameterOption("fpc0", "Count"),
        sr.SelectParameterOption("fpc1", "Percentage")
    ]
    sr.SingleSelectParameter.CreateSimple("percent_toggle", "Percent/Count", fraud_percent_count)

    ## TODO: Add from-source parameters for single select


    """ Example of creating MultiSelectParameter from lookup query/table """
    category_ds = sr.MultiSelectDataSource("SELECT DISTINCT Category FROM LU_JobCategories", "Category", "Category")
    sr.MultiSelectParameter.CreateFromSource("job_category", "Job Category Filter", category_ds)

    """ Example of creating MultiSelectParameter with parent from lookup query/table """
    subcategory_ds = sr.MultiSelectDataSource("Lu_JobCategories", "JobTitle", "JobTitle", parent_id_col="Category")
    sr.MultiSelectParameter.CreateFromSource("job_subcategory", "Job Filter", subcategory_ds, parent_name="job_category")

    # Note to Tim, can you make sure that I'm using the createSimple correctly here?
    is_online_options = [
        sr.SelectParameterOption("Person", "In-Person"),
        sr.SelectParameterOption("Online", "Online"),
        sr.SelectParameterOption("Uncertain", "Uncertain")
    ]
    sr.SingleSelectParameter.Create("is_online", "Online/In-Person", is_online_options)

    """Multiselect Simple Parent and Source Multiselect child"""
    trans_category_ds = sr.MultiSelectDataSource("LU_Online", "category", "category", parent_id_col= "isOnline")
    sr.MultiSelectParameter.CreateFromSource("transaction_category", "Transaction Category", trans_category_ds, parent_name="is_online")

    """Date and DateRange Parameters"""

    
    """ Example of creating DateParameter """
    sr.DateParameter.CreateSimple("start_date", "Start Date", "2018-01-01")

    """ Example of creating DateParameter from list of DateParameterOption's """
    end_date_option = [sr.DateParameterOption("2023-12-31")]
    sr.DateParameter.Create("end_date", "End Date", end_date_option)

    """ Example of creating DateRangeParameter """
    sr.DateRangeParameter.CreateSimple("date_range", "Date Range", "2018-01-01", "2023-12-31")

    """"DateRangeParameter from Source"""
    dob_data_source = sr.DateRangeDataSource("select min(date(dob)) as min_dob, max(date(dob)) as max_dob from transactions", "min_dob", "max_dob")
    sr.DateRangeParameter.CreateFromSource("between_dob", "Date of Birth Between", dob_data_source)
    
    """ Example of Creating DateParameter from source"""
    minimum_date_source = sr.DateDataSource("select min(date(trans_date_trans_time)) as oldest_date, max(date(trans_date_trans_time)) as nearest_date from transactions", "oldest_date")
    sr.DateParameter.CreateFromSource("min_date_source", "Minimum Transaction Date", minimum_date_source)

    """ Example of Creating DateParameter from source"""
    max_date_source = sr.DateDataSource("select min(date(trans_date_trans_time)) as oldest_date, max(date(trans_date_trans_time)) as nearest_date from transactions", "nearest_date")
    sr.DateParameter.CreateFromSource("max_date_source", "Maximum Transaction Date", max_date_source)


    """Number and number range parameters"""

    sr.NumberParameter.CreateSimple("min_filter", "Amounts Greater Than", min_value=0, max_value=50000, increment=100)
    
    query = "SELECT 0 as min_value, round(max(amt),-1) as max_value, 10 as increment FROM transactions WHERE is_fraud = '1'"
    max_amount_ds = sr.NumberDataSource(query, "min_value", "max_value", increment_col="increment", default_value_col="max_value")
    sr.NumberParameter.CreateFromSource("max_filter", "Amounts Less Than", max_amount_ds)

    sr.NumberRangeParameter.CreateSimple("between_filter", "Amounts Between", 0, 500, default_lower_value=10, default_upper_value=400)
