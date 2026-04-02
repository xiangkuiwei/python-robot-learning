"""
涉及到API:
    imshow() 基于HWC 展示图像
    imread() 读取图像 获取HWC
    imsave() 基于HWC 保存图片
"""
# 导包
import numpy as np
import matplotlib.pyplot as plt
import torch

# 1.定义函数 绘制黑白 全白图
def dm01():
    # 1.定义全黑图像 像素点越接近0越黑 越接近255越白
    img1 = np.zeros((200,200,3))
    print(f'img1:{img1}')

    # 绘制图像
    plt.imshow(img1)
    plt.show()

    # 2.定义全白图片
    img2 = torch.full(size=(200,200,3),fill_value=255)
    plt.imshow(img2)
    plt.show()


# 定义函数 加载图片
def dm02():
    # 1.加载图片
    img1 = plt.imread('./data/img.jpg')
    # print(f'img1:{img1}')
    # print(f'img1.shape:{img1.shape}')

    # 2.保存图片
    plt.imsave('./data/img_copy.png',img1)

    # 3.展示图像
    plt.imshow(img1)
    plt.show()



# 测试
if __name__ == '__main__':
    # dm01()
    dm02()