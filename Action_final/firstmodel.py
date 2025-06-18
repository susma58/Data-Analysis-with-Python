'''
You'll master:
- Model building: Supervised ML (classification, regression)
- Feature engineering: Creating, scaling and selecting features
- Production prep: Pipelines, model evaluation, saving
- Reporting: Dashboards (Streamlit, Dash, Tableau)
- Deployment: Realtime predictions, ETL, APIs
'''


import pandas as pd

# BUILD FIRST ML MODEL (Scikit-learn)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# sample dataset
df = pd.DataFrame({
    'Hours_studied': [5, 3, 8, 2, 7, 6],
    'Sleep_hours': [6, 5, 8, 4, 7, 6],
    'Passed': [1, 0, 1, 0, 1, 1]
})

# features and target
x = df[['Hours_studied', 'Sleep_hours']]
y = df['Passed']

# split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# model
model = LogisticRegression()
model.fit(x_train, y_train)



# predict
y_pred = model.predict(x_test)

print('Accuracy:', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))