def merge_sort(arr):

   if len(arr) <= 1;
      return arr
   mid = len(arr) //2

   left,right = merge_sort(arr[:mid]), merge_sort(arr[:mid])

   return merge(left, right, arr.copy())



def merge(left, right, merged):

   left_cursor ,right_cursor = 0, 0
   while left_cursor < len(left) and right_cursor < len(right):

      if left[left_cursor] <= right[right_cursor]:
         merged[left_cursor+right_cursor] = left[left_cursor]
         left_cursor += 1
      else:
         merged[left_cursor+right_cursor] =right[right_cursor]
         right_cursor += 1

   for left_cursor in range(left_cursor , len(left)):
      merged[left_cursor + right_cursor] = left[left_cursor]

   for right_cursor in range(right_cursor, len(right)):
      merged[left_cursor + right_cursor] = right[right_cursor]


   return merged



   # Merge sort เป็นตัวอย่างที่ดีของ Divide and Conquer algorithm โดยมีการทำ 2 ขั้นตอน ดังนี้:

   # 1.ทำการแบ่ง list ที่ยังไม่ได้ถูกเรียงลำดับ (Unsorted list) จนกว่าจะได้ N sublists 
   # ซึ่งแต่ละ sublist จะมี 1 element ที่ยังไม่ได้ถูกเรียงลำดับ (Unsorted) และ N คือจำนวนของ element  ใน array เดิม
   # 2.ทำการ Merge แต่ละ sublist เข้าด้วยกัน จนเกิดเป็น sublist ใหม่ที่มีการเรียงลำดับเรียบร้อยแล้ว ทำไปเรื่อยๆ จนกว่าทุก element ถูกเรียงลำดับอย่างถูกต้อง