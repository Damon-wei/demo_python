# PIL
# 强大的图像处理库
# 在命令行下直接通过pip安装：
# $ pip install pillow
from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random

# 图像缩放模糊处理等操作：
def option_image():
    # 打开一个jog图像文件
    im = Image.open('test.jpg')
    # 获得图像尺寸
    w, h = im.size
    print('Original image to: %s x %s' % (w, h))
    im.thumbnail((w // 2, h // 2))
    # 缩放到50%:
    print('Resize image to: %s x %s' % (w // 2, h // 2))
    # 应用模糊滤镜:
    im = im.filter(ImageFilter.BLUR)
    # 把缩放后的图像用jpeg格式保存:
    im.save('thumbnail.jpg', 'jpeg')


# 生成验证码：
def code_image():
    # 随机字母
    def randomChar():
        return chr(random.randint(65, 90))

    # 随机颜色1
    def randomColor1():
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 随机颜色2
    def randomColor2():
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象
    font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
    # 创建Draw对象
    draw = ImageDraw.Draw(image)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randomColor1())
    # 输出文字
    for t in range(4):
        draw.text((60 * t + 10, 10), randomChar(), font=font, fill=randomColor2())
    # 模糊处理
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

code_image()

