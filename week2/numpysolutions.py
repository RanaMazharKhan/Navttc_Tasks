
#1st Problem
#Create a 1D NumPy array `temperatures` from the list `[30, 32, 29, 35, 31]`. 
# Print its `.shape`, `.ndim`, `.size`, and `.dtype`.

import numpy as np
tempartures =np.array([[32, 45, 50, 60, 70, 80, 90],
                    [32, 45, 50, 60, 70, 80, 90]])

print(tempartures.shape)
print(tempartures.ndim)
print(tempartures.size)
print(tempartures.dtype)


#2nd Problem
#Create a `4x4` array of zeros, a `3x3` array filled with the value `9`, and a `5x5` identity matrix.
# Print all three.

array1=np.zeros((4,4))
array2=np.full((3,3), 9)
array3=np.eye(5)
print(array1)
print(array2)
print(array3)


#3rd Problem
#Create the array `values = np.arange(10, 60, 5)`. Print the first 3 elements, 
# the last 3 elements, and every second element.

values = np.arange(10, 60, 5)
print(values[0:4])
print(values[-4:])
print(values[::2])


#4th Problem
#Create the 2D array below and print: (a) the element at row 2, column 1, (b) the entire second row, (c) the entire first column.

grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print(grid[1, 0]) 
print(grid[1,:])
print(grid[:, 1])


#5th Problem
#Create `celsius = np.array([0, 10, 20, 30, 40])`. Convert it to Fahrenheit using the formula `F = C * 9/5 + 32`, 
# in a single vectorized line (no loop).

celsius = np.array([0, 10, 20, 30, 40])
f=(celsius * 9/5) + 32
print(f)


#6th Problem
#Given `scores = np.array([55, 89, 76, 92, 40, 67, 98])`, 
# extract only the scores that are `>= 70` using boolean indexing. 
# Then print how many scores passed that filter.


scores = np.array([55, 89, 76, 92, 40, 67, 98])
mask = scores >= 70
print(scores[mask])


#7th Problem
#Create `numbers = np.arange(1, 25)`. Reshape it into a `(4, 6)` array.
#Print the sum of each row (`axis=1`) and the sum of each column (`axis=0`).

numbers = np.arange(1, 25)
array1 = numbers.reshape(4, 6)
print(array1)
print(array1.sum(axis=0))
print(array1.sum(axis=1))


#8th Problem
#Create `original = np.array([5, 10, 15, 20, 25])`. Create a *view* called `partial_view = original[1:3]` 
#and modify one of its elements. Print `original` to confirm it changed. Then repeat the process but with
#`.copy()` instead, and confirm `original` is unaffected this time.


original = np.array([5, 10, 15, 20, 25])
partial_view = original[1:3]
partial_view[0]=9
print(original)
print(partial_view)

new_copy=original[1:3].copy()
new_copy[0]=3
print(original)
print(new_copy)


#9th Problem
#Create two 1D arrays, `group_a = np.array([1, 2, 3])` and `group_b = np.array([4, 5, 6])`. 
# Use `np.concatenate` to join them, and separately use `np.vstack` to stack them as two rows of a 2D array.
# Print both results.

group_a = np.array([1, 2, 3])
group_b = np.array([4, 5, 6])

new_array=np.concatenate([group_a,group_b])
print(new_array)
new_array1=np.vstack([group_a,group_b])
print(new_array1)


#10th Problem
#Given `grades = np.array(["B", "A", "C", "A", "B", "A", "D"])`,
#print the unique grades along with a count of how many times each occurs, 
#sorted so the most common grade appears first (hint: use `return_counts=True`, then sort by the counts).


grades = np.array(["B", "A", "C", "A", "B", "A", "D"])
updated_grades=np.unique(grades, return_counts=True)
print(updated_grades)

sorted_grades=np.sort(grades)
print(sorted_grades)


#11th Problem
#Normalize this array so every value is scaled into the range `[0, 1]`, 
#using the formula `(value - min) / (max - min)`. Do this in a single vectorized line (no loop), 
#then print the result.


house_sizes = np.array([850, 900, 1200, 1500, 2000, 750, 1100])
normalized_array=[(house_sizes-house_sizes.min())/(house_sizes.max()-house_sizes.min())]
print(normalized_array)


#12th Problem
#Compute the predictions for all three samples in a single line using `@`.
# Then find the index of the sample with the **highest** predicted value using `np.argmax`.

X = np.array([
    [2, 3, 1],
    [5, 1, 4],
    [1, 1, 1],
])
weights = np.array([0.4, 0.4, 0.2])

prediction = X @ weights
print(prediction)
print(np.argmax(prediction))


#13th Problem
#Using only vectorized NumPy operations (no Python loops):
#1. Compute each student's average mark (`axis=1`).
#2. Compute the class average for each subject (`axis=0`).
#3. Use boolean indexing to find which students have an average `>= 80`.
#4. Save the array of per-student averages to a file `student_averages.npy`, then load it back and print it.


student_marks = np.array([
    [78, 85, 90],
    [88, 92, 95],
    [55, 62, 58],
    [90, 87, 93],
])

average_marks=student_marks.sum(axis=1)/len(student_marks)
print(average_marks)
class_average_marks=student_marks.sum(axis=0)/len(student_marks)
print(class_average_marks)

mask = student_marks >= 80
print(student_marks[mask])

np.save("student_averages.npy",average_marks)
loaded_data=np.load("student_averages.npy")
print(loaded_data)