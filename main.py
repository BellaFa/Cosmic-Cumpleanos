# package imports taipy
from taipy.gui import Gui, notify, navigate, Html

# pages imports
from pages.pageOne import page1_md
from pages.pageTwo import page2_md


root_md="<|menu|label=SpaceMan|lov={[('Page-1', 'Photo of the Day'), ('Page-2', 'Graph')]}|on_action=on_menu|>"
page1_md= page1_md
page2_md= page2_md



def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)
   
   
pages = {
    "/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "/": root_md,
    "Page-1": page1_md,
    "Page-2": page2_md,
}



text = "Original text"



def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return
    

my_theme = {
  "palette": {
    "background": {"default": "#000204"},
    "primary": {"main": "#000204"}
  }
}



Gui(pages=pages).run(use_reloader=True, theme = my_theme)


