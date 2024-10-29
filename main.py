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
api_key = "16VOT2UEUPIROENX"  # Replace with your Alpha Vantage API key
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

import streamlit as st
from datetime import datetime
import pytz

# Τίτλος σελίδας
st.title("Πληροφορίες για Σημερινή Ημερομηνία και Ώρα στην Κύπρο")

# Ορισμός ζώνης ώρας για την Κύπρο
cyprus_timezone = pytz.timezone("Europe/Nicosia")
current_datetime_cyprus = datetime.now(cyprus_timezone)

# Εμφάνιση στατικών πληροφοριών
st.write("Σημερινή ημερομηνία:", current_datetime_cyprus.strftime("%d/%m/%Y"))
st.write("Τρέχουσα ώρα (Κύπρος):", current_datetime_cyprus.strftime("%H:%M:%S"))
st.write("Ημέρα της εβδομάδας:", current_datetime_cyprus.strftime("%A"))

# Επιπλέον πληροφορίες
st.write("Χρονιά:", current_datetime_cyprus.year)
st.write("Μήνας:", current_datetime_cyprus.month)
st.write("Ημέρα:", current_datetime_cyprus.day)
st.write("Ώρα:", current_datetime_cyprus.hour)
st.write("Λεπτά:", current_datetime_cyprus.minute)
st.write("Δευτερόλεπτα:", current_datetime_cyprus.second)


import json

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
    }




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
