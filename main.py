import streamlit as st
import requests

st.title("Dashboard για Εργασία 1 - ΜΗΥΠ 521")
st.subheader("Web-enabled Εφαρμογή με Widgets")

# Στατικό Widget 1 - Πληροφορίες Καιρού (προκαθορισμένη τοποθεσία)
st.header("Πληροφορίες Καιρού για Λευκωσία")
response = requests.get("https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Nicosia")
weather_data = response.json()
st.write(f"Θερμοκρασία: {weather_data['current']['temp_c']}°C")
st.write(f"Συνθήκες: {weather_data['current']['condition']['text']}")

# Στατικό Widget 2 - Γενικές Πληροφορίες Χρηματοοικονομικής Αγοράς
st.header("Γενικές Πληροφορίες Χρηματοοικονομικής Αγοράς")
st.write("Παράδειγμα πληροφοριών από το χρηματιστήριο της Νέας Υόρκης...")

# Στατικό Widget 3 - Πληροφορίες Νέων
st.header("Ειδήσεις της Ημέρας")
st.write("Ανάκτηση ειδήσεων από ένα δημόσιο API...")

# Διαδραστικό Widget 1 - Πληροφορίες Καιρού για Επιλεγμένη Τοποθεσία
st.header("Επιλογή Τοποθεσίας για Πληροφορίες Καιρού")
location = st.text_input("Εισάγετε τοποθεσία:")
if location:
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={location}")
    weather_data = response.json()
    st.write(f"Θερμοκρασία: {weather_data['current']['temp_c']}°C")
    st.write(f"Συνθήκες: {weather_data['current']['condition']['text']}")

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
    # Κλήση serverless function για μαθηματικό υπολογισμό
    st.write(f"Αποτέλεσμα: ...")
