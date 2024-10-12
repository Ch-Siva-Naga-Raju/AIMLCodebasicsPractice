def calc_area(s1, s2, shape="triangle"):
    if shape == "rectangle":
        return s1 * s2
    return 1/2 * s1 * s2

print(calc_area(10,30))