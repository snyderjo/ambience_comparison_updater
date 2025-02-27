with threeWeeksAgo as
(
    select current_date - interval'3 weeks' as baseday
    )
,
bounds as
(
    select
        baseday + interval'3 days' as upper_bound
        , baseday as lower_bound
    from threeWeeksAgo
)
,
ambience_recs as (
    select a.reading_id, b.room, a.reading_dttm
        , a.temp, a.pressure, a.humidity
        , a.pitch, a.roll, a.yaw
        , a.accel_x, a.accel_y, a.accel_z
    from ambience.readings a
    right join ambience.location b
        on a.location_id = b.id
    where 1 = 1
        and reading_dttm > (select lower_bound from bounds)
        and reading_dttm < (select upper_bound from bounds)
    order by reading_dttm
)
select * from ambience_recs order by room, reading_dttm;
