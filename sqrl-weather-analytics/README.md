# weather_analytics

Example Squirrels project for weather analytics and ice cream sales

## Setup

1. In this project, copy the ".env.example" file as ".env" in the root of the project (note that this filename is git ignored)
    - In the ".env" file, set the "SQRL_SECRET__KEY" and "SQRL_SECRET__ADMIN_PASSWORD" variables. We will set the "MOTHERDUCK_TOKEN" variable later.
2. Create an account on MotherDuck for free: https://motherduck.com/
3. Run the following in a notebook to attach the public database containing ice cream sales data:
    - ATTACH 'md:_share/squirrels_analytics_public_db/e0d2843d-c8b2-4c25-9eaa-6a0bc9bb8222' as squirrels_public_data_db;
4. Go to "https://app.motherduck.com/settings/tokens" and create an access token. Save the access token in ".env" as "MOTHERDUCK_TOKEN".

Going forward (or until your access token expires), you will be able to use the APIs for the "ice_cream_sales_trend" dataset!
