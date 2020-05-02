import pandas as pd
import numpy as np
import sqlite3
df = pd.read_pickle('sarco_count.pk')

names = '''KimOBok
JungOJeom
KimOHan
LeeOJe
KimOSaeng
KwonOSu
AnOJa
JungOJa
ShimOJa
LeeOOk
ParkOJa'''.split('\n')

labels = '''1
1
1
1
1
0
1
0
0
0
0'''.split('\n')

exp1           = [x for x,y in zip(names,labels) if y == '0']
exp1_counts    =  [','.join(map(str,x)) for x in df[exp1].values]
exp1_genenames = list(df[exp1].index)
exp1_values    = np.array([*zip(exp1_genenames, exp1_counts)])

exp2           = [x for x,y in zip(names,labels) if y == '1']
exp2_counts    =  [','.join(map(str,x)) for x in df[exp2].values]
exp2_genenames = list(df[exp2].index)
exp2_values    = np.array([*zip(exp2_genenames, exp2_counts)])

con = sqlite3.connect('./db.sqlite3')
cur = con.cursor()

cur.executemany("INSERT INTO exp1 (geneName, countArray) VALUES (?,?)",exp1_values) # INTO 다음의 v1은 model에서 지정해준 class Meta: dbtable = 'v1' 
cur.executemany("INSERT INTO exp2 (geneName, countArray) VALUES (?,?)",exp2_values)

con.commit()
con.close()