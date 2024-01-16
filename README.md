# Hint Log Report

This repository aims to make a Program that retrieve logs from Cloudwatch, treat the data, and generate a report of how many User Creation on the platform result in error and why.


## Dependencies

All the code is developed in python3.

* [boto3](https://pypi.org/project/boto3/)
* [datetime](https://docs.python.org/3/library/datetime.html)
* [json](https://docs.python.org/3/library/json.html)
* [pandas](https://pypi.org/project/pandas/)
* [time](https://docs.python.org/3/library/time.html)


## Directory

The basic structure is:

* hint_report.py -> main file that will call the other functions
* process_date.py -> this file contains a function tha process time used in this program
* create_query.py -> in this function, based on the time passed, it will be created a query on CloudWatch
* retrieve_results.py -> once the query is created, you can retrieve its results, this is what this function does
* process_logs.py -> With the raw logs, now you can process the data using Python libraries and have as the result how many errors happened during the month

## Report

The final report  will have the following structure

date | action | company_id | company_name | employee_name | error_name | error_message

## Run

Basically to run this Program you must have python3 and their dependencies installed on you machine..

Another requirement is to have access to **AWS_ACCESS_KEY_ID** and **AWS_SECRET_ACCESS_KEY**

After done this you just need to run **hint_report.py** file

```bash
python3 hint_report.py
```