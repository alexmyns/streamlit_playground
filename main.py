import streamlit as st
import pandas as pd
from assets import t_info
import sqlite3


# SQL connection
con = sqlite3.connect('./data/chinook.sqlite')
c = con.cursor()


# Function to execute SQL
def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data


# Main functions to execute


def main():
    st.title('SQL Playground')

    menu = ['Home', 'About', 'Contact']

    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home')
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area('Your Code here!')
                submit_code = st.form_submit_button('Execute Code!')

            # Table of info
            with st.expander('Table Info'):
                table_info = {
                    'Album': t_info.table_info['Album'],
                    'Artist': t_info.table_info['Artist'],
                    'Customer': t_info.table_info['Customer'],
                    'Employee': t_info.table_info['Employee'],
                    'Genre': t_info.table_info['Genre'],
                    'Invoice': t_info.table_info['Invoice'],
                    'InvoiceLine': t_info.table_info['InvoiceLine'],
                    'MediaType': t_info.table_info['MediaType'],
                    'Playlist': t_info.table_info['Playlist'],
                    'PlaylistTrack': t_info.table_info['PlaylistTrack'],
                    'Track': t_info.table_info['Track']}

                st.json(table_info)
           # Table
            with col2:
                if submit_code:
                    st.info('Query submitted')
                    st.code(raw_code)

                    # Results
                    query_result = sql_executor(raw_code)
                    with st.expander("Results"):
                        st.write(query_result)

                    with st.expander('Beautify'):
                        query_df = pd.DataFrame(query_result)
                        st.dataframe(query_df)

    elif choice == 'About':
        st.subheader('''About
        - This is a simple app to play with SQL queries in SQLite.''')

        st.markdown(
            '''
          #### If you love to play with SQL, you can find more info about it here:
          * `https://www.sqlite.org/`




          * Buy me a coffee☕️: `8600 5729 7247 4170`
         '''
        )

    else:
        st.subheader('Contact')
        st.markdown(
            '''
               #### Last but not least, If you have any questions, please contact me at:
               * alixan.me@yandex.com
               * https://t.me/alexmyn
               '''
        )


if __name__ == '__main__':
    main()
