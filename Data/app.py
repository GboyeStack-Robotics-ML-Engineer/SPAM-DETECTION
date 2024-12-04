import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import os

import pages.Inference as Inference
from pages.Inference import generate


import DataGenerator
import warnings
warnings.filterwarnings(action='ignore')
SAVED_WEIGHTS_PATH='t5-base'#""
SAVED_TOKENIZER_PATH=""

from transformers import T5ForConditionalGeneration,T5Tokenizer
MODEL_NAME='t5-base'
model=T5ForConditionalGeneration.from_pretrained(SAVED_WEIGHTS_PATH)
tokenizer=T5Tokenizer.from_pretrained(MODEL_NAME)

def email_prediction(msg,model,tokenizer):
    
    return  generate(model=model,tokenizer=tokenizer,content=msg)


def main():
    
    st.title("SPAM e-MAIL CLASSIFICATION")
    st.subheader('Built with Python and Streamlit')

    msg = st.text_input("Enter you Email Content to detect whether its HAM or SPAM")
    
    if st.button('Predict'):
        
        result = email_prediction(msg,model,tokenizer)

        if result:
            st.error("SPAM")
        else:
            st.success("HAM")
   

if __name__ == '__main__':
	main()