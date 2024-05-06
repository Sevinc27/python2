#task1
mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
def define(mylist):
    new_list = [i for i in mylist if i >= 0 and (i ** (1/2)) % 1 == 0]
    print(new_list)

define(mylist)


#task2
input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']

def unique_list(my_list):
    return [i for i in my_list if my_list.count(i) == 1]

result = unique_list(input_list)
print(result)

#task3
input_list = [2, 2, 6, 7, 7, 9, 11]

def multiplication(my_list):
    return 1 if len(my_list) == 0 else 1 if 0 in my_list else eval('*'.join(map(str, my_list)))

result = multiplication(input_list)
print(result)


#task4
num= int(input("ededi daxil edin: "))
bolenler=[i for i in range(1,num+1) if num%i==0]
print(bolenler)

#task5
mylist=['may','iyun','iyul'] 
month_length = {i: len(i) for i in mylist}
print(month_length)

#task6
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

def get_first_name(name):
    return name.split()[0].lower()

first_names = list(map(get_first_name, names))
print(first_names)


#task7
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
results=[]
if len(nums1)==len(nums2):
   for i in range(len(nums1)):
      ortalama=(nums1[i]+nums2[i])/2
      results.append(ortalama)
print(results)