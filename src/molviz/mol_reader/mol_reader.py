import rdkit
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem


def smilesToMol(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return mol

# Function to render molecule from SMILES and get the image
def smilesToImage(smiles):
    mol = smilesToMol(smiles)
    if mol:
        img = Draw.MolToImage(mol, size=(100, 100))
        return img
    return None

def smilesToBlock(smiles):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    mblock = Chem.MolToMolBlock(mol)
    return mblock