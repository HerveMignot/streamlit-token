import os
import random
import streamlit as st


APP_TOKEN = os.environ.get('APP_TOKEN', str(random.randint(100, 1_000_000_000)))
st.set_page_config(layout='wide')

params = st.experimental_get_query_params()
if 'token' in params:
    token_access = params['token'][0]
else:
    token_access = ''

# st.write("{} / {}".format(APP_TOKEN, token_access))

if token_access == APP_TOKEN:
    with st.sidebar:
        st.write('### VINCI AIRPORTS ASSISTANT')
    st.markdown('## You have access to the app')

else:
    st.markdown('##  Nothing to say, sorry')
