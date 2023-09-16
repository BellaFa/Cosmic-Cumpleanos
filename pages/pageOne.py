#Packages
from taipy.gui import Html, State, Gui

#API
import requests

api_key = 'bCktnBQ9LJKx8ReMeg5UFrVeOGRUivobfFVX86G9'
url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'


def call_APOD():
    print("callLLLLLLLLLLLLLLLLLLLLLLLLL")
    return  "Title: Fireball over IcelandDate: 2023-09-16Explanation: On September 12, from a location just south of the Arctic Circle, stones of Iceland's modern Arctic Henge point skyward in this startling scene. Entertaining an intrepid group of aurora hunters during a geomagnetic storm, alluring northern lights dance across the darkened sky when a stunning fireball meteor explodes. Awestruck, the camera-equipped skygazers captured video and still images of the boreal bolide, at its peak about as bright as a full moon. Though quickly fading from view, the fireball left a lingering visible trail or persistent train. The wraith-like trail was seen for minutes wafting in the upper atmosphere at altitudes of 60 to 90 kilometers along with the auroral glow.Image URL: https://apod.nasa.gov/apod/image/2309/_DSC7280-1s_1024.jpg"
    # Make the API request
    response = requests.get(url)

    if response.status_code == 200:
        apod_data = response.json()
        # Now, you can access various APOD data fields
        response = f"Title: {apod_data['title']}" + f"Date: {apod_data['date']}" + f"Explanation: {apod_data['explanation']}" + f"Image URL: {apod_data['url']}"
    else:
        print(f"Request failed with status code: {response.status_code}")
    


res = call_APOD()

print(res)

x = 55

def on_status(state: State):
    return {
        "x": state.x,
        "info": "Some information..."
    }


page1_md = """
# Status page

Value of x: <|{x}|>
"""



#Gui(pages=page1_md).run(use_reloader=True)

meh = Html("""

<head>
    <style>
        body {
            background-image: url('space3PNGgrey.png');
            background-size: cover; /* Optional: Adjust the image size to cover the entire container */
            background-repeat: no-repeat; /* Optional: Prevent the image from repeating */
            background-color: rgba(0, 0, 255, 0.5); /* Set the background color to blue with 50% opacity */
            text-align: center; /* Center-align content horizontally */
            font-family: Arial, sans-serif; /* Specify a font */
            }
                  
            .container {
            padding: 20px; /* Add padding for spacing */
            
        }
        .title {
                  
            font-size: 24px; /* Adjust the font size as needed */
        }
        .image {
            display: block; /* Make the image a block element */
            margin: 0 auto; /* Center the image horizontally */
            max-width: 100%; /* Ensure the image doesn't exceed its container's width */
        }
                          
    </style>
</head>
 <body>
    <div class="container">
        <div class="title">
            Photo of the day
        </div>
        
    </div>
</body>
               
""")