import numpy as np
k = 0
for i in range(1,1001):
  random = np.random.randint(1,10,100)
  proc = int((random > 7).sum()/len(random)*100)
  if proc==20:
    k+=1
print(str(k/1000*100)+' %')
