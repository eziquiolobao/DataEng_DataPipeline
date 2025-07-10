select * from {{ source('MA_HOUSES', 'stg_house_sales') }}
