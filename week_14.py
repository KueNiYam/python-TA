import math
import matplotlib.pyplot as plt

# 꺾은선 그래프
plt.plot([0, 100, 200, 300,400])
plt.show()


# r-- option: 빨간색 점선 그래프
plt.plot([0, 100, 200, 300,400], 'r--')
plt.show()

# 사인(Sine) 곡선 그리기
samples = 1024
x, y = [], []

for n in range(samples):
    k = n / (samples - 1)
    x.append(2 * math.pi * k)
    y.append(math.sin(x[-1]))

plt.plot(x, y)
plt.show()

# 막대 그래프
plt.bar(x, y, width=(2*math.pi)/samples)
plt.show()

# 점 그래프
plt.scatter(x, y)
plt.show()

# 설정
fig = plt.figure()
axis = fig.add_subplot(1,1,1)
axis.set_ylim(-2, 2)
axis.grid(True)

plt.scatter(x, y)
plt.show()

# 두 개의 곡선 동시에 그리기 (1)
samples = 32
x, y1, y2 = [], [], []

for n in range(samples):
    k = n / (samples - 1)
    x.append(2 * math.pi * k)
    y1.append(math.sin(x[-1])) # 사인
    y2.append(math.cos(x[-1])) # 코사인

plt.plot(x, y1)
plt.scatter(x, y2)
plt.show()

# 두 개의 곡선 동시에 그리기 (2)
plt.plot(x, y1, linestyle='--', c='magenta', label='sin(x)')
plt.plot(x, y2, linewidth=5, label='cos(x)')
plt.legend(loc='best')
plt.show()

# 두 개의 곡선 동시에 그리기 (3)
fig = plt.figure()
fig.add_subplot(2, 1, 1) # 2행 1열 그래프의 첫 번째
plt.scatter(x, y2)

fig.add_subplot(2, 1, 2) # 2행 1열 그래프의 두 번째
plt.plot(x, y1)

plt.show()

import random
# 랜덤 데이터 만들기

y = []

for i in range(5):
    y += [random.randrange(0, 1000)]

# 리스트 뒤섞기
list_0to9 = [x for x in range(10)]
print(list_0to9)

random.shuffle(list_0to9)
print(list_0to9)

# 거품정렬(bubble sort)
"""
가장 단순한 알고리즘

Step 1: 리스트에서 첫 번째 위치의 요소를 선택한다
Step 2: 그 요소가 다음 위치의 요소보다 크다면, 요소를 맞바꿔준다.
Step 3: 다음 위치의 요소를 선택하여 step2를 수행하는 것을 리스트의 마지막에 이르기 까지 반복한다.
Step 4: 리스트의 가장 큰 요소가 맨 뒤로 이동하였다.
Step 5: 맨 뒤로 이동한 요소를 제외한 나머지에 대해 step1부터 반복한다.
"""

list_0to9 = [x for x in range(10)]
print(list_0to9)

random.shuffle(list_0to9)
print(list_0to9)

def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)-1):
        for j in range(len(unsorted_list) - 1 - i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

bubble_sort(list_0to9)
print(list_0to9)

random.shuffle(list_0to9)
print(list_0to9)

def selection_sort(unsorted_list):
    for size in reversed(range(len(unsorted_list))):
        max_i = 0
        for i in range(1, size + 1):
            if unsorted_list[i] > unsorted_list[max_i]:
                max_i = i
        unsorted_list[max_i], unsorted_list[size] = unsorted_list[size], unsorted_list[max_i]

selection_sort(list_0to9)
print(list_0to9)

random.shuffle(list_0to9)
print(list_0to9)

def insertion_sort(unsorted_list):
    for size in range(1, len(unsorted_list)):
        val = unsorted_list[size]
        i = size
        while i > 0 and unsorted_list[i-1] > val:
            unsorted_list[i] = unsorted_list[i-1]
            i -= 1
        unsorted_list[i] = val

selection_sort(list_0to9)
print(list_0to9)

# 정렬 전/후 그래프로 비교해서 보기
list1 = [x for x in range(1000)]

random.shuffle(list1)
list2 = list1.copy()

selection_sort(list2)
fig = plt.figure()
fig.add_subplot(2, 1, 1)
plt.bar([x for x in range(1000)], list1)

fig.add_subplot(2, 1, 2)
plt.bar([x for x in range(1000)], list2)

plt.show()

# 성능 측정
import time

def is_prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
        return True

start = time.time()
for i in range(2, 500):
    if is_prime(i):
        print(i, end='')
print()
end = time.time()

elapsed = end - start
print(elapsed)