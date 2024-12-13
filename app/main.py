import streamlit as st
from models.database import init_db
from views.task_view import task_view
from utils.json_handler import export_to_json, import_from_json

def main():
    st.set_page_config(page_title="Task Manager", layout="wide")
    
    st.sidebar.title("Menu")
    option = st.sidebar.selectbox(
        "Select an option",
        ["Tasks Manager", "Export/Import Data"]
    )
    
    if option == "Tasks Manager":
        task_view()
    elif option == "Export/Import Data":
        st.header("Export/Import Tasks")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Export to JSON"):
                export_to_json("tasks.json")
                st.success("Data exported to tasks.json")
        
        with col2:
            if st.button("Import from JSON"):
                import_from_json("tasks.json")
                st.success("Data imported from tasks.json")

if __name__ == "__main__":
    init_db()
    main()