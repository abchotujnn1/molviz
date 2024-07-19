import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
import plotly.graph_objs as go

import sys
import os
from PIL import Image
from streamlit_ketcher import st_ketcher
sys.path.insert(0, os.path.join('..'))
from molviz_streamlit.utils import MolFromChembl
from molviz_streamlit.session_state import session_state_variables

session_state_variables()
st.set_page_config(layout='wide')
st.title("MolViz: Molecule image and Properties visualization")

SMILE  = ['Enter Molecule', 'Chembl ID', 'Draw']

st.image(r"C:\Users\YUI2KOR\BOSCH\KNOWLEDGE\MOLVIZ\molviz\docs\molecule_viz.png")
# st.image(os.path.join('doc', 'molecule_viz.png'))

expander = st.sidebar.expander('Enter Smile')
with st.sidebar:
    smile_enter_mode = expander.radio(label="Select mode for Smile",
                   options=SMILE,
                   )

if smile_enter_mode == SMILE[0]:
    smile = expander.text_input("Smile", placeholder="cccccc")
elif smile_enter_mode == SMILE[1]:
    chembl_id = expander.text_input("chembl_id", placeholder='CHEMBL4803817')
    smile = MolFromChembl(chembl_id)
    st.session_state.chembl_id = chembl_id
elif smile_enter_mode == SMILE[2]:
    smile = st_ketcher()

if not st.session_state.smile:
    st.session_state.smile = smile

st.write(smile)
