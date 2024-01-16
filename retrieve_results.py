import boto3

###
### Retrieving Data from Log Group
###

def retrieve_results(query_id):

  client1 = boto3.client('logs', region_name='us-west-2')

  query_result = client1.get_query_results(
      queryId=f"{query_id}"
  )

  return query_result