import sys, time, os, json, re,codecs,math, tensorflow as tf, pandas as pd, numpy as np, eli5
import numpy.random,string,warnings
from pandas.core.frame import DataFrame as PD_DataFrame
from ast import literal_eval as make_tuple
from os import listdir
from os.path import isfile, join
from random import shuffle
from collections import Counter
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import shutil
import pyspark.sql.functions as F


import umap
import pyarrow as pa
import pyarrow.parquet as pq
import pathlib,pickle,lime
import lime.lime_tabular
from numpy import nan

from pyspark.sql import SQLContext
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.catalog import Function
from pyspark.sql.window import Window
from pyspark.sql.functions import *
from pyspark.sql import SparkSession, SQLContext, Row
from pyspark.sql import SparkSession, HiveContext, SQLContext, Row
from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf

from pyspark.sql.types import StructType, StructField, DoubleType, IntegerType, StringType, FloatType, LongType, DecimalType
# from pyspark.sql.functions import desc, row_number, monotonically_increasing_id
from pyspark.sql.functions import sum as fsum
from pyspark.ml.feature import VectorAssembler

#from imblearn.over_sampling import SMOTE
#from mlxtend.evaluate import confusion_matrix,scoring

import keras
from keras.wrappers.scikit_learn import KerasClassifier, KerasRegressor
from keras.models import model_from_json, Sequential
from keras.layers import Dense ,Input, Dropout, Flatten, ConvLSTM2D
from keras.utils.np_utils import to_categorical
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam

import sklearn
from sklearn import linear_model,preprocessing,metrics
from sklearn.preprocessing import LabelEncoder, StandardScaler,LabelBinarizer,OneHotEncoder
from sklearn.model_selection import train_test_split,RandomizedSearchCV, KFold,learning_curve, GridSearchCV, StratifiedKFold
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, roc_curve,roc_auc_score, mean_absolute_error, mean_squared_error, r2_score, explained_variance_score,f1_score,auc
from sklearn.utils import resample
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from eli5.sklearn import PermutationImportance
import networkx as nx