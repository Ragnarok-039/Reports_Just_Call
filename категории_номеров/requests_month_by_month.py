import pandas as pd
import time
import pymysql

from tqdm import tqdm
from clickhouse_driver import Client
from calendar import monthrange

tqdm.pandas()

start_time = time.time()

path = r'D:\������\���������_�������\files\\'

my_connect = pymysql.Connect(host="192.168.1.128", user="base_dep_slave", passwd="QxPGHGdzCLao",
                             db="suitecrm",
                             charset='utf8')

for req_year in range(2016, 2017):
    for i in range(1, 13):
        time_1 = time.time()

        req_month = i
        calls_month = (req_month - 3) % 12 + 1
        if calls_month > req_month:
            calls_year = req_year - 1
        else:
            calls_year = req_year
        #         print(req_month, req_year, calls_month, calls_year)

        sql = f"""
        with requests as (select 'RTK'                              as project,
                         if(length(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                           '')) <=
                            10,
                            concat(8,
                                   replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ', '')),
                            concat(8,
                                   right(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                                 ''), 10))) as phone_request,
                         date(r.date_entered)               as request_date,
                         assigned_user_id                   as user,
                         user_id_c                          as super,
                         status
                  from suitecrm.jc_meetings_rostelecom as r
                           left join suitecrm.jc_meetings_rostelecom_cstm as r_c on r.id = r_c.id_c
                  where status != 'Error'
                    and month(date_entered) = {req_month}
                    and year(date_entered) = {req_year}

                  union all
                  select 'Beeline'                          as project,
                         if(length(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                           '')) <=
                            10,
                            concat(8,
                                   replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ', '')),
                            concat(8,
                                   right(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                                 ''), 10))) as phone_request,
                         date(b.date_entered)               as request_date,
                         assigned_user_id                   as user,
                         user_id_c                          as super,
                         status
                  from suitecrm.jc_meetings_beeline as b
                           left join suitecrm.jc_meetings_beeline_cstm as b_c on b.id = b_c.id_c
                  where status != 'Error'
                    and month(date_entered) = {req_month}
                    and year(date_entered) = {req_year}

                  union all
                  select 'DOMRU'                            as project,
                         if(length(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                           '')) <=
                            10,
                            concat(8,
                                   replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ', '')),
                            concat(8,
                                   right(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                                 ''), 10))) as phone_request,
                         date(d.date_entered)               as request_date,
                         assigned_user_id                   as user,
                         user_id_c                          as super,
                         status
                  from suitecrm.jc_meetings_domru as d
                           left join suitecrm.jc_meetings_domru_cstm as d_c on d.id = d_c.id_c
                  where status != 'Error'
                    and month(date_entered) = {req_month}
                    and year(date_entered) = {req_year}

                  union all
                  select 'TTK'                              as project,
                         if(length(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                           '')) <=
                            10,
                            concat(8,
                                   replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ', '')),
                            concat(8,
                                   right(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                                 ''), 10))) as phone_request,
                         date(t.date_entered)               as request_date,
                         assigned_user_id                   as user,
                         user_id_c                          as super,
                         status
                  from suitecrm.jc_meetings_ttk as t
                           left join suitecrm.jc_meetings_ttk_cstm as t_c on t.id = t_c.id_c
                  where status != 'Error'
                    and month(date_entered) = {req_month}
                    and year(date_entered) = {req_year}

                  union all
                  select 'NBN'                              as project,
                         if(length(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                           '')) <=
                            10,
                            concat(8,
                                   replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ', '')),
                            concat(8,
                                   right(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                                 ''), 10))) as phone_request,
                         date(n.date_entered)               as request_date,
                         assigned_user_id                   as user,
                         user_id_c                          as super,
                         status
                  from suitecrm.jc_meetings_netbynet as n
                           left join suitecrm.jc_meetings_netbynet_cstm as n_c on n.id = n_c.id_c
                  where status != 'Error'
                    and month(date_entered) = {req_month}
                    and year(date_entered) = {req_year}

                  union all
                  select 'MTS'                              as project,
                         if(length(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                           '')) <=
                            10,
                            concat(8,
                                   replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ', '')),
                            concat(8,
                                   right(replace(replace(replace(replace(phone_work, '-', ''), ')', ''), '(', ''), ' ',
                                                 ''), 10))) as phone_request,
                         date(m.date_entered)               as request_date,
                         assigned_user_id                   as user,
                         user_id_c                          as super,
                         status
                  from suitecrm.jc_meetings_mts as m
                           left join suitecrm.jc_meetings_mts_cstm as m_c on m.id = m_c.id_c
                  where status != 'Error'
                    and month(date_entered) = {req_month}
                    and year(date_entered) = {req_year}),

        new_rob as (select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2023_04
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2023_03
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2023_02
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2023_01
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_12
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_11
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_10
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_09
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_08
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_07
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_06
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_05
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_04
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_03
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_02
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2022_01
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2021_12
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2021_11
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2021_10
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2021_09
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2021_08
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1
                 union all
                 select *
                 from (select date(call_date)                                              as my_date,
                              uniqueid,
                              substring(dialog, 11, 4)                                     as ochered,
                              phone,
                              row_number() over (partition by phone order by my_date desc) as num
                       from suitecrm_robot.jc_robot_log_2021_07
                       where month(call_date) between {calls_month} and {req_month}
                         and year(call_date) between {calls_year} and {req_year}) as temp
                 where temp.num = 1)

    select requests.phone_request,
           requests.user,
           requests.status,
           requests.request_date,
           new_rob.uniqueid,
           new_rob.ochered,
           new_rob.phone,
           requests.project
    from requests
             left join new_rob on requests.phone_request = new_rob.phone;
        """

        df = pd.read_sql_query(sql, my_connect)
        df_to_file = f'{req_month}_{req_year}.csv'
        full_path = f'{path}{df_to_file}'

        df.to_csv(full_path, index=False, sep=';', encoding='utf-8')

        time_2 = time.time()
        #         print(sql)
        #         print(df.head())
        print(f'���������: {df_to_file}')
        print(f'���� �������: {round(time_2 - time_1, 3)} ���.')
