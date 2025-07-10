





with validation_errors as (

    select
        address, sold_date
    from HOUSEMARKET.MA_HOUSES_ma_houses.stg_house_sales
    group by address, sold_date
    having count(*) > 1

)

select *
from validation_errors


