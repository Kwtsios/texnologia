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
import requests
import streamlit as st

# Τίτλος ενότητας
st.header("Γενικές Πληροφορίες Κρυπτονομισμάτων")

# Επιλογή σύμβολου κρυπτονομίσματος
symbol = "bitcoin"  # Παράδειγμα κρυπτονόμισμα (Bitcoin)
crypto_url = f"https://api.coincap.io/v2/assets/{symbol}"

# Ανάκτηση δεδομένων για το συγκεκρημένο σύμβολο
crypto_response = requests.get(crypto_url)

# Έλεγχος αν η απάντηση ήταν επιτυχής
if crypto_response.status_code == 200:
    crypto_data = crypto_response.json()
    
    # Ελέγχει αν υπάρχουν δεδομένα
    if "data" in crypto_data and crypto_data["data"]:
        latest_data = crypto_data["data"]

        # Εμφάνιση πληροφοριών
        st.write(f"Σύμβολο: {latest_data['symbol']}")
        st.write(f"Όνομα: {latest_data['name']}")
        st.write(f"Τιμή: ${float(latest_data['priceUsd']):.2f}")
        st.write(f"Αλλαγή 24 ώρες: {float(latest_data['changePercent24Hr']):.2f}%")
        st.write(f"Κεφαλαιοποίηση αγοράς: ${float(latest_data['marketCapUsd']):,.2f}")
        st.write(f"Όγκος 24 ώρες: ${float(latest_data['volumeUsd24Hr']):,.2f}")
    else:
        st.error("Δεν βρέθηκαν δεδομένα για το σύμβολο που επιλέξατε.")
else:
    st.error("Δεν ήταν δυνατή η σύνδεση με το API του CoinCap για δεδομένα κρυπτονομισμάτων.")
    

# Στατικό Widget 3 - Πληροφορίες για Σημερινή Ημερομηνία και Ώρα στην Κύπρο
st.header("Πληροφορίες για Σημερινή Ημερομηνία και Ώρα στην Κύπρο")
cyprus_timezone = pytz.timezone("Europe/Nicosia")
current_datetime_cyprus = datetime.now(cyprus_timezone)
st.write("Σημερινή ημερομηνία:", current_datetime_cyprus.strftime("%d/%m/%Y"))
st.write("Τρέχουσα ώρα (Κύπρος):", current_datetime_cyprus.strftime("%H:%M:%S"))
st.write("Ημέρα της εβδομάδας:", current_datetime_cyprus.strftime("%A"))

# Διαδραστικό Widget 1 - Υπολογιστική μηχανή για Πρόσθεση
st.header("Υπολογιστική μηχανή για Πρόσθεση")
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
st.header("Μέτρηση γραμμάτων/λέξεων")
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
third_text = st.text_input('Εισάγετε κείμενο για υπολογισμό χαρακτήρων', 'This is a sentence')
st.write('Αποτέλεσμα')
send_third = f'https://6oswps446zy2qud64ngemd34bi0cgppp.lambda-url.ap-northeast-1.on.aws/?st={third_text}'
response_third = requests.get(send_third)
st.write(response_third.text)
st.text("")
