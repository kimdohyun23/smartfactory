from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "factory_sensor.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)

    return df

if __name__ == "__main__":
    data = load_data()

    print(data.head())
    print()
    print(data.info())

    

