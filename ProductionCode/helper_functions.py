import csv
from ProductionCode.datasource import DataSource
#dont nead this stuff update to file that we do not need helper functions.

def load_data():
   '''Arguments: None
        Return value: None
        Purpose: Loads data'''
   dummy_data = []

   with open('Data/dummy_data.csv', newline='') as f:
       reader = csv.reader(f)
       for row in reader:
            dummy_data.append(row)
   return dummy_data

def get_ses_by_county(county_name,data):
    '''Arguments: county_name
        Return value: ses or "No matching county"
        Purpose: Looks through data to see if there is a matching county, and returns the socioeconomic status'''
    for i in range(len(data)):
        if data[i][1] == county_name:
            print(data[i][2])
            return data[i][2]
    print("No matching county")
    return "No matching county"

def get_scores_by_county(county_name,data):
    '''Arguments: county_name
        Return value: scores or "No matching county"
        Purpose: Looks through data to see if there is a matching county, and returns the test scores'''
    for i in range(len(data)):
        if data[i][1] == county_name:
            print(data[i][3])
            return data[i][3]
    print("No matching county")
    return "No matching county"

if __name__ == "__main__":
    load_data()