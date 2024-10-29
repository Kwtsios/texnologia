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

import http.client

conn = http.client.HTTPSConnection("real-time-finance-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "3c6eefd087mshe93f15fa0ced7ecp14448djsnd6db5503a79a",
    'x-rapidapi-host': "real-time-finance-data.p.rapidapi.com"
}

conn.request("GET", "/market-trends?trend_type=MARKET_INDEXES&country=us&language=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

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
