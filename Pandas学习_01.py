#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：pandas学习，Series
时间：2018年04月28日10:29:22
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 示例1，data是ndarray
# （1）传递索引
data = np.random.randn(5)
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data=data, index=index)
print("----ndarray，传递索引----")
print(s)
print(s.index)

# （2）不传递索引
print("----ndarray，不传递索引----")
print(pd.Series(data))

# 示例2，data是dic
data = {'a': 0., 'b': 1., 'c': 2.}
# （1）传递索引
print("----dic，传递索引----")
print(pd.Series(data, index=["a", "b", "D", "E"]))

# （2）不传递索引
print("----dic，不传递索引----")
print(pd.Series(data))

# 示例3，data是标量值
# 必须传递索引
print("----标量值，必须传递索引----")
print(pd.Series(5., index=['a', 'b', 'c', 'd', 'e']))

# 切片
print(s[0])
print(s[:3])
print(s[s > s.median()])
print(s[[4, 3, 1]])
print(np.exp(s))

s = pd.Series(np.random.randn(5), name='something')
print(s.name)

if __name__ == "__main__":
    pass
