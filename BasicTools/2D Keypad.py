# 2D Basic phone number pad

numpad = ((1, 2, 3), 
          (4, 5, 6), 
          (7, 8, 9), 
          ("*", 0, "#"))

for row in numpad:
    print(row)

for row in numpad:
    for num in row: 
        print(num, end=" ")
    print()