import matplotlib.pyplot as plt
import numpy as np
## ------ SPECIFY STRESSES ON MOHR CIRCLE ------ ##
Ox=-50   #Axial x Stress
Oy=0    #Axial x Stress
Txy=50  #Shear xy Stress
C=(Ox+Oy)/2
R=(((Ox-Oy)/2)**2+Txy**2)**0.5
Ce=(C,0)
## ------ SPECIFY ROTATION ANGLE ON MOHR CIRCLE ------ ##
## Negative values means clockwise rotation
## Positive values means anti-clockwise rotation
Th=143.3 #Angle of rotation

## ------ New Stresses Values ------ ##
Ox1=((Ox+Oy)/2) + ((Ox-Oy)/2)*np.cos(np.deg2rad(2*Th)) + Txy*np.sin(np.deg2rad(2*Th))  #Axial x Stress
Oy1=((Ox+Oy)/2) + ((Ox-Oy)/2)*np.cos(np.deg2rad(2*(Th+90))) + Txy*np.sin(np.deg2rad(2*(Th+90)))    #Axial x Stress
Tx1y1=-((Ox-Oy)/2)*np.sin(np.deg2rad(2*Th)) + Txy*np.cos(np.deg2rad(2*Th)) #Shear xy Stress

## ------ MOHR'S CIRCLE GRAPH ------ ##

print("Ox1="+str(Ox1))
print("Oy1="+str(Oy1))
print("Tx1y1="+str(Tx1y1))

theta = np.linspace(0, 2 * np.pi, 1000)

# Calculate the x and y coordinates of the circle's points
x = Ce[0] + R * np.cos(theta)
y = Ce[1] + R * np.sin(theta)

plt.style.use("classic")
fig, ax = plt.subplots()
# Plot the circle
ax.plot(x, y, color='red', linewidth=2)
x1=(Oy,Oy,Ox,Ox)
y1=(0,-Txy,Txy,0)
x2=(Oy1,Oy1,Ox1,Ox1)
y2=(0,-Tx1y1,Tx1y1,0)
# Plot the polyline
ax.plot(x1, y1, marker='o', linestyle='-', color='red', linewidth=2)
ax.plot(x2, y2, marker='+', linestyle='-', color='blue', linewidth=2)
# Set aspect ratio to be equal, so the circle looks like a circle
ax.set_aspect('equal')
ax.invert_yaxis()
#Activate axes and grids
ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)
ax.grid(True, linestyle='--', linewidth=0.5)
# Set labels and title
ax.set_xlabel(r'$\sigma$ [MPa] Axial stress')
ax.set_ylabel(r'$\tau$ [MPa] Shear stress')
ax.set_title('Mohr Circle for 2D Stresses')
for i, (xi, yi) in enumerate(zip((Oy,Oy,Ox,Ox), (0,-Txy,Txy,0))):
    ax.text(xi, yi, f'Point {i+1}', fontsize=12, ha='right', va='bottom', color='red')
# Display the plot
plt.show()