import boto3

###
### Creating query on the Log Group Insight
###

def create_query(start, end):

  client = boto3.client('logs', region_name='us-west-2')

  created_query = client.start_query(
      logGroupName='tuned-logs-production',
      startTime=start,
      endTime=end,
      queryString='fields @timestamp, @message | filter @message like /\"error\"/ and @message like /\"action\":\"create_hint_user\"/',
      limit=500
  )

  query_id = str(created_query['queryId'])

  return query_id