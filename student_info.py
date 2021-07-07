students = {
    "SID1234" : ["John Doe", 2005, "Dubai, UAE"],
    "SID1212" : ["David Letterman", 1990, "Abu Dhabi, UAE"],
    "SID1034" : ["Rick Grimes", 2001, "Dubai, UAE"]
}

for student_id, student_info in students.items():
    print(f'''Student ID: {student_id:10}
Student Name: {student_info[0]}
Year Of Birth: {student_info[1]}
Address: {student_info[2]}
''')


students["SID1002"] = ["Joseph Stevens", 2000, "Dubai, UAE"]

print()
for student_id, student_info in students.items():
    print(f'''Student ID: {student_id:10}
Student Name: {student_info[0]}
Year Of Birth: {student_info[1]}
Address: {student_info[2]}
''')

students.pop("SID1234")

print()
for student_id, student_info in students.items():
    print(f'''Student ID: {student_id:10}
Student Name: {student_info[0]}
Year Of Birth: {student_info[1]}
Address: {student_info[2]}
''')