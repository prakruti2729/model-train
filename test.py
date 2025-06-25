from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import pandas as pd

X,y = load_diabetes(return_X_y = True)
_, X_test, _, y_test = train_test_split(X,y_test_size = 0.2)

model = joblib.load("model.pkl")
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Model MSE: {mse:.2f}")

result_df = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})
print(result_df.head(20))
print(f"\n... displaying {len(results_df)} total samples.")

