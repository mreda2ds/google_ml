# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:00:40 2016

@author: MOHAMED.RABDELAAL
"""

from sklearn import tree
features = [[140,0],[130,0],[150,1],[170,1]]
labels = ["Orange","Orange","Apple","Apple"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print (clf.predict([[180,1]]))#enter values to check