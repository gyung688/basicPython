jumin = "000120-1234567"

print("성별 :" + jumin[7])
print("연 :" + jumin[0:2]) #0부터 2직전까지
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])

print("생년월일 : "+ jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : "+ jumin[7:])
print("뒤에서 7자리 : "+ jumin[-7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)