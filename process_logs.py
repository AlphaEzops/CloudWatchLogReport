import pandas as pd
import json

###
### Processing Logs and Generating Report
###

def process_logs(raw_dataset):
  # Initial columns
  initial_column = ['@timestamp', '@message']

  # Creating empty dataset
  dataset = pd.DataFrame(columns=initial_column)

  # Processing Raw Data to be Used as Dataframe
  for item in raw_dataset['results']:
    timestamp = item[0]['value']
    message = item[1]['value']

    new_row = [timestamp, message]

    dataset.loc[len(dataset.index)] = new_row


  # Convert message to json
  dataset['@message'] = dataset['@message'].apply(json.loads)
  
  # Columns of New Dataset
  col = ['date', 'action', 'company_id', 'company_name', 'employee_name', 'error_name', 'error_message']
  new_dataframe = pd.DataFrame(columns=col)

  # Populate New Dataset
  for index, row in dataset.iterrows():
    date = row['@timestamp']
    action = row['@message']['action']
    company_id = row['@message']['metadata']['data']['object']['company']['id']
    company_name = row['@message']['metadata']['data']['object']['company']['name']
    employee_name = row['@message']['metadata']['data']['object']['name']
    error_name = row['@message']['metadata']['error']['name']
    error_message = row['@message']['metadata']['error']['message']
    
    new_row = [date, action, company_id, company_name, employee_name, error_name, error_message]
    
    new_dataframe.loc[len(new_dataframe.index)] = new_row


  formated_and_ordered = new_dataframe.sort_values(by='company_name').reset_index(drop=True)

  formated_and_ordered.to_csv(path_or_buf='/mnt/c/Projects/TunedCare/hint-report/testing.csv' ,index=False)

  return None