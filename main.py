# package imports taipy
from taipy.gui import Gui, notify, navigate, Html, State
import dateutil.parser

# pages imports
#from pages.pageOne import page1_md
from pages.pageTwo import page2_md

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
        if(type == "photo"): return apod_data['url']
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    

#root menu -----------------------------------------------------------------------------------------------------------
root_md="<|menu|label=SpaceMan|lov={[('Page-1', 'Birthday Astronomy'), ('Page-2', 'Graph')]}|on_action=on_menu|>"

#Astonomy photo of the day-----------------------------------------------------------------------------------------------------------
page1_md= """
# Birthday Astronomy



**<|{title}|>**

<|{date}|>

<|{explanation}|>

<|{p}|image|label=Astronomy Image|> 

Birthday: <|{text}|>

<|{text}|input|>

<|Submit|button|on_action=on_button_action|>

"""

#not available-----------------------------------------------------------------------------------------------------------
page2_md= """#graph"""


# menu navigation
def on_menu(state, var_name, info):
    page = info['args'][0]
    navigate(state, to=page)
   
# Different Tabs   
pages = {
    "/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "/": root_md,
    "Page-1": page1_md,
    "Page-2": page2_md,
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
    state.x  = call_APOD("allInfo",state.text)
    state.title = state.x[0]
    state.date = state.x[1]
    state.explanation = state.x[2]
    state.p= call_APOD("photo",state.text)

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return
   
       

x  = ''
p  = ''#call_APOD("photo",birth)


# terrible magic numbers but i'm desperate
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


#why