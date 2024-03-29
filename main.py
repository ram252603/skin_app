import streamlit as st
import numpy as np
import tensorflow as tf


def model_prediction(test_image):
    model = tf.keras.models.load_model("C:\\Users\\Ramchandra\\Desktop\\Deployment\\melanoma_classification_model.h5")
    
    image = tf.keras.preprocessing.image.load_img(test_image,target_size = (128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #retutn max index value 

#sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page" , ["Home","About Project" , "Prediction"])


#main page
if(app_mode == "Home"):
    st.header("SKIN CANCER DETECTION")
    image_path = "melanoma_10108.jpg"
    st.image(image_path)
    
    
#About project
elif(app_mode == "About Project"):
    st.header("About Our Project")
    st.subheader("About Dataset")
    st.text("Melanoma skin cancer detection involves the identification and diagnosis of melanoma, a type of skin cancer that originates in melanocytes, the cells responsible for producing the pigment melanin. Melanoma is considered the most serious type of skin cancer due to its potential to spread to other parts of the body if not detected and treated early. Risk Factors:Exposure to UV Radiation: Prolonged exposure to ultraviolet (UV) radiation from the sun or tanning beds increases the risk.Fair Skin: Individuals with fair skin, light-colored hair, and light-colored eyes are at a higher risk.Family History: A family history of melanoma may contribute to an increased risk.")        
    st.code("Alternaria, Anthracnose, Black Mould Rot and Stem and Rot. An additional category in the dataset is healthy fruits")
     
    
    
#prediction page
elif(app_mode == "Prediction"):
    st.header("Model Prediction")
    test_image = st.file_uploader("Choose an Image")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
        
    if(st.button("Predict")):
        st.write("Our prediction")
        result_index = model_prediction(test_image)
        
        with open("label.txt") as f:
            content = f.readlines()
        label = ['Benign','Malignant']
        
        for i in content:
            label.append(i[:-1])
        st.success("Model is predicting its a {}".format(label[result_index]))