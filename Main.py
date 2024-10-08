import streamlit as st

# Set page title and configuration
#st.set_page_config(page_title="starfixGeoImager")

#Custom CSS styling for the options menu
custom_css = """
<style>
.option-menu {
    padding: 5px;
    background-color: black;
    border-radius: 5px;
}

.option-menu option {
    color: white;
    font-size: 20px;
}

.option-menu select {
    color: white;
    background-color: black;
    border: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    font-size: 20px;
}

.option-menu select:focus {
    outline: none;
}

.option-menu select::-ms-expand {
    display: none;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Importing modules after setting page configuration to ensure it's called first
from streamlit_option_menu import option_menu
import Home,Inference,Train,Developer

#Create the selection menu in the sidebar
selected_app = st.sidebar.selectbox(
    "Selections",
    ["Home", "TRAIN", "INFERENCE","👩‍💻 Developer"],
)

<<<<<<< HEAD

=======
>>>>>>> e0cb30a7fc1e267ed85c4374e9af6e4ed314e06e
# Define a function to render the selected app
def render_app(selected_app):
    if selected_app == "Home":
        Home.app()
    if selected_app == "TRAIN":
        Train.app()
    if selected_app == "INFERENCE":
        Inference.app()
    if selected_app == "👩‍💻 Developer":
        Developer.app()

# Render the selected app in the main body
render_app(selected_app)
