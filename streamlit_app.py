import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Welcome to ColeHaaan')
streamlit.header('Colehaan Brand New Items')
streamlit.text('🥣 Shoes')
streamlit.text('🥗 Bags')
streamlit.text('🐔 Clothes')
streamlit.text('🥑🍞Wallets')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
#lets put a picklist to pick the fruits they want
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
# to display the table on the page
streamlit.dataframe(fruits_to_show)

# New Section to Display Fruityvice response api
streamlit.header('Fruityvice Fruit Advice!')
try:
fruit_choice = streamlit.text_input('what fruit would you like information about?')
if not fruit_choice:
  streamlit.error("Please select a fruit to get information.")
  else:
streamlit.write('The User Entered', fruit_choice)

#import requests
fruity_response=requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json verson of the response and normalize it

fruityvice_normalized=pandas.json_normalize(fruity_response.json())

#Output it the screen as a table

streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()

# Dont run anything paste here while we troubleshoot
streamlit.stop()

#import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruitLoad List Contains:")
streamlit.text(my_data_rows)
streamlit.dataframe(my_data_rows)



fruit_choice=streamlit.text_input('what fruit would you like information about?', 'Jackfruit')
add_my_fruit=streamlit.write('The User Entered', fruit_choice)
streamlit.write('Thanks for Adding', add_my_fruit)
my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit')")
