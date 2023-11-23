import streamlit as st
import oracledb
import pandas as pd
import datetime
from functions import *
#import toml
blue_start = "\033[34m"
blue_end = "\033[0m"
current_time = datetime.datetime.now().strftime("%H:%M:%S")


''
# Creating the DSN
dsn = oracledb.ConnectParams(host=host, port=port, service_name=service_name)
print("["+current_time+"]"+blue_start+ " Got DSN !"+blue_end)
print("["+current_time+"]"+blue_start+ " Trying to connect on server "+ host +blue_end)
start_time = datetime.datetime.now()


# Connection to the database
try:
    print("["+current_time+"]"+blue_start+" Establishing connection...."+blue_end)
    connection = oracledb.connect(user=user, password=password, params=dsn)
    print(f'[{current_time}] ......')
    cursor = connection.cursor()
    print("["+current_time+"]" "\033[32m" + " Connection successfully established to server " + host+ " With user : "+user+ "\033[0m")

except oracledb.DatabaseError as e:
    print(f"[{current_time}] Connection error:", e)

end_time = datetime.datetime.now()

# Function to execute queries
@st.cache_data
def searchtodf(QUERRY):
    cursor = connection.cursor()
    cursor.execute(QUERRY)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    return df




#searchtodf("")

