import numpy as np
#Arreglo de numero en un rango dado
arr = np.array([i for i in range (6)]);
print(arr);
#una matriz en un rango
arr2 = np.arange(0,9).reshape(3,3);
print(arr2);
#una matriz en un rango de dos en dos
arr2 =np.arange(0,36,4).reshape(3,3);
print(arr2);
print("-------------------------");
import matplotlib.pyplot as plt
import numpy as np
N=5
menMeans=(20,35,30,35,-27)
womenMeans=(25,32,34,20,-25)
menStd=(2,3,4,1,2)
womenStd=(3,5,2,3,3)
ind=np.arange(N)
width=0.35
fig,ax=plt.subplots()
p1=ax.bar(ind,menMeans,width,yerr=menStd,label='Men')
p2=ax.bar(ind,womenMeans,width, bottom=menMeans, yerr=womenStd,label='Men')
ax.axhline(0,color='grey',linewidth=0.8)
ax.set_ylabel('scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind)
ax.set_xticklabels(('G1','G2','G3','G4','G5'))
ax.legend()
ax.bar_label(p1,label_type='center')
ax.bar_label(p2,label_type='center')
ax.bar_label(p2)
plt.show()