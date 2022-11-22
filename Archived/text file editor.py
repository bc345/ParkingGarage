import numpy as np
import array as arr
import random as random
Floor1=np.random.randint(low=1, high=20, size=5)
print(Floor1)
#Libraries
i=0
while (i<=4):
  if Floor1[i]<5:
    Floor1[i]=1
    print("lool")
  else:
    Floor1[i]=0
    print("tihto")
  

  i=i+1
a_file = open("randomfile.txt", "w")
Filearray1=str(Floor1)
a_file.write(Filearray1)
a_file.close()
a_file = open("randomfile.txt", "r")
content = a_file.read()


