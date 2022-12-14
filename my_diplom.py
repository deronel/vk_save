import requests, pprint, urllib, json, datetime
from datetime import datetime
from urllib.parse import urljoin
from pprint import pprint

from VkAPI import VkAPI
from YaAPI import YaAPI


def init():
    y_token = input('YandexDisk token:')
    uid = input('VK user id:')
    gty = input("Number of photos to upload:")
    vk_api = VkAPI()
    ya_api: YaAPI = YaAPI(y_token)
    ya_api.upload(uid, vk_api.get_photos(uid, int(gty)))


if __name__ == '__main__':
    init()