import streamlit as st

import functions

todos = functions.get_todo_list()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todo_list(todos)
    st.session_state["new_todo"] = ""


st.title('_My Todo App_ is :blue[cool] :sunglasses:')
st.subheader("This is my todo app", divider="rainbow")
st.write("This app is to help people remember things to do")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo_list(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a Todo", placeholder="Add a new todo item...", on_change=add_todo, key="new_todo")

