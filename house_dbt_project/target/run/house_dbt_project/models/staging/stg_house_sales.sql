
  create or replace   view HOUSEMARKET.MA_HOUSES_ma_houses.stg_house_sales
  
   as (
    select * from HOUSEMARKET.MA_HOUSES.stg_house_sales
  );

