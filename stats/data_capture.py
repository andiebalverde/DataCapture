from stats.stats import Stats

class DataCapture:
    def __init__(self):
        self.myarr = {}
        self.max = 0

    def add(self, new_int):
        if new_int not in self.myarr:
            self.myarr[new_int] = 1
        else:
            self.myarr[new_int] += 1
        if new_int > self.max:
            self.max = new_int

    def build_stats(self):
        count_dict = {}
        current_count = 0
        for i in range(self.max + 1):
            if i in self.myarr:
                count_dict[i] = self.myarr[i] + current_count
                current_count = count_dict[i]
            else:
                count_dict[i] = current_count

        return Stats(count_dict, self.max)

    def _repr_(self):
        return f"build_stats is {self.myarr}"