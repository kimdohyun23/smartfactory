from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "production.csv"
IMAGE_DIR = BASE_DIR / "images"

IMAGE_DIR.mkdir(exist_ok=True)


# 1. 데이터 로딩
df = pd.read_csv(DATA_PATH)

print("=== 데이터 미리보기 ===")
print(df.head())

print("\n=== 데이터 정보 ===")
df.info()


# 2. 파생 지표 생성
df["defect_rate"] = (
    df["defect_count"] / df["production_count"] * 100
)


# 3. 제조 KPI 분석
total_production = df["production_count"].sum()
average_production = df["production_count"].mean()
average_defect_rate = df["defect_rate"].mean()
average_operating_rate = df["operating_rate"].mean()

print("\n=== 제조 데이터 분석 결과 ===")
print(f"총 생산량: {total_production:,}개")
print(f"평균 생산량: {average_production:.1f}개")
print(f"평균 불량률: {average_defect_rate:.2f}%")
print(f"평균 가동률: {average_operating_rate:.2f}%")


# 4. 불량률 2% 이상 탐지
warning_df = df[df["defect_rate"] >= 2]

print("\n=== 불량률 2% 이상 날짜 ===")

if warning_df.empty:
    print("이상 데이터가 없습니다.")
else:
    print(
        warning_df[
            ["date", "machine_id", "production_count",
             "defect_count", "defect_rate"]
        ].to_string(index=False)
    )


# 5. 생산량 추이
plt.figure(figsize=(8, 4))
plt.plot(
    df["date"],
    df["production_count"],
    marker="o"
)
plt.title("Production Trend")
plt.xlabel("Date")
plt.ylabel("Production Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "production_trend.png")
plt.close()


# 6. 불량률
plt.figure(figsize=(8, 4))
plt.bar(
    df["date"],
    df["defect_rate"]
)
plt.axhline(
    y=2,
    linestyle="--",
    label="Warning threshold (2%)"
)
plt.title("Defect Rate")
plt.xlabel("Date")
plt.ylabel("Defect Rate (%)")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(IMAGE_DIR / "defect_rate.png")
plt.close()


# 7. 설비 가동률
plt.figure(figsize=(8, 4))
plt.plot(
    df["date"],
    df["operating_rate"],
    marker="o"
)
plt.title("Operating Rate")
plt.xlabel("Date")
plt.ylabel("Operating Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "operating_rate.png")
plt.close()


print("\n그래프 저장 완료!")
