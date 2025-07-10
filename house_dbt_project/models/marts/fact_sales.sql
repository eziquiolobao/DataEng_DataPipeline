with source as (
    select * from {{ ref('stg_house_sales') }}
)
select
    sold_date,
    price,
    beds,
    baths,
    square_feet,
    property_type
from source
