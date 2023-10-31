import streamlit as st
from Module import helperFunction

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    helperFunction.writeCurrentList(todos)

todos = helperFunction.getCurrentList()
st.title("Todo app")
st.subheader('this is the todo app')
st.write('The add increse the productivity')

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(idx)
        helperFunction.writeCurrentList(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', placeholder="Add new item", on_change = add_todo, key = 'new_todo')