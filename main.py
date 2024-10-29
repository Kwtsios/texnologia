import streamlit as st
import requests

st.title("Dashboard για Εργασία 1 - ΜΗΥΠ 521")
st.subheader("Web-enabled Εφαρμογή με Widgets")

# Στατικό Widget 1 - Πληροφορίες Καιρού (προκαθορισμένη τοποθεσία)
st.header("Πληροφορίες Καιρού για Λευκωσία")

# Correct Visual Crossing URL
response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Cyprus?unitGroup=metric&key=H7U5R9FXYMF7ZPUHR4PU4RH8P&contentType=json")

if response.status_code == 200:
    weather_data = response.json()
    st.write(f"Θερμοκρασία: {weather_data['days'][0]['temp']}°C")
    st.write(f"Συνθήκες: {weather_data['days'][0]['conditions']}")
else:
    st.error("Δεν ήταν δυνατή η ανάκτηση των δεδομένων καιρού.")

# Στατικό Widget 2 - Γενικές Πληροφορίες Χρηματοοικονομικής Αγοράς
st.header("Γενικές Πληροφορίες Χρηματοοικονομικής Αγοράς")

# Fetch stock market data using Alpha Vantage API
symbol = "AAPL"  # Example stock symbol (Apple Inc.)
api_key = "HHDQCSHRJ7VJPCDP"  # Replace with your Alpha Vantage API key
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"

stock_response = requests.get(stock_url)

if stock_response.status_code == 200:
    stock_data = stock_response.json()
    try:
        # Extract the most recent data point
        latest_time = list(stock_data['Time Series (5min)'].keys())[0]
        latest_data = stock_data['Time Series (5min)'][latest_time]
        st.write(f"Σύμβολο: {symbol}")
        st.write(f"Τιμή: ${latest_data['1. open']} (Άνοιγμα)")
        st.write(f"Υψηλό: ${latest_data['2. high']}")
        st.write(f"Χαμηλό: ${latest_data['3. low']}")
        st.write(f"Όγκος: {latest_data['5. volume']}")
    except KeyError:
        st.error("Σφάλμα κατά την ανάκτηση των δεδομένων χρηματιστηρίου.")
else:
    st.error("Δεν ήταν δυνατή η σύνδεση με το API του Alpha Vantage για χρηματιστηριακά δεδομένα.")

# Στατικό Widget 3 - Πληροφορίες Νέων
st.header("Ειδήσεις της Ημέρας")

# Fetch news data using News API
news_api_key = "aff1d5721a8148adbcee1cae0f237d13"  # Replace with your News API key
news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"

news_response = requests.get(news_url)

if news_response.status_code == 200:
    news_data = news_response.json()
    articles = news_data.get("articles", [])
    for article in articles[:5]:  # Display the top 5 news articles
        st.subheader(article["title"])
        st.write(article["description"])
        st.write(f"[Read more]({article['url']})")
else:
    st.error("Δεν ήταν δυνατή η ανάκτηση των ειδήσεων.")

