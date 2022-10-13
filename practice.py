print(5)
print("연탄")

animal = "강아지"
name = "연탄이"
age = 4
is_adult = age >= 3

# 정수형은 str로 감싸줘야한다.
print("우리집 " + animal + name + "은 " + str(age) + "살이다.")
# ,콤마로 +를 대체 가능하지만 공백이 들어간다.
print("우리집 " , animal , name , "은 " , str(age) , "살이다.")
# boolean은 str로 감싸줘야한다.
print(name + "는 어른일까요? " + str(is_adult))

#주석
'''
    여러 줄
    주석 처리
'''
# Ctrl + / 로 여러줄 동시에 주석 처리 가능
# print()
# print()
# print()

