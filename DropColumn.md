data.drop(['GameplayID'], axis=1, inplace = True)

data = data[data.GamestateNum == 0]

result = pd.concat([data1, data2, data3, data4])

data1 = pd.read_csv("DiscountSimple4_Last.csv", index_col = 0)
