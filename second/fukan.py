import matplotlib.pyplot as plt
import math


"""
Genelate fula
"""


def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment

    return numbers


"""
Draw the trajectory of a body in projectlie motion
"""


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.title("Projectile motion of a ball")


def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g
    # find time intervals
    intervals = frange(0, t_flight, 0.0001)
    # list of x and y
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)

    draw_graph(x, y)


if __name__ == "__main__":
    try:
        u = float(input("Enter the intial velocity (m/s): "))
        theta = float(input("Enter the angele of projection (degrees): "))
    except ValueError:
        print("You enterd an invalid input")
    else:
        draw_trajectory(u, theta)
        plt.show()
