
  
    

        create or replace transient table HOUSEMARKET.MA_HOUSES_ma_houses.mart_monthly_trends
         as
        (with base as (
    select * from HOUSEMARKET.MA_HOUSES_ma_houses.fact_sales
)
, monthly as (
    select
        date_trunc('month', sold_date) as month,
        sum(price) as total_sales,
        avg(price / nullif(square_feet,0)) as price_per_sqft
    from base
    group by 1
)
select * from monthly
        );
      
  