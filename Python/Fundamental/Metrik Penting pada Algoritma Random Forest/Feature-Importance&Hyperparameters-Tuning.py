#--- Menggunakan Feature Importance ---
#Kode sebelumnya
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
dataset_credit_scoring = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/credit_scoring_dqlab.xlsx')
dataset_credit_scoring['kpr_aktif'].replace(['YA', 'TIDAK'], [1, 0], inplace=True)
dataset_credit_scoring['rata_rata_overdue'].replace({'0 - 30 days':1, '31 - 45 days':2, '46 - 60 days':3, '61 - 90 days':4, '> 90 days':5}, inplace=True)
X = dataset_credit_scoring.drop(columns=['kode_kontrak', 'risk_rating', 'rata_rata_overdue']).values
y = dataset_credit_scoring['risk_rating'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
rfc = RandomForestClassifier(criterion='entropy', random_state=42)
model = rfc.fit(X_train, y_train)
#mendapatkan importance
importance = model.feature_importances_
#nama feature
feature_names = dataset_credit_scoring.drop(columns=['kode_kontrak', 'risk_rating', 'rata_rata_overdue']).columns
#summarize feature importance
for f, fi in zip(feature_names, importance):
	print('Feature: %24s, Score: %.5f' % (f, fi))

#--- Visualisasi Feature Importance dengan Bar Chart ---
#Kode sebelumnya
#Buat data frame agar lebih mudah dalam pengurutan
fi_df = pd.DataFrame({'Feature': feature_names, 'Score': importance}).sort_values('Score')
#import matplotlib dan plot fi_df
import matplotlib.pyplot as plt
barh = plt.barh(fi_df['Feature'], fi_df['Score'])
plt.bar_label(barh, fmt='%.5f', padding=5, c='red')
plt.title('Feature Importance')
plt.xlabel('Score')
plt.xlim([0, 0.5])
plt.grid(axis='x')
plt.tight_layout()
plt.show()

#--- Menghilangkan Kolom durasi_pinjaman_bulan ---
#Kode sebelumnya
#Feature matrix X1
X1 = dataset_credit_scoring.drop(columns=['kode_kontrak', 'risk_rating', 'rata_rata_overdue', 'durasi_pinjaman_bulan']).values
#membagi data training dan data testing, dimana training 70% dan testing 30%
X_train, X_test, y_train, y_test = train_test_split(X1, y, test_size=0.3, random_state=0)
#menampilkan jumlah data train dan test
print('Ukuran X_train:', X_train.shape)
print('Ukuran X_test :', X_test.shape)
print('Ukuran y_train:', y_train.shape)
print('Ukuran y_test :', y_test.shape)

#--- Melakukan Pemodelan Ulang ---
#Kode sebelumnya
#Melakukan pemodelan ulang dengan Random Forest
rfc = RandomForestClassifier(criterion='entropy', random_state=42)
model = rfc.fit(X_train, y_train)
# Melihat hyperparameters yang tersedia
from pprint import pprint
print('Hyperparameters yang sedang digunakan:')
pprint(rfc.get_params())
#--- Hyperparameter untuk RandomizedGridCV ---
import numpy as np
from pprint import pprint
#jumlah pohon pada random forest
n_estimators = list(np.linspace(200, 2000, num=100, dtype=np.int32))
#jumlah fitur yang dipertimbangkan untuk setiap pemisahan (split)
max_features = ['auto', 'sqrt']
#jumlah maksimum level pada setiap pohon
max_depth = list(np.linspace(10, 110, num=11, dtype=np.int32))
max_depth.append(None)
#jumlah minimum sample yang dibutuhkan untuk memisahkan node
min_samples_split = [2, 5, 10]
#jumlah minimum sample yang dibutuhkan untuk setiap leaf node
min_samples_leaf = [1, 2, 4]
#metode untuk memilih sampel untuk training setiap pohon
bootstrap = [True, False]
#membuat random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
pprint(random_grid)

#--- Random Forest dengan RandomizedGridCV ---
#Kode sebelumnya
#Random Forest
rfc = RandomForestClassifier(criterion='entropy', random_state=42)
#Import RandomizedSearchCV
from sklearn.model_selection import RandomizedSearchCV
#Menggunakan random grid untuk mencari hyperparameters terbaik 
rf_random = RandomizedSearchCV(estimator=rfc, param_distributions=random_grid, n_iter=10, cv=3, verbose=2, random_state=0)
#Fit the random search model
rf_random.fit(X_train, y_train)
#Tampilkan parameter terbaik
print('\nParameter terbaik:')
pprint(rf_random.best_params_)

#--- Base Model vs Best Model ---
#Kode sebelumnya
#Fungsi untuk mengevaluasi model berdasarkan data testing
def evaluate(model, X_test, y_test):
    predictions = model.predict(X_test)
    errors = abs(predictions - y_test)
    mape = 100 * np.mean(errors / y_test)
    accuracy = 100 - mape
    print('Model Performance')
    print('Average Error: %.4f degrees.' % (np.mean(errors),))
    print('Accuracy = %.2f%%.' % (accuracy,))
#Base Model
base_model = rfc.fit(X_train, y_train)
print('Base Model:')
print('-----------')
evaluate(base_model, X_test, y_test)
#Best Model
best_model = rf_random.best_estimator_
print('\n\nBest Model:')
print('-----------')
evaluate(best_model, X_test, y_test)
