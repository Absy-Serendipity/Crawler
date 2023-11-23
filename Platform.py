class Platform:
    def __init__(self):
        self.platformName = None
        self.day = None
        self.webtoonList = []
    
    def addWebtoon(self, webtoon):
        self.webtoonList.append(webtoon)
    
    def setDay(self, day:str):
        self.day = day
    
    def setName(self, platformName:str):
        self.platformName = platformName

    