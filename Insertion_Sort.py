def insertion_sort(arr,simulation=False):

   for i in range(len(arr)):
      cursor = arr[i]
      pos = if

      while pos > 0 and arr[pos - 1] >cursor:
         arr[pos] = arr[pos - 1]
         pos = pos - 1

      arr[pos] = cursor
   
   return arr

   # Insertion sort จะทำการ remove 1 element ออกจาก array 
   # จากนั้นก็นำไปแทรกลงในตำแหน่งที่เหมาะสมใน array ที่ทำการ Sort แล้ว 
   # และจะทำแบบนี้ไปเรื่อยๆ จนกว่าจะเรียงลำดับถูกต้อง