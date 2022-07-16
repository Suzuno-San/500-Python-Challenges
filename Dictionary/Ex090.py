#กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe'} สร้าง key ใหม่ชื่อ 'age' และ 'hobby' โดยมี value เป็น 32 และ ['coding','studying]

dict1 = {'first_name':'John','last_name':'Doe'}

# dict1['age'] = 32
# dict1['hobby'] = ['coding','studying']

dict1.update({'age':32,'hobby':['coding','studying']})

print(dict1)