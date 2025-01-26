my_list = ["apple", "banana", "cherry"]

print("=============================Now run for txt file ==========================")
with open("my_list.txt", "w") as f:
    for item in my_list:
        f.write(f"{item}\n")

print("The contents of the list are:")
for item in my_list:
    print(item)

print("=================== Now run for CSV file ===============================")
import csv

my_list = ["apple", "banana", "cherry"]

with open("my_list.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for item in my_list:
        writer.writerow([item])

print("The contents of the list are:")
for item in my_list:
    print(item)


print(
    "========Saving a 2D numpy array to a CSV file and reading it back ================="
)

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

# CSV file
np.savetxt("array.csv", array, delimiter=",")

# Read the CSV file
loaded_array = np.loadtxt("array.csv", delimiter=",")
print(loaded_array)


print(
    "======== Saving the array to a pickle file and loading it back ================="
)
import pickle

with open("array.pkl", "wb") as f:
    pickle.dump(array, f)

with open("array.pkl", "rb") as f:
    loaded_array_from_pickle = pickle.load(f)
print(loaded_array_from_pickle)
