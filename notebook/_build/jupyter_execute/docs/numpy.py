#!/usr/bin/env python
# coding: utf-8

# (numpy)=
# 
# # NumPy
# 
# > \"Let\'s be clear: the work of science has nothing whatever to do with
# > consensus. Consensus is the business of politics. Science, on the
# > contrary, requires only one investigator who happens to be right,
# > which means that he or she has results that are verifiable by
# > reference to the real world. In science consensus is irrelevant. What
# > is relevant is reproducible results.\" -- Michael Crichton
# 
# ## Overview
# 
# [NumPy](https://en.wikipedia.org/wiki/NumPy) is a first-rate library for
# numerical programming
# 
# -   Widely used in academia, finance and industry.
# -   Mature, fast, stable and under continuous development.
# 
# We have already seen some code involving NumPy in the preceding
# lectures.
# 
# In this lecture, we will start a more systematic discussion of both
# 
# -   NumPy arrays and
# -   the fundamental array processing operations provided by NumPy.
# 
# ### References
# 
# -   [The official NumPy documentation](http://docs.scipy.org/doc/numpy/reference/).
# 
# (numpy_array)=
# 
# ## NumPy Arrays
# 
# The essential problem that NumPy solves is fast array processing.
# 
# The most important structure that NumPy defines is an array data type
# formally called a
# [numpy.ndarray](http://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html).
# 
# NumPy arrays power a large proportion of the scientific Python
# ecosystem.
# 
# Let\'s first import the library.

# In[1]:


import numpy as np


# To create a NumPy array containing only zeros we use
# [np.zeros](http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html#numpy.zeros)

# In[2]:


a = np.zeros(5)
a


# format: jb-book
# root: docs/index
# parts:
#   - caption: Introduction to Python
#     numbered: true
#     chapters:
#     - file: docs/about_py
#     - file: docs/getting_started
#       sections:
#       - file: docs/numpy
#   - caption: Introduction to ML
#     numbered: true
#     chapters:
#     - file: docs/python_by_example
#     - file: docs/learn_more
#       sections:
#       - file: docs/pandas
#   - caption: Exploratory Data Analysis
#     numbered: true
#     chapters:
#     - file: docs/Exploratory_Data_Analysis
# 
#  - caption: Feature Engineering and Selection
#     numbered: true
#     chapters:
#     - file: docs/Feature_Engineering_and_Selection
# 
#   - caption: Model Selection
#     numbered: true
#     chapters:
#     - file: docs/Model_Selection
#     - file: docs/Automatic_Machine_Learning
#       sections:
#       - file: docs/Model_Performance_Metrics
# 
# - caption: Machine Learning for Imbalanced Data
#     numbered: true
#     chapters:
#     - file: docs/Machine_Learning_for_Imbalanced_Data
# 
#  - caption: Big Data Processing
#     numbered: true
#     chapters:
#     - file: docs/Big_Data_Processing
# 
#  - caption: Unsupervised Machine Learning
#     numbered: true
#     chapters:
#     - file: docs/AnomalyDetection
# 
# - caption: Time Series Analysis
#     numbered: true
#     chapters:
#     - file: docs/Time_Series_Analysis
# 
# - caption: Time to Event Models
#     numbered: true
#     chapters:
#     - file: docs/Survival_Analysis
# 
# - caption: Time to Event Models
#     numbered: true
#     chapters:
#     - file: docs/Survival_Analysis
# 
# 
# - caption: Machine Learning for Imbalanced Data
#     numbered: true
#     chapters:
#     - file: docs/Machine_Learning_for_Imbalanced_Data
# 
# - caption: Deep_Learning
#     numbered: true
#     chapters:
#     - file: docs/Deep_Learning_for_Structured_Data
#     - file: docs/Computer_Vision
#     - file: docs/Natural_Language_Processing
# 
# - caption: Machine Learning Operations.
#     numbered: true
#     chapters:
#     - file: docs/Machine_Learning_Operations
#     - file: docs/Model_Deployment
#     - file: docs/Data_Validation_and_Monitoring
# 
# - caption: Machine Learning Interpretability
#     numbered: true
#     chapters:
#     - file: docs/Machine_Learning_Interpretability
#     - file: docs/CausalInference
