import pandas as pd
import xgboost as xgb
import lightgbm as lgb
import catboost as cb
from sklearn.preprocessing import LabelEncoder

def main():
    input_path = "input_data.csv"
    model_path = "models/model_cb_fe"
    output_path = "output.csv"

    df = pd.read_csv(input_path, sep = ",")

    #transform
    df = df.dropna(how='any',axis=0)
    df = df[df["drop_sequence"] > 0]
    df = df[df["distance_calculated"] > 0]
    df = df[df["distance_covered_till_drop"] > 0]
    df = df[df["total_quantity"] > 0]
    df["trip_start_time"] = pd.to_datetime(df["trip_start_time"], format="ISO8601")

    #feature engineering
    if "fe" in model_path:
        print("Feature Engineering...")
        df[["year", "month", "m_day", "hour"]] = df["trip_start_time"].apply(lambda x: x.timetuple()[0:4]).tolist()
        df["w_day"] = df["trip_start_time"].apply(lambda x: x.weekday())
        cols = ['drop_sequence', 'distance_calculated','distance_covered_till_drop', 'origin_warehouse_code',
            'destination_warehouse_code', 'total_quantity', 'trip_start_time','year', 'month', 'm_day', 'hour', 'w_day']
    else:
        cols = ['drop_sequence', 'distance_calculated','distance_covered_till_drop', 'origin_warehouse_code',
            'destination_warehouse_code', 'total_quantity', 'trip_start_time']
    
    le = LabelEncoder()
    df['trip_start_time'] = le.fit_transform(df['trip_start_time'])
    df['origin_warehouse_code'] = le.fit_transform(df['origin_warehouse_code'])
    df['destination_warehouse_code'] = le.fit_transform(df['destination_warehouse_code'])

    if "xgb" in model_path:
        model = xgb.XGBRegressor(objective='reg:squaredlogerror')
        model.load_model(model_path)

    if "lgb" in model_path:
        model = lgb.Booster(model_file=model_path)

    if "cb" in model_path:
        model = cb.CatBoostRegressor()
        model.load_model(model_path)

    preds = model.predict(df[cols])
    df["Predicted_ETA"] = preds
    df.to_csv(output_path)

if __name__ == "__main__":
  main()
