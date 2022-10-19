subway = [10, 20, 30]
print(subway)

print(subway.index(20))

subway.append(40)
print(subway)

subway.insert(1,50) # (a,b) a자리에 50을 집어넣음
print(subway)

print(subway.pop()) #뒤에서 하나씩 꺼냄
print(subway)

# 같은 값이 몇 개 있는지 확인
subway.append(50)
print(subway)
print(subway.count(50))

# 정렬
num_list = [5,2,4,3,2]
num_list.sort()
print(num_list) # 정렬되어 나옴
#순서 뒤집기
num_list.reverse()
print(num_list)
#모두 지우기
num_list.clear()
print(num_list)


