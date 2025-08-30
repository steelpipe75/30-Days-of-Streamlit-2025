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

button_disabled_radio = st.radio('ボタンの有効/無効を切り替え', ["有効", "無効"])

if button_disabled_radio == "有効":
    button_disabled = False
else:
    button_disabled = True

st.button('ラジオボタンによるボタンの有効無効の切り替え', disabled=button_disabled)


st.markdown('## width : ボタンの幅')

st.markdown('### width = "content" : コンテンツ幅に合わせる（デフォルト）')
st.button('width = "content"', width="content")

st.markdown('### width = "stretch" : 親コンテナの幅に合わせて広げる')
st.button('width = "stretch"', width="stretch")

width_int_markdown = """### width = int数値 : 幅をピクセル単位で指定（上限は親コンテナの幅まで）
右上の ⋮ → Settings → Wide mode で親コンテナの幅を変えるとボタンの幅も広くなる
"""

st.markdown(width_int_markdown)
st.button('width = 50', width=50)
st.button('width = 250', width=250)
st.button('width = 500', width=500)
st.button('width = 1000', width=1000)
st.button('width = 1500', width=1500)
st.button('width = 2000', width=2000)


st.markdown('### help : ボタンにマウスオーバーしたときに表示されるツールチップ')

st.button('help表示ありボタン', help='マウスオーバーすると表示')


st.markdown('### icon : ボタンラベルの横に表示する絵文字またはアイコン')

st.button('icon表示ありボタン1', icon='♨')
st.button('icon表示ありボタン2', icon='🏍')
st.button('icon表示ありボタン3', icon='🎲')
st.button('icon表示ありボタン4', icon=':material/home:')
st.button('icon表示ありボタン5', icon=':material/settings:')
st.button('icon表示ありボタン6', icon=':material/face:')


st.markdown('### type : ボタンの種類を指定するオプション')

st.button('type = "primary"', type="primary")
st.button('type = "secondary"', type="secondary")
st.button('type = "tertiary"', type="tertiary")
