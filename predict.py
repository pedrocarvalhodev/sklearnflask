import json
import requests
import pandas as pd


"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

"""Reading test batch
"""
#df = pd.read_csv(utils.path+'/data/test.csv', encoding="utf-8-sig")
#df = df.head()

"""Converting Pandas Dataframe to json
"""

data = [
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 24, "Sex": '"female"', "Embarked": "C"},
    {"Age": 3, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}]

#data = df.to_json(orient='records')

#print(data)


"""POST <url>/predict
"""
resp = requests.post("http://0.0.0.0:8888/predict", \
                    data = json.dumps(data),\
                    headers= header)

print("STATUS-------------")
print(resp.status_code)


"""The final response we get is as follows:
"""
print("===== PREDICTIONS ===")
print(resp.json())