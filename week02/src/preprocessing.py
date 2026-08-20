import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    제조 데이터 전처리
    """

    # 결측치 확인
    print("=== 결측치 확인 ===")
    print(df.isnull().sum())

    # 중복 제거
    df = df.drop_duplicates()

    # 불량률 계산
    df["defect_rate"] = (
        df["defect_count"] / df["production_count"] * 100
    )

    return df


if __name__ == "__main__":
    from load_data import load_data

    df = load_data()

    df = preprocess_data(df)

    print()
    print(df.head())