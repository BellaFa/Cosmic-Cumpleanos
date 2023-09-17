# package imports taipy
import base64
from io import BytesIO
from flask import render_template
from taipy.gui import Gui, notify, navigate, Html, State
import dateutil.parser
import matplotlib.pyplot as plt



#API
import requests
import json

api_key = 'bCktnBQ9LJKx8ReMeg5UFrVeOGRUivobfFVX86G9'


# API request APOD
def call_APOD(type,date='2020-09-18'):

   
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}'
    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        apod_data = response.json()
        # Now, you can access various APOD data fields
        # if(type == "allInfo"): return f"Title: {apod_data['title']}" + f"Date: {apod_data['date']}" + f"Explanation: {apod_data['explanation']}"
        if(type == "allInfo"):
            data = [apod_data['title'], apod_data['date'], apod_data['explanation']]
            return data
        if(type == "photo"):
            return apod_data['url']
        
    else:
        print(f"Request failed with status code: {response.status_code}")
        return "oof"
    
#API request DONKI Coronal Mass Ejection
def call_DONKI_CME(type, startDate='2020-09-18', endDate='2020-09-18'):
    url = f'https://api.nasa.gov/DONKI/CME?startDate={startDate}&endDate={endDate}&api_key={api_key}'
    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        donki_data = response.json()
        # Now, you can access DONKI CME data fields
        data = [donki_data['activityID'], donki_data['catalog'], donki_data['startTime'], donki_data['sourceLocation'], donki_data['activeRegionNum'], donki_data['note']]

#root menu -----------------------------------------------------------------------------------------------------------
root_md="<|navbar|>"

#Astonomy photo of the day-----------------------------------------------------------------------------------------------------------
page1_md= """
# Birthday Astronomy
*Find out what astronomy picture was posted by NASA the same day you came into this world!!!*


**<|{title}|>**

<|{date}|>

<|{explanation}|>

<|{p}|image|> 

Birthday Y-MM-DD: <|{text}|>

<|{text}|input|>

<|Submit|button|on_action=on_button_action|>

"""

#not available-----------------------------------------------------------------------------------------------------------
page2_md = """
<|You would not believe your eyes if ten million fireflys beep beep beeop bop bop be bop be|button|on_action=get_disaster|center|>
<|Slider|>

"""

 






# menu navigation
def on_menu(state, var_name, info):
    page = info['args'][0]
    navigate(state, to=page)
   
# Different Tabs   


pages = {
    "/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "/": root_md,
    "Birthday-Astronomy": page1_md,
    "Graph": page2_md
    
}



# Astronomy Picture of the Day uncomment 
birth = '2023-4-7'
text = ''
def valid_date(state: State):
    print(state.text)
    date = dateutil.parser.parse(state.text)
    print(date)
    text=date
    #on_statusBirth(state)

def on_button_action(state):
    #date = dateutil.parser.parse(state.text)
    notify(state, 'info', f'APOD The date is: {state.text}')
    state.text = state.text
    state.x = call_APOD("allInfo",state.text)
    if (state.x != 'oof'):
        state.title = state.x[0]
        state.date = state.x[1]
        state.explanation = state.x[2]
        state.p = call_APOD("photo",state.text)
    else:
        state.title = "Error: Please enter a date in the YYYY-MM-DD format and no earlier than 1995-06-16."
        state.date = ''
        state.explanation = ''
        state.p = 'imgs/tryagain.png'


def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return
   

x  = ''
p  = 'imgs/telescope.jpg'#call_APOD("photo",birth)
title = ''
date = ''
explanation = ''



# Use State for Picture of the day Info
#def on_statusBirth(state: State):
  #  return {
   #     "text": state.text,
   #     "info": "Some information..."
   # }
# Use State for Picture of the day Info
def on_status(state: State):
    return {
        "x": state.x,
        "info": "Some information..."
    }
# Use State for Picture of the day Info photo
def on_status(state: State):
    return {
        "p": state.p,
        "info": "Some information..."
    }

# input birthdate 
def on_status(state: State):
    return{
        "birth": state.birth,   
         "info": "Some information..."
    }



# Graphics User Interface
Gui(pages=pages).run(use_reloader=True)


#whywhywhy