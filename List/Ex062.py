#กำหนดให้ list1 = ['a','b','c'] และ list2 = [0,1,2] เขียนโปรแกรมเพื่อนำสมาชิกทั้งหมดของ list2 ไปต่อท้าย list1 และพิมพ์ list1 และ list2

list1 = ['a','b','c']
list2 = [0,1,2]

list1.extend(list2)

print(list1)
print(list2)