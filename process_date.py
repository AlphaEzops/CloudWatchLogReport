from datetime import datetime, timedelta

###
### Process and Sanitize Date
###

def process_date(start, finish, range_days):
  if finish == 0: 
    start_date = int((datetime.now() - timedelta(30)).timestamp())
    end_date = int(datetime.now().timestamp())
    return [start_date, end_date]

### TO DO: Implement logic to sanitize date