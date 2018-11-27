# tech-assessment

### Prerequisites:
install the following if you don't have them already:
```
$ pip3 install numpy
$ pip3 install pandas
$ pip3 install requests
```
  
Download the dataset required for question 2 (save it as 'PopulationData.csv'):
https://blog.splitwise.com/2013/09/18/the-2010-us-census-population-by-zip-code-totally-free/


Create a .csv file using the data from the website below (save it as 'NYC_Zips.csv'):
https://www.nycbynatives.com/nyc_info/new_york_city_zip_codes.php                                                                       
**Used to clean up 'Unspecified' boroughs*


### Run:
Run 'get_data.py' to grab the NYC city data from the Socrata API:
```
$ python3 get_data.py
```


Run 'assessment.ipynb' in Jupyter Notebook
###### *note: make sure the three .csv files are in the same directory as the Jupyter Notebook*
