# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:35:12 2016

@author: MOHAMED.RABDELAAL
"""

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[1])
print(iris.target[1])
