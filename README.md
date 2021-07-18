# Outlier Detection

[![Downloads](https://pepy.tech/badge/outlier-detection)](https://pepy.tech/project/outlier-detection)
[![Generic badge](https://img.shields.io/pypi/v/outlier-detection.svg?logo=pypi&logoColor=white&color=orange)](https://pypi.org/project/outlier-detection/)
![Generic badge](https://img.shields.io/badge/python-v3.6%20%7C%203.7%20%7C%203.8-blue)

Detect outliers from pandas dataframe using various statistical tools
# INSTALLATION AND USAGE
```python
!pip install outlier-detection
from outlier_detection import detect_outliers_using_iqr
import pandas as pd

# Pandas Dataframe
data = pd.read_csv('titanic.csv')

# Detect outliers using IQR Method
# On overall data
detect_outliers_using_iqr(df, 'Fare')

# Based on factors data
detect_outliers_using_iqr(data, 'Fare', is_factor=True, factor='Sex')
```

**Github Repository: https://github.com/bilalProgTech/outlier-detection.git**

**Tutorial Data Credit: https://www.kaggle.com/c/titanic**