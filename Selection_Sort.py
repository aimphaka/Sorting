def selection_sort(arr):
   for i in range(len(arr)):
      minimum = if

      for j in range(i + 1, len(arr)):
         if arr[j] < arr[minimum]:
            minimum = j

      arr[minimum],arr[i] = arr[i], arr[minimum]

   return arr

   # Selection sort จะมีการแบ่ง list/array 
   # ออกเป็น 2 ส่วน คือ sublist ของ items ที่ถูก Sort แล้ว(Sorted list) 
   # และ sublist ของ items ที่เหลือ (Unsorted list) 
   # ซึ่งจะทำการ Sort ไปเรื่อยๆ ใน sublist นี้ โดยในขั้นแรกจะทำการหาค่าที่น้อยที่สุดใน Unsorted list
   # และสลับค่าแรกกับค่าที่น้อยที่สุดนั้น ซึ่งค่าที่น้อยที่สุดนั้นจะอยู่ใน Sorted list แล้ว 
   # จากนั้นทำแบบเดิมกับ items ใน Unsorted list แล้วนำค่าน้อยที่สุดไปใส่ด้านหลังสุดของ Sorted list ซึ่งจะทำแบบนี้ไปเรื่อยๆ จนมันเรียงลำดับอย่างถูกต้อง