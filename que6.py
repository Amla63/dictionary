student_data={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)

