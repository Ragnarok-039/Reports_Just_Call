insert into suitecrm_robot_ch.phone_category_total

with jc_rl as (select toDate(jc_rl.call_date) as call_date,
                      jc_rl.phone,
                      jc_rl.uniqueid,
                      case
                          when
                                      jc_rl.ptv_c like '%^3^%'
                                  or jc_rl.ptv_c like '%^5^%'
                                  or jc_rl.ptv_c like '%^6^%'
                                  or jc_rl.ptv_c like '%^10^%'
                                  or jc_rl.ptv_c like '%^11^%'
                                  or jc_rl.ptv_c like '%^19^%'
                                  or jc_rl.ptv_c like '%^14^%' then 'Разметка Наша'
                          when
                                      jc_rl.ptv_c like '%^3_19^%'
                                  or jc_rl.ptv_c like '%^5_19^%'
                                  or jc_rl.ptv_c like '%^6_19^%'
                                  or jc_rl.ptv_c like '%^10_19^%'
                                  or jc_rl.ptv_c like '%^11_19^%'
                                  or jc_rl.ptv_c like '%^19_19^%'
                                  or jc_rl.ptv_c like '%^14_19^%' then 'Разметка не наша 50+'
                          when
                                      jc_rl.ptv_c like '%^3_21^%'
                                  or jc_rl.ptv_c like '%^5_21^%'
                                  or jc_rl.ptv_c like '%^6_21^%'
                                  or jc_rl.ptv_c like '%^10_21^%'
                                  or jc_rl.ptv_c like '%^11_21^%'
                                  or jc_rl.ptv_c like '%^19_21^%'
                                  or jc_rl.ptv_c like '%^14_21^%' then 'Разметка не наша Телеком'
                          when
                                      jc_rl.ptv_c like '%^3_18^%'
                                  or jc_rl.ptv_c like '%^5_18^%'
                                  or jc_rl.ptv_c like '%^6_18^%'
                                  or jc_rl.ptv_c like '%^10_18^%'
                                  or jc_rl.ptv_c like '%^11_18^%'
                                  or jc_rl.ptv_c like '%^19_18^%'
                                  or jc_rl.ptv_c like '%^14_18^%' then 'Разметка не наша 50-40'
                          when
                                      jc_rl.ptv_c like '%^5_20^%'
                                  or jc_rl.ptv_c like '%^3_20^%'
                                  or jc_rl.ptv_c like '%^6_20^%'
                                  or jc_rl.ptv_c like '%^10_20^%'
                                  or jc_rl.ptv_c like '%^11_20^%'
                                  or jc_rl.ptv_c like '%^19_20^%'
                                  or jc_rl.ptv_c like '%^14_20^%' then 'Разметка не наша Спутник'
                          when
                                      jc_rl.ptv_c like '%^3_17^%'
                                  or jc_rl.ptv_c like '%^5_17^%'
                                  or jc_rl.ptv_c like '%^6_17^%'
                                  or jc_rl.ptv_c like '%^10_17^%'
                                  or jc_rl.ptv_c like '%^11_17^%'
                                  or jc_rl.ptv_c like '%^19_17^%'
                                  or jc_rl.ptv_c like '%^14_17^%' then 'Разметка не наша 40-30'
                          when
                                      jc_rl.ptv_c like '%^5_16^%'
                                  or jc_rl.ptv_c like '%^3_16^%'
                                  or jc_rl.ptv_c like '%^6_16^%'
                                  or jc_rl.ptv_c like '%^10_16^%'
                                  or jc_rl.ptv_c like '%^11_16^%'
                                  or jc_rl.ptv_c like '%^19_16^%'
                                  or jc_rl.ptv_c like '%^14_16^%' then 'Разметка не наша 30-20'
                          when
                                      jc_rl.ptv_c like '%^5_15^%'
                                  or jc_rl.ptv_c like '%^3_15^%'
                                  or jc_rl.ptv_c like '%^6_15^%'
                                  or jc_rl.ptv_c like '%^10_15^%'
                                  or jc_rl.ptv_c like '%^11_15^%'
                                  or jc_rl.ptv_c like '%^19_15^%'
                                  or jc_rl.ptv_c like '%^14_15^%' then 'Разметка не наша 20-0'
                          else ''
                          end                    ptv,
                      case
                          when region_c = 1 then 'Наша полная'
                          when region_c = 2 then 'Наша неполная'
                          when region_c = 4 then 'Фиас из разных источников'
                          when region_c = 5 then 'Фиас до города'
                          when region_c = 6 then 'Старый town_c'
                          when region_c = 7 then 'Def code'
                          else ''
                          end                    region,
                      last_step
               from suitecrm_robot_ch.jc_robot_log as jc_rl
               where last_step not in ('0', '1', '111', '261', '262')),

     requests as (select toDate(requests.request_date) as request_date, requests.phone_request, requests.uniqueid
                  from suitecrm_robot_ch.all_requests_id as requests)

select jc_rl.call_date,
       jc_rl.phone,
       phone_category.category,
       jc_rl.ptv,
       jc_rl.region,
       if(jc_rl.ptv not in ('', ' '), jc_rl.ptv, jc_rl.region) as markup,
       requests.request_date,
       requests.phone_request
from jc_rl
         left join suitecrm_robot_ch.phone_category on jc_rl.phone = phone_category.phone
         left join requests on jc_rl.uniqueid = requests.uniqueid;
