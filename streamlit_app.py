import streamlit
streamlit.title('Welcome to ColeHaaan')
streamlit.header('Colehaan Brand New Items')
streamlit.text('🥣 Shoes')
streamlit.text('🥗 Bags')
streamlit.text('🐔 Clothes')
streamlit.text('🥑🍞Wallets')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
