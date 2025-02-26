# Predict schizophrenia using brain anatomy

We aim to predict schizophrenia based on brain grey matter (GM). Schizophrenia is linked to a widespread and intricate pattern of brain atrophy. Our objective is to develop a model that can distinguish between individuals with schizophrenia and healthy controls using GM measurements. This project was conducted as part of an exam assignment for Professor Edouard Duchesnay’s Machine Learning course in the MoSEF Data Science program at Paris 1 Panthéon-Sorbonne.

## Dataset

There are 410 samples in the training set and 103 samples in the test set.

### Input data

Voxel-based_morphometry [VBM](https://en.wikipedia.org/wiki/Voxel-based_morphometry)
using [cat12](http://www.neuro.uni-jena.de/cat/) software which provides:

- Regions Of Interest (`rois`) of Grey Matter (GM) scaled for the Total
  Intracranial Volume (TIV): `[train|test]_rois.csv` 284 features.

- VBM GM 3D maps or images (`vbm3d`) of [voxels](https://en.wikipedia.org/wiki/Voxel) in the
  [MNI](https://en.wikipedia.org/wiki/Talairach_coordinates) space:
  `[train|test]_vbm.npz` contains 3D images of shapes (121, 145, 121).
  This npz contains the 3D mask and the affine transformation to MNI
  referential. Masking the brain provide *flat* 331 695 input features (voxels)
  for each participant.


## Installation

This starting kit requires Python and the following dependencies:

* `numpy`
* `scipy`
* `pandas`
* `scikit-learn`
* `matplolib`
* `seaborn`
* `jupyter`
* `ramp-workflow`


To run a submission and the notebook you will need the dependencies listed in requirements.txt.
You can install the dependencies with the following command-line:

```
pip install -U -r requirements.txt
```



## Getting started

1. download the data locally:

```
python download_data.py
```

2. Execute the jupyter notebook, from the root directory using:

```
jupyter notebook notebook_final.ipynb
```


3. Submission (Run locally)


Run locally:

```
ramp-test --submissions my_submission


```

