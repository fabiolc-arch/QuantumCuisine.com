import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Konstanten
G = 1.0       # Gravitationskonstante (willkürlich)
M = 1.0       # Masse des Zentralkörpers
m = 1.0       # Masse des Körpers
k = G * M * m

# Zeitparameter
t_max = 50
dt = 0.01
t = np.arange(0, t_max, dt)

# Anfangsbedingungen (z. B. Ellipse)
r0 = np.array([1.0, 0.0])
v0 = np.array([0.0, 1.2])  # < sqrt(GM/r) -> elliptisch

def acceleration(r):
    return -k * r / np.linalg.norm(r)**3

# Numerische Integration (Verlet-Verfahren)
r = [r0]
v = [v0]

for i in range(len(t)-1):
    r_new = r[-1] + v[-1] * dt + 0.5 * acceleration(r[-1]) * dt**2
    a_new = acceleration(r_new)
    v_new = v[-1] + 0.5 * (acceleration(r[-1]) + a_new) * dt
    r.append(r_new)
    v.append(v_new)

r = np.array(r)
v = np.array(v)

# Wähle 4 zufällige Zeitpunkte
np.random.seed(42)
indices = np.random.choice(len(t), size=4, replace=False)

# Berechne LRL-Vektoren an diesen Punkten
A_vecs = []
for idx in indices:
    pos = r[idx]
    vel = v[idx]
    p = m * vel
    L = np.cross(pos, p)
    A = np.cross(p, L) - m * k * pos / np.linalg.norm(pos)
    A_vecs.append((pos, A))

# Animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

orbit_line, = ax.plot([], [], 'gray', lw=0.5)
body_dot, = ax.plot([], [], 'ro')

vec_quivers = [ax.quiver([], [], [], [], color='blue', scale=10) for _ in A_vecs]

def init():
    orbit_line.set_data(r[:,0], r[:,1])
    body_dot.set_data([], [])
    for q in vec_quivers:
        q.set_UVC(0, 0)
    return [orbit_line, body_dot] + vec_quivers

def update(frame):
    body_dot.set_data(r[frame,0], r[frame,1])
    for i, (pos, A) in enumerate(A_vecs):
        if frame == indices[i]:
            vec_quivers[i].set_offsets([pos])
            vec_quivers[i].set_UVC(A[0], A[1])
    return [orbit_line, body_dot] + vec_quivers

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=30)
plt.title("Laplace-Runge-Lenz-Vektor an 4 Punkten")
plt.show()



