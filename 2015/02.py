file = open('input2.txt').read().split()


# part 1
sum = 0
for line in file:
    l, w, h = [int(x) for x in line.split('x')]
    surface_area = 2*l*w + 2*w*h + 2*h*l
    slack = l*w*h / max(l,w,h)
    sum += surface_area + slack
print(int(sum))

#part 2
ribbonsum = 0
for line in file:
    l, w, h = [int(x) for x in line.split('x')]
    perimeter = 2*(l+w+h - max(l,w,h))
    bow = l*w*h
    ribbonsum += perimeter + bow
print(ribbonsum)