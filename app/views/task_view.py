import streamlit as st
from models.task_model import Task
from controllers.task_controller import create_task, get_tasks, delete_task
from models.database import get_db

def task_view():
    st.title("Task Manager")
    
  
    with st.form("new_task_form"):
        st.header("Add New Task")
        title = st.text_input("Title")
        description = st.text_area("Description")
        submitted = st.form_submit_button("Add Task")
        
        if submitted:
            if title:
                create_task(title, description)
                st.success("Task created successfully!")
                
            else:
                st.error("Please enter a title")
    
  
    st.header("Tasks List")
    
  
    with get_db() as db:
        tasks = db.query(Task).order_by(Task.id.desc()).all()
        
        task_data = [{
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'created_at': task.created_at,
            'updated_at': task.updated_at
        } for task in tasks]
    

    for task in task_data:
        with st.expander(f"{task['title']} - {task['status']}"):
            st.write("Description:", task['description'])
            if task['created_at']:
                st.write("Created:", task['created_at'])
            if task['updated_at']:
                st.write("Last updated:", task['updated_at'])
            
       
            new_status = st.selectbox(
                "Status",
                ['pending', 'in_progress', 'done'],
                index=['pending', 'in_progress', 'done'].index(task['status']),
                key=f"status_{task['id']}"
            )
            
            if new_status != task['status']:
                with get_db() as db:
                    task_obj = db.query(Task).filter(Task.id == task['id']).first()
                    if task_obj:
                        task_obj.status = new_status
                
            
            if st.button("Delete Task", key=f"delete_{task['id']}"):
                delete_task(task['id'])
                st.success("Task deleted!")
                