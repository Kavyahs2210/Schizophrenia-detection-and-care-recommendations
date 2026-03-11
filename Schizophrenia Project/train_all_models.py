import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ------------------- Create models folder -------------------
if not os.path.exists('models'):
    os.makedirs('models')
    logger.info("Created models directory")

# ------------------- Load Dataset -------------------
logger.info("Loading dataset...")
df = pd.read_csv('SchizophreniaData.csv')

# Display dataset info
logger.info(f"Dataset shape: {df.shape}")
logger.info(f"Columns: {df.columns.tolist()}")

# Drop non-predictive columns
if 'Name' in df.columns:
    df.drop('Name', axis=1, inplace=True)

# Handle missing values
logger.info("Handling missing values...")
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

# Encode categorical features
logger.info("Encoding categorical features...")
for col in ['Gender', 'Marital_Status']:
    if col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

# Encode target
le_target = LabelEncoder()
df['Schizophrenia'] = le_target.fit_transform(df['Schizophrenia'])
num_classes = len(df['Schizophrenia'].unique())
logger.info(f"Number of classes: {num_classes}")
logger.info(f"Class distribution:\n{df['Schizophrenia'].value_counts()}")

# ------------------- Split Features & Target -------------------
X = df.drop('Schizophrenia', axis=1).values
y = df['Schizophrenia'].values

logger.info(f"Feature shape: {X.shape}")
logger.info(f"Target shape: {y.shape}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

logger.info(f"Training set size: {X_train.shape[0]}")
logger.info(f"Test set size: {X_test.shape[0]}")

# ------------------- Scale Features -------------------
logger.info("Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Save scaler
pickle.dump(scaler, open('models/scaler.pkl', 'wb'))
logger.info("✓ Scaler saved")

# ------------------- Neural Network -------------------
logger.info("\n" + "="*50)
logger.info("Training Neural Network...")
logger.info("="*50)

if num_classes > 2:
    y_train_cat = to_categorical(y_train)
    y_test_cat = to_categorical(y_test)
    activation_last = 'softmax'
    loss_fn = 'categorical_crossentropy'
    output_units = num_classes
else:
    y_train_cat = y_train
    y_test_cat = y_test
    activation_last = 'sigmoid'
    loss_fn = 'binary_crossentropy'
    output_units = 1

nn_model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(output_units, activation=activation_last)
])

nn_model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss=loss_fn,
    metrics=['accuracy']
)

# Class weights for imbalance
classes = np.unique(y_train)
class_weights = compute_class_weight(class_weight='balanced', classes=classes, y=y_train)
class_weight_dict = dict(zip(classes, class_weights))

# Callbacks
early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=5,
    min_lr=0.00001
)

# Train NN
history = nn_model.fit(
    X_train_scaled, y_train_cat,
    epochs=100,
    batch_size=16,
    validation_split=0.2,
    class_weight=class_weight_dict,
    callbacks=[early_stopping, reduce_lr],
    verbose=1
)

# Evaluate NN
nn_pred = nn_model.predict(X_test_scaled, verbose=0)
if num_classes > 2:
    nn_pred_classes = np.argmax(nn_pred, axis=1)
else:
    nn_pred_classes = (nn_pred > 0.5).astype(int).flatten()

nn_accuracy = accuracy_score(y_test, nn_pred_classes)
logger.info(f"\nNeural Network Accuracy: {nn_accuracy:.4f}")
logger.info(f"\nClassification Report:\n{classification_report(y_test, nn_pred_classes)}")

# Save NN model
nn_model.save('models/nn_model.h5')
logger.info("✓ Neural Network model saved")

# ------------------- Support Vector Machine -------------------
logger.info("\n" + "="*50)
logger.info("Training SVM...")
logger.info("="*50)

svm_model = SVC(kernel='rbf', probability=True, random_state=42, C=1.0, gamma='scale')
svm_model.fit(X_train_scaled, y_train)

# Evaluate SVM
svm_pred = svm_model.predict(X_test_scaled)
svm_accuracy = accuracy_score(y_test, svm_pred)
logger.info(f"SVM Accuracy: {svm_accuracy:.4f}")

# Cross-validation
svm_cv_scores = cross_val_score(svm_model, X_train_scaled, y_train, cv=5)
logger.info(f"SVM Cross-validation scores: {svm_cv_scores}")
logger.info(f"SVM Mean CV score: {svm_cv_scores.mean():.4f} (+/- {svm_cv_scores.std() * 2:.4f})")

pickle.dump(svm_model, open('models/svm_model.pkl', 'wb'))
logger.info("✓ SVM model saved")

# ------------------- K-Nearest Neighbors -------------------
logger.info("\n" + "="*50)
logger.info("Training KNN...")
logger.info("="*50)

knn_model = KNeighborsClassifier(n_neighbors=5, weights='distance')
knn_model.fit(X_train_scaled, y_train)

# Evaluate KNN
knn_pred = knn_model.predict(X_test_scaled)
knn_accuracy = accuracy_score(y_test, knn_pred)
logger.info(f"KNN Accuracy: {knn_accuracy:.4f}")

# Cross-validation
knn_cv_scores = cross_val_score(knn_model, X_train_scaled, y_train, cv=5)
logger.info(f"KNN Cross-validation scores: {knn_cv_scores}")
logger.info(f"KNN Mean CV score: {knn_cv_scores.mean():.4f} (+/- {knn_cv_scores.std() * 2:.4f})")

pickle.dump(knn_model, open('models/knn_model.pkl', 'wb'))
logger.info("✓ KNN model saved")

# ------------------- Random Forest -------------------
logger.info("\n" + "="*50)
logger.info("Training Random Forest...")
logger.info("="*50)

rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

# Evaluate RF
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
logger.info(f"Random Forest Accuracy: {rf_accuracy:.4f}")

# Cross-validation
rf_cv_scores = cross_val_score(rf_model, X_train, y_train, cv=5)
logger.info(f"RF Cross-validation scores: {rf_cv_scores}")
logger.info(f"RF Mean CV score: {rf_cv_scores.mean():.4f} (+/- {rf_cv_scores.std() * 2:.4f})")

# Feature importance
feature_names = df.drop('Schizophrenia', axis=1).columns
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

logger.info(f"\nFeature Importance:\n{feature_importance}")

pickle.dump(rf_model, open('models/rf_model.pkl', 'wb'))
logger.info("✓ Random Forest model saved")

# ------------------- Summary -------------------
logger.info("\n" + "="*50)
logger.info("TRAINING SUMMARY")
logger.info("="*50)
logger.info(f"Neural Network Accuracy: {nn_accuracy:.4f}")
logger.info(f"SVM Accuracy: {svm_accuracy:.4f}")
logger.info(f"KNN Accuracy: {knn_accuracy:.4f}")
logger.info(f"Random Forest Accuracy: {rf_accuracy:.4f}")

best_model = max(
    [('Neural Network', nn_accuracy), ('SVM', svm_accuracy), 
     ('KNN', knn_accuracy), ('Random Forest', rf_accuracy)],
    key=lambda x: x[1]
)
logger.info(f"\nBest performing model: {best_model[0]} ({best_model[1]:.4f})")

logger.info("\n✅ All models and scaler saved in /models directory")
logger.info("Models ready for deployment!")
