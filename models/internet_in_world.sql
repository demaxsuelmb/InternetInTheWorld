select 
  int.Entity as country
  ,int.Code	as country_code
  ,int.Year	
  ,int.Cellular_Subscription as cellulars
  ,int.Internet_Users___	as internet_users
  ,int.No__of_Internet_Users as no_internet_users
  ,int.Broadband_Subscription	as broadband_subscription	
from `dbt_database.f_internet_world` as int