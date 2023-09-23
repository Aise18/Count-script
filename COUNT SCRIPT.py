import csv
import pandas as pd
import datetime


current_date_map = datetime.datetime.now().strftime("%Y%m%d")

results1 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv")
print(len(results1))
results2 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv")
print(len(results2))
file_path = f"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/first_part_of_file_name {current_date_map} second_part_of_file_name.csv"
results3 = pd.read_csv(file_path)
print(len(results3))
results4 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv", encoding='ANSI')
print(len(results4))
results5 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv", encoding='latin-1')
print(len(results5))
results6 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv", encoding='latin-1', dtype=str, low_memory=False) 
print(len(results6))
results7 = pd.read_csv(r"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name.csv", encoding='Windows-1251')
print(len(results7))
file_path2 = f"//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/file_name {current_date_map}.csv"
results8 = pd.read_csv(file_path2)
print(len(results8))


header = ['REPORT_NAME', 'COUNT', 'DATE', 'BUSINESS_UNIT', 'EMAIL', 'TEAM', 'VIEW', 'SUBJECT', 'REPORT_PATH']
current_date = datetime.datetime.now().strftime('%d-%b-%Y')

data = [
['REPORT NAME', (len(results1)), current_date, 'UK', 'email_address@example.com', 'TEAM1', 'VIEW NAME1', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name'], 
['REPORT NAME', (len(results2)), current_date, 'IE', 'email_address@example.com', 'TEAM1', 'VIEW NAME1', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name'], 
['REPORT NAME', (len(results3)), current_date, 'GR', 'email_address@example.com', 'TEAM2', 'VIEW NAME2', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name'], 
['REPORT NAME', (len(results4)), current_date, 'US', 'email_address@example.com', 'TEAM3', 'VIEW NAME3', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name'], 
['REPORT NAME', (len(results5)), current_date, 'DE', 'email_address@example.com', 'TEAM4', 'VIEW NAME4', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name'], 
['REPORT NAME', (len(results6)), current_date, 'CH', 'email_address@example.com', 'TEAM5', 'VIEW NAME5', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name']
['REPORT NAME', (len(results7)), current_date, 'US', 'email_address@example.com', 'TEAM3', 'VIEW NAME6', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name']
['REPORT NAME', (len(results8)), current_date, 'DK', 'email_address@example.com', 'TEAM6', 'VIEW NAME7', 'SUBJECT (USUALLY THE REPORT\'S NAME)', r'\\sharedrive_path\sharedrive_path\sharedrive_path_folder\sharedrive_path_folder\file_name']


with open("//sharedrive_path/sharedrive_path/sharedrive_path_folder/sharedrive_path_folder/Count_Report_File.csv", 'a', encoding='utf-8', newline='') as f:


    writer = csv.writer(f)

    # write the header
    #if f.tell() == 0:
    #writer.writerow(header)
    

    #write multiple rows
    writer.writerows(data)





