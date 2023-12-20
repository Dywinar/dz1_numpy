import numpy as np
random = np.random.randint(1,10,100)
print(str((random > 7).sum()/len(random)*100)+' %')
#по сути так как элементов 100 то кол-во семерок и будет процент семерок в векторе
