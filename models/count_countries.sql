select 
    region
    , count(*) as total 
from `dbt_database.countries_world`
group by region
order by total desc 