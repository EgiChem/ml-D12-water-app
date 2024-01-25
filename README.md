# ml-D12-water-app

Prediction of binary diffusivities at infinite dilution of any solute in water at atmospheric pressure.

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

Create a `conda` virtual environment using the provided `environment.yml` file:

```
$ conda env create -f environment.yml
$ conda activate ml-water
```


## Usage

To use the `ML-T-RDKit`:

```python
from ml_D12_water import ML_Prop_4

model = ML_Prop_4()

model.predict(temp=313, visc=0.6548, crit_vol=93.9, diam_lj=3.26)
# Output: array([2.77346518e-05])
```

More usage examples are provided in the [`examples.ipynb`](examples.ipynb) file.

