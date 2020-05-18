import numpy as np
import os
import sys

txt = np.loadtxt('./kitti_eval/pose_data/ground_truth/09_full.txt')
#print(txt)
print(txt.shape)

dir_name = os.listdir('./output/sfmlerner/09')
dir_name = sorted(dir_name,key=lambda x: int(x.split('.')[0]))

#print(dir_name)

for i in range(1,txt.shape[0]-2):
    gt = []
    gt.append(txt[i-1])
    gt.append(txt[i])
    gt.append(txt[i+1])
    gt = np.array(gt)
    np.savetxt('./dataset/poses/09/'+dir_name[i],gt,fmt='%f')
    #sys.exit()
    
