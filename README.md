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

## Brief explanation and results

A stacking approach was implemented, combining the strengths of multiple models. The base models selected were the SVM with an RBF kernel, which effectively identified complex decision boundaries, and the Gradient Boosting model, which captured non-linear dependencies. A logistic regression model was used as the meta-learner, trained on the predictions of the base models to optimally combine their outputs. This ensemble approach improved predictive accuracy by leveraging the complementary strengths of both models.

However, due to the large number of features, training times were excessively long, particularly for the SVM model, which is sensitive to high-dimensional data. To mitigate this, feature selection via SelectKBest was applied, reducing dimensionality while maintaining relevant information. The final model evaluation also included permutation importance analysis to determine the most influential predictors. This method assessed the impact of randomly permuting each feature on model performance, confirming that certain brain regions played a key role in classification.

The final stacked model successfully integrated the best-performing algorithms, improving classification accuracy and robustness while addressing computational efficiency challenges.

----------------------------
Bagged scores
----------------------------
        score   auc  bacc
        valid  0.84  0.75
        test   0.84  0.76

## Authors
- [Alisa Chekalina](https://github.com/chekalisa)
- [Lia Gasparin](https://github.com/LiaGasparin)
- [Carmen Cristea](https://github.com/CarmenParis)
