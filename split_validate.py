import pickle
import pandas 
import numpy 
import scipy.io as sio
import random

df=pandas.read_csv('interactions.tsv',delimiter='\t',index_col=None)
udf=pandas.read_csv('users.csv',delimiter='\t',index_col=None)
users=pandas.unique(df.user_id.ravel())
jobs=pandas.unique(df.item_id.ravel())

total_users = pickle.load(open('All_Data/total_users.txt','rb'))
train_users=total_users[0:20]
test_users=total_users[20:40]
m = total_users[40:100]
train_users = numpy.append(train_users,m)
ratings_full=df.loc[df['user_id'].isin(total_users)]
ratings_train=df.loc[df['user_id'].isin(train_users)]
pickle.dump(total_users,open('All_Data/total_users.txt','wb'))
pickle.dump(train_users,open('All_Data/train_users.txt','wb'))
pickle.dump(test_users,open('All_Data/test_users.txt','wb'))
pickle.dump(ratings_full,open('All_Data/ratings_full.txt','wb'))
pickle.dump(ratings_train,open('All_Data/ratings_train.txt','wb'))
final_users=udf.loc[udf['id'].isin(total_users)]
pickle.dump(final_users,open('All_Data/final_users.txt','wb'))
