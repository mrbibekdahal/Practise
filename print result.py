score = int(input("enter the score:"))
result = ""
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score > 70:
    result = "C"
else:
    result = "F"
print(result)

