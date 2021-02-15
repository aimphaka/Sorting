def bubble_sort(arr):
   def swap(i,j):
      arr[i],arr[j] = arr[j], arr[i]

      n = len(arr)
      swapped = True

      x = -1
      while swapped:
         swapped = False
         x = x+1
         for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
               swap(i - 1, i)
               swapped = True
      
      return arr

      # Bubble sort จะทำการเปรียบเทียบ elements 
      # ที่อยู่ติดกันใน list ซึ่ง elements เหล่านั้นก็จะถูกสลับที่กันทีละคู่ไปเรื่อยๆ 
      # หากมันยังเรียงลำดับผิดอยู่และจะทำไปจนครบทุกค่า จากนั้นก็จะกลับมาทำซ้ำใหม่ จนทุก elements 
      # อยู่ในตำแหน่งที่เรียงลำดับถูกต้อง และเนื่องจากการ Sort ประเภทนี้จะถูกทำซ้ำๆ 
      # ดังนั้น จำนวนครั้งในการ Sort กรณีที่เป็น Worst case คือ O(n2)