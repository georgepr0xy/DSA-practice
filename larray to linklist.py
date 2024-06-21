if not arr:
 return None
    
head = Node(arr[0])
current = head
for value in arr[1:]:
    current.next = Node(value)
    current = current.next
    
return head