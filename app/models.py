class Source:
  '''
  This class is for the source object
  '''

  def __init__(self, source_name, info, headline, link_to_site, image, date_written, daysSince):
    self.source_name = source_name
    self.info = info
    self.headline = headline
    self.link_to_site = link_to_site
    self.image = image
    self.date_written = date_written
    self.daysSince = daysSince
  

class Article:
  '''
  This class defines the Article objects
  '''

  def __init__(self, info, headline, link_to_site, image, date_written, daysSince):
    self.info = info
    self.headline = headline
    self.link_to_site = link_to_site
    self.image = image
    self.date_written = date_written
    self.daysSince = daysSince
