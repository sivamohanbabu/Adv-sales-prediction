import pandas as pd
import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))

st.title("Advertisement Sales pediction")
st.write("Enter the values to get the predicted sales")

tv = st.number_input("Enter the tv budget",min_value=0.0,key='tv')
radio = st.number_input("Enter the radio budget",min_value=0.0,key='radio')
news = st.number_input("Enter the news budget",min_value=0.0,key='news')


if st.button("pedict the sales"):
    input_values = pd.DataFrame(
        [[float(tv),float(radio),float(news)]],columns=['TV','Radio','Newspaper']
    )
    pediction = model.predict(input_values)

    st.success(f"Predicted sales {pediction[0]:.2f}")