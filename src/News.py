

class News():

    def set_title(self, title):
        self.title=title

    def set_summary(self, summary):
        self.summary=summary

    def set_link(self, link):
        self.link=link
    
    def set_published_date(self, pubdate):
        self.published_date=pubdate

    def set_sentiment(self,sentiment):
        self.sentiment=sentiment
    
    def get_sentiment(self):
        return self.sentiment

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title