def partition(array, begin, end):
   pivot_idx = begin
   for i in xrange(begin+1, end+1):
      if array[i] <= array[begin]:
         pivot_idx += 1
         array[i] ,array[pivot_idx] array[pivot_idx], array[i]
      array[pivot_idx], array[begin] =array[begin], array[pivot_idx]
   return pivot_idx

def quick_sort_recurion(array, begin, end):
   if begin >= end:
      return
   pivot_idx = partition(array, begin, end)
   quick_sort_recurion(array, begin, pivot_idx-1)
   quick_sort_recurion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
   if end is None:
      end = len(array) - 1

   return quick_sort_recurion(array, begin, end)



# Quick sort ใช้หลักการ Divide and Conquer algorithm คล้ายๆ กับ Merge sort 
# แม้ว่ามันจะมีความซับซ้อนกว่าเล็กน้อย แต่ในการใช้งานตามมาตรฐานส่วนใหญ่แล้ว จะทำงานได้รวดเร็วกว่า Merge sort 
# และแทบจะไม่เคยใช้จำนวนครั้งในการเรียงถึงขั้น worst case ถึง O(n2) เลย โดยมี 3 ขั้นตอนหลักๆ ดังนี้:

# 1.ก่อนอื่นทำการเลือกค่ามา 1 element จาก array ซึ่งจะเรียกว่า pivot
# 2.ทำการย้าย element ที่มีค่าน้อยกว่า pivot ไปไว้ด้านซ้ายของ pivot และย้ายค่าที่มากกว่า pivot ไปไว้ด้านขวา ซึ่งขั้นตอนนี้จะเรียกว่า partition operation
# 3. ตอนนี้เราได้ 2 sublists ขึ้นมา จากนั้นก็ย้อนกลับไปทำขั้นตอนที่ 1 และ 2 ของในแต่ละ sublist ซ้ำๆ ไปเรื่อยๆ จนกว่าจะเรียงลำดับอย่างถูกต้อง