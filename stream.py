import streamlit as st
from notebook import Notebook

if "notebook" not in st.session_state:
    st.session_state.notebook = Notebook()

st.title("Notes App")

st.subheader("Add a Note")
title = st.text_input("Title")
content = st.text_area("Content")

if st.button("Add Note"):
    if title and content:
        st.session_state.notebook.add_note(title, content)
        st.success(f"{title} added successfully!")

st.subheader("Search Notes")
search_title = st.text_input("Enter title to search")

if st.button("Search"):
    if search_title:
        result = st.session_state.notebook.get_note(search_title)
        if result != "Note not found":
            st.write(f"**{search_title}**: {result}")
        else:
            st.warning("Note not found.")

st.subheader("Your Notes")
for title, content in st.session_state.notebook.get_notes().items():
    st.write(f"**{title}**: {content}")