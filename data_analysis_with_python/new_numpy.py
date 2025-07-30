import numpy as np

# Creating array using numpy
"""1D array."""

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1)) # <class 'numpy.ndarray'> tells that it is 'n' dimensional array.
print(arr1.shape)


"""2D array."""
reshaped_arr = arr1.reshape(1,5) # returns new array doesn't change the original one.
# (1,5) (no. of rows x no. of columns)

print(reshaped_arr)
print(reshaped_arr.shape)

reshaped_arr = arr1.reshape(5,1)
print(reshaped_arr)
print(reshaped_arr.shape)

# similar to 'arr1.reshape(1,5)'.
arr1 = np.array([[1,2,3,4,5]])
print(arr1.shape)


arr2 = np.array([[1,2,3,4,5], [2,3,4,5,6]])
print(arr2)
print(arr2.shape)


arr3 = np.arange(0,10,2).reshape(5,1)
print(arr3)

ones= np.ones((3,4)) # Be careful about paranthesis.
print(ones)

zeros= np.zeros((3,4)) # Be careful about paranthesis.
print(zeros)

eye= np.eye(4) # Identity matrix/ Unit matrix
print(eye)




# Creating a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array:\n", arr)
print("Shape:", arr.shape)              # Output: (2, 3)
print("Number of dimensions:", arr.ndim)  # Output: 2 (dimension)
print("Size (number of elements):", arr.size)  # Output: 6
print("Data type:", arr.dtype)          # Output: int64 (may vary based on plateform)
print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on plateform)





# Numpy vectorized operation.
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)


# Universal function
arr1 = np.array([1,2,3,4,5])
print(np.sqrt(arr1)) # Squre root
print(np.exp(arr1)) # Exponential
print(np.sin(arr1)) # Sine
print(np.log(arr1)) # Natural log


# Array slicing and indexing operations.
# Indexing starts with zero.
"""While the data looks like a matrix, slicing in NumPy is done in the style of nested lists, not linear algebra."""
arr1 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
print(arr1)

print(arr1[0])
print(arr1[0][0])
print(arr1[1][3])
print(arr1[1,2]) # when accessing single elemenr (row 1 and column 2 element is 4.)
print(arr1[1:]) 
print(arr1[1:, 2:]) # arr[start_row:end_row, start_col:end_col](end_row, end_col are exclusive)
print(arr1[0:2, 2:]) # 0:2 → Select rows 0 and 1 ||| 2: → Select columns from index 2 to end (i.e., columns 2 and 3)
print(arr1[1:,1:3])
# Hint: Slice like nested list.


# Modify array elements.
arr1[0,0]=100
print(arr1)
arr1[1:]=100
print(arr1)


# Statistical concepts ---> Normalization.
# To have a mean of 0 and standard daviation of 1.
data = np.array([1, 2, 3, 4, 5])

# Calculate the mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Normalize the data
normalized_data = (data - mean) / std_dev
print("Normalized data:", normalized_data)

# Output:
# Normalized data: [-1.26491106 -0.63245553  0.          0.63245553  1.26491106]

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Mean
mean = np.mean(data)
print("Mean:", mean)

# Median
median = np.median(data)
print("Median:", median)

# Standard deviation
std_dev = np.std(data)
print("Standard Deviation:", std_dev)

# Variance
variance = np.var(data)
print("Variance:", variance)


# Logical opeartion

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(data>5)
print(data[data>5])
print(data[(data>=5) & (data<=8)])
print(data[(data>=5) | (data<=8)])