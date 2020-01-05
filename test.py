import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.font_manager as fm

fontname = u"/System/Library/Fonts/Supplemental/AppleMyungjo.ttf"
fontname = font_manager.FontProperties(fname=fontname).get_name()
print("fontname:", fontname)
rc("font", family=fontname)


# font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# for font in font_list:
#     print(font)


filename = "./data/201801.csv"
# standard(open)


fp = open(filename, "r")
lines = fp.readlines()

colume = lines[0][:-1]
colume = colume.split("\t")
# print(colume)

data_list = []
for line in lines[1:]:
    data = {}
    line = line[:-1]
    value = line.split("\t")
    data["거래금액"] = value[0]
    data["건축년도"] = value[1]
    data["년"] = value[2]
    data["월"] = value[3]
    data_list.append(data)


# print(data_list)

# print(data_list[0]["거래금액"])

# pandas - reading data
df = pd.read_csv(filename, sep="\t")

# print(df.head(5))  # df = data frame
print("df:", df)
print("df.values:", df.values)

# 항상 데이터를 확인하는 습관을 길러라
print(df.dtypes)  # object: string
print(df.head(3))
print(df.tail(3))
print(df.columns)
print(df[(df["건축년도"] == 2008) & (df["일"] == 9)])  # filtering with dataframe
df["거래금액"] = (
    df["거래금액"].apply(lambda x: x.replace(",", "")).astype(int)
)  # Type casting from object to int64
# df["거래금액"] = df["거래금액"].apply(
#     lambda x: int(x.replace(",", ""))
# )  # Type casting from object to int64
print(df.dtypes)

df.to_csv("sample.csv", index=False)


# Statstic
# 평균
print(df["거래금액"].mean())
# 표준편차
print(df["거래금액"].std())
# everything including mean, std
print(df["거래금액"].describe())


# Group
apt_df = df[["아파트", "거래금액"]].groupby("아파트").mean()
print(apt_df)

apt_df.plot(kind="bar", figsize=(20, 6))  # kind defalut is line
plt.xlabel("Apt")
plt.ylabel("Price")
plt.title("apt price")
plt.show()


# df2 = pd.DataFrame(data_list)

# df2 = df.sort_values("건축년도", ascending=True)

# print(df2)

# print(df2)

