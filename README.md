<<<<<<< HEAD
# Video Game Sales Predictive Analytics

This project analyzes video game sales data and builds predictive models to estimate whether a game is likely to have Low, Medium, or High sales. It follows the INT234 Predictive Analytics syllabus by covering data preprocessing, EDA, regression, classification, model evaluation, cross-validation, and ensemble methods.

## Project Files

| File | Purpose |
| --- | --- |
| `cleaned_data.csv` | Main dataset used for analysis and modeling |
| `Database.ipynb` | Loads the CSV into a SQLite database |
| `video_sales_database.db` | SQLite database version of the dataset |
| `DataPreprocessing.ipynb` | Initial preprocessing and data cleaning workflow |
| `EDA.ipynb` | Exploratory data analysis and visualizations |
| `Model_Implementation.ipynb` | Final modeling notebook with preprocessing, model comparison, metrics, predictions, and conclusion |
| `build_model_artifacts.py` | Script used to regenerate the modeling notebook and output visuals |
| `requirements.txt` | Python packages required to run the project |
| `model_outputs/` | Saved model comparison and interpretation plots |

## Dataset Fields

The dataset contains game metadata and sales information, including:

- `title`
- `console`
- `genre`
- `publisher`
- `developer`
- `critic_score`
- `total_sales`
- `na_sales`
- `jp_sales`
- `pal_sales`
- `other_sales`
- `release_date`
- `last_update`

Regional sales columns were not used as model inputs because they directly leak the target value `total_sales`.

## Preprocessing

The final model uses these preprocessing steps:

- Converts `release_date` into `release_year` and `release_month`.
- Treats `critic_score = 0` as missing or unavailable.
- Adds a `critic_score_available` indicator.
- Imputes missing numeric values with the median.
- Imputes missing categorical values with the most frequent value.
- One-hot encodes categorical columns.
- Scales numeric columns where needed.
- Excludes leakage columns: `total_sales`, `na_sales`, `jp_sales`, `pal_sales`, and `other_sales`.

## Modeling Goal

The main goal is classification:

- Low sales: `<= 0.22M`
- Medium sales: `> 0.22M` and `<= 0.50M`
- High sales: `> 0.50M`

A secondary regression task predicts total sales volume in millions using `log1p(total_sales)`.

## Models Compared

Classification models:

- Logistic Regression
- K-Nearest Neighbors
- Naive Bayes
- Decision Tree
- Random Forest
- Linear SVM

Regression models:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## Final Results

Best classification model: **Logistic Regression**

- Accuracy: `50.70%`
- Macro F1 score: `0.5017`
- ROC-AUC: `0.6843`

Best regression model: **Linear Regression**

- MAE: `0.4383 million`
- RMSE: `1.0584 million`
- R-squared: `0.2730`

## Important Insights

- Sports and Action generated the highest total sales.
- Shooter games had the strongest average sales among major genres.
- PS2, X360, and PS3 were the strongest historical platforms by total sales.
- Games with available critic scores had much higher average sales than games without critic scores.
- The model is most useful as an early sales-risk screening tool for publishers.

## Real-World Use Case

A game publisher can use this project to estimate whether a planned game is likely to fall into a Low, Medium, or High sales tier before regional sales data is available. This can support decisions about:

- Marketing budget
- Platform selection
- Release timing
- Publisher and developer strategy
- Risk assessment before launch

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Open and run:

```text
Model_Implementation.ipynb
```

To regenerate the notebook and saved plots:

```bash
python build_model_artifacts.py
```

## Output Visuals

The `model_outputs/` folder contains:

- `classification_model_comparison.png`
- `regression_model_comparison.png`
- `confusion_matrix.png`
- `random_forest_feature_importance.png`

## Conclusion

The final outcome is a syllabus-aligned machine learning project that predicts video game sales category, compares classification and regression models, and gives practical business insights for marketing, platform choice, and launch planning.
=======
# Video-Game-Sales-Analysis
>>>>>>> 352b0d300be0b579f6c983e1ba4c5a5ed8c6643e
