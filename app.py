import os
import streamlit as st


APP_TOKEN = os.environ.get('APP_TOKEN', str(ramdom.randint(100, 1_000_000_000)))
st.set_page_config(layout='wide')

params = st.experimental_get_query_params()
token_access = params.get('token', [''])[0]

if token_access == APP_TOKEN:
    with st.sidebar:
        st.write('### VINCI AIRPORTS ASSISTANT')
    st.markdown('## You have access to the app')

else:
    st.markdown('##  Nothing to say, sorry')
