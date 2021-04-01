import numpy as np
import pandas as pd

def load_preg_data_final(datafile, path='data/final/'):
    '''
    The function below only works on our simulated data.
    This one was rewritten to work with our real, preprocessed data.
    '''
    assert datafile in ['stillbirth', 'preterm']
    # List of three pandas data frames
    data = []
    for setname in  ['train', 'test', 'val']:
        print(f'Loading {setname} data for {datafile}...')
        data.append(pd.read_csv(f'{path}{datafile}_{setname}.csv'))
        print('\tdone.')
    # Separate into predictor variables (x) and labels (y)
    xtrain, xtest, xval = data[0].drop(columns=['outcome']), data[1].drop(columns=['outcome']), data[2].drop(columns=['outcome'])
    ytrain, ytest, yval = data[0]['outcome'], data[1]['outcome'], data[2]['outcome']
    # Done!
    return xtrain, ytrain, xtest, ytest, xval, yval

def outcome_to_binary(y, outcome):
    assert outcome in ['early stillbirth', 'late stillbirth', 'preterm']
    return (y == outcome).to_numpy().astype(np.int)

# N.B. THESE FUNCTIONS ARE OLD / DESIGNED FOR THE SIMULATION DATA

def load_preg_data(sim=True, onehots=True):
    # Assumes that we're in the top-level working directory
    if sim:
        path = 'data/sim/'
    else:
        path = 'data/cdc/'
        raise NotImplementedError('No unsimulated data yet')        
    # Load from CSVs
    data = [pd.read_csv(f'{path}{file}.csv') for file in ['train', 'test', 'val']]
    # Separate and format the data
    X = []
    Y = []
    for df in data:
        # Separate into predictor variables (x) and labels (y)
        y = df['outcome']
        x = df.drop(columns=['outcome', 'g.weeks', 'id'])
        # Keep race and education as either one-hot or ordinal/categorical
        if onehots:
            x = x.drop(columns=['race.f', 'education.f'])
        else:
            x = x.drop(columns=[c for c in x.columns if "race_" in c or "education_" in c])
        X.append(x)
        Y.append(y)
    # Done!
    xtrain, xtest, xval = X
    ytrain, ytest, yval = Y
    return xtrain, ytrain, xtest, ytest, xval, yval

def preg_outcome_to_binaries(y):
    early_still = (y == 'early stillbirth').to_numpy().astype(np.int)
    late_still = (y == 'late stillbirth').to_numpy().astype(np.int)
    preterm = (y == 'preterm').to_numpy().astype(np.int)
    return early_still, late_still, preterm

def preg_outcome_to_onehot(y):
    oh = y.str.get_dummies()
    print("Protype one-hot vector for outcome:", oh.columns.values.tolist())
    return oh.values

# Example calls to load data:
# xtrain, ytrain, xtest, ytest, xval, yval = util.load_preg_data(sim=True, onehots=True)
# ytrain_early, ytrain_late, ytrain_preterm = util.preg_outcome_to_binaries(ytrain)
# ytest_early, ytest_late, ytest_preterm = util.preg_outcome_to_binaries(ytest)
# yval_early, yval_late, yval_preterm = util.preg_outcome_to_binaries(yval)