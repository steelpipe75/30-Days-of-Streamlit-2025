import streamlit as st

# st.title('st.experimental_get_query_params')
st.title('st.query_params')

with st.expander('About this app'):
#   st.write("`st.experimental_get_query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")
  st.write("`st.query_params` allows the retrieval of query parameters directly from the URL of the user's browser.")

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?firstname=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes 
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# # 2. Contents of st.experimental_get_query_params
# 2. Contents of st.query_params
# st.header('2. Contents of st.experimental_get_query_params')
st.header('2. Contents of st.query_params')
# st.write(st.experimental_get_query_params())
st.write(st.query_params.to_dict())


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

query_params = st.query_params.to_dict()

# firstname = st.experimental_get_query_params()['firstname'][0]
firstname = query_params.get('firstname')
# surname = st.experimental_get_query_params()['surname'][0]
surname = query_params.get('surname')

st.write(f'Hello **{firstname} {surname}**, how are you?')
