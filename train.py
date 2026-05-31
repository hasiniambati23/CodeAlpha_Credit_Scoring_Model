import pandas as pd
df = pd.read_csv("data/german_credit_data.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
df.fillna(df.mode().iloc[0],inplace = True)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in df.select_dtypes(include="object"):
    df[col]= le.fit_transform(df[col].astype(str))

print(df.head())

x = df.drop("Risk",axis=1)
y = df["Risk"]

print(x.shape)
print(y.shape)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print(x_train.shape)
print(x_test.shape)


from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)

model = LogisticRegression(max_iter=5000)
model.fit(x_train,y_train)


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

y_pred = model.predict(x_test)

y_prob = model.predict_proba(x_test)[:, 1]

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))


from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(x_train, y_train)

rf_pred = rf.predict(x_test)
rf_prob = rf.predict_proba(x_test)[:, 1]

print("\nRandom Forest Results")
print("Accuracy:", accuracy_score(y_test, rf_pred))
print("Precision:", precision_score(y_test, rf_pred))
print("Recall:", recall_score(y_test, rf_pred))
print("F1 Score:", f1_score(y_test, rf_pred))
print("ROC-AUC:", roc_auc_score(y_test, rf_prob))

import joblib

joblib.dump(model, "models/credit_model.pkl")

print("Model saved successfully!")