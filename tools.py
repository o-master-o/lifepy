import configparser


def log(comment, msg):
    print(comment, msg)


class AdvancedConfigParser(configparser.ConfigParser):

    def __init__(self):
        super().__init__()
        self.dict_config = {}

    def get_dict(self):
        di = dict(self._sections)
        for key in di:
            di[key] = dict(self._defaults, **di[key])
            di[key].pop('__name__', None)
        self.dict_config = di
        return di

    # def filter_dict(self, chosen=[]):
    #     return {k: v for k, v in self.dict_config.items() if v[0] < 5 and v[1] < 5}
