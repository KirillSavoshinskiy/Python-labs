import unittest
import json
from json_parse import json_parse
from N_demiss_vector import NVector
from Large_file_sort import Large_file_sort


b = True
data_list = [11, 3, 5, 'Hello']
data_dict = {'h': [1, 22, "3"], 't': 2, '2': 'ree'}
data_str = 'hello'
data_int = 1234
data_tuple = tuple('hello')
vect = NVector([1, 2, 3, 4])
data_erorr = "ewsd"
sort = Large_file_sort()
arr = []
with open('numbers.txt', 'r') as file:
    for line in file:
        arr.append(int(line))

test_vect = NVector([2, 4, 6, 8])

class test(unittest.TestCase):

    def test_to_json(self):
        self.assertEqual(json.dumps(b), json_parse().to_json(b))
        self.assertEqual(json.dumps(data_list), json_parse().to_json(data_list))
        self.assertEqual(json.dumps(data_dict), json_parse().to_json(data_dict))
        self.assertEqual(json.dumps(data_str), json_parse().to_json(data_str))
        self.assertEqual(json.dumps(data_int), json_parse().to_json(data_int))
        self.assertEqual(json.dumps(data_tuple), json_parse().to_json(data_tuple))

    def test_loads(self):
        data = json.dumps(data_list)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(data_dict)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(data_str)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(data_int)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        data = json.dumps(data_tuple)
        self.assertEqual(json.loads(data), json_parse().loads(data))
        try:
            a = json.loads(data_erorr)
        except BaseException:
            a = None
        self.assertEqual(a, json_parse().loads(data_erorr))

    def test_vector(self):
        self.assertEqual(test_vect.__str__(), (vect + [1, 2, 3, 4]).__str__())
        test_vect + [1, 2, 3, 4]
        self.assertEqual(test_vect.__str__(), (vect + [1, 2, 3, 4]).__str__())
        test_vect * [0, 0, 0, 0]
        self.assertEqual(test_vect.__str__(), (vect * [0, 0, 0, 0]).__str__())
        self.assertEqual(4, vect.__len__())
        self.assertEqual(test_vect.__str__(), vect.__const_mull__(1).__str__())

    def test_large_sort(self):
        self.assertEqual(arr.sort(), sort.sort('numbers.txt'))