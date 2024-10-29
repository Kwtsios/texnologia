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



# Διαδραστικό Widget 1 - Υπολογιστική
import streamlit as st
import requests

# Τίτλος εφαρμογής
st.title("Υπολογιστική μηχανή για Πρόσθεση")

# Εισαγωγή αριθμών
col1, col2 = st.columns(2)
with col1:
    number1 = st.number_input('Εισάγετε τον πρώτο αριθμό')
with col2:
    number2 = st.number_input('Εισάγετε τον δεύτερο αριθμό')

# Εμφάνιση αποτελέσματος της πρόσθεσης μέσω της serverless function
st.write('Αποτέλεσμα από την serverless function (Πρόσθεση)')
send = f'https://vhkmdl2db7wsc3cggv3ozoj4ne0owrdk.lambda-url.ap-northeast-1.on.aws/?num1={number1}&num2={number2}&op=add'
response = requests.get(send)
st.write(response.text)




# Διαδραστικό Widget 2 - Currency Conversion (Παράδειγμα)
import streamlit as st
import requests

# Τίτλος εφαρμογής
st.title("Μέτρηση γραμμάτων/λέξεων")
st.text("")
st.text("")
col5, col6 = st.columns(2)
with col5:
    first_text = st.text_input('Εισάγετε κείμενο                                               ', 'Thats a sentence')
with col6:
    second_text = st.text_input('Εισάγετε γράμμα/λέξη για να δείτε αν υπάρχει στην πρόταση', 'e')

st.write('Αποτέλεσμα')
send_second = 'https://e7mdkoecvxzbqhjjymxdw3red40tmbun.lambda-url.ap-northeast-1.on.aws/?astring=%s&con=%s' % (first_text, second_text)
response_second = requests.get(send_second)
st.write(response_second.text)
st.text("")






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
