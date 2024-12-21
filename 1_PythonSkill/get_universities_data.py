import os
import sys
import json 
import requests
from urllib.parse import quote


def get_universities_data(country='indonesia'):
    keep_try = True
    retry = 2
    while keep_try==True and retry>0:
        if retry==0:
            print(f"INFO >> NO DATA RETRIEVED!")
            return []
        try:
            response = requests.get(
                url=f"http://universities.hipolabs.com/search?country={quote(country)}"
            ).json()
            keep_try = False
            return response
        except:
            print(f"INFO >> NO DATA RETRIEVED, retrying...")
            retry -= 1


def get_universities_data_bulk(country_list:list):
    all_data = []
    for i, country in enumerate(country_list):
        temp_data = get_universities_data(country.lower())
        print(f"INFO >> {i+1} - get universities data from '{country}' ({len(temp_data)})")
        all_data.extend(temp_data)
    print(f"INFO >> Finished!")
    return all_data


# SAVE DATA TO JSON FILE
def save_to_json(data:list|dict, filename="southeast_asia_data"):
    filepath = os.path.join(os.getcwd(), f"{filename}.json")
    with open(filepath, "w") as final:
        json.dump(data, final)
    print(f"INFO >> DATA IS EXPORTED TO {filepath}")
    return True

def pipeline_universities(country_list, filename="southeast_asia_data"):
    data = get_universities_data_bulk(country_list)
    save_to_json(data, filename=filename)
    return data

# if __name__=='__main__':
#     pipeline_universities(list(sys.argv[1:]), filename="southeast_asia_data")