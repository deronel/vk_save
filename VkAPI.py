from urllib.parse import urljoin

import requests

from Photo import Photo


class VkAPI:
    BASE_URL = "https://api.vk.com/method/"

    @staticmethod
    def find_largest(sizes):
        sizes_chart = ['x', 'z', 'y', 'r', 'o', 'x', 'm', 's']
        for chart in sizes_chart:
            for size in sizes:
                if size['type'] ==chart:
                    return size

    def __init__(self):
        self.token = 'vk1.a.lsXUxJyMP5hq9hcVeGUKAfyz3zjIgEEyqaptdnrE7lvHbkQmzpALmqHKLKfb8bUkq7X0NCEozU8cM_7Gh7I71UcopREbQhs53k5-JI9ZrToP4SPe5tuop461QLnDnpckN2lOzd-4q7OhYDgt9x7nvp84JoxeQbQeCSECJcrnqbCsmKq-GrMP4XTfO4zQ8jQU-7uJ03abTJg5VW-CaNXU6g&expires_in=0&user_id=301757361'
        self.version = '5.124'


    def get_photos(self, uid, gty=5):
        get_url = urljoin(self.BASE_URL, params={
         'access_token': self.token,
         'v': self.version,
         'owner_id': uid,
         'album_id': 'profile',
         'photo_sizes': 1,
         'extended': 1
        }).json().get('response').get('items')

        return sorted([Photo(photo.get('date'),
                             photo.get('likes')['count'],
                             self.find_largest(photo.get('sizes'))) for photo in resp],
                      key=lambda p: p.maxsize, reverse=True)[:qty]



