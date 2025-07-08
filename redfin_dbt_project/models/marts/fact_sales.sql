with source as (
    select * from {{ ref('stg_redfin_sales') }}
)
select
    address,
    sold_date,
    price,
    beds,
    baths,
    square_feet,
    property_type
from source
