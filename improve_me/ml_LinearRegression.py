"""
线性回归是基于最小二乘法的，其目标是寻找最小化损失函数的参数。数据相同，训练出的模型也相同
"""
# # 导入所需的库
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
#
# # 加载凤凰城气温数据集
# url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
# data = pd.read_csv(url)
#
# # 查看数据集的前5行数据
# print(data.head())
#
# # 将日期转换为pandas的日期格式
# data['Date'] = pd.to_datetime(data['Date'])
#
# # 将日期作为索引
# data = data.set_index('Date')
#
# # 提取最高气温作为特征
# X = data['Temp'].values.reshape(-1, 1)
#
# # 提取最低气温作为目标变量
# y = data['Temp'].values.reshape(-1, 1)
#
# # 划分数据集为训练集和测试集，比例为3:1
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
#
# # 创建线性回归模型对象
# model = LinearRegression()
#
# # 在训练集上训练模型
# model.fit(X_train, y_train)
#
# # 在测试集上进行预测
# y_pred = model.predict(X_test)
#
# # 计算均方误差
# mse = mean_squared_error(y_test, y_pred)
# print('Mean squared error: %.2f' % mse)
#
# # 绘制预测值与真实值的散点图
# plt.scatter(y_test, y_pred)
# plt.xlabel('True Values')
# plt.ylabel('Predictions')
# plt.show()

# 导入必要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 加载加利福尼亚住房数据集
# california = fetch_california_housing(as_frame=True)["frame"]
california = fetch_california_housing()
# print(california.head())
# 创建特征矩阵和标签
X = pd.DataFrame(california.data, columns=california.feature_names)
y = california.target

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测测试集结果
y_pred = model.predict(X_test)

# 计算模型的均方误差
mse = mean_squared_error(y_test, y_pred)
print("均方误差：", mse)

# 绘制真实值和预测值的散点图
plt.rcParams['font.family'] = 'SimHei'

plt.scatter(y_test, y_pred)
plt.xlabel("真实房价")
plt.ylabel("预测房价")
plt.title("加利福尼亚住房价格预测")
plt.show()
