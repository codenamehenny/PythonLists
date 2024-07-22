# Problem Statement: You have two lists of student names. 
# One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Find out if Alice submitted their assignment and attended class. 

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Alice" in submitted and "Alice" in attended) # checks if Alice is in both lists.

