# #Exercise 1
# #Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# class Statistics():
#     def __init__(self, data):
#         self.data = sorted(data)

#     def count(self):
#         return len(self.data)
    
#     def sum(self):
#         return sum(self.data)
    
#     def min(self):
#         return min(self.data)
    
#     def max(self):
#         return max(self.data)
    
#     def range(self):
#         return self.max() - self.min()
    
#     def mean(self):
#         return self.sum() / self.count()
    
#     def median(self):
#         index = (self.count() - 1) // 2

#         if (self.count() % 2):
#             return self.data[index]
#         else:
#             return (self.data[index] + self.data[index + 1]) / 2
        
#     def mode(self):
#         mode_dct = {}
#         for i in self.data:
#             mode_dct[i] = mode_dct.get(i, 0) + 1
#         max_count = max(mode_dct.values())
#         mode_values = [k for k, v in mode_dct.items() if v == max_count]
#         return mode_values, max_count
    
# stats = Statistics(ages)
    
# print('Count:', stats.count()) # 25
# print('Sum: ', stats.sum()) # 744
# print('Min: ', stats.min()) # 24
# print('Max: ', stats.max()) # 38
# print('Range: ', stats.range()) # 14
# print('Mean: ', stats.mean()) # 30
# print('Median: ', stats.median()) # 29
# print('Mode: ', stats.mode()) # {'mode': 26, 'count': 5}



#Exercise 2
# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
    
    def total_income(self):
        return sum(amount for amount, desc in self.incomes)
    
    def total_expense(self):
        return sum(amount for amount, desc in self.expenses)
    
    def account_info(self):
        print(self.firstname, self.lastname)

    def add_income(self, amount, description=''):
        self.incomes.append((amount, description))

    def add_expense(self, amount, desctiption=''):
        self.expenses.append((amount, desctiption))

    def account_balance(self):
        return self.total_income() - self.total_expense()