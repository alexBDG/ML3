import sys
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from skorch import * 
from sklearn.model_selection import GridSearchCV
import modules

train_images = pd.read_pickle('input/new_train_images.pkl')
train_labels = pd.read_csv('input/train_labels.csv')


train_images2 = train_images.reshape(len(train_images), 1,  51, 51)
train_labels2 = np.zeros(len(train_labels), dtype=int)
for i in range(len(train_labels)):
  train_labels2[i] = train_labels.iloc[i]['Category']

train_images3 = torch.tensor(train_images2)
train_labels3 = torch.tensor(train_labels2)
net = NeuralNetClassifier(
        modules.Net_3,
        criterion = torch.nn.CrossEntropyLoss,
        max_epochs=10,
        lr=1e-2,
        iterator_train__shuffle=True,
        )
net.fit(train_images2, train_labels2)
params = {
          'lr': [1e-2, 1e-4, 1e-6],
          'max_epochs': [10, 20]}
#gs = GridSearchCV(net, params, refit=False, cv=3, scoring='accuracy')
#gs.fit(train_images, train_labels2)
#print(gs.best_score_, gs.best_params_)
