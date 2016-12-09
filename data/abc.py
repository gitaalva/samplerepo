import pandas as pd
import csv
import numpy as np
from math import sqrt
from sklearn.feature_extraction.text import CountVectorizer
countVector = CountVectorizer(min_df=1)
import re
with open('/Users/abhyudaya/Desktop/samplerepo/data/y_true.csv') as f:
    reader = csv.reader(f)
    affectivavideooutput = list(reader)
resultdf = pd.DataFrame(affectivavideooutput, columns = ['TrueVal', 'PredVal'])


from sklearn import metrics
from math import sqrt
from ggplot import *
count1 = 0
count0 = 0
count = 0
sum1 = 0.0
#per = result.predict(dfmovietest[['act_rate','dir_rate' , 'pro_rate' ,'rating']] )

fpr, tpr, pr = metrics.roc_curve(resultdf['TrueVal'], resultdf['PredVal'])
df = pd.DataFrame(dict(fpr=fpr, tpr=tpr))
ggplot(df, aes(x='fpr', y='tpr')) +\
    geom_line() +\
    geom_abline(linetype='dashed')
