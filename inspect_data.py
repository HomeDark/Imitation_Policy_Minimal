import numpy as np
d = np.load('expert_demo.npz') 
print(list(d.key()))
for k in d:
  print(f' {k}:{d[k].shape} {d[k].dtype}')
print('obs[0]:',d['observations'][0])
print('act[0]:',d['actions'][0])
