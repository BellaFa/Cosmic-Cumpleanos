from taipy.gui import Html




page2_md= Html("""

<head>
    <style>
        body {
            background-image: url('space3PNGgrey.png');
            background-size: cover; /* Optional: Adjust the image size to cover the entire container */
            background-repeat: no-repeat; /* Optional: Prevent the image from repeating */
            background-color: rgba(0, 0, 255, 0.5); /* Set the background color to blue with 50% opacity */
            
    </style>
</head>
 <body>

    <div>Pagehkkkhkh2</div>
</body>
               
""")
               

eh = """
My text: <|{text}|>

<|{text}|input|>"""