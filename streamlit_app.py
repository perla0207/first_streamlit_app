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

#create the repeatable code block(called a function)

def get_fruityvice_data(this_fruit_choice):
    fruity_response=requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
# take the json verson of the response and normalize it
    fruityvice_normalized=pandas.json_normalize(fruity_response.json())
    return fruityvice_normalized  

# New Section to Display Fruityvice response api
    streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('what fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
   else:
       back_from_function=get_fruityvice_data(fruit_choice)

#Output it the screen as a table
       streamlit.dataframe(back_from_function)

except URLError as e:
       streamlit.error()

# Dont run anything paste here while we troubleshoot
streamlit.stop()

#import snowflake.connector

streamlit.header("the fruitLoad List Contains:")
#snowflake related function
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")  
         return my_cur.fetchall()
    
#Allow the end user to add to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')")
         return "Thanks for adding " + new_fruit
add_my_fruit=streamlit.text_input('what fruit would you like to add?')    
# add a button to load the list
if streamlit.button('Add a Fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function=insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
                                           
