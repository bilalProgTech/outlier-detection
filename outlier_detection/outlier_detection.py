import seaborn as sns
import matplotlib.pyplot as plt
def detect_outliers_using_iqr(data, target, is_factor = False, factor = None):
    if is_factor:
        for pred in data[factor].unique():
            print('\nFactor: '+ pred)
            total = data[data[factor]==pred].shape[0]
            Q1 = data[data[factor]==pred][target].quantile(0.25)
            Q3 = data[data[factor]==pred][target].quantile(0.75)
            IQR = Q3- Q1
            upper = Q3 + 1.5 * IQR
            lower = Q1 - 1.5 * IQR
            print('Lower Bound Threshold: '+str(lower))
            print('Upper Bound Threshold: '+str(upper))

            lower_obs = data[(data[target] < lower) & (data[factor]==pred)][target].count()
            upper_obs = data[(data[target] > upper) & (data[factor]==pred)][target].count()
            total_obs = data[(data[target] < upper) & (data[target] > lower) & (data[factor]==pred)][target].count()

            print('No. of Observation beyond lower bound: ' +str(lower_obs))
            print('No. of Observation beyond upper bound: ' +str(upper_obs))
            print('No. of Observation between upper and lower bound: ' +str(total_obs))

            print('Ratio of Outliers for target variable '+str(pred)+
                  ': '+str(round((lower_obs+upper_obs)/total, 2)*100)+'%')
        
        sns.catplot(x=factor, y=target, data=data, kind='box', aspect=2)
        plt.tight_layout()
        plt.show()
    else:
        total = data.shape[0]
        Q1 = data[target].quantile(0.25)
        Q3 = data[target].quantile(0.75)
        IQR = Q3- Q1
        upper = Q3 + 1.5 * IQR
        lower = Q1 - 1.5 * IQR
        print('Lower Bound Threshold: '+str(lower))
        print('Upper Bound Threshold: '+str(upper))

        lower_obs = data[(data[target] < lower)][target].count()
        upper_obs = data[(data[target] > upper)][target].count()
        total_obs = data[(data[target] < upper) & (data[target] > lower)][target].count()

        print('No. of Observation beyond lower bound: ' +str(lower_obs))
        print('No. of Observation beyond upper bound: ' +str(upper_obs))
        print('No. of Observation between upper and lower bound: ' +str(total_obs))

        print('Ratio of Outliers for target variable: '+str(round((lower_obs+upper_obs)/total, 2)*100)+'%')
        
        sns.boxplot(x=target, data=data)
        plt.tight_layout()
        plt.show()