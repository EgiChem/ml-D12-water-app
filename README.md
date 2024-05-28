# ml-D12-water-app

Prediction of binary diffusivities at infinite dilution of any solute in water at atmospheric pressure.

For more information see our paper: [Aniceto et al., 2024, Journal of Molecular Liquids](https://doi.org/10.1016/j.molliq.2024.125009)

## Available models

The models in the Table below are ranked from better performance to worse. The AARD achieved by the models in the test set ranges from 3.92 to 5.48 %.

| Model            | Input parameters required                                                                    |
|------------------|----------------------------------------------------------------------------------------------|
| `ML-T-RDKit`     | temperature and solute identifier (SMILES)                                                   |
| `ML-T-Mordred`   | temperature and solute identifier (SMILES)                                                   |
| `ML-PropRD4it-4` | temperature, solvent viscosoty, solute critical volume, molar refractivity (MolMR, see note) |
| `ML-T-ECFP6`     | temperature and solute identifier (SMILES)                                                   |
| `ML-Prop-4`      | temperature, solvent viscosoty, solute critical volume, solute Lenard-Jones diameter         |
| `ML-T-MACCS`     | temperature and solute identifier (SMILES)                                                   |

Note: the molar refractivity parameter (MolMR) can be computed from a molecular identifier (SMILES).


## Installation

1. Download this repository by clicking `Code` > `Download ZIP`. Unzip the folder.

2. Install Python. We recommend a installing the [Anaconda Distribution](https://www.anaconda.com/download) or [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html).

3. Open the Anaconda Prompt and change the directory to where you extracted the repository files: `cd path/to/folder`.

3. Create a `conda` virtual environment using the provided `environment.yml` file: `conda env create -f environment.yml`

4. Activate the environment with: `conda activate ml-water`.

5. You can now use the models following instructions bellow either in a `.py` script file or in a Jupyter Notebook (already provided in the environment by running `jupyter lab`).


## Usage

To use the `ML-Prop-4` model:

```python
from ml_D12_water import ML_Prop_4

model = ML_Prop_4()

model.predict(temp=313, visc=0.6548, crit_vol=93.9, diam_lj=3.26)
# Output: array([2.77346518e-05])
```

To use the `ML-T-RDKit` model for two conditions/solutes:

```python
from ml_D12_water import ML_T_RDKit

model = ML_T_RDKit()

model.predict(
    temp=[313, 303.2], 
    smiles=['C(=O)=O', 'O=CC1=CC=C(O)C(OC)=C1']  # CO2 and vanilin
)
# Output: array([2.81059139e-05, 1.01639130e-05])
```

The outputed D12 values are in cm2/s.

More usage examples are provided in the [`examples.ipynb`](examples.ipynb) file.


## Citing

If these models are useful to you, please cite the following publication:

[J.P.S. Aniceto, B. Zêzere, and C.M. Silva, Prediction of diffusion coefficients in aqueous systems by machine learning models, Journal of Molecular Liquids, 405, 125009, 2024, DOI: 10.1016/j.molliq.2024.125009.](https://doi.org/10.1016/j.molliq.2024.125009)
