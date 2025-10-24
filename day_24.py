# To summarize, the main differences with python lists are:

#     Arrays support vectorized operations, while lists don’t.
#     Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
#     Every array has one and only one dtype. All items in it should be of that dtype.
#     An equivalent numpy array occupies much less space than a python list of lists.
#     numpy arrays support boolean indexing.




import numpy as np

#Creating int numpy arrays
python_list = [1,2,3,4,5]
numpy_array_from_list = np.array(python_list)
# print(type(numpy_array_from_list)) #checking list type
# print(numpy_array_from_list) #[1 2 3 4 5]


#Creating float numpy arrays
numpy_array_from_list_float = np.array(python_list, dtype=float)
# print(numpy_array_from_list_float) #[1. 2. 3. 4. 5.]


#Creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
# print(numpy_bool_array) #[False  True  True False False]


#Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
# print(numpy_two_dimensional_list) 
#[[0 1 2]
# [3 4 5]
# [6 7 8]]


#Converting numpy array to list
np_to_list = numpy_array_from_list.tolist()
# print(np_to_list)


#Creating numpy array from tuple
python_tuple = (1, 2, 3, 4, 5) #tuple
numpy_array_from_tuple = np.array(python_tuple)
# print(type(numpy_array_from_tuple)) #<class 'numpy.ndarray'>
# print(numpy_array_from_tuple) #[1 2 3 4 5]


#.shape Shape of numpy array - returns the size of mltidimensional list (first row, second columns). If the array is just one dimensional it returns it's size
nums = np.array([1,2,3,4,5])
# print(nums.shape) #(5,)
# print(numpy_two_dimensional_list.shape) #(3, 3)


#.dtype Data type of numpy array - str, int, float, complex, bool, list, None
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
# print(int_array.dtype) #int64
# print(float_array.dtype) #float64


#.size Size of the numpy array
# print(numpy_array_from_list.size) #5
# print(numpy_two_dimensional_list.size) #9



#Mathematical operation - using numpy we can do mathematical operations on lists without using loops
#Addition
ten_plus_original = numpy_array_from_list + 10
# print(ten_plus_original) #[11 12 13 14 15]

#Subtraction
ten_minus_original = numpy_array_from_list - 10
# print(ten_minus_original) #[-9 -8 -7 -6 -5]

#Multiplication
ten_times_original = numpy_array_from_list * 10
# print(ten_times_original) #[10 20 30 40 50]

#Division
ten_divided_original = numpy_array_from_list / 10
# print(ten_divided_original) #[0.1 0.2 0.3 0.4 0.5]

#Modulus
ten_modulus_original = numpy_array_from_list % 3
# print(ten_modulus_original) #[1 2 0 1 2] - reminder after division

#Floor division
ten_floor_original = numpy_array_from_list // 3
# print(ten_floor_original) #[0 0 1 1 1] - how many times 3 can fit in the number

#Exponential
ten_exponential_original = numpy_array_from_list ** 2
# print(ten_exponential_original) #[ 1  4  9 16 25] - a^2



#Getting items from a numpy array
first_row = numpy_two_dimensional_list[0]
second_row = numpy_two_dimensional_list[1]
third_row = numpy_two_dimensional_list[2]
# print(first_row) #[0 1 2]
# print(second_row) #[3 4 5]
# print(third_row) #[6 7 8]

first_column = numpy_two_dimensional_list[:,0]
second_column = numpy_two_dimensional_list[:,1]
third_column = numpy_two_dimensional_list[:,2]
# print(first_column) #[0 3 6]
# print(second_column) #[1 4 7]
# print(third_column) #[2 5 8]


#Slicing numpy array
first_two_rows_and_columns = numpy_two_dimensional_list[0:2, 0:2]
# print(first_two_rows_and_columns) #[[0 1]
                                    # [3 4]]

#Reversing rows in whole array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# print(two_dimension_array[::]) #it stays the same

#Reverse the row and column position
# print(two_dimension_array[::-1, ::-1])
#[[9 8 7]
#  [6 5 4]
#  [3 2 1]]


#.zeroes Array filled with zeros
numpy_zeros = np.zeros((3,3), dtype=int, order='C') #C - array is stored row by row, F - array is stored column by column
# print(numpy_zeros)
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

#.ones Array filled with ones
numpy_ones = np.ones((3,3), dtype=int, order='C')
# print(numpy_ones)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

# Array filled with twoes
twoes = numpy_ones * 2
# print(twoes)
# [[2 2 2]
#  [2 2 2]
#  [2 2 2]]

#.reshape Reshape the array
first_shape = np.array([(1,2,3), (4,5,6)])
reshaped = first_shape.reshape(3,2)
# print(reshaped)
# [[1 2]
#  [3 4]
#  [5 6]]

#.flatten Flatten the array
flattened = reshaped.flatten()
# print(flattened) #[1 2 3 4 5 6]

#.random Generate random float
random_float = np.random.random()
# print(random_float) #0.4896825429428855
random_floats = np.random.random(5) #array od random floats
# print(random_floats) #[0.99814195 0.91047266 0.98754423 0.17714966 0.54627031]

#Generate random int
random_int = np.random.randint(0, 11) #(0, 11) - between those numbers
# print(random_int) #3
random_ints = np.random.randint(0,11, size=4) #between 0 and 11 and 4 times
# print(random_ints) #[4 6 3 5]
random_ints_array = np.random.randint(2,10, size=(3,3)) #between 2,10, do it 3 times, 3 items per list
# print(random_ints_array)
# [[9 5 5]
#  [4 8 7]
#  [9 7 3]]

#Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
# print(four_by_four_matrix)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]


#Numpy arrange
lst = range(0, 11, 2) #starting, stop, step
# for i in lst:
#     print(i)
# 0 2 4 6 8 10

whole_numbers = np.arange(0, 20, 1) #start, stop, step
# print(whole_numbers) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

#linear algebra
#dot product - product of two arrays
f = np.array([1, 2, 3])
g = np.array([4, 5, 6])
#1*4 + 2*5 +3*6
# print(np.dot(f, g)) #32