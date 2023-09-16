from taipy.gui import Html




page1_md =  """
# Getting started with Taipy GUI

My text: <|{text}|>

<|{text}|input|>

<|{variable}|slider|min=0|max=10|>
""" 



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