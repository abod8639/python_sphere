# Powered by DEXTER 

import numpy as np
import matplotlib.pyplot as plt # type: ignore
from mpl_toolkits.mplot3d import Axes3D # type: ignore
import matplotlib.animation as animation # type: ignore


plt.rcParams['toolbar'] = 'None'

plt.style.use('dark_background')  

fig = plt.figure(figsize=(10, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d')

ax.set_facecolor('black')

radius = 1

u = np.linspace(0, 3 * np.pi, 59)  
v = np.linspace(0, np.pi, 59)  

x = radius * np.outer(np.cos(u), np.sin(v))
y = radius * np.outer(np.sin(u), np.sin(v))
z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

def animate(frame):
    ax.clear()
    
   
    angle_z = frame * 0.02   
    angle_y = frame * 0.001 
    
    cos_z = np.cos(angle_z)
    sin_z = np.sin(angle_z)
    x_z = x * cos_z - y * sin_z
    y_z = x * sin_z + y * cos_z
    z_z = z
    
    cos_y =   np.cos(angle_y)
    sin_y =   np.sin(angle_y)
    x_rot =   x_z * cos_y + z_z * sin_y
    y_rot =   y_z
    z_rot = - x_z * sin_y + z_z * cos_y
    
    ax.plot_wireframe(x_rot, y_rot, z_rot, 
                     color='lime', 
                     linewidth=0.9,
                     alpha=0.5)
    
    ax.set_xlim([-0.9, 0.8])
    ax.set_ylim([-0.9, 0.8])
    ax.set_zlim([-0.9, 0.8])
    
    ax.set_axis_off()
    
    # ax.title.set_text('Dexter')

    
    # ax.set_xlabel('X')
    
    
    # ax.view_init(elev=20, azim=frame/2)

anim = animation.FuncAnimation(fig, animate, interval=60, repeat=False )

plt.tight_layout()
plt.show()

anim.save('rotating_sphere.gif', writer='pillow', fps=30, dpi=10)
