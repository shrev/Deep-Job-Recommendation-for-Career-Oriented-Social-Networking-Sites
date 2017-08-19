import pickle

import pandas
 
import numpy 


membership=pickle.load( open( "C:\\Users\\Shreya\\Documents\\MATLAB\\files\\k_clusters_2.txt", "rb" ) )
#print "membership matrix"
membership=numpy.asarray(membership)
#print membership
data=pickle.load( open( "C:\\Users\\Shreya\\Documents\\MATLAB\\files\\uservector.txt", "rb" ) )

#data=data.as_matrix()
data=data.astype(numpy.int)

#print data
users=data[:,0]

indices=list(data[:,0])



def select_users(user,threshold,location1,location2):
   li=[]
   i=0
   index=indices.index(user)
   cl=membership[index]	
   selected_users = numpy.where(membership==cl)[0]
   i=0
   selected_users=users[selected_users]
   print "selected are "
   print selected_users
   create_ratings(selected_users,location2)
   fi=open('C:\\Users\\Shreya\\Documents\\MATLAB\\files\\'+location1,'wb')
   pickle.dump(selected_users,fi)


def create_ratings(users,location2):
   df=pandas.read_csv('C:\\Users\\Shreya\\Documents\\MATLAB\\data\\interactions.tsv', sep='\t',index_col=None)
   matrix=df.as_matrix().astype(numpy.int)
   rating=[]
   i=0
   count=0
   ra=df.loc[df['user_id'].isin(users)]
   print ra
   pickle.dump(ra,open("C:\\Users\\Shreya\\Documents\\MATLAB\\files\\"+location2,"wb"))

select_users(data[list(membership).index(0)][0],0.06,"selected_users_0","ratings_0.txt")

select_users(data[list(membership).index(0)][0],0.06,"selected_users_1","ratings_1.txt")

select_users(data[list(membership).index(1)][0],0.06,"selected_users_2","ratings_2.txt")

select_users(data[list(membership).index(2)][0],0.06,"selected_users_3","ratings_3.txt")

#data[list(membership).index(1)]
