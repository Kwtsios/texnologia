import streamlit as st
import requests
from datetime import datetime
import pytz

st.title("Dashboard για Εργασία 1 - ΜΗΥΠ 521")
st.subheader("Web-enabled Εφαρμογή με Widgets")

# Στατικό Widget 1 - Πληροφορίες Καιρού για Λευκωσία
st.header("Πληροφορίες Καιρού για Λευκωσία")
response = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Cyprus?unitGroup=metric&key=H7U5R9FXYMF7ZPUHR4PU4RH8P&contentType=json")
if response.status_code == 200:
    weather_data = response.json()
    st.write(f"Θερμοκρασία: {weather_data['days'][0]['temp']}°C")
    st.write(f"Συνθήκες: {weather_data['days'][0]['conditions']}")
else:
    st.error("Δεν ήταν δυνατή η ανάκτηση των δεδομένων καιρού.")

# Στατικό Widget 2 - Γενικές Πληροφορίες Χρηματοοικονομικής Αγοράς
st.header("Γενικές Πληροφορίες Χρηματοοικονομικής Αγοράς")
symbol = "AAPL"
api_key = "16VOT2UEUPIROENX"
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}"
stock_response = requests.get(stock_url)
if stock_response.status_code == 200:
    stock_data = stock_response.json()
    try:
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

# Στατικό Widget - Πληροφορίες για Σημερινή Ημερομηνία και Ώρα στην Κύπρο
st.header("Πληροφορίες για Σημερινή Ημερομηνία και Ώρα στην Κύπρο")
cyprus_timezone = pytz.timezone("Europe/Nicosia")
current_datetime_cyprus = datetime.now(cyprus_timezone)
st.write("Σημερινή ημερομηνία:", current_datetime_cyprus.strftime("%d/%m/%Y"))
st.write("Τρέχουσα ώρα (Κύπρος):", current_datetime_cyprus.strftime("%H:%M:%S"))
st.write("Ημέρα της εβδομάδας:", current_datetime_cyprus.strftime("%A"))

# Διαδραστικό Widget 1 - Υπολογιστική μηχανή για Πρόσθεση
st.title("Υπολογιστική μηχανή για Πρόσθεση")
col1, col2 = st.columns(2)
with col1:
    number1 = st.number_input('Εισάγετε τον πρώτο αριθμό')
with col2:
    number2 = st.number_input('Εισάγετε τον δεύτερο αριθμό')
st.write('Αποτέλεσμα από την serverless function (Πρόσθεση)')
send = f'https://vhkmdl2db7wsc3cggv3ozoj4ne0owrdk.lambda-url.ap-northeast-1.on.aws/?num1={number1}&num2={number2}&op=add'
response = requests.get(send)
st.write(response.text)

# Διαδραστικό Widget 2 - Μέτρηση γραμμάτων/λέξεων
st.title("Μέτρηση γραμμάτων/λέξεων")
st.text("")
st.text("")
col5, col6 = st.columns(2)
with col5:
    first_text = st.text_input('Εισάγετε το πρώτο κείμενο για έλεγχο', 'This is a sentence')
with col6:
    second_text = st.text_input('Εισάγετε τη λέξη/γράμμα προς αναζήτηση', 'e')
st.write('Αποτέλεσμα')
send_second = 'https://e7mdkoecvxzbqhjjymxdw3red40tmbun.lambda-url.ap-northeast-1.on.aws/?astring=%s&con=%s' % (first_text, second_text)
response_second = requests.get(send_second)
st.write(response_second.text)

# Διαδραστικό Widget 3 - Χρήση serverless για υπολογισμό
st.header("Υπολογισμός πλήθους χαρακτήρων στο κείμενο")
st.text("")
st.text("")
third_text = st.text_input('Εισάγετε κείμενο για υπολογισμό χαρακτήρων', 'This is a sentence')
st.write('Αποτέλεσμα')
send_third = f'https://6oswps446zy2qud64ngemd34bi0cgppp.lambda-url.ap-northeast-1.on.aws/?st={third_text}'
response_third = requests.get(send_third)
st.write(response_third.text)
st.text("")
