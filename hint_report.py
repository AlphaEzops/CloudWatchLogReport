from process_date import process_date
from create_query import create_query
from retrieve_results import retrieve_results
from process_logs import process_logs
from time import sleep

# Or Start or Range Date
start_date = 0
range_days = 0
finish_date = 0

## Take 30 days passing 0 as start and finish date
date_array = process_date(start_date, finish_date, range_days)

## Create CloudWatch Query 
query_id = create_query(date_array[0], date_array[1])

## Sleep To Load Query
sleep(30)

## Take the results
results =  retrieve_results(query_id)

## Process logs
end = process_logs(results)