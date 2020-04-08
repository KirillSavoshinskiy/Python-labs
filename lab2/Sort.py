
class Sorting(object):

    def merge_sort(self, array):
        if len(array) < 2:
            return array
        else:
            middle = int(len(array) / 2)
            left = self.merge_sort(array[:middle])
            right = self.merge_sort(array[middle:])
            return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

