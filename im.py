import numpy as np
import matplotlib.pyplot as plt
from math import * 

t=np.linspace(-4,4,1000)

m=np.array([0,1,2,3,4,5])

d=2*20**(-4)
Dn=9*20**(-3)
lamba2=2*d*Dn/(2*m+1)
lamba4=4*d*Dn/(2*m+1)
for [l,i] in np.ndenumerate(lamba2[1:]):
	delta=lamba2[int(i)]-lamba2[int(i)-1]
# Dlamba2=abs(2/(4*m**2-1))
# plt.plot(Dlamba2, Dlamba2/Dlamba2,'r.')
# plt.plot(Dlamba4, Dlamba2/Dlamba2,'r.')
# plt.savefig('../plot/pila.pdf', format='pdf')
# plt.show()
