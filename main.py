import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
import pymysql
# import sqlalchemy

from phonepe2 import *


# Connection to SQL
from sqlalchemy import create_engine, text
engine1 = create_engine("mysql+pymysql://{user}:{pw}@localhost"
                       .format(user="root",
                               pw="Password"))
connection = engine1.connect()
# Execute the SQL query
query = text("SHOW DATABASES;")
result = connection.execute(query)
# Fetch the query result
databases = result.fetchall()
existing_databases = [d[0] for d in databases]
database = "phonepe1"

if database not in existing_databases:
    connection.execute("CREATE DATABASE {0}".format(database))
    print("Created database {0}".format(database))
    connection.execute("USE phonepe1")
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Password",
                              db = database))
d1.to_sql('aggregated_transaction', con = engine, if_exists = 'replace')
d2.to_sql('aggregated_user', con = engine, if_exists = 'replace')
d3.to_sql('map_transaction', con = engine, if_exists = 'replace')
d4.to_sql('map_user', con = engine, if_exists = 'replace')
d5.to_sql('top_transaction', con = engine, if_exists = 'replace')
d6.to_sql('top_user', con = engine, if_exists = 'replace')

# Comfiguring Streamlit GUI
st.set_page_config(layout='wide')

# Title
st.header(':violet[Phonepe Pulse Data Visualization ]')
st.write('*(Note):-This data between **2018* to *2022* in *INDIA*')

# ---------------------Basic Insights -----------------#
conn = mysql.connector.connect(user='root', password='Password', host='localhost')
cursor = conn.cursor()

# with st.sidebar:
SELECT = option_menu(
    menu_title="Main Menu",
    options=["Home", "Insights"],
    orientation="horizontal")

if SELECT == "Home":
    col1, col2, = st.columns(2)
    with col1:
        st.subheader(
            "PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        col2.write("This is column1 of Home page")

if SELECT == "Insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 10 Registered-users based on States and District",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 Districts based on states and amount of transaction",
               "List 10 Transaction_Count based on Districts and states",
               "Top 10 RegisteredUsers based on states and District"]

    # 1

    select = st.selectbox("Select the option", options)
    if select == "Top 10 states based on year and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT State, Year, SUM(Transaction_amount) AS Total_Transaction_Amount FROM top_trans_dist GROUP BY State, Year ORDER BY Total_Transaction_Amount DESC LIMIT 10");

        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year', 'Transaction_amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df, x="Transaction_amount", y="State")

            # 2

    elif select == "List 10 states based on type and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT State, SUM(Transaction_count) as Total FROM top_trans_dist GROUP BY State ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Transaction'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df, x="Total_Transaction", y="State")

            # 3

    elif select == "Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute(
            "SELECT DISTINCT Transaction_type, SUM(Transaction_amount) AS Amount FROM agg_user GROUP BY Transaction_type ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_type', 'Transaction_amount '])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_Type based on Transaction_Amount")
            st.bar_chart(data=df, x="Transaction_type", y="Amount")

            # 4

    elif select == "Top 10 Registered-users based on States and District":
        cursor.execute(
            "SELECT DISTINCT State, District, SUM(Registered_users) AS Users FROM top_user_dist GROUP BY State, District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'District', 'Registered_users'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Registered-users based on States and District")
            st.bar_chart(data=df, x="State", y="Registered_users")

            # 5

    elif select == "Top 10 Districts based on states and Count of transaction":
        cursor.execute(
            "SELECT DISTINCT State,District,SUM(Transaction_count) AS Counts FROM map_tran GROUP BY State,District ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'District', 'Transaction_count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df, x="State", y="Transaction_count")

            # 6

    elif select == "List 10 Districts based on states and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT State, Year,SUM(Transaction_amount) AS Amount FROM agg_trans GROUP BY State, Year ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year', 'Transaction_amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df, x="State", y="Transaction_amount")

            # 7

    elif select == "List 10 Transaction_Count based on Districts and states":
        cursor.execute(
            "SELECT DISTINCT State, District, SUM(Transaction_count) AS Counts FROM map_tran GROUP BY State,District ORDER BY Counts ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'District', 'Transaction_count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Transaction_Count based on Districts and states")
            st.bar_chart(data=df, x="State", y="Transaction_Count")

            # 8

    elif select == "Top 10 RegisteredUsers based on states and District":
        cursor.execute(
            "SELECT DISTINCT State,District, SUM(Registered_users) AS Users FROM map_user GROUP BY State,District ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'District', 'Registered_users'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            st.bar_chart(data=df, x="State", y="Registered_users")
#
# # ----------------Home----------------------#
# cursor = conn.cursor()
#
# rows = cursor.fetchall()
