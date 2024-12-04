import streamlit as st
import time
#st.set_page_config(page_title="SpamDetector",layout='wide',initial_sidebar_state='auto')
def app():
    st.markdown(
        """
        <style>
            .title-container {
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }
            .title {
                font-size: 3em;
                color: #5a5a5a;
                animation: fadeIn 1s ease-in-out forwards; /* Add animation */
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            /* Other styles (previous styles) */
            .description {
                font-size: 1.2em;
                color: #777;
                line-height: 1.6;
                padding: 10px;
            }
            .feature-highlight {
                color: #007bff;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div ><h1 class="title">Spam Detector</h1></div>',
        unsafe_allow_html=True,
    )


    st.markdown(
        """
        <div>
          <p class="description">This application is designed for accurate spam detection, leveraging advanced machine learning models.</p>
          <p class="description">This application provides a streamlined approach for training and deploying spam detection models.
           Upload your labeled dataset, configure relevant hyperparameters, and watch as the model trains to accurately identify spam.
          </p>
          <p class="description">
            Key features include:
            <ul>
              <li><b>Easy Data Upload</b>: Load your labeled dataset from a CSV file.</li>
              <li><b>Configurable Model Training</b>:  Customize training parameters for optimal results.</li>
              <li><b>Detailed Visualizations</b>:  Monitor training progress with clear loss and accuracy plots.</li>
              <li><b>High Accuracy</b>:  Expect a well-trained model that distinguishes spam from legitimate messages.</li>
            </ul>
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


    if st.button("Start"):
        # pass
        @st.dialog('Sign up')
        def sign_up_form():
            user_name=st.text_input('Username: ')
            email=st.text_input('Email: ')
            if st.button('login'):
                st.switch_page('pages\Train.py')
        sign_up_form()
        


if __name__ == "__main__":
    app()