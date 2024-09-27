import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

# 加载数据
got_master = pd.read_csv("test.csv", thousands=',')
test_master = pd.read_csv("needing_test.csv", thousands=',')

# prepare the data
