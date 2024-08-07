# Q1.
# import numpy as np

# # create 2D Array
# arr = np.array([[85,90,78],
#                [92,88,95],
#                [76,95,85],
#                [90,85,92],
#                [88,76,89]])



    

# # calculate the mean for each column or each subjects of each students
# mean_col = np.mean(arr, axis=1)
# print("Mean of each subjects:", mean_col)
# print("\n")

# # Calculate the mean of all elements
# mean_all = np.mean(arr)
#  print("Mean of all elements:", mean_all)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#  #Q2.
# import numpy as np

# # create 2D Array
# arr = np.array([[85,90,78],
#                [92,88,95],
#                [76,95,85],
#                [90,85,92],
#                [88,76,89]])

# #calulate the median for each column or each subjects of each students

# median_col = np.median(arr,axis=1)
# print("Median of each subjects:",median_col)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
 #Q3.
# import numpy as np

# create 2D Array
# arr = np.array([[85,90,78],
#                [92,88,95],
#                [76,95,85],
#                [90,85,92],
#                [88,76,89]])


# # Calculate the total score for each student
# total_scores = np.sum(arr, axis=1)

# # Find the index of the student with the highest total score
# max_score_index = np.argmax(total_scores)

# # Extract the scores of the student with the highest total score
# highest_scores = arr[max_score_index]

# print("Scores of the student with the highest total score:", highest_scores)

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Q4.

# import numpy as np

#  # create 2D Array
# arr = np.array([[85,90,78],
#                [92,88,95],
#                [76,95,85],
#                [90,85,92],
#                [88,76,89]])

# #Calculate min and max scores in each subject

# min_scores = np.min(arr,axis=0)
# max_scores = np.max(arr,axis=0)

# print("min scores: ",min_scores)
# print("max scores: ",max_scores)

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Q5.

# import numpy as np

# # Create the original 2D array
# arr = np.array([[85, 90, 78],
#                 [92, 88, 95],
#                 [76, 95, 85],
#                 [90, 85, 92],
#                 [88, 76, 89]])

# # Transpose the array to switch rows and columns
# arr_transposed = arr.T

# # Reshape the transposed array to shape (3, 5)

# reshaped_array = arr_transposed.reshape(3, 5)

# print("Reshaped array (3, 5):\n", reshaped_array)
  
            






