import pandas as pd
import joblib


class ML_Prop_4:
    MODEL = 'ML-Prop-4'

    def __init__(self):
        self.data = None
        self.model_pipeline = joblib.load(f'models/{ML_Prop_4.MODEL}-pipeline.mod')
    
    def predict(self, temp=None, visc=None, crit_vol=None, diam_lj=None):
        data_dict = {
            'T': temp,
            'visc': visc,
            'Vc': crit_vol,
            'dLJ': diam_lj,
        }
        self.data_df = pd.DataFrame.from_dict(data_dict)
        return self.model_pipeline.predict(self.data_df)
    

class ML_PropRDKit_4:
    MODEL = 'ML-PropRDKit-4'

    def __init__(self):
        self.model_pipeline = joblib.load(f'models/{ML_PropRDKit_4.MODEL}-pipeline.mod')

    def _get_RDKit_descriptors(self):
        from rdkit import Chem
        from descriptastorus.descriptors.DescriptorGenerator import MakeGenerator

        # Add RDKit mol objects
        self.data_df['mol'] = [Chem.MolFromSmiles(smi) for smi in self.data_df['canonical_smiles'].to_list()]

        # Compute descriptors
        generator = MakeGenerator(('RDKit2D',))
        rdkit2d = [generator.process(x)[1:] for x in self.data_df['canonical_smiles']]
        rdkit2d_name = []
        for name, numpy_type in generator.GetColumns():
            rdkit2d_name.append(name)
        df_rdkit2d = pd.DataFrame(rdkit2d, index=self.data_df.canonical_smiles, columns=rdkit2d_name[1:])

        # Merge descriptors with the main df
        df_rdkit2d = df_rdkit2d.reset_index()
        df_all_rdkit2d = self.data_df.merge(df_rdkit2d, on='canonical_smiles')

        return df_all_rdkit2d[['T', 'visc', 'Vc', 'MolMR']]

    def predict(self, temp=None, visc=None, crit_vol=None, smiles=None):
        data_dict = {
            'T': temp,
            'visc': visc,
            'Vc': crit_vol,
            'canonical_smiles': smiles,
        }
        self.data_df = pd.DataFrame.from_dict(data_dict)
        data_descriptors_df = self._get_RDKit_descriptors()
        return self.model_pipeline.predict(data_descriptors_df)


class ML_T_RDKit:
    MODEL = 'ML-T-RDKit'

    def __init__(self):
        self.data = None
        self.model_pipeline = joblib.load(f'models/{ML_T_RDKit.MODEL}-pipeline.mod')

    def _get_RDKit_descriptors(self):
        from rdkit import Chem
        from descriptastorus.descriptors.DescriptorGenerator import MakeGenerator

        # Add RDKit mol objects
        self.data_df['mol'] = [Chem.MolFromSmiles(smi) for smi in self.data_df['canonical_smiles'].to_list()]

        # Compute descriptors
        generator = MakeGenerator(('RDKit2D',))
        rdkit2d = [generator.process(x)[1:] for x in self.data_df['canonical_smiles']]
        rdkit2d_name = []
        for name, numpy_type in generator.GetColumns():
            rdkit2d_name.append(name)
        df_rdkit2d = pd.DataFrame(rdkit2d, index=self.data_df.canonical_smiles, columns=rdkit2d_name[1:])

        # Merge descriptors with the main df
        df_rdkit2d = df_rdkit2d.reset_index()
        df_all_rdkit2d = self.data_df.merge(df_rdkit2d, on='canonical_smiles')

        # Remove irrelevant columns
        df_all_rdkit2d = df_all_rdkit2d.drop(columns=['canonical_smiles', 'mol'])
        df_all_rdkit2d = df_all_rdkit2d.drop(columns=['MaxAbsPartialCharge', 'MaxPartialCharge', 'MinAbsPartialCharge', 'MinPartialCharge'])

        return df_all_rdkit2d

    def predict(self, temp=None, smiles=None):
        data_dict = {
            'T': temp,
            'canonical_smiles': smiles,
        }
        self.data_df = pd.DataFrame.from_dict(data_dict)
        data_descriptors_df = self._get_RDKit_descriptors()
        return self.model_pipeline.predict(data_descriptors_df)
