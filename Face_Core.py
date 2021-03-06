import requests
import base64

URL = "https://api-cn.faceplusplus.com/facepp/v3/detect"
Key = ""  # 此处填写上你在Face++上申请的API_Key
Secret = ""  # 此处填写上你在Face++上申请的API_Secret


def getpicbase64(path):
    file = open(path, mode="rb")
    code = base64.b64encode(file.read())
    file.close()
    return code


def GetFaceToken(picpath):
    info = {"api_key": Key, "api_secret": Secret, "image_base64": getpicbase64(picpath)}
    response = requests.post(url=URL, data=info)
    return response.json()["faces"][0]["face_token"]



