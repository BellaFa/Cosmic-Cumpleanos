# package imports taipy
from taipy.gui import Gui, notify, navigate, Html, State
import dateutil.parser

# pages imports
#from pages.pageOne import page1_md
from pages.pageTwo import page2_md

#API
import requests

api_key = 'bCktnBQ9LJKx8ReMeg5UFrVeOGRUivobfFVX86G9'


# API request APOD
def call_APOD(type,date='2020-09-18'):

   
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}'
    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        apod_data = response.json()
        # Now, you can access various APOD data fields
        if(type == "allInfo"):response = f"Title: {apod_data['title']}" + f"Date: {apod_data['date']}" + f"Explanation: {apod_data['explanation']}"
        if(type == "photo"):response = apod_data['url']
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    return response
    

#root menu -----------------------------------------------------------------------------------------------------------
root_md="<|menu|label=SpaceMan|lov={[('Page-1', 'Photo of the Day'), ('Page-2', 'Graph')]}|on_action=on_menu|>"

#Astonomy photo of the day-----------------------------------------------------------------------------------------------------------
page1_md= """
# Photo of the Day



Value of x: <|{x}|>

<|{p}|image|label=this is an image|on_action=function_name|>

My text: <|{text}|>

<|{text}|input|>

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
x  = call_APOD("allInfo")
p  = call_APOD("photo",birth)




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


