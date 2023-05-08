def smartdublin_requester(starts, ends, monitor):
    """Takes the start time, end time as lists and a monitor to give the json response from smartDublinAPI"""
    import requests
    import json
    loopCount = 0
    for i, j in zip(starts, ends):
        starter = i
        ender = j
        url = str(f"https://data.smartdublin.ie/sonitus-api/api/hourly-averages?username=dublincityapi&password=Xpa5vAQ9ki&monitor={monitor}&start={starter}&end={ender}")
        payload={}
        headers = {
        'Authorization': 'Basic ZHVibGluY2l0eWFwaTpYcGE1dkFROWtp',
        'Cookie': 'AWSALB=oLy1Wu0aHMYqyOhrORk8Ks4BTMvw+2qPK7k7r1P09YwzB/e5Uya8oIySC8fx+2HJDVjVmlL0JspX4HxSUWwZvZxunIO8umGspbXu2YxDj44U1Mg6qjtryX37xPxK; AWSALBCORS=oLy1Wu0aHMYqyOhrORk8Ks4BTMvw+2qPK7k7r1P09YwzB/e5Uya8oIySC8fx+2HJDVjVmlL0JspX4HxSUWwZvZxunIO8umGspbXu2YxDj44U1Mg6qjtryX37xPxK; AWSALBTG=gW0xqwv2CaNK64eOApK6PV72zWMWVtj7w4Pi20AgDOheoPkH2416FI4eyFOPGUuB0kqjiIBTT2+eJgx3eepcgEkYEo9JWWJ2RXRQ4eiyoHczKGMGhJjQjn2Xj6fe7woe8QV5mLM130KEcNdAVxuEYS1PKnNbxnUpPGzmaO+TuXKj; AWSALBTGCORS=gW0xqwv2CaNK64eOApK6PV72zWMWVtj7w4Pi20AgDOheoPkH2416FI4eyFOPGUuB0kqjiIBTT2+eJgx3eepcgEkYEo9JWWJ2RXRQ4eiyoHczKGMGhJjQjn2Xj6fe7woe8QV5mLM130KEcNdAVxuEYS1PKnNbxnUpPGzmaO+TuXKj; app_session=eyJpdiI6Im5lWkVpM0VTd3V3M0hLb1hHeWtCbHc9PSIsInZhbHVlIjoiQWpZZ0dEV2xFNlhnMmJpVzhlVE9mMjZMVXBHXC9laGRGcmx0VWo1RXFqYUhrWnBOVUw3bW00ZW5POTJqUWJLTFhTOHZTcCtncUI3OUlybmhWZkNoYWlRPT0iLCJtYWMiOiIzNjMyODFiYTZmYzJiMGMwZmY2ZmExMjI1YzkwNjkzMjNlNjE3ZDFmMWVhZDM5ODEzYTJlZDcyNWI1ZTAzOTdjIn0%3D'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data = response.json()
        with open(f'dumpWriteAttempt{loopCount}.json', 'a') as f:
            json.dump(data, f)
        loopCount += 1

# date is given in unix timestamp. API only allows for a call of span 2 weeks max so create two lists with a span of 2 weeks in between them arriving from 2015 to 2021
# given below is an example of two date lists which would provide data for 2020-01-01 00:00:00 (1577836800 unix timestamp) to 2020-02-12 00:00:00 (1581465600 unix timestamp).


date1 = [1577836800, 1579046400,1580256000]
date2 = [1579046400,1580256000, 1581465600]

# make the request using the above function and date1, date2
smartdublin_requester(date1, date2, 'monitor_serial')