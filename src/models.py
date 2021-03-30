import lightgbm as lgb
import pickle
import sklearn.linear_model
import tensorflow as tf

#################### Logistic regression ####################

def build_logreg():
    '''
    Scikit-Learn model for logistic regression
    Reference: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    '''
    m = sklearn.linear_model.LogisticRegression(
        solver='lbfgs', penalty='l2', tol=1e-4, C=1, max_iter=100, class_weight='balanced')
    return m

def fit_logreg(m, xtrain, ytrain):
    m.fit(xtrain, ytrain)


#################### Boosting with LightGBM ####################

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
    
def fit_gbdt(m, xtrain, ytrain, xval, yval, verbose=100):
    m.fit(xtrain, ytrain, eval_set=(xval, yval), eval_metric='auc', verbose=verbose)


#################### Saving and loading as pickle, for the two above model types (not NNs) ####################

def load_pickle(filename):
    m = None
    with open(filename, 'rb') as file:
        m = pickle.load(file)
    return m

def save_pickle(m, name):
    with open(name, 'wb') as file:
        pickle.dump(m, file)

#################### Neural nets! ####################

def build_NN_lrelu():
    raise NotImplementedError("todo")

def build_NN_selu(input_len):
    '''
    Second neural net architecture used by the authors. References:
    General models in Keras https://keras.io/guides/sequential_model/
    selu and lecun normalization (Keras API) https://keras.io/api/layers/activations/
    selu example from the original selu authors https://github.com/bioinf-jku/SNNs/blob/master/TF_2_x/MNIST-MLP-SELU.py
    AlphaDropout https://keras.io/api/layers/regularization_layers/alpha_dropout/
    '''
    N_NODES = input_len
    ALPHA_DROPOUT = 0.15
    ADAM_LR = 0.001

    # Input
    selu_in = tf.keras.layers.Input(shape=(N_NODES,))
    # Hidden 1
    x = tf.keras.layers.Dense(N_NODES, kernel_initializer='lecun_normal', activation='selu', name='selu1')(selu_in)
    x = tf.keras.layers.AlphaDropout(ALPHA_DROPOUT)(x)
    # Hidden 2
    x = tf.keras.layers.Dense(N_NODES, kernel_initializer='lecun_normal', activation='selu', name='selu2')(x)
    x = tf.keras.layers.AlphaDropout(ALPHA_DROPOUT)(x)
    # Hidden 3
    x = tf.keras.layers.Dense(N_NODES, kernel_initializer='lecun_normal', activation='selu', name='selu3')(x)
    x = tf.keras.layers.AlphaDropout(ALPHA_DROPOUT)(x)
    # Hidden 4
    x = tf.keras.layers.Dense(N_NODES, kernel_initializer='lecun_normal', activation='selu', name='selu4')(x)
    x = tf.keras.layers.AlphaDropout(ALPHA_DROPOUT)(x)
    # Output
    selu_out = tf.keras.layers.Dense(1, activation='sigmoid')(x)

    m = tf.keras.Model(inputs=selu_in, outputs=selu_out, name='NN_selu')
    m.compile(
        loss='binary_crossentropy',
        optimizer=tf.keras.optimizers.Adam(learning_rate=ADAM_LR),
        metrics=['Accuracy', 'AUC'],
    )
    # model is now ready for fitting!
    return m

def fit_NN_lrelu(m, xtrain, ytrain, xval, yval):
    # Gotta figure out batch size and epochs. ?????
    raise NotImplementedError('todo')

def fit_NN_selu(m, xtrain, ytrain, xval, yval):
    return fit_NN(m, xtrain, ytrain, xval, yval, batch_size=256, epochs=10)

def fit_NN(m, xtrain, ytrain, xval, yval, batch_size, epochs):
    '''
    Reference: https://keras.io/guides/training_with_built_in_methods/
    '''
    history = m.fit(
        xtrain,
        ytrain,
        batch_size=batch_size,
        epochs=epochs,
        validation_data=(xval, yval),  # Monitor our metrics after each epoch, just 'cause
    )
    return history

def save_NN(m, name):
    m.save(name)

def load_NN(filename):
    return tf.keras.models.load_model(filename)