# Διαδραστικό Widget 1 - Πληροφορίες Καιρού για Επιλεγμένη Τοποθεσία
st.header("Επιλογή Τοποθεσίας για Πληροφορίες Καιρού")
location = st.text_input("Εισάγετε τοποθεσία:")
if location:
    response = requests.get(f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key=H7U5R9FXYMF7ZPUHR4PU4RH8P&contentType=json")
    if response.status_code == 200:
        weather_data = response.json()
        st.write(f"Θερμοκρασία: {weather_data['days'][0]['temp']}°C")
        st.write(f"Συνθήκες: {weather_data['days'][0]['conditions']}")
    else:
        st.error("Δεν ήταν δυνατή η ανάκτηση των δεδομένων καιρού για την τοποθεσία.")

# Διαδραστικό Widget 2 - Currency Conversion (Παράδειγμα)
st.header("Μετατροπή Νομισμάτων")
amount = st.number_input("Ποσό:")
from_currency = st.selectbox("Από νόμισμα", ["USD", "EUR", "GBP"])
to_currency = st.selectbox("Σε νόμισμα", ["USD", "EUR", "GBP"])
if st.button("Μετατροπή"):
    # Κλήση serverless function για μετατροπή
    st.write(f"Αποτέλεσμα: ...")

# Διαδραστικό Widget 3 - Χρήση δεδομένων από serverless για υπολογισμό
st.header("Αλληλεπίδραση με Υπηρεσία για Επίλυση Μαθηματικού Υπολογισμού")
operation = st.selectbox("Επιλέξτε υπολογισμό", ["Πρόσθεση", "Αφαίρεση"])
num1 = st.number_input("Αριθμός 1:")
num2 = st.number_input("Αριθμός 2:")
if st.button("Υπολογισμός"):
    if operation == "Πρόσθεση":
        result = num1 + num2
        st.write(f"Αποτέλεσμα Πρόσθεσης: {result}")
    elif operation == "Αφαίρεση":
        result = num1 - num2
        st.write(f"Αποτέλεσμα Αφαίρεσης: {result}")



import streamlit as st
import requests
import json
import requests
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px
import os
from PIL import Image
# from web3 import Web3
import asyncio
import nest_asyncio
from requests.exceptions import ConnectionError
import yfinance as finance
nest_asyncio.apply()

# Set the page to a wide layout
st.set_page_config(layout="wide")

# Title



# Set the parameters for a requests call and get the data from the API


st.title("Serverless functions") # Displays title
col3, col4,col5 = st.columns(3)
with col3:
    number1 = st.number_input('Insert first number')
 #   st.write('The current number is ', number1)

with col4:
    number2 = st.number_input('Insert second number')
  #  st.write('The current number is ', number2)

with col5:
    operator = st.selectbox('Choose an operator:',
                                ('+', '-', '/', '*'))
  #  st.write("You chose ",operator)
    if(operator=='+'):
        operator='add'


st.write('Result from the first serverless function ')
send = 'https://vhkmdl2db7wsc3cggv3ozoj4ne0owrdk.lambda-url.ap-northeast-1.on.aws/?num1=%f&num2=%f&op=%s' % (number1,number2,operator)
#st.write(send)
response = requests.get(send)
st.write(response.text)
st.text("")
st.write('Code implementation below from aws lambda')
code = '''import json

def lambda_handler(event, context):
    return_text = ""
    if "queryStringParameters" not in event:
        return_text = "No query string present"
    else:
        query = event["queryStringParameters"]
        if "num1" not in query:
            return_text = "No num1 chosen"
        elif "num2" not in query:
            return_text = "No num2 chosen"
        elif "op" not in query:
            return_text = "No op chosen"
        else:
            num1 = float(query["num1"])
            num2 = float(query["num2"])
            op = query['op']
            
            if (op == 'add'):
                x=float("{0:.2f}".format(num1 + num2))
                return_text = f"Your numbers add to: {x}"
            elif (op == '-'):
                x=float("{0:.2f}".format(num1 - num2))
                return_text = f"Your numbers substract to: {x}"
            elif (op == '/'):
                x=float("{0:.2f}".format(num1 / num2))
                return_text = f"Your numbers divide to: {x}"
            elif (op == '*'):
                x=float("{0:.2f}".format(num1*num2))
                return_text = f"Your numbers multiply to: {x}"
            else:
                return_text = "No op chosen"
    return {
        'statusCode': 200,
        'body': f'{return_text}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')

st.text("")
st.text("")
col5, col6 = st.columns(2)
with col5:
    first_text = st.text_input('Enter first text', 'This is a sentence')
with col6:
    second_text = st.text_input('Enter a condition to see if exists in the sentence', 'e')

st.write('Result from the second serverless function ')
send_second = 'https://e7mdkoecvxzbqhjjymxdw3red40tmbun.lambda-url.ap-northeast-1.on.aws/?astring=%s&con=%s' % (first_text,second_text)
response_second = requests.get(send_second)
st.write(response_second.text)
st.text("")
st.write('Code implementation below from aws lambda')
code = '''import json

def lambda_handler(event, context):
    return_text = ""
    if "queryStringParameters" not in event:
        return_text = "No query string present"
    else:
        query = event["queryStringParameters"]
        if "astring" not in query:
            return_text = "No string entered"
        elif "con" not in query:
            return_text = "No condition entered"
        else:
            x = query["astring"]
            condition=query["con"]
            howmany="The %s appears %d times in your sentence"% (condition,x.count(condition))
            return_text = f"{howmany}"
    return {
        'statusCode': 200,
        'body': f'{return_text}',
        'headers': { 'Content-Type': "text/html" }
    } '''
st.code(code, language='python')

st.text("")
st.text("")
third_text = st.text_input('Enter text', 'This is a sentence')
st.write('Result from the third serverless function ')
send_third = 'https://6oswps446zy2qud64ngemd34bi0cgppp.lambda-url.ap-northeast-1.on.aws/?st=%s' % (third_text)
response_third = requests.get(send_third)
st.write(response_third.text)
st.text("")
st.write('Code implementation below from aws lambda')
code = '''import json

def lambda_handler(event, context):
    return_text = ""
    if "queryStringParameters" not in event:
        return_text = "No query string present"
    else:
        query = event["queryStringParameters"]
        if "st" not in query:
            return_text = "No string entered"
        else:
            x = query["st"]
            c=len(x)
            howmany="There are  %d characters in your sentence"% (c)
            return_text = f"{howmany}"
    return {
        'statusCode': 200,
        'body': f'{return_text}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')
st.text("")
st.text("")
st.title("Widgets") # Displays title

st.subheader("Exploring RapidAPI's weather Endpoints - 1") # Displays subheader
st.text("")

st.text("")

url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
	"X-RapidAPI-Key": "0312d33db3msh895b45c60fda80ep1c980ajsn320bd55b226e",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
location = st.text_input("Enter the location", "Cyprus")
querystring = {"q":{location}}
response = requests.request("GET", url, headers=headers, params=querystring)
result = response.text
data = json.loads(result)
# st.json(data)
col1, col2 = st.columns(2)

with col1:

    st.write(f'Name: {data["location"]["name"]}')
    st.write(f'Region: {data["location"]["region"]}')
    st.write(f'Country: {data["location"]["country"]}')
    st.write(f'Local Time: {data["location"]["localtime"]}')
    st.metric(label="wind_kph", value= f'{data["current"]["wind_kph"]}')
    st.write(f'Feels like: {data["current"]["feelslike_c"]} ℃')

with col2:

    st.write(f'Temp in Celcius: {data["current"]["temp_c"]}')
    st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
    st.write(f'Condition: {data["current"]["condition"]["text"]}')
    st.image(f'http:{data["current"]["condition"]["icon"]}')
    st.metric(label = "Humidity", value = f'{data["current"]["humidity"]}')

st.text("")
st.write('Code implementation below for weather')
code = '''url = "https://weatherapi-com.p.rapidapi.com/current.json"

headers = {
	"X-RapidAPI-Key": "0312d33db3msh895b45c60fda80ep1c980ajsn320bd55b226e",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
location = st.text_input("Enter the location", "Cyprus")
querystring = {"q":{location}}
response = requests.request("GET", url, headers=headers, params=querystring)
result = response.text
data = json.loads(result)
# st.json(data)
col1, col2 = st.columns(2)

with col1:

    st.write(f'Name: {data["location"]["name"]}')
    st.write(f'Region: {data["location"]["region"]}')
    st.write(f'Country: {data["location"]["country"]}')
    st.write(f'Local Time: {data["location"]["localtime"]}')
    st.metric(label="wind_kph", value= f'{data["current"]["wind_kph"]}')
    st.write(f'Feels like: {data["current"]["feelslike_c"]} ℃')

with col2:

    st.write(f'Temp in Celcius: {data["current"]["temp_c"]}')
    st.write(f'Temp in Farenheit: {data["current"]["temp_f"]}')
    st.write(f'Condition: {data["current"]["condition"]["text"]}')
    st.image(f'http:{data["current"]["condition"]["icon"]}')
    st.metric(label = "Humidity", value = f'{data["current"]["humidity"]}')'''
st.code(code, language='python')
st.text("")

st.text("")
st.subheader("Enter a movie title - 2")


st.text("")


title = st.text_input("Type the movie title")
if title:
    try:
        url= f"http://www.omdbapi.com/?t={title}&apikey=29423572"
        re = requests.get(url)
        re = re.json()
        col1,col2 = st.columns([1, 2])
        with col1:
            st.image(re['Poster'])
        with col2:
            st.subheader(re['Title'])
            st.caption(f"Genre: {re['Genre']} Year: {re['Year']}")
            st.write(re['Plot'])
            st.text(f"Rating: {re['imdbRating']}")
            st.progress(float(re['imdbRating'])/10)
    except:
        st.error("no movie with that title")



st.text("")
st.write('Code implementation below for movies')
code = '''

    try:
        url= f"http://www.omdbapi.com/?t={title}&apikey=29423572"
        re = requests.get(url)
        re = re.json()
        col1,col2 = st.columns([1, 2])
        with col1:
            st.image(re['Poster'])
        with col2:
            st.subheader(re['Title'])
            st.caption(f"Genre: {re['Genre']} Year: {re['Year']}")
            st.write(re['Plot'])
            st.text(f"Rating: {re['imdbRating']}")
            st.progress(float(re['imdbRating'])/10)
    except:
        st.error("no movie with that title")

'''
st.code(code, language='python')
st.text("")
st.text("")
st.subheader("See your geolocation - 3")
st.text("")


API_KEY ='af6818474c75e8d4085ce4b4aee79f6b17788850f5e19f2feef6243e'
API_URL = 'https://api.ipdata.co/'



# def query_ip(ips):
#     df = pd.DataFrame()
#     for ip in ips.split(','):
#         ip = ip.strip()
#         response = requests.get(f'{API_URL}{ip}?api-key={API_KEY}')
#         if response.status_code == 200:
#             data = json.loads(response.content)
#             df = df.append(pd.DataFrame(pd.io.json.json_normalize(data)))
#     return df
def query_ip(ips):
    data_frames = []  # List to hold individual dataframes
    for ip in ips.split(','):
        ip = ip.strip()
        response = requests.get(f'{API_URL}{ip}?api-key={API_KEY}')
        if response.status_code == 200:
            data = json.loads(response.content)
            # Use pd.json_normalize to process the JSON data
            data_frames.append(pd.json_normalize(data))
    
    # Concatenate all dataframes in the list
    if data_frames:
        df = pd.concat(data_frames, ignore_index=True)
    else:
        df = pd.DataFrame()  # Return an empty DataFrame if no data

    return df

# def query_ip(ips):
#     df = pd.DataFrame()
#     for ip in ips.split(','):
#         ip = ip.strip()
#         response = requests.get(f'{API_URL}{ip}?api-key={API_KEY}')
#         if response.status_code == 200:
#             data = json.loads(response.content)
#             df = df.append(pd.DataFrame(pd.io.json.json_normalize(data)))
#             df = df.append(pd.DataFrame(pd.json_normalize(data)))
#     return df
st.title('IP Geolocation')
ips = st.text_area('IP addresses separated by comma', '8.8.8.8, 9.9.9.9')

df = query_ip(ips)
st.table(df[['ip', 'emoji_flag', 'country_name', 'city', 'asn.name', 'asn.type']].reset_index())

st.map(df)
st.text("")
st.write('Code implementation below for geolocation')
code = '''
API_KEY ='af6818474c75e8d4085ce4b4aee79f6b17788850f5e19f2feef6243e'
API_URL = 'https://api.ipdata.co/'


def query_ip(ips):
    df = pd.DataFrame()
    for ip in ips.split(','):
        ip = ip.strip()
        response = requests.get(f'{API_URL}{ip}?api-key={API_KEY}')
        if response.status_code == 200:
            data = json.loads(response.content)
            df = df.append(pd.DataFrame(pd.io.json.json_normalize(data)))
    return df


st.title('IP Geolocation')
ips = st.text_area('IP addresses separated by comma', '8.8.8.8, 9.9.9.9')

df = query_ip(ips)
st.table(df[['ip', 'emoji_flag', 'country_name', 'city', 'asn.name', 'asn.type']].reset_index())

st.map(df)
'''
st.code(code, language='python')

st.text("")
st.text("")
st.subheader("NASA's Astronomy Picture of the Day - 4")
st.text("")
# NASA's Astronomy Picture of the Day Section

# Display NASA title and date input widget above the image
# st.header("NASA")
d = st.date_input("Select a date:", key="nasa_date")
params = {'api_key': "ZQOMZ3UGqe2936EECapppMPHznR8eZgsu0vWJmR8", 'date': d}
response_nasa = requests.get('https://api.nasa.gov/planetary/apod', params=params)

# Proceed with the data display for the selected date
if response_nasa:
    data = response_nasa.json()

    col1, col2 = st.columns(2, gap="small")

    with col1:
        # Check the data type and display accordingly
        if data['media_type'] == 'video':
            st.video(data['url'])
        else:
            st.image(data['hdurl'])

        # If there is a copyright message then display it
        if 'copyright' in data:
            st.caption(f'Copyright: {data["copyright"]}')
        else:
            st.caption("Public domain image courtesy of NASA")

    with col2:
        # Write the text fields in column 2
        st.title(data['title'])
        st.write(data['date'])
        st.write(data['explanation'])

# Handle any response errors
else:
    st.write(response_nasa.text)


st.text("")

st.write('Code implementation below for nasa')
code = '''
params = {'api_key': "ZQOMZ3UGqe2936EECapppMPHznR8eZgsu0vWJmR8", 'date': d}
response_nasa = requests.get('https://api.nasa.gov/planetary/apod', params=params)
if response_nasa:
  
    data = response_nasa.json()

    col1, col2 = st.columns(2, gap="small")

    with col1:
        # Check the data type and display accordingly
        if data['media_type'] == 'video':
            st.video(data['url'])
        else:
            st.image(data['hdurl'])

        # If there is a copyright message then display it
        if 'copyright' in data:
            st.caption(f'Copyright: {data["copyright"]}')
        # Otherwise here is a default caption
        else:
            st.caption("Public domain image courtesy of NASA")

    with col2:
        # Write the text fields in column 2
        st.title(data['title'])
        st.write(data['date'])
        st.write(data['explanation'])

# If the response is bad just print it out
else:
    st.write(response_nasa.text)
'''
st.code(code, language='python')
st.text("")
st.text("")


st.text("")
st.text("")

