from lib import JCDecaux as jcd
import time

city = 'Toulouse'

while True:
    dataframe = jcd.information(city)
    dataframe.to_csv('static/data/{0}.csv'.format(city), index=False))
    time.sleep(60)
