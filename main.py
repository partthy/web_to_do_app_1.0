import streamlit as st

import functions

todos = functions.get_todo_list()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to help people remember things to do")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="", placeholder="Add a new todo item")
