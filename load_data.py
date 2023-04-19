import os
import pandas as pd

file_list = []

folder_path = os.path.join('D:\\','Github','NLP','Spam_classification','maildir')

def get_list_of_files(path):
    contents = os.listdir(path)
    for content in contents:
        new_path = os.path.join(path, content)
        if os.path.isdir(new_path):
            get_list_of_files(new_path)
        else:
            file_list.append(new_path)

get_list_of_files(folder_path)

file_list_df = pd.DataFrame(file_list, columns=['file_path'])
file_list_df.to_csv(r'Spam_classification\file_list.csv', index= False)

email_dfs = []

for file in file_list:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        temp_df = pd.DataFrame(f.readlines(), columns=['content'])
    email_dfs.append(temp_df)

email_df = pd.concat(email_dfs,ignore_index=True)
email_df.to_csv(r'Spam_classification\extracted_emails.csv', index = False)