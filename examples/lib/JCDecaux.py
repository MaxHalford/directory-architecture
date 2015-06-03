from six.moves.urllib.request import urlopen
import json
import pandas as pd
from datetime import datetime


key = '644ba49840f4c1021dfa661e67c3c9bfeb41b88e'
base = 'https://api.jcdecaux.com/vls/v1/'


def query_API(url):
    # Send a query to the API and decode the bytes it returns
    query = urlopen(url).read().decode('utf-8')
    # Return the obtained string as a JSON file
    return json.loads(query)


def stations_list(city):
    url = base + 'stations/?contract={0}&apiKey={1}'.format(city, key)
    data = query_API(url)
    return data


def timestamp_to_ISO(timestamp):
    moment = datetime.fromtimestamp(timestamp / 1000)
    return moment.time().isoformat()


def information(city):
    # Collect JSON data
    data = stations_list(city)
    # Convert it to a dataframe
    df = pd.io.json.DataFrame(data)
    # The positions are embedded so they have to be extracted
    positions = df.position.apply(pd.Series)
    df['latitude'] = positions['lat']
    df['longitude'] = positions['lng']
    # Make the timestamps human readable
    df['last_update'] = df['last_update'].apply(timestamp_to_ISO)
    return df[['available_bikes', 'last_update', 'name', 'latitude',
               'longitude', 'available_bike_stands', 'bike_stands',
               'status']]
