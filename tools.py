import configparser


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

    def get_filtered_dict(self, filter_list=None):
        if not self.dict_config:
            self.get_dict()
        if filter_list:
            filter_list = force_to_list(filter_list)
            di = {}
            for k in self.dict_config:
                if k in filter_list:
                    di.update({k: self.dict_config[k]})
            return di
        else:
            return self.dict_config


def log(comment, msg):
    print(comment, msg)


def force_to_list(parameter):
    return [parameter] if not isinstance(parameter, list) else parameter


# def change_list_elements_type(input_list, type='int'):
    # fn = getattr(bui, type, None)
    # if callable(fn):
    #     fn()
    # return [type(i) for i in input_list]
