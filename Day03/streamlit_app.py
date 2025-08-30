import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.divider()

st.markdown('# st.button について踏み込んで実践')


st.markdown('## disabled : ボタンを押せなくする')

st.button('disable button', disabled=True)

st.markdown('## width : ボタンの幅')

st.markdown('### width = "content" : コンテンツ幅に合わせる（デフォルト）')
st.button('width = "content"', width="content")

st.markdown('### width = "stretch" : 親コンテナの幅に合わせて広げる')
st.button('width = "stretch"', width="stretch")

st.markdown('### width = int数値 : 幅をピクセル単位で指定（上限は親コンテナの幅まで）')
st.button('width = 50', width=50)
st.button('width = 250', width=250)
st.button('width = 500', width=500)
st.button('width = 1000', width=1000)
st.button('width = 1500', width=1500)
st.button('width = 2000', width=2000)


