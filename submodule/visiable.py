import matplotlib.pyplot as plt
from matplotlib import style


def plt_3d(x, y, z, saveimage):
    style.use('ggplot')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x[1:], y[1:], z[1:], c='r', marker='o')  # 三个数组对应三个维度（三个数组中的数一一对应）
    ax.set_xlabel(x[0])
    ax.set_ylabel(y[0])
    ax.set_zlabel(z[0])
    plt.savefig(saveimage, bbox_inches='tight', dpi=2400)  # 保存图片，如果不设置 bbox_inches='tight'，保存的图片有可能显示不全
    plt.show()

def plt_all(element):
    plt_3d(element[0], element[1], element[2], "images/AlcoholDrinking_Stroke.jpg")
    plt_3d(element[0], element[1], element[3], "images/AlcoholDrinking_MentalHealth.jpg")
    plt_3d(element[0], element[2], element[3], "images/Stroke_MentalHealth.jpg")