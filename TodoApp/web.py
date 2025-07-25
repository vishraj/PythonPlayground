import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.text("List of current tasks")

# loop through the todos and load them
for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo", placeholder="Add a todo ...")
