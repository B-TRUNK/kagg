import numpy as np

# in python. data types prioritized from high to low as follows:
# 1 - complex > float > int > bool
float_vector = np.array([1, 2., 3])
print('auto_coverted_vector = ', float_vector)
print()

# 2 - to specify data type at creation time
str_vector = np.array(float_vector, dtype=str)
print('str_vector = ',str_vector)
print()

# 3 - to convert data types, use the astype method
int_vector = float_vector.astype(int)
print('int_vector = ', int_vector)
print()

# 4 - Find dimensions of an array
print('float_vector dimensions = ', float_vector.ndim)

# Find shape of an array
print('float_vector shape = ', float_vector.shape)

# Find size of an array
print('float_vector size = ', float_vector.size)
print()

# Find data type of an array
print('float_vector data type = ', float_vector.dtype)
print()

# Create a Full Vector
full_vector = np.full((5,), 7)
print('full_vector = ', full_vector)
print()


# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print('2D_matrix = \n', matrix)
print('2D_matrix dimensions = ', matrix.ndim)
print('2D_matrix shape = ', matrix.shape)
print('2D_matrix size = ', matrix.size)
print('2D_matrix data type = ', matrix.dtype)
print()

# Create a 3D array
tensor_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print('3D_tensor = \n', tensor_3d)
print('3D_tensor dimensions = ', tensor_3d.ndim)
print('3D_tensor shape = ', tensor_3d.shape)
print('3D_tensor size = ', tensor_3d.size)
print('3D_tensor data type = ', tensor_3d.dtype)
print()

# Create a Zeroes Vector
zeroes_vector = np.zeros(5)
print('zeroes_vector = ', zeroes_vector)
print()

# Create a Zeroes Matrix
zeroes_matrix = np.zeros((3, 4))
print('zeroes_matrix = \n', zeroes_matrix)
print()

# Create a Ones Vector
ones_vector = np.ones(5)
print('ones_vector = ', ones_vector)
print()

# Create a Ones Matrix
ones_matrix = np.ones((2, 3))
print('ones_matrix = \n', ones_matrix)
print()

# Create a Identity Matrix
identity_matrix = np.eye(4)
print('identity_matrix = \n', identity_matrix)
print()

# Create a Random Vector
random_vector = np.random.rand(5)
print('random_vector = ', random_vector)
print()

# Create a Random Matrix
random_matrix = np.random.rand(3, 3)
print('random_matrix = \n', random_matrix)
print()

# Create a Random Integer Vector
random_int_vector = np.random.randint(0, 10, size=5)
print('random_int_vector = ', random_int_vector)
print()

# Create a Random Integer Matrix
random_int_matrix = np.random.randint(0, 10, size=(2, 4))
print('random_int_matrix = \n', random_int_matrix)
print()

# Create a Sequence Vector using arange
sequence_vector = np.arange(0, 10, 2)
print('sequence_vector = ', sequence_vector)
print()

# Create a Linearly Spaced Vector using linspace
linspace_vector = np.linspace(0, 1, 5)
print('linspace_vector = ', linspace_vector)
print()

# Reshape a Vector into a Matrix
reshaped_matrix = sequence_vector.reshape(5, 1)
print('reshaped_matrix = \n', reshaped_matrix)
print()

# Flatten a Matrix into a Vector
flattened_vector = matrix.flatten()
print('flattened_vector = ', flattened_vector)
print()

# Transpose a Matrix
transposed_matrix = matrix.T
print('transposed_matrix = \n', transposed_matrix)
print() 

# Slicing a Vector
sliced_vector = float_vector[1:3]
print('sliced_vector = ', sliced_vector)
print()

# Slicing a Matrix
sliced_matrix = matrix[0:2, 1:3]
print('sliced_matrix = \n', sliced_matrix)
print()

# Accessing Elements in a 3D Tensor
element_3d = tensor_3d[1, 0, 1]
print('element_3d = ', element_3d)
print()

# Boolean Indexing
bool_indexed_vector = float_vector[float_vector > 1.5]
print('bool_indexed_vector = ', bool_indexed_vector)
print()

# Fancy Indexing
fancy_indexed_vector = float_vector[[0, 2]]
print('fancy_indexed_vector = ', fancy_indexed_vector)
print()

# Basic Arithmetic Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print('a + b = ', a + b)
print('a - b = ', a - b)
print('a * b = ', a * b)
print('a / b = ', a / b)
print()

# Matrix Multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print('matrix_product = \n', matrix_product)
print()

# Statistical Operations
data = np.array([1, 2, 3, 4, 5])
print('mean = ', np.mean(data))
print('median = ', np.median(data))
print('std deviation = ', np.std(data))
print('sum = ', np.sum(data))
print('min = ', np.min(data))
print('max = ', np.max(data))   
print()

# Save and Load Numpy Arrays
np.save('array.npy', data)
loaded_data = np.load('array.npy')
print('loaded_data = ', loaded_data)
print()

# Copy vs View
original_array = np.array([1, 2, 3])
copied_array = original_array.copy()
viewed_array = original_array.view()    
original_array[0] = 10
print('original_array = ', original_array)
print('copied_array = ', copied_array)
print('viewed_array = ', viewed_array)
print()

# Broadcasting Example
vector = np.array([1, 2, 3])
matrix = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
broadcasted_sum = matrix + vector
print('broadcasted_sum = \n', broadcasted_sum)
print()

# Universal Functions (ufuncs)
angles = np.array([0, np.pi/2, np.pi])
sine_values = np.sin(angles)
print('sine_values = ', sine_values)
print()

# Conditional Operations
conditional_result = np.where(data > 3, data * 2, data - 2)
print('conditional_result = ', conditional_result)
print()

# Stacking Arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
stacked_array = np.vstack((array1, array2))
print('stacked_array = \n', stacked_array)
print()

# Splitting Arrays
split_arrays = np.array_split(data, 2)
print('split_arrays = ', split_arrays)
print()

# Unique Elements
unique_elements = np.unique(np.array([1, 2, 2, 3, 4, 4, 5]))
print('unique_elements = ', unique_elements)    
print()

# Set Random Seed for Reproducibility
np.random.seed(42)
random_numbers = np.random.rand(3)
print('random_numbers with seed = ', random_numbers)
print()

# Save Multiple Arrays
array_a = np.array([1, 2, 3])   
array_b = np.array([4, 5, 6])
np.savez('multiple_arrays.npz', array_a=array_a, array_b=array_b)
loaded_arrays = np.load('multiple_arrays.npz')
print('loaded_arrays array_a = ', loaded_arrays['array_a'])
print('loaded_arrays array_b = ', loaded_arrays['array_b'])
print()

# Memory Layout
contiguous_array = np.ascontiguousarray(np.array([[1, 2], [3, 4]]).T)
print('contiguous_array flags = \n', contiguous_array.flags)
print()

# Advanced Indexing with np.ix_
row_indices = np.array([0, 1])
col_indices = np.array([1, 2])
ix_matrix = matrix[np.ix_(row_indices, col_indices)]
print('ix_matrix = \n', ix_matrix)
print()

# Some Statistical Functions
# random.normal examples

a = np.random.normal(0, 1, (3, 4))
print('a = \n', a)
print()

normal_dist_samples = np.random.normal(loc=0.0, scale=1.0, size=5)
print('normal_dist_samples = ', normal_dist_samples)
print()


# End of numpy tutorial code

