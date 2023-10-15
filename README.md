# Milkrun ETA Prediction
## Overview
Regression based models to estimate arrival time for milk runs. Milk run logistics are a type of delivery system where shipments are delivered to multiple locations in one trip.

## Installation Instructions
##### Step 1: Clone
Clone this git repository using:
```bash
git clone https://github.com/raashidsalih/milkrun-eta.git
```

##### Step 2: Configure
- Replace the content of ```input_source.csv``` with the data you want predictions for. Pay attention to the columns since not all features are required by the model for the prediction.
- Change the model you want to use (if needed) by modifying ```model_path``` in ```main.py```. You can refer to available models in the section below.
- If you'd like to use another location for the ```input_source.csv```, you can do so by changing ```model_path``` in ```main.py```.
- You can do the same for output by modifying ```output_path``` in ```main.py```.

##### Step 3: Define Python Virtual Environment [Optional]
I suggest running the program in a Python venv for stability and reproducibility. Although optional, it is highly recommended to avoid potential dependency related issues. Navigate to the cloned directory and create a Python virtual environment using the following command *[Windows]:*
```bash
python -m venv myenv
```
Activate your Python venv using:
```bash
myenv\Scripts\activate
```
If you get a permission error with regards to not being able to run scripts, use this command first:
```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```
It'll not enforce restrictions for the rest of the session.

##### Step 4: Install Requirements
Install the dependencies for the program to run via the handy requirements.txt:
```bash
pip install -r requirements.txt
```

##### Step 5: Ready To Go
All the requirements have been satisfied, and you are now ready to use the program. Just run ```main.py``` from a CLI or using an IDE of your choosing. The results should be present as ```output.csv```.

## Available Models

|                |                          **Description**                          |  **mse** |  **mae** | **rmse** |
|:--------------:|:-----------------------------------------------------------------:|:--------:|:--------:|:--------:|
|     **xgb**    |           XGBoost model without any data transformations          |  97485.6 | 254.1317 | 312.2268 |
|   **xgb_fe**   |               XGBoost model with Feature Engineering              |  97485.6 | 254.1317 | 312.2268 |
|   **xgb_out**  |                XGBoost model with Outliers removed                | 55828.41 | 193.0433 | 236.2804 |
| **xgb_fe_out** |  XGBoost model with Feature Engineering and with Outliers removed | 55828.41 | 193.0433 | 236.2804 |
|     **lgb**    |             LGBModel without any data transformations             | 10865613 | 2960.099 | 3296.303 |
|   **lgb_fe**   |                 LGBModel with Feature Engineering                 | 10784384 | 2934.576 | 3283.959 |
|   **lgb_out**  |                   LGBModel with Outliers removed                  |  6904475 | 2327.508 | 2627.637 |
| **lgb_fe_out** | LGBModel model with Feature Engineering and with Outliers removed |  6929543 | 2323.559 | 2632.402 |
|     **cb**     |          CatBoost model without any data transformations          | 10723974 | 2941.428 | 3274.748 |
|    **cb_fe**   |              CatBoost model with Feature Engineering              | 11386283 | 3041.718 | 3374.357 |
|   **cb_out**   |                CatBoost model with Outliers removed               |  6825637 | 2329.512 | 2612.592 |
| **cb_fe_out**  | CatBoost model with Feature Engineering and with Outliers removed | 7177033  | 2396.327 | 2678.999 |

 - When sorted by MAE and RMSE, it is clear that XGBoost clearly leads the pack in terms of performance.
 - XGBoost is the de facto standard when it comes to tabular data, and is therefore the first choice when it comes to model selection.
	 - However, LightGBM is faster and more efficient than XGBoost, and this quality can be brought into consideration when moving the model into production is concerned.
	 - Likewise, CatBoost is more robust because it can handle features with high cardinality, and can also handle missing values natively.
	 - Regardless, estimation performance is the most significant factor here, and we'll need to have data at much larger scales for these aspects to manifest.
- Hyperparameter tuning must be considered for even better performance.
