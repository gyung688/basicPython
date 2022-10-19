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

index = python.index("n") # n이 몇번째에 있는지
print(index)
index = python.index("n", index+1) # 첫번째 n 뒤에서부터 n 찾음
print(index)

print(python.find("Java")) # 포함하지 않으면 -1이 나옴
# print(python.index("Java")) # 원하는 값이 없으면 에러가 나오면서 프로그램 종료시킴

print(python.count("n")) #n이 몇번 등장하는지 나옴

##########################################
print("나는 %d살입니다." % 20) #d는 정수값만 넣을 수 있음
print("나는 %s을 좋아해요." % "파이썬") 
print("Apple은 %c로 시작해요." %"A") #c는 캐릭터로 한 문자만 나옴
# %s만 써도 잘 나옴

print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간")) #중괄호0에 0번째 값을 넣는다.

print("나는 {age}살이며, {color}색을 좋아해요" .format(age =20, color="빨간"))

age=20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") #f를 넣어주면 위에 변수를 갖다 써준다.

# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
print("저는 '나도코딩'입니다.")
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print("C:\\User\\Coding")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple > Pine을 0번째부터 써줘서 'Red '가 덮어쓰기 된 것

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")


site = "http://naver.com"
site = site.replace("http://", "")
rule = site[:site.index(".")]
pwd = rule[:3] + str(len(rule)) + str(rule.count("e")) + "!"
print(pwd)
