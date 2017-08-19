import pickle
import pandas 
import numpy 
import scipy.io as sio
import random

df=pandas.read_csv('C:\\Users\\Shreya\\Documents\\MATLAB\\data\\interactions.tsv',delimiter='\t',index_col=None)
udf=pandas.read_csv('C:\\Users\\Shreya\\Documents\\MATLAB\\data\\users.csv',delimiter='\t',index_col=None)
users=pandas.unique(df.user_id.ravel())
jobs=pandas.unique(df.item_id.ravel())
x =[]

for i in range(0,500) :
   x.append(random.randint(0,users.shape[0]))


total_users=users[x]
train_users=total_users[0:350]
test_users=total_users[350:500]
ratings_full=df.loc[df['user_id'].isin(total_users)]
ratings_train=df.loc[df['user_id'].isin(train_users)]
pickle.dump(total_users,open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\total_users.txt','wb'))
pickle.dump(train_users,open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\train_users.txt','wb'))
pickle.dump(test_users,open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\test_users.txt','wb'))
pickle.dump(ratings_full,open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\ratings_full.txt','wb'))
pickle.dump(ratings_train,open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\ratings_train.txt','wb'))
final_users=udf.loc[udf['id'].isin(total_users)]
pickle.dump(final_users,open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\final_users.txt','wb'))






