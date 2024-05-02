with track_flights as (
    select *
     from  {{source('Raw_data','flights')}}
),

airlines as (
    select * from  {{source('Raw_data','airlines')}}
), 

flight_airline as (
    select  a.*, f.id as flight_id
    from track_flights f
    left join airlines a
    on a.ICAO = f.airline_icao
),

flights_per_airline as (
    select count(*),Code,ICAO
    from flight_airline
    group by Code,ICAO
)
select * from flights_per_airline