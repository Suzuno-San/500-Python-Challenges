#กำหนดให้ dict1 = {'first_name':'John','last_name':'Doe','age':'32'} รับ input 1 ตัว และตรวจสอบว่าเป็นหนึ่งใน key ของ dict1 หรือไม่

dict1 = {'first_name':'John','last_name':'Doe','age':'32'}

str1 = input("input: ")

print(str1 in dict1.keys())