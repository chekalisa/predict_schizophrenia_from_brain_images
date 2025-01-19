from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import StackingClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif, VarianceThreshold
from sklearn.pipeline import Pipeline

class ROIsFeatureExtractor(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[:, :284]



def get_estimator():
    
    base_models = [
        ('gb', GradientBoostingClassifier(
            learning_rate=0.01, 
            max_depth=3,  
            min_samples_split=2, 
            n_estimators=100,  
            subsample=0.8,
            random_state=42
        )),
        ('svc', SVC(
            probability=True, 
            random_state=42, 
            C=1,   
            gamma='auto',  
            kernel='rbf'
        ))
       ]


    stacking_clf = StackingClassifier(
        estimators=base_models,
        final_estimator=LogisticRegression(max_iter=5000),  
        cv=3,  
        n_jobs=-1  
    )


    estimator = Pipeline([
            ('scaler', StandardScaler()),
            ('remove_constant', VarianceThreshold(threshold=0.01)),  # excude constants
            ('feature_selection', SelectKBest(score_func=f_classif, k=150)), # select 150 variables 
            ('stacking', stacking_clf)  
        ])



    return estimator

