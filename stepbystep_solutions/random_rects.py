def random_rects():
    rectengles = int(input("How many rectangles? "))
    area =0
    for i in range (1, (rectengles + 1)):
        width = int(input(f"Width {i}? "))
        height = int(input(f"Height {i}? "))
        area += (width*height)
        for i in range(1, (height+1)):
            print(str("*") * width)
    print(f"Total area: {area} ")