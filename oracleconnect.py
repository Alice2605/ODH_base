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
#dsn = oracledb.ConnectParams(host=st.secrets.host, port=st.secrets.port, service_name=st.secrets.service_name)

dsn = """(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=st.secrets.host)(PORT=int(st.secrets.port)))
          (CONNECT_DATA=(SERVICE_NAME=st.secrets.service_name)))"""

print("["+current_time+"]"+blue_start+ " Got DSN !"+blue_end)
print("["+current_time+"]"+blue_start+ " Trying to connect on server "+ st.secrets.host +blue_end)
start_time = datetime.datetime.now()

connection = oracledb.connect(user=st.secrets.user, password=st.secrets.password, dsn=dsn)
# Connection to the database
try:
    print("["+current_time+"]"+blue_start+" Establishing connection...."+blue_end)
    connection = oracledb.connect(user=st.secrets.user, password=st.secrets.password, dsn=dsn)
    print(f'[{current_time}] ......')
    cursor = connection.cursor()
    print("["+current_time+"]" "\033[32m" + " Connection successfully established to server " + st.secrets.host+ " With user : "+st.secrets.user+ "\033[0m")

except oracledb.DatabaseError as e:
    print(f"[{current_time}] Connection error:", e)

end_time = datetime.datetime.now()

# Function to execute queries
#@st.cache_data
def searchtodf(QUERRY):
    cursor = connection.cursor()
    cursor.execute(QUERRY)
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    return df

