# package imports taipy
from taipy.gui import Gui, notify, navigate, Html, State

# pages imports
from pages.pageOne import page1_md
from pages.pageTwo import page2_md

#API
import requests

api_key = 'bCktnBQ9LJKx8ReMeg5UFrVeOGRUivobfFVX86G9'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

# API request APOD
def call_APOD(type):
    print("callLLLLLLLLLLLLLLLLLLLLLLLLL")
    return  "Title: Fireball over IcelandDate: 2023-09-16Explanation: On September 12, from a location just south of the Arctic Circle, stones of Iceland's modern Arctic Henge point skyward in this startling scene. Entertaining an intrepid group of aurora hunters during a geomagnetic storm, alluring northern lights dance across the darkened sky when a stunning fireball meteor explodes. Awestruck, the camera-equipped skygazers captured video and still images of the boreal bolide, at its peak about as bright as a full moon. Though quickly fading from view, the fireball left a lingering visible trail or persistent train. The wraith-like trail was seen for minutes wafting in the upper atmosphere at altitudes of 60 to 90 kilometers along with the auroral glow.Image URL: https://apod.nasa.gov/apod/image/2309/_DSC7280-1s_1024.jpg"
    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        apod_data = response.json()
        # Now, you can access various APOD data fields
        if(type == "allInfo"):response = f"Title: {apod_data['title']}" + f"Date: {apod_data['date']}" + f"Explanation: {apod_data['explanation']}"
        if(type == "photo"):response = f"Image URL: {apod_data['url']}"
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    

#root menu -----------------------------------------------------------------------------------------------------------
root_md="<|menu|label=SpaceMan|lov={[('Page-1', 'Photo of the Day'), ('Page-2', 'Graph')]}|on_action=on_menu|>"

#Astonomy photo of the day-----------------------------------------------------------------------------------------------------------
page1_md= """
# Photo of the Day  

Value of x: <|{x}|>

<|{pe}|image|label=this is an image|on_action=function_name|>

"""

#not available-----------------------------------------------------------------------------------------------------------
page2_md= page2_md


# menu navigation
def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)
   
# Different Tabs   
pages = {
    "/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "/": root_md,
    "Page-1": page1_md,
    "Page-2": page2_md,
}



# Astronomy Picture of the Day
x  = call_APOD("allInfo")
p  = call_APOD("photo")


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



# Graphics User Interface
Gui(pages=pages).run(use_reloader=True)


