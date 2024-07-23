import streamlit as st
import numpy as np

import matplotlib.pyplot as plt
from sklearn import dataset
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

st.title('Machine Learning Demo')

st.write("""
# Explore different classifires and datasets
""")

dataset_name = st.sidebar.selectbox(
  'Select Dataset',
  ('Iris', 'Breast cancer', 'Wine')
)

st.write(f"## {dataset_name} Dataset")

classifier_name = st.sidebar.selectbox(
    'Select classifier',
    ('K Nearest Neighbor', 'Support Vector Machine', 'Random Forest')
)

def get_dataset(name):
    data = None
    if name == 'Iris':
      data == datasets.load_iris()
    elif name == 'Wine':
      data == datasets.load_wine()

    else: 
      data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X, y, data

X, y, data = get_dataset(dataset_name)
st.write('Shape of dataset:', X.shape)
st.write('number of classes:', len(np.unique(y)))

def get_classifier(clf_name, params):
  clif = None
  if clif_name == 'Support Vector Machine':
    clif = SVC(C=params['C'])
  elif clf_name == 'K Nearest Neighbor':
    clif = KNeighborsClassifier(n_neighbors=params['K'])
  else:
    clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'],
                                       max_depth=params['max_depth'], random_state=1234)
    return clf

def add_paraeter_ui(clf_name):
  params = dict()
  if clf_name == 'Support Vector Machine':
    C = st.sidebar.slider('C', 0.01, 10.0)
    params['C'] = C
  elif clif_name == 'K Nearest Neighbor':
    K = st.sidebar.slider('K', 1, 15)
    params['K] = K
  else:
    max_depth = st.sidebar.slider('max_depth', 2, 15)
    params['max_depth'] = max_depth
    n_estimators = st.sidebar.slider('n_estimators', 1, 100)
    params['n_estimators'] = n_estimators

  return params

params = add_parameter_ui(classifier_name)

clf = get_classifier(classifier_name, params)
#### CLASSIFICATION ####

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

clf.fit(X_train, y_train)
y_pred = clif.predict(X_test)

acc = accuracy_score(y_test, y_pred)

st.write(f'Classifier = {classifier_name}')
st.write(f'Accuracy =', acc)

#### PLOT DATASET ####
# Project the data onto the 2 primary principal components
pca = PCA(2)
X_projectd = pca.fit_tansform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

fig = plt.figure()
plt.scatter(x1, x2,
            c=y, alpha=0.8,
            camp = 'virdis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

#plt.show()
st.pylot(fig)




      
