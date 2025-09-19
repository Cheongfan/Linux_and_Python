import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from scipy.datasets import face  # 用于获取示例图像
import os

# 创建一个简单的示例图像（黑白渐变）
def create_gradient_image():
    image = np.zeros((100, 100))
    for i in range(100):
        image[i, :] = i / 100.0
    return image

# 显示图像
def display_images(images, titles, cmap='gray'):
    plt.figure(figsize=(15, 5))
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(image, cmap=cmap)
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# 处理指定图像文件
def process_custom_image(image_filename):
    """
    处理用户指定的图像文件

    参数:
    image_filename: 要处理的图像文件名（可以包含路径）
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(image_filename):
            print(f"错误: 文件 '{image_filename}' 不存在")
            print(f"当前工作目录: {os.getcwd()}")
            print(f"目录中的文件: {os.listdir('.')}")
            return

        # 读取图像
        image = plt.imread(image_filename)
        print(f"成功读取图像: {image_filename}")
        print(f"图像形状: {image.shape}")

        # 如果图像是彩色的，转换为灰度
        if len(image.shape) == 3:
            gray_image = np.mean(image, axis=2)
            print("已将彩色图像转换为灰度图像")
        else:
            gray_image = image

        # 应用高斯模糊
        blurred_image = ndimage.gaussian_filter(gray_image, sigma=2)

        # 应用中值滤波器去噪
        median_image = ndimage.median_filter(gray_image, size=3)

        # 应用边缘检测
        sobel_image = ndimage.sobel(gray_image)

        # 显示结果
        display_images([gray_image, blurred_image, median_image, sobel_image],
                       ['原始图像', '高斯模糊', '中值滤波', '边缘检测'])

    except Exception as e:
        print(f"处理图像时出错: {e}")

# 主程序
def main():
    # 方法1: 创建渐变图像
    print("创建并处理渐变图像...")
    image = create_gradient_image()

    # 使用Scipy进行高斯模糊处理
    blurred_image = ndimage.gaussian_filter(image, sigma=2)

    # 使用Scipy进行旋转处理
    rotated_image = ndimage.rotate(image, angle=45, reshape=False)

    # 显示结果
    display_images([image, blurred_image, rotated_image],
                   ['原始图像', '高斯模糊后', '旋转45度后'])

    # 方法2: 处理用户指定的图像文件
    print("\n处理自定义图像文件...")

    # 指定要处理的图像文件名
    # 修改这里的文件名以处理您自己的图像
    image_filename = "example.png"  # 使用正确的文件名

    # 处理指定图像
    process_custom_image(image_filename)

    # 方法3: 使用Scipy自带的示例图像（如果自定义图像处理失败）
    try:
        print("\n处理Scipy示例图像...")
        # 获取Scipy示例图像
        color_image = face()

        # 转换为灰度图像
        gray_image = np.mean(color_image, axis=2)

        # 应用边缘检测滤波器
        sobel_image = ndimage.sobel(gray_image)

        # 应用中值滤波器去噪
        median_image = ndimage.median_filter(gray_image, size=3)

        # 显示结果
        display_images([color_image, sobel_image, median_image],
                       ['Scipy示例图像', 'Sobel边缘检测', '中值滤波去噪'],
                       cmap=None)  # 对于彩色图像不使用colormap

    except Exception as e:
        print(f"处理Scipy示例图像时出错: {e}")

if __name__ == "__main__":
    main()