
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from stmol import showmol

from molviz_streamlit.utils import create_canvas_with_molecule, smileToMolecule3D, molblockToPymol3D
from src.molviz.mol_reader.mol_reader import smilesToImage, smilesToBlock

st.set_page_config(layout='wide')
st.title("visualize Molecule")


if 'smile' not in st.session_state:
    st.error("enter valid smile to visualize")
    st.stop()
else:
    if not st.session_state.smile: # None
        st.error("enter valid smile to visualize")
        st.stop()
    smile = st.session_state.smile

MODE = ['2D', 'py3dmol', '3d']

col1, col2 = st.columns(2)
with col1:
    st.text("Mol Graph visualization")
    visualization_mode = st.radio(label='Select mode of visualization',
         options=MODE,
         horizontal=True)
    if visualization_mode == MODE[0]:
        molecule_image = smilesToImage(smile)
        if molecule_image:
            canvas = create_canvas_with_molecule(molecule_image)
            st.image(canvas, caption=smile)
        else:
            st.error("Invalid SMILES string")
    elif visualization_mode == MODE[1]:
        molblock = smilesToBlock(smile)
        pymol3d_viewer = molblockToPymol3D(molblock)
        showmol(pymol3d_viewer,height=400,width=400)
    elif visualization_mode == MODE[2]:
        trace, bonds = smileToMolecule3D(smile)
        if trace:
            fig = go.Figure(data=[trace] + bonds)
            fig.update_layout(scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z'
            ))
            st.plotly_chart(fig)
    else:
        st.error("Invalid SMILES string")

    if st.session_state.chembl_id:
        st.markdown( body=f'https://www.ebi.ac.uk/chembl/compound_report_card/{st.session_state.chembl_id}/', 
                    unsafe_allow_html=True)
with col2:
    st.text("Mol Properties visualization")
    data = pd.DataFrame({"molecule properties name":["molecular weight", 
                                                     "total no of atoms", 
                                                     "no of heavy atoms", 
                                                     "no of rings", 
                                                     "no of benzene ring"],
                        "Values":[50,
                                  9,
                                  4,
                                  2,
                                  1]})
    st.table(data)
   