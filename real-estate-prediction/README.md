# Real Estate Price Prediction

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-green?logo=streamlit)](https://real-estate-prediction-1.streamlit.app)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Streamlit%20Cloud-lightgrey)](https://streamlit.io/)
[![Made With](https://img.shields.io/badge/Made%20With-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

---

## Project Overview
This project was developed as part of a **6-week internship with InternPro** under the **AI/ML domain**.  
This project predicts **real estate prices (NT$/ping)** based on features such as transaction year, house age, distance to MRT stations, number of nearby convenience stores, and coordinates.  
It includes **data preprocessing, model building, evaluation, and a user-friendly web app** built with Streamlit.

The goal is to help buyers, sellers, and analysts make informed property decisions using machine learning.

---

## Features
- Exploratory Data Analysis (EDA)
- Data cleaning and feature engineering
- Multiple ML models with performance comparison
- Best model selection using RMSE and R²
- Streamlit app for real-time prediction
- Feature importance visualization

---

## Dataset
- **Source file:** `data/cleaned_data_with_transaction_year.csv`
- **Target variable:** `price_per_unit_area`
- **Features used:**
  - `transaction_year`
  - `house_age`
  - `distance_to_mrt`
  - `num_convenience_stores`
  - `latitude`
  - `longitude`

---

## Model Performance

| Model               | RMSE  | R²     |
|---------------------|-------|--------|
| Tuned Random Forest | 5.58  | 0.81   |
| Random Forest       | 5.69  | 0.81   |
| XGBoost             | 6.23  | 0.77   |
| Linear Regression   | 7.35  | 0.68   |
| Decision Tree       | 7.73  | 0.64   |

The **Tuned Random Forest** was selected as the final model and saved as `models/final_model.pkl`.

---

## How to Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/your-username/real-estate-prediction.git
cd real-estate-prediction
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Launch the app**
```bash
streamlit run app/real_estate_app.py
```

Visit `http://localhost:8501` in your browser.

---

## Live Demo
The application is deployed using Streamlit Cloud:  
🔗 [Real Estate Price Predictor (Live App)](https://real-estate-prediction-1.streamlit.app)

---


## Model Performance

### Final Model Metrics
- **Model Type**:Tuned Random Forest
- **RMSE**: 5.58 
- **R² Score**: 0.81

### Model Details
- **Algorithm**: Tuned Random Forest
- **Features Used**: 
  - transaction_year
  - house_age
  - distance_to_mrt
  - num_convenience_stores
  - latitude
  - longitude
- **Sample Prediction**: 53.93 (price per unit area)

### Model Files
- `models/final_model.pkl`: Complete model package with trained Tuned Random Forest, feature columns, and target column.
---
## Future Scope
- Add support for LightGBM and CatBoost models
- Integrate real-time data APIs
- Enable CSV-based bulk predictions
- Add geospatial visualizations (e.g., heatmaps)
- Deploy on AWS/GCP with CI/CD pipelines

See detailed roadmap in [future_scope.md](future_scope.md)

---

## Team Members
This project was developed by:
- **Akash J** 
- Rajana Durga Pavan Kumar
- M. Surya Teja
- Borigi Jyothiradhithya
- Hema Sudabathula
- Anushka Parihar
- Yuvanesh S
- Reddy Bunny Sridhar Reddy

---

## License
This project is licensed under the [MIT License](LICENSE).
