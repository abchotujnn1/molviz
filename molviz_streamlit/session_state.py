import streamlit as st

def session_state_variables():
    if 'smile' not in st.session_state: 
        st.session_state.smile = None
    if 'chembl_id' not in st.session_state:
        st.session_state.chembl_id = None