import matplotlib.pyplot as plt
import numpy as np
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
    raise ValueError("Los vectores deben tener la misma longitud")
Ay = []
for i in range(len(A)):
    Ay.append(A[i] * y[i])
Xc= sum(Ay)/sum(A)
print(sum(Ay))
print(sum(A))
print(A)
print(y)
print(I)
print("El centroide de la figura esta a "+str(Xc)+" m desde la cara inferior")
d=[]
for i in range(len(y)):
    d.append(A[i]*(abs(y[i]-Xc))**2)
Ic=sum(I)+sum(d)
print(Ic)

## plotear
plt.style.use('_mpl-gallery')
# make data
x = np.linspace(0, h1+h2+h3, 100)
print(x)


y = 4 + 2 * np.sin(2 * x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()




def gen_passw():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    char=MAYUS+MINUS+NUMS+CHARS
    password=[]
    for i in range(15):
        char_rand=random.choice(char)
        password.append(char_rand)
    password="".join(password)
    return password

def run(): 
    password=gen_passw()
    print('Your new password is: '+password)

if __name__=='__main__':
    run()