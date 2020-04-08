class cache:

    def __init__(self, func):
        self.func_to_decorate = func
        self.my_dict = dict()

    def __call__(self, *args):
        for key, value in self.my_dict.items():
            if value == args:
                return key
        res = self.func_to_decorate(*args)
        self.my_dict[res] = args
        return res


class json_parse(object):
    symbols = [' ', '{', '}', '":"']

    @classmethod
    def to_json(cls, value):
        if isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, str):
            return f"\"{value}\""
        elif isinstance(value, int) or isinstance(value, float):
            return f"{str(value)}"
        elif isinstance(value, list) or isinstance(value, tuple):
            return cls.__collection_to_json(value)
        elif isinstance(value, dict):
            return cls.__dict_to_json(value)
        elif value is None:
            return 'null'

    @classmethod
    @cache
    def __check_item(cls, item):
        if isinstance(item, str):
            return f"\"{item}\""
        elif isinstance(item, bool):
            return str(item).lower()
        elif isinstance(item, int) or isinstance(item, float):
            return str(item)
        elif isinstance(item, list) or isinstance(item, tuple):
            return cls.__collection_to_json(item)
        elif isinstance(item, type(None)):
            return 'null'

    @classmethod
    def __collection_to_json(cls, collect):
        if isinstance(collect, list) or isinstance(collect, tuple):
            return cls.__tuple_list_to_json(collect)

    @classmethod
    def __tuple_list_to_json(cls, collect):
        res = ''
        count = 0
        for i in collect:
            count += 1
            if len(collect) != count:
                res += cls.__check_item(i) + ',' + ' '
            else:
                res += cls.__check_item(i)
        return f"[{res}]"

    @classmethod
    def __dict_to_json(cls, dict_collect):
        res = ''
        count = 0
        for k, v in dict_collect.items():
            count += 1
            key = cls.__check_item(k)
            if len(dict_collect) != count:
                res += key + ':' + ' ' + cls.__check_item(v) + ',' + ' '
            else:
                res += key + ':' + ' ' + cls.__check_item(v)
        return f"{cls.symbols[1]}{res}{cls.symbols[2]}"

    @staticmethod
    def loads(json_str):
        try:
            return eval(json_str.replace('true', 'True').replace('false', 'False').replace('null', 'None'))
        except BaseException:
            return


