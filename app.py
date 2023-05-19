import streamlit as st
import pickle
import requests
import os
import pandas as pd
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
st.title('Book Recommendation system')
list_book=np.array(popular_df['Book-Title'])
option=st.selectbox("Select a  book",(list_book))
st.write('You selected:', option)
if st.button('Recommend'):
#def recommend():
    user_input = option
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
    data = []
    for i in similar_items:

        with st.container():
        
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            x = temp_df.drop_duplicates('Book-Title')['Book-Title'].values
            st.header(x[0])
            st.subheader(temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0])
            st.image(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0])

        
       

