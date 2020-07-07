from fitsnap3.io.sections.sections import Section


class Scraper(Section):

    def __init__(self, name, config, args):
        super().__init__(name, config, args)
        self.scraper = self.get_value("SCRAPER", "scraper", "JSON")
        self.save_group_scrape = self.get_value("SCRAPER", "save_group_scrape", "None", "str")
        self.read_group_scrape = self.get_value("SCRAPER", "read_group_scrape", "None", "str")
        self.delete()