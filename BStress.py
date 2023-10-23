import matplotlib.pyplot as plt
import numpy as np
V=float(10)
print(type(V))
b1=0.2
b2=0.1
b3=0.2
h1=0.15
h2=0.3
h3=0.15
h=h1+h2+h3
A=[b1*h1,b2*h2,b3*h3]
y=[h1/2,h1+(h2/2),h1+h2+(h3/2)]
I=[b1*(h1**3)/12,b2*(h2**3)/12,b3*(h3**3)/12]
if len(A) != len(y):
    raise ValueError("Vector's need to have same length. Check!")
Ay = []
for i in range(len(A)):
    Ay.append(A[i] * y[i])
Xc= sum(Ay)/sum(A)
#print("El centroide de la figura esta a "+str(Xc)+" m desde la cara inferior")
d=[]
for i in range(len(y)):
    d.append(A[i]*(abs(y[i]-Xc))**2)
Ic=sum(I)+sum(d)
## plotear
plt.style.use('_mpl-gallery')
# make data
x = np.linspace(0, h1+h2+h3, 100)
print(x)
q = np.zeros_like(x)
T = np.zeros_like(x)
print(type(T))
q[(x<=Xc)&(x<=h1)] = x[(x<Xc)&(x<h1)]*b1*(Xc-x[(x<Xc)&(x<h1)]/2)
q[(x<=Xc)&(x>h1)] = h1*b1*(Xc-h1/2)+b2*(x[(x<Xc)&(x>h1)]-h1)*(Xc-h1-(x[(x<Xc)&(x>h1)]-h1)/2)
q[(x>Xc)&(x<=(h1+h2))] = h3*b3*(h-Xc-h3/2)+b2*(h1+h2-x[(x>Xc)&(x<=(h1+h2))])*(h1+h2-Xc-((h1+h2-x[(x>Xc)&(x<=(h1+h2))])/2))
q[(x>Xc)&(x>(h1+h2))] = b3*(h-x[(x>Xc)&(x>(h1+h2))])*(h-Xc-((h-x[(x>Xc)&(x>(h1+h2))])/2))
print(q)
T[(x<=Xc)&(x<=h1)]=V*q[(x<=Xc)&(x<=h1)]/(Ic*b1)
T[(x<=Xc)&(x>h1)]=V*q[(x<=Xc)&(x>h1)]/(Ic*b2)
T[(x>Xc)&(x<=(h1+h2))]=V*q[(x>Xc)&(x<=(h1+h2))]/(Ic*b2)
T[(x>Xc)&(x>(h1+h2))]=V*q[(x>Xc)&(x>(h1+h2))]/(Ic*b3)

plt.plot(T, x, label='Shear Stress')
plt.axis((0,np.max(T)+10,0,h))
plt.xlabel('Shear stress [KPa]')
plt.ylabel('Beam height [m]')
plt.title('Shear stress distribution on Beam section')
plt.grid(True)
plt.legend()
plt.show()
