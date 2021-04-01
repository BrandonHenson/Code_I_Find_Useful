import mouse




# drag from (0, 0) to (100, 100) relatively with a duration of 0.1s
#mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)

#mouse.click('left')
#mouse.click('right')
#mouse.click('middle')


position = mouse.get_position()
print(position)

# move 100 right & 100 down
#mouse.move(100, 100, absolute=False, duration=0.2)

#mouse.move(1519, 709, absolute=True, duration=0.2)
#mouse.click('left')