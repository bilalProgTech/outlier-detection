# Outlier Detection
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

**Tutorial Data Credit: https://www.kaggle.com/c/titanic**