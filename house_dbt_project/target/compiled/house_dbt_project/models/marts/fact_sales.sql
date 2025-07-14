with source as (
    select * from HOUSEMARKET.MA_HOUSES_ma_houses.stg_house_sales
)
select
    sold_date,
    price,
    beds,
    baths,
    square_feet,
    property_type
from source