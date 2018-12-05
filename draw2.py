from PIL import Image, ImageDraw
from math import cos, sin, pi
import imageio


RHO = 100
originalpoint = (250, 250)
theta0 = pi/6
def generateXY(rho, theta, XY, theta0):
    '''

    :param rho: given rho
    :param theta: given theta
    :param XY:  (float, float) -> original point
    :param theta0: direction of original point
    :return:(float, float) -> (x, y)
    '''
    x_1, y_1 = XY[0], XY[1]
    x = rho*cos(theta - theta0) + x_1
    y = rho*sin(theta - theta0) + y_1
    return (x, y)
dimtheta = 1000
k = 5
def flowerlist():
    dtheta = (2*pi)/dimtheta
    flowerlist_xy = []
    for i in range(dimtheta):
        r = RHO*sin(k*i*dtheta)
        flowerlist_xy.append(generateXY(r, dtheta*i, originalpoint, theta0))
    return flowerlist_xy

def draw(n):
    edgelist = []
    x_y = flowerlist()
    for i in range(dimtheta - 1):
        edgelist.append((x_y[i], x_y[i + 1]))

    img = Image.new('RGB', (500, 500), (230, 230, 230))
    draw = ImageDraw.Draw(img)

    for edge in edgelist[:n]:
        draw.line((edge[0], edge[1]), fill = (0, 200, 200))
    img.save("temp/flower_{0}.jpg".format(n))


def create_gif(gif_name):
    frames = []
    for i in range(200):
        img_name = "temp/flower_{0}.jpg".format(i*5)
        frames.append(imageio.imread(img_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.05)
    return


if(__name__ == "__main__"):
    for i in range(200):
        print("draw {0}".format(i))
        draw(i*5)
    create_gif("Hello_flower.gif")
