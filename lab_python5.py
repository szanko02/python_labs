import time, random
from statistics import mean
def selection_sort(nums):  
    # значение i соответствует тому, сколько значений было отсортировано
    for i in range(len(nums)):
        # Мы предполагаем, что первый элемент несортированного сегмента является наименьшим
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Поменять местами значения самого низкого несортированного элемента с первым несортированным
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
# Проверяем, что это работает
listOfValues = [100, 1000, 3000, 5000, 7000, 10000, 20000, 50000]
timeList = []
listOfTimeList = [timeList, timeList, timeList, timeList, timeList, timeList, timeList, timeList, timeList, timeList]
for k in range(0, 10):
    for j in range(0, 8):
        x = [random.random() for i in range(listOfValues[j])]
        start = time.time()
        selection_sort(x)
        timeList.append(time.time()-start)
        #print(listOfValues[j], ' - ', a[j], sep='')
    print(timeList)

for i in range(len(timeList)):
    c = 0
    print(timeList[i+c])
    c = c + 8 
"""
listOfAverageTime=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for k in range(0, 10):
    temp = [-1, -1, -1, -1, -1, -1, -1, -1]
    aver = 0
    for j in range(0, 8):
        print ("temp -", temp)
        temp[j] = listOfTimeList[k][j]
        print("temp -", temp)
        aver = mean(temp)
        print("mean - ", aver)
    listOfAverageTime[k] = aver
print(listOfAverageTime)
"""
