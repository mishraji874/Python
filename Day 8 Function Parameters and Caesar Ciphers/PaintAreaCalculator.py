test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint(height = test_h, width = test_w, cover = coverage):
    result = (height * width) / cover
    print(result)
    print(round(result))

paint()