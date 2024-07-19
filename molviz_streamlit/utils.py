import requests
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
import py3Dmol
from rdkit.Chem import AllChem
import plotly.graph_objs as go
from src.molviz.mol_reader.mol_reader import smilesToMol



# Function to create a blank canvas and paste molecule image onto it
def create_canvas_with_molecule(molecule_image, canvas_size=(150, 150)):
    canvas = Image.new('RGB', canvas_size, (255, 255, 255))  # Create a white canvas
    if molecule_image:
        molecule_size = molecule_image.size
        # Calculate position to paste the molecule image at the center of the canvas
        position = ((canvas_size[0] - molecule_size[0]) // 2, (canvas_size[1] - molecule_size[1]) // 2)
        canvas.paste(molecule_image, position)
    return canvas

def smileToMolecule3D(smiles):
    mol = smilesToMol(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)
    conf = mol.GetConformer()
    
    atoms = [atom.GetSymbol() for atom in mol.GetAtoms()]
    x = [conf.GetAtomPosition(i).x for i in range(mol.GetNumAtoms())]
    y = [conf.GetAtomPosition(i).y for i in range(mol.GetNumAtoms())]
    z = [conf.GetAtomPosition(i).z for i in range(mol.GetNumAtoms())]
    
    trace = go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=10, color='red', opacity=0.8),
        text=atoms
    )
    
    bonds = []
    for bond in mol.GetBonds():
        i = bond.GetBeginAtomIdx()
        j = bond.GetEndAtomIdx()
        bonds.append(go.Scatter3d(
            x=[x[i], x[j], None],
            y=[y[i], y[j], None],
            z=[z[i], z[j], None],
            mode='lines',
            line=dict(color='black', width=2)
        ))
    
    return trace, bonds

def molblockToPymol3D(molblock):
    xyzview = py3Dmol.view(width=400,height=400)#(width=400,height=400)
    xyzview.addModel(molblock,'mol')
    xyzview.setStyle({'stick':{}})
    xyzview.setBackgroundColor('black')
    xyzview.zoomTo()
    return xyzview

def MolFromChembl(chembl_id:str):
    url = f'https://www.ebi.ac.uk/chembl/api/data/molecule/{chembl_id}.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['molecule_structures']['canonical_smiles']
    else:
        return None
