class Photo:
    name = '030.jpg'

    def __init__(self, date, likes, sizes ):
        self.data = date
        self.likes =likes
        self.sizes = sizes
        self.size_type = sizes['type']
        self.url = sizes['url']
        self.maxsize = max(sizes['width'], sizes['height'])


    def __repr__(self):
        return f'date: {self.date},likes: {self.likes}, size: {self.maxsize}, url{self.url}'