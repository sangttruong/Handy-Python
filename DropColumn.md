data.drop(['GameplayID'], axis=1, inplace = True)

data = data[data.GamestateNum == 0]
