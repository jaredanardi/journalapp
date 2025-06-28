import streamlit as st

st.title("Personal Task Tracker")

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

st.subheader("Add a New Task")
task_title = st.text_input("Task Title")
task_desc = st.text_area("Task Description")
if st.button("Add Task"):
    if task_title:
        st.session_state['tasks'].append({'title': task_title, 'desc': task_desc})
        st.success(f"Task '{task_title}' added!")
    else:
        st.warning("Task title is required.")

st.subheader("Your Tasks")
if st.session_state['tasks']:
    for i, task in enumerate(st.session_state['tasks']):
        st.markdown(f"**{task['title']}**\n{task['desc']}")
        if st.button(f"Delete Task {i+1}"):
            st.session_state['tasks'].pop(i)
            st.experimental_rerun()
else:
    st.info("No tasks added yet.")
