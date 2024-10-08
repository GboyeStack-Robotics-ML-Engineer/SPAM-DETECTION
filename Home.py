import streamlit as st
import time

def app():
<<<<<<< HEAD
=======
    
>>>>>>> e0cb30a7fc1e267ed85c4374e9af6e4ed314e06e
    # Displaying the logo and subtext with a nice color
    st.markdown(
        """
        <div style='text-align: center; padding: 20px;'>
            <h1 style='color: rgb(153, 51, 153); font-size: 100px;'>Spam Detector</h1>
            <h3 style='color: #444444;'>Spam Detection</h3>
            <h4 style='color: #444444;'>Brief information about the project</h4>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Loading animation
    #with st.spinner("Loading..."):
        #time.sleep(6) 


if __name__ == "__main__":
    app()
