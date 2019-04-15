import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):

    def setup(self):

        self.new_news = News('Bitcoin Article','All articles about Bitcoin from the last month, sorted by recent first','https://newsapi.org/v2/everything?q=bitcoin&from=2019-03-14&sortBy=publishedAt&apiKey=API_KEY')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
    unittest.main()            