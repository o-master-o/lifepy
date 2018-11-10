import pprint as pp
import json


class JSONConfigParser(object):

    def __init__(self):
        self.configuration = {}

    def read(self, *config_files):
        for file_name in config_files:
            if isinstance(file_name, str):
                try:
                    with open(file_name) as json_data_file:
                        self.configuration.update(json.load(json_data_file))
                except OSError:
                    continue

    def filter_dict(self, filter_list=None):
        if filter_list:
            filter_list = self.force_to_list(filter_list)
        return {k: v for k, v in self.configuration.items() if k in filter_list}

    @staticmethod
    def force_to_list(parameter):
        return [parameter] if not isinstance(parameter, list) else parameter


def auto_type(self, untyped_str):
    for fn in (self._boolify, self._listify, int, float):
        try:
            typed_str = fn(untyped_str)
            return typed_str
        except ValueError:
            pass
    return untyped_str


def _boolify(self, untyped):
    if untyped == 'True':
        return True
    if untyped == 'False':
        return False
    raise ValueError("It is not bool Type")


def _listify(self, untyped):
    if untyped[0] == '[' and untyped[-1] == ']':
        listified = untyped[1: -1].split(',')
        for i, item in enumerate(listified):
            listified[i] = self.auto_type(item)
        return listified
    raise ValueError("It is not list")


def log(comment, msg):
    print(comment, msg)
