# Pipelines (Automate ML Workflow)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split



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

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

pipe.fit(x_train, y_train)
pipe.predict(x_test)
print(pipe.predict(x_test))

