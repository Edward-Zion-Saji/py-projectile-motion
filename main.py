import matplotlib.pyplot as plt
import numpy as np


def projectile_motion(initial_velocity, angle):
    theta = np.pi/(180/int(angle))
    sin = np.sin(theta)
    cos = np.cos(theta)
    g = 9.8
    t = np.linspace(0, 10000, num=1000000)
    u = initial_velocity

    x, y = [], []

    for i in t:
        xi = (u * i * cos)
        yi = (u * i * sin) - (0.5 * g * (i ** 2))

        x.append(xi)
        y.append(yi)

    h_max = ((u ** 2) * (sin ** 2)) / (2 * g)
    r_max = ((u ** 2) * (np.sin(2 * theta))) / g

    plt.plot(x, y)
    plt.title('Trajectory of the Projectile')
    plt.xlabel('Horizontal Distance --->')
    plt.ylabel('Vertical Distance --->')
    plt.xlim([0, r_max + (r_max*0.2)])
    plt.ylim([0, h_max + (h_max*0.2)])
    plt.show()


if __name__ == '__main__':
    v = int(input("Enter velocity in m/s: "))
    a = int(input("Enter angle in degrees: "))
    projectile_motion(v, a)
