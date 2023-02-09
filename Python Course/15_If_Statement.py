ball_color = "red"
box_a = 0
box_b = 0
box_c = 0

if ball_color == 'blue':
    box_a = box_a + 1
elif ball_color == 'red':
    box_c = box_c + 1
else:
    box_b = box_b + 1
    
print(box_a)
print(box_b)
print(box_c)