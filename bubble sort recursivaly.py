def bubbleSort(self,arr, n):
        if n == 1:
            return
        swap = False
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            return
        
        self.bubbleSort(arr, n-1)