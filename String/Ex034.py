'''
เขียนโปรแกรมรับอินพุต 2 ตัวที่เป็นสายอักขระ(string1,string2) ให้ทำการตรวจสอบว่า string1 มี string2 ในนั้นหรือไม่ ให้พิมพ์ค่าความจริงออกมา
'''

string1 = str(input("Input String1: "))
string2 = str(input("Input String2: "))
print(string2 in string1)
