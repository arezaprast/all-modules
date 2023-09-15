# ---  Import library yang dibutuhkan  ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pickle
from pathlib import Path

# ---  File Unloading  ---
import pandas as pd
df_load = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlab_telco_final.csv")
# Tampilkan bentuk dari dataset
print(df_load.shape)
# Tampilkan 5 data teratas
print(df_load.head())
# Tampilkan jumlah ID yang unik
print(df_load.customerID.nunique())
