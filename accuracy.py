import pickle
import pandas as pd 
import numpy as np
import scipy.io as sio



total_users = pickle.load(open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\total_users.txt','rb'))
test_users=pickle.load(open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\test_users.txt','rb'))
X = sio.loadmat('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\r_0.mat')
all_ratings = sio.loadmat('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\ratings_0.mat')
all_ratings = pd.DataFrame(all_ratings['R'])


f =pickle.load(open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\final_users.txt','rb')) 

X = X['binary_jobs']

job_ids = sio.loadmat('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\jobids_0.mat')
job_ids = job_ids['jid']
recj = X*job_ids
recj = pd.DataFrame(recj)

recj = recj[recj[0].isin(test_users)]
t = recj.sort([0])
t = np.asarray(t)
Y = all_ratings[all_ratings[0].isin(test_users)]
Yt = Y.sort([0])
temp = np.asarray(Yt)

count =0
correct =0
rec=0
avg =0


for i in range(0,temp.shape[0]) :
   ind = (temp[i]>0)&(temp[i]!=1)
   count= count + len(t[i][ind]) -1
   co = len(t[i][ind]) -1
   cr =sum(t[i][ind]>0) - 1
   correct = correct +sum(t[i][ind]>0) - 1
   if(co>0) :
     rec=rec+1
     avg = avg + float(cr)/float(co)


acc = float(correct)/float(count)
avg/rec







temp = np.asarray(Yt.loc[36])



misprediction=len(R[R == 4])
total  = len(R) - len(R[R == 0]) 

accuracy = (total - misprediction)/total *100 