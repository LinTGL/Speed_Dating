import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import random
import os
import faker

with open('model.pkl', 'rb') as f:
    speedvoisin = pickle.load(f)


clean_speed = pd.read_csv(r"C:\Users\DELL 7480\Documents\PROTOJAM\speed_data_data.csv")


st.title('❤️Welcome in your LoveMachine❤️')

imageDate = Image.open(r'C:\Users\DELL 7480\Documents\PROTOJAM\SpeedDating.jpeg')
st.image(imageDate, caption='LoveIsInTheAir')

st.sidebar.title('Find your Lover 👩🏽‍❤️‍💋‍👨🏼')
st.sidebar.image(r'C:\Users\DELL 7480\Documents\PROTOJAM\SpeedDating.jpeg')


st.sidebar.title('Questionnary')

# gender = st.sidebar.selectbox('What gender are you looking for ? :',('female', 'male', 'Both') )
# age = st.sidebar.number_input('How old are you ? :', min_value=18, value=77, step=1)
# attraction = st.sidebar.number_input('From 1 to 10, how important is attractiveness to you?', min_value=1, value=5, max_value=10, step=1)
# ambitious = st.sidebar.number_input('From 1 to 10, How ambitious you want your partner ?', min_value=1, value=5, max_value=10, step=1)
# fun = st.sidebar.number_input('From 1 to 10, How much fun you want your sweety ?', min_value=1, value=5, max_value=10, step=1)



    
#Step 1: Create select boxes for each feature
selected_features = {}
for feature in clean_speed[['gender', 'age','attr','fun', 'amb' ]].columns:
    if feature == 'gender':
        selected_features[feature] = st.sidebar.selectbox('What gender are you looking for ? :',('female', 'male', 'Both') )   
        if selected_features[feature] == 'female':
           selected_features[feature] = 0
        elif selected_features[feature] == 'male':
            selected_features[feature] = 1
        else:
            selected_features[feature] = random.randint(0,1)
    elif feature == 'age':
        selected_features[feature] = st.sidebar.number_input('How old are you ? :', min_value=18, value=77, step=1)
    elif feature == 'amb':
        selected_features[feature] =  st.sidebar.number_input('From 1 to 10, How ambitious you want your partner ?', min_value=1, value=5, max_value=10, step=1)
    elif feature == 'attr':
        selected_features[feature] = st.sidebar.number_input('From 1 to 10, how important is attractiveness to you?', min_value=1, value=5, max_value=10, step=1)
    elif feature == 'fun':
        selected_features[feature] = st.sidebar.number_input('From 1 to 10, How much fun you want your sweety ?', min_value=1, value=5, max_value=10, step=1)


# Ajouter un bouton pour valider
if st.sidebar.button("Let's Love ❤️ ❤️ ❤️!!!!!", key=1):
    st.sidebar.write('You clicked the button.')
   
    

    #Step 2: Collect the selected values from the select boxes
    selected_values = [selected_features[feature] for feature in clean_speed[['gender', 'age','attr','fun', 'amb' ]].columns]

    #Step 3: Create a DataFrame using the collected values
    input_df = pd.DataFrame([selected_values], columns=clean_speed[['gender', 'age','attr','fun', 'amb' ]].columns)

    #Step 4: Use the trained KNN model to find the closest neighbors
    distances, indices = speedvoisin.kneighbors(input_df)

     
    #Print the indices and distances of the closest neighbors
    speedfiltre = clean_speed.iloc[indices[0][:2]]
    # st.write("Indices of nearest neighbors:", speedfiltre['career'])

   
    
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("Indices of nearest neighbors:", speedfiltre['career'])
    
        st.title("Do you feel the love ? :") 
        st.write("(http:://paypal.me/CupidonClub)")


        imageDate2 = Image.open(r'C:\Users\DELL 7480\Documents\PROTOJAM\PAYPAL.png')
        st.image(imageDate2, caption='LoveIsInTheAir')

    with right_column:
        # Define the path to your image directory
        image_directory = r'C:\Users\DELL 7480\Documents\PROTOJAM\avatar_speed'
        
        # List all files in the directory
        all_images = os.listdir(image_directory)
        
        # Select a random image
        random_image = random.choice(all_images)
        
        # Display the random image
        st.image(os.path.join(image_directory, random_image), caption='Your Lover')
        
    
    
        
        
    
    



