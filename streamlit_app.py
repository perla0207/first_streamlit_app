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
my_fruit_list=my_fruit_list.set_index('Fruit')
#lets put a picklist to pick the fruits they want
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
# to display the table on the page
streamlit.dataframe(fruits_to_show)

# New Section to Display Fruityvice response api
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('what fruit would you like information about?', 'kiwi')
streamlit.write('The User Entered',fruity_choice)

import requests
fruity_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json verson of the response and normalize it

fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

#Output it the screen as a table

streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select current_user(),current_account(),current_region()")
my_data_row=my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
