import lightgbm as lgb
import sklearn.linear_model

def build_logreg():
    '''
    Scikit-Learn model for logistic regression
    Reference: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    '''
    m = sklearn.linear_model.LogisticRegression(
        solver='lbfgs', penalty='l2', tol=1e-4, C=1, max_iter=100, class_weight='balanced')
    return m

def load_logreg():
    raise NotImplementedError("todo")

def save_logreg():
    raise NotImplementedError("todo")

def build_gbdt():
    '''
    Scikit-Learn model for gradient boosting, with LightGBM backend
    Reference: https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMModel.html
    '''
    m = lgb.LGBMClassifier(
        num_leaves=48, min_child_samples=500, max_depth=-1, learning_rate=0.001, colsample_bytree=1.0, subsample=1.0,
        boosting_type='gbdt', n_estimators=2000, objective='binary', random_state=None, is_unbalance=True)
    # N.b. that "learning rate" and "shrinkage rate" are sometimes interchanged
    # In this case, "colsample_bytree" to the SKLearn api is "feature_fraction", and "subsample" is "bagging_fraction", and "n_estimators" is "num_iterations"
    # See https://lightgbm.readthedocs.io/en/latest/Parameters.html
    # Also n.b. we should double-check that the `is_unbalance` paramater works as expected
    return m
    
def save_logreg():
    raise NotImplementedError("todo")

def load_logreg():
    raise NotImplementedError("todo")