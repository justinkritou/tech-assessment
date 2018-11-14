import requests
import pandas as pd

offset = 0
LIMIT = 1000000 #max rows which can be pulled from the api with a single call
arr_of_df = [] #array which will hold multiple batches of data
URL_CONSTANT = "https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$WHERE=created_date between '2017-01-01T00:00:00.000' and '2017-12-31T23:59:59.999' &$limit=" + str({}) + " &$offset=" + str({})

print("loading in data...")

#pull data from api in batches of 1000000 (limit) until theres no more rows to pull
while True:
    apiData = requests.get(URL_CONSTANT.format(LIMIT, offset)).json()
    dfTemp = pd.DataFrame(data=apiData) #convert each batch of data into a dataframe so we can easily use the pandas concat method later
    arr_of_df.append(dfTemp)
    offset += LIMIT
    if (len(apiData)-LIMIT) >= 0: #check if the max limit was pulled from the api
        continue
    else: #near end of dataset, no need to send another request
        break
        
#concatenate all of the batches of data into one DataFrame
df_cityData = pd.concat(arr_of_df)


print("converting to csv file...")
#convert dataframe into a csv file and save it to the current directory (should be the same as your jupyter notebook)
df_cityData.to_csv('2017_NYC_Data.csv', index=False)

print("COMPLETE!")