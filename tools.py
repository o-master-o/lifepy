import configparser
import pprint as pp


class AdvancedConfigParser(configparser.ConfigParser):

    def __init__(self):
        super().__init__()
        self.dict_config = {}
        self.filtered_dict_config = {}

    def filter_dict(self, filter_list=None, auto_type=True):
        if not self.dict_config:
            self.get_dict(auto_type)
        if filter_list:
            filter_list = self.force_to_list(filter_list)
            self.filtered_dict_config.update({k: v for k, v in self.dict_config.items() if k in filter_list})
        return self.filtered_dict_config

    def get_dict(self, auto_type=True):
        clear_dict_config = self.__ordered_dict_to_dict()
        if auto_type:
            self.dict_config.update(self.__dict_config_auto_type(clear_dict_config))
        else:
            self.dict_config.update(clear_dict_config)
        return self.dict_config

    def __ordered_dict_to_dict(self):
        dict_config = dict(self._sections)
        return {k: dict(self._defaults, **dict_config[k]) for k in dict_config}

    def __dict_config_auto_type(self, data):
        return {section: self.__sub_dict_auto_type(sub_dict) for section, sub_dict in data.items()}

    def __sub_dict_auto_type(self, dict_config):
        return {k: self.__auto_type(v) for k, v in dict_config.items()}

    def __auto_type(self, untyped_str):
        for fn in (self.__boolify, self.__listify, int, float):
            try:
                typed_str = fn(untyped_str)
                return typed_str
            except ValueError:
                pass
        return untyped_str

    def __boolify(self, untyped):
        if untyped == 'True':
            return True
        if untyped == 'False':
            return False
        raise ValueError("It is not bool Type")

    def __listify(self, untyped):
        if untyped[0] == '[' and untyped[-1] == ']':
            listified = untyped[1: -1].split(',')
            for i, item in enumerate(listified):
                listified[i] = self.__auto_type(item)
            return listified
        raise ValueError("It is not list")

    @staticmethod
    def force_to_list(parameter):
        return [parameter] if not isinstance(parameter, list) else parameter


def log(comment, msg):
    print(comment, msg)
