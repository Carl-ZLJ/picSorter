from PIL import Image
from PIL.ExifTags import TAGS
import os
import shutil


pic_formats = ['JPG', 'PNG', ]


def picture_exif(src, file_name):
    # print('begin')
    file_path = src + '\\' + file_name
    img = Image.open(file_path)
    # 获取图片exif信息
    exifdata = []
    if hasattr(img, '_getexif'):
        exifdata = img._getexif()
        # 获取日期
    ret = {}
    for tag, value in exifdata.items():
        decode = TAGS.get(tag, tag)
        ret[decode] = value
        # print('ret:{}'.format(ret))
    return ret


def copy_picture(src, dst, file_name):
    ret = picture_exif(src, file_name)
    # 以日期命名文件夹
    n = ret.get('DateTimeOriginal', 'None')
    old_file = src + '\\' + file_name
    dst_path = dst + '\\' + '{}-{}-{}'.format(n[0:4], n[5:7], n[8:10])
    new_file = dst_path + '\\' + file_name
    # 判断文件夹是否存在
    # 不存在
    if not os.path.exists(dst_path):
        # 创建文件夹 复制文件
        os.mkdir(dst_path)
        shutil.copyfile(old_file, new_file)
    # 存在
    else:
        # 文件不存在
        if not os.path.exists(file_name):
            # 复制文件
            shutil.copyfile(old_file, new_file)


def sort_by_date(src, dst):
    # 照片计数
    pic_counter = 0
    # 打开图片
    files = os.listdir(src)
    # print('begin:{}'.format(len(files)))
    for file in files:
        print(file)
        pic_counter += 1
        if file[-3:] in pic_formats:
            # print('file:{}'.format(file))
            copy_picture(src, dst, file)
            print('dealed_pictures dealed/pictures: {}/{}'.format(pic_counter, len(files)))


if __name__ == '__main__':
    # 路径
    src_pth = 'G:\\DCIM\\101PHOTO'
    # 目标路径
    dst_pth = 'F:\\Pictures'
    sort_by_date(src_pth, dst_pth)