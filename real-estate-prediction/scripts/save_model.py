import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Use the original raw data
RAW_PATH = "data/Real estate.csv"
MODEL_PATH = "models/final_model.pkl"
SCALER_PATH = "models/scaler.pkl"

# Map original columns to model features
def load_and_prepare_raw():
    raw = pd.read_csv(RAW_PATH)
    raw = raw.rename(columns={
        'X1 transaction date': 'transaction_date',
        'X2 house age': 'house_age',
        'X3 distance to the nearest MRT station': 'distance_to_mrt',
        'X4 number of convenience stores': 'num_convenience_stores',
        'X5 latitude': 'latitude',
        'X6 longitude': 'longitude',
        'Y house price of unit area': 'price_per_unit_area'
    })
    # Extract transaction_year from transaction_date
    raw['transaction_year'] = raw['transaction_date'].astype(int)
    return raw

def train_and_save():
    df = load_and_prepare_raw()
    features = ['transaction_year', 'house_age', 'distance_to_mrt', 'num_convenience_stores', 'latitude', 'longitude']
    X = df[features]
    y = df['price_per_unit_area']

    # Fit and save scaler on raw data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, SCALER_PATH)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Model hyperparameters
    param_grid = {
        "n_estimators": [100, 200],
        "max_depth": [10, None],
        "min_samples_split": [2, 5]
    }

    grid_search = GridSearchCV(
        RandomForestRegressor(random_state=42),
        param_grid=param_grid,
        scoring="neg_mean_squared_error",
        cv=5,
        n_jobs=-1
    )

    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    joblib.dump(best_model, MODEL_PATH)
    print(f"Model and scaler saved to {MODEL_PATH} and {SCALER_PATH} with params: {grid_search.best_params_}")

if __name__ == "__main__":
    train_and_save()
