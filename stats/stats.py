class Stats:
    def __init__(self, count_dict, number_of_items):
        self.count_dict = count_dict
        self.number_of_items = number_of_items

    def greater(self, limit):
        if limit > self.number_of_items:
            return 0
        return self.count_dict[self.number_of_items] - self.count_dict[limit]

    def less(self, limit):
        if limit > self.number_of_items:
            return self.count_dict[self.number_of_items]
        elif limit < 1:
            return 0
        return self.count_dict[limit-1]

    def between(self, limit_low, limit_high):
        return self.less(limit_high+1) - self.less(limit_low)

