select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      





with validation_errors as (

    select
        address, sold_date
    from HOUSEMARKET.MA_HOUSES_ma_houses.stg_house_sales
    group by address, sold_date
    having count(*) > 1

)

select *
from validation_errors



      
    ) dbt_internal_test