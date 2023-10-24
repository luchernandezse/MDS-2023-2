import matplotlib.pyplot as plt
import numpy as np
V=float(10)
M=float(10)
print(type(V))
#Los materiales van de abajo hacia arriba.
b1=0.1
b2=0.1
b3=0.1
h1=0.08
h2=0.08
h3=0.08
h=h1+h2+h3
E1=200000000 #[Kpa]
E2=21500000 #[Kpa]
E3=2000000000 #[Kpa]
#Se transforma todo al material 3
n1=E1/E3
n2=E2/E3
n3=E3/E3
b1t=b1*n1
b2t=b2*n2
b3t=b3*n3
A=[b1t*h1,b2t*h2,b3t*h3]
y=[h1/2,h1+(h2/2),h1+h2+(h3/2)]
I=[b1t*(h1**3)/12,b2t*(h2**3)/12,b3t*(h3**3)/12]
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
print("El centroide es "+str(Xc))
print("La inercia es "+str(Ic))

# make data
x = np.linspace(0, h, 100)
print(x)
q = np.zeros_like(x)
T = np.zeros_like(x)
print(type(T))
q[(x<=Xc)&(x<=h1)] = x[(x<=Xc)&(x<=h1)]*b1t*(Xc-x[(x<=Xc)&(x<=h1)]/2)
q[(x<=Xc)&(x>h1)] = h1*b1t*(Xc-h1/2)+b2t*(x[(x<=Xc)&(x>h1)]-h1)*(Xc-h1-(x[(x<=Xc)&(x>h1)]-h1)/2)
q[(x>Xc)&(x<=(h1+h2))] = h3*b3t*(h-Xc-h3/2)+b2t*(h1+h2-x[(x>Xc)&(x<=(h1+h2))])*(h1+h2-Xc-((h1+h2-x[(x>Xc)&(x<=(h1+h2))])/2))
q[(x>Xc)&(x>(h1+h2))] = b3t*(h-x[(x>Xc)&(x>(h1+h2))])*(h-Xc-((h-x[(x>Xc)&(x>(h1+h2))])/2))
print(q)
T[(x<=Xc)&(x<=h1)]=V*q[(x<=Xc)&(x<=h1)]*n1/(Ic*b1t)
T[(x<=Xc)&(x>h1)]=V*q[(x<=Xc)&(x>h1)]*n2/(Ic*b2t)
T[(x>Xc)&(x<=(h1+h2))]=V*q[(x>Xc)&(x<=(h1+h2))]*n2/(Ic*b2t)
T[(x>Xc)&(x>(h1+h2))]=V*q[(x>Xc)&(x>(h1+h2))]*n3/(Ic*b3t)
print(T)

Yi = np.zeros_like(x)
S1 = np.zeros_like(x)
S2 = np.zeros_like(x)
Yi[(x<=Xc)&(x<=h1)] = Xc-x[(x<=Xc)&(x<=h1)]
Yi[(x<=Xc)&(x>h1)] = Xc-x[(x<=Xc)&(x>h1)]
Yi[(x>Xc)&(x<=(h1+h2))] = Xc-x[(x>Xc)&(x<=(h1+h2))]
Yi[(x>Xc)&(x>(h1+h2))] = Xc-x[(x>Xc)&(x>(h1+h2))]
S1[(x<=Xc)&(x<=h1)] = M*Yi[(x<=Xc)&(x<=h1)]*n1/Ic
S1[(x<=Xc)&(x>h1)] = M*Yi[(x<=Xc)&(x>h1)]*n2/Ic
S2[(x>Xc)&(x<=(h1+h2))] = M*Yi[(x>Xc)&(x<=(h1+h2))]*n2/Ic
S2[(x>Xc)&(x>(h1+h2))] = M*Yi[(x>Xc)&(x>(h1+h2))]*n3/Ic
print(S1)
print(S2)

plt.style.use("classic")
plt.subplot(1,2,1)
plt.plot(T, x, label='Shear Stress', linewidth=3,color='blue')
plt.xlabel('Shear stress [KPa]')
plt.ylabel('Beam height [m]')
plt.title('Shear stress distribution on Beam section')
plt.grid(True)
plt.legend()
plt.gcf().set_size_inches(10,6)
plt.fill_betweenx(x,T,alpha=0.2,color='blue')
#plt.show()
plt.subplot(1,2,2)
plt.plot(S1, x, label='Axial Stress', linewidth=3,color='blue')
plt.plot(S2, x, label='Axial Stress', linewidth=3,color='red')
plt.xlabel('Axial stress [KPa]')
plt.ylabel('Beam height [m]')
plt.title('Axial stress distribution on Beam section')
plt.grid(True)
plt.legend()
plt.gcf().set_size_inches(10,6)
plt.fill_betweenx(x,0,S1,alpha=0.2,color='blue')
plt.fill_betweenx(x,S2,h,alpha=0.2,color='red')
#plt.fill(S,x)
plt.show()