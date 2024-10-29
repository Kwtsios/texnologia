import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
from PIL import Image
pip install nest_asyncio
import nest_asyncio
nest_asyncio.apply()

# Set the page to a wide layout
st.set_page_config(layout="wide")

# Title
st.title("Serverless functions") # Displays title

# First Serverless Function for Basic Calculator
col3, col4, col5 = st.columns(3)
with col3:
    number1 = st.number_input('Insert first number')
with col4:
    number2 = st.number_input('Insert second number')
with col5:
    operator = st.selectbox('Choose an operator:', ('+', '-', '/', '*'))
    if operator == '+':
        operator = 'add'

# Display result from serverless function
st.write('Result from the first serverless function')
send = f'https://vhkmdl2db7wsc3cggv3ozoj4ne0owrdk.lambda-url.ap-northeast-1.on.aws/?num1={number1}&num2={number2}&op={operator}'
response = requests.get(send)
st.write(response.text)

# Code implementation for first serverless function (display only)
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
            
            if op == 'add':
                x = float("{0:.2f}".format(num1 + num2))
                return_text = f"Your numbers add to: {x}"
            elif op == '-':
                x = float("{0:.2f}".format(num1 - num2))
                return_text = f"Your numbers subtract to: {x}"
            elif op == '/':
                x = float("{0:.2f}".format(num1 / num2))
                return_text = f"Your numbers divide to: {x}"
            elif op == '*':
                x = float("{0:.2f}".format(num1 * num2))
                return_text = f"Your numbers multiply to: {x}"
            else:
                return_text = "No valid operator chosen"
    return {
        'statusCode': 200,
        'body': f'{return_text}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')

# Second Serverless Function for Text Processing
col5, col6 = st.columns(2)
with col5:
    first_text = st.text_input('Enter first text', 'This is a sentence')
with col6:
    second_text = st.text_input('Enter a condition to check in the sentence', 'e')

st.write('Result from the second serverless function')
send_second = f'https://e7mdkoecvxzbqhjjymxdw3red40tmbun.lambda-url.ap-northeast-1.on.aws/?astring={first_text}&con={second_text}'
response_second = requests.get(send_second)
st.write(response_second.text)

# Code implementation for second serverless function (display only)
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
            condition = query["con"]
            count = x.count(condition)
            return_text = f"The condition '{condition}' appears {count} times in the sentence."
    return {
        'statusCode': 200,
        'body': f'{return_text}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')

# Third Serverless Function for Counting Characters
third_text = st.text_input('Enter text to count characters', 'This is a sentence')
st.write('Result from the third serverless function')
send_third = f'https://6oswps446zy2qud64ngemd34bi0cgppp.lambda-url.ap-northeast-1.on.aws/?st={third_text}'
response_third = requests.get(send_third)
st.write(response_third.text)

# Code implementation for third serverless function (display only)
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
            char_count = len(x)
            return_text = f"There are {char_count} characters in the sentence."
    return {
        'statusCode': 200,
        'body': f'{return_text}',
        'headers': { 'Content-Type': "text/html" }
    }'''
st.code(code, language='python')

# Weather API Example
st.subheader("Weather API Example")
url = "https://weatherapi-com.p.rapidapi.com/current.json"
headers = {
    "X-RapidAPI-Key": "0312d33db3msh895b45c60fda80ep1c980ajsn320bd55b226e",  # Replace with your actual RapidAPI key
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
location = st.text_input("Enter the location", "Cyprus")
querystring = {"q": location}
response = requests.get(url, headers=headers, params=querystring)
if response.status_code == 200:
    data = response.json()
    st.write(f'Location: {data["location"]["name"]}, {data["location"]["country"]}')
    st.write(f'Temperature: {data["current"]["temp_c"]}°C')
    st.write(f'Condition: {data["current"]["condition"]["text"]}')
    st.image(f'http:{data["current"]["condition"]["icon"]}')
else:
    st.error("Could not retrieve weather data.")
