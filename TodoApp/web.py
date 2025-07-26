import streamlit as st
import functions

# get the current list of todos and add a new one
todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"].strip() + "\n"
    todos.append(todo)
    functions.write_todos(todos)

    # Clear the text box
    st.session_state["new_todo"] = ""

def save_edited_todo(index):
    edited_todo = st.session_state[f"edit_todo_{index}"].strip() + "\n"
    todos[index] = edited_todo
    functions.write_todos(todos)
    st.session_state["edit_index"] = None

# Page layout
st.title("My Todo App")
st.text("Manage your tasks easily")

# initialize the edit index if not set
if "edit_index" not in st.session_state:
    st.session_state["edit_index"] = None

# loop through the todos and load them
for i, todo in enumerate(todos):
    if st.session_state["edit_index"] == i:
        # show the text input to edit the todo
        st.text_input(
            label=f"Edit your todo task",
            value=todo.strip(),
            key=f"edit_todo_{i}",
            on_change=save_edited_todo,
            args=(i,),
            help="Press Enter to save the changes"
        )

        # cancel button to exit the edit mode
        if st.button("Cancel", key=f"cancel_button_{i}"):
            st.session_state["edit_index"] = None
            st.rerun()
    else:
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            checkbox = st.checkbox(todo, key=todo)
            if checkbox:
                todos.pop(i)
                functions.write_todos(todos)
                del st.session_state[todo]
                st.rerun()
        with col2:
            if st.button("Edit", key=f"edit_button_{i}"):
                st.session_state["edit_index"] = i
                st.rerun()

# input for adding a new todo
st.text_input(label="Enter a todo",
              placeholder="Add a todo ...",
              on_change=add_todo,
              key="new_todo")