import logging

from qiniu import Auth, put_data

# 需要填写你的 Access Key 和 Secret Key
access_key = 'oVkYb9iCeL8UWJEhrfb6An-tYG8P_GZT8WwSXXZ0'
secret_key = 'Bf6oSGkgQZmh822i6DGI5H_HIaNRBuepeRN4yr5B'

# 要上传的空间
bucket_name = 'xuanli'


def storage(data, key):
    """七牛云存储上传文件接口,data图片，key名字"""
    if not data:
        return None
    if not key:
        return None
    try:
        # 构建鉴权对象
        q = Auth(access_key, secret_key)

        # 生成上传 Token，可以指定过期时间等
        token = q.upload_token(bucket_name)

        # 上传文件
        ret, info = put_data(token, key, data)

    except Exception as e:
        logging.error(e)
        raise e

    if info and info.status_code != 200:
        logging.error("上传文件到七牛失败，状态码：%s" % info.status_code)
        raise Exception("上传文件到七牛失败")

    # 返回七牛中保存的图片名，这个图片名也是访问七牛获取图片的路径
    return ret["key"]


if __name__ == '__main__':
    file_name = input("输入上传的文件")
    with open(file_name, "rb") as f:
        storage(f.read(), 'text')
