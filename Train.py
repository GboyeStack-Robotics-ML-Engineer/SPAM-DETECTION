import streamlit as st
import time
import pandas as pd
import random
import numpy as np
import plotly.graph_objects as go 
import streamlit.components.v1 as comp

def train_model(df, input_col, target_col, hyperparameters):
    """Simulates training a model."""
    #st.write("Training...")
    # Simulate training process (replace with your real logic)
    #time.sleep(2) # Simulate training time
    
    # Create dummy data if the data is empty
    if df.empty:
        st.error("No data loaded. Please upload a CSV file.")
        return
    
    # Make sure columns exist!
    if input_col not in df.columns or target_col not in df.columns:
        st.error(f"Column '{input_col}' or '{target_col}' not found in the uploaded dataset.")
        return
    
    train_loss = [random.uniform(0.1, 0.5)] * 10
    train_accuracy = [random.uniform(0.8, 0.95)] * 10
    
    my_bar = st.progress(0, text='Training....')
    # Create a progress bar (simulated)
    for i in range(100):
        time.sleep(0.01)
        my_bar.progress(i+1, text='Training....')
    time.sleep(0.001)  # Small delay for animation
    my_bar.empty()
    st.success("Training Complete!")
    
    metrics_df = pd.DataFrame({
        "Step": range(len(train_loss)),
        "Train Loss": train_loss,
        "Train Accuracy": train_accuracy,
    })

    return metrics_df
def app():
    data,input_col,target_col,hyperparameters=None,None,None,None
    tab1, tab2, tab3, tab4 = st.tabs(["DATA", "MODEL", "HYPERPARMETER","VISUALIZE"])

    with tab1:
        st.header("DATA",help='Prepare Data for Training model',divider=True)
        data_file = st.file_uploader("Upload Training Data (CSV)", type=["csv"])

        if data_file is not None:
            # Read the CSV data into a Pandas DataFrame
            data = pd.read_csv(data_file)
            #st.write("Data Preview:")
            #st.write(data.head())

            # Select input and target columns
            input_col = st.selectbox("Select Input Column", data.columns)
            target_col = st.selectbox("Select Target Column", data.columns)
            
            if st.button("SAVE"):
                
                st.success('Succesfull 🎉🎉🎉')
        else:
            st.error('Provide the Data to be used for finetuning....')
                
                
        
        
    with tab2:
        st.header("MODEL")
        
    with tab3:
        st.header("HYPERPARMETERS",help='Configure Model Hyperparameters for Training',divider=True)
        
        st.subheader("Configure Hyperparameters")
        
        epochs = st.slider("Epochs", min_value=1, max_value=50, value=10, step=1)
        
        lr = st.slider("Learning Rate", min_value=0.0001, max_value=0.1, value=0.001, step=0.0001)
        
        batch_size = st.slider("Batch Size", min_value=16, max_value=512, value=32, step=16)
        
        if st.button('START TRAINING'):
            
            hyperparameters = {'batch_size': batch_size, 'learning_rate': lr, 'epochs':epochs}
            
            try:
                metrics_df = train_model(data, input_col, target_col, hyperparameters)
                print('hell0')
            except Exception as e:
                st.error(f"An error occurred: {e}")
                pass
            
            
<<<<<<< HEAD
=======
        
>>>>>>> e0cb30a7fc1e267ed85c4374e9af6e4ed314e06e
    with tab4:
        
        st.header("VISUALIZE",help='Visualize Training Metrics. Displays the loss ,accuracy when training and Validatiing the model',divider=True)
        
        try:
            if not metrics_df.empty:
                    with st.spinner('loading...'):
                        time.sleep(5)
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=metrics_df['Step'], y=metrics_df['Train Loss'], mode='lines', name='Train Loss'))
                    fig.add_trace(go.Scatter(x=metrics_df['Step'], y=metrics_df['Train Accuracy'], mode='lines', name='Train Accuracy'))
                    st.plotly_chart(fig,use_container_width=True)
            else:
                comp.iframe('https://lottie.host/embed/754a2905-46e1-4846-8bc1-30f31dbdbce3/gq0GebmriB.json')
                st.error('No Logged metrics yet. Start training to view Logged metric...')
        except:
            comp.iframe('https://lottie.host/embed/754a2905-46e1-4846-8bc1-30f31dbdbce3/gq0GebmriB.json')
            st.error('No Logged metrics yet. Start training to view Logged metric...')
                

        
        
    