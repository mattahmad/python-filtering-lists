import re

students = ["Abid", "Natasha", "Nick", "Matthew"]

# regex pattern
pattern = "N.*"

# Match the above pattern using list comprehension
filtered_students = [x for x in students if re.match(pattern, x)]

print(filtered_students)