import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split, RandomizedSearchCV



# Load the dataset from CSV
data = pd.read_csv('NRL_matches.csv')

# Extract the features and target variables
X = data[['Home Team', 'Away Team', 'Venue']].values
y_home = data['Home Score'].values
y_away = data['Away Score'].values

# Perform one-hot encoding on categorical features
encoder = OneHotEncoder(categories='auto', sparse=False)
X_encoded = encoder.fit_transform(X)

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

# Split the dataset into training and testing sets for Home Team
X_train_home, X_test_home, y_train_home, y_test_home = train_test_split(X_scaled, y_home, test_size=0.2, random_state=42)

# Split the dataset into training and testing sets for Away Team
X_train_away, X_test_away, y_train_away, y_test_away = train_test_split(X_scaled, y_away, test_size=0.2, random_state=42)

# Hyperparameter Tuning using RandomizedSearchCV for Home Team
param_dist = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

rf_home = RandomForestRegressor(random_state=42)
random_search_home = RandomizedSearchCV(rf_home, param_distributions=param_dist, n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=42)
random_search_home.fit(X_train_home, y_train_home)

# Train the RandomForestRegressor model for Home Team with the best hyperparameters
best_model_home = random_search_home.best_estimator_
best_model_home.fit(X_train_home, y_train_home)

# Hyperparameter Tuning using RandomizedSearchCV for Away Team
rf_away = RandomForestRegressor(random_state=42)
random_search_away = RandomizedSearchCV(rf_away, param_distributions=param_dist, n_iter=10, cv=5, scoring='neg_mean_squared_error', random_state=42)
random_search_away.fit(X_train_away, y_train_away)

# Train the RandomForestRegressor model for Away Team with the best hyperparameters
best_model_away = random_search_away.best_estimator_
best_model_away.fit(X_train_away, y_train_away)

# Evaluate the models for Home Team
y_train_pred_home = best_model_home.predict(X_train_home)
rmse_train_home = mean_squared_error(y_train_home, y_train_pred_home, squared=False)
print(f"Root Mean Squared Error on Training Data (Home Team): {rmse_train_home}")

y_test_pred_home = best_model_home.predict(X_test_home)
rmse_test_home = mean_squared_error(y_test_home, y_test_pred_home, squared=False)
print(f"Root Mean Squared Error on Testing Data (Home Team): {rmse_test_home}")

# Evaluate the models for Away Team
y_train_pred_away = best_model_away.predict(X_train_away)
rmse_train_away = mean_squared_error(y_train_away, y_train_pred_away, squared=False)
print(f"Root Mean Squared Error on Training Data (Away Team): {rmse_train_away}")

y_test_pred_away = best_model_away.predict(X_test_away)
rmse_test_away = mean_squared_error(y_test_away, y_test_pred_away, squared=False)
print(f"Root Mean Squared Error on Testing Data (Away Team): {rmse_test_away}")

# Save the encoders and scalers
joblib.dump(encoder, 'encoder.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Save the trained models
joblib.dump(best_model_home, 'model_home.pkl', protocol=4)
joblib.dump(best_model_away, 'model_away.pkl', protocol=4)
