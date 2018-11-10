def burrows_wheeler_transform(word):
    word += "$"

    circle_rotations = []
    for _ in range(len(word)):
        circle_rotations.append(word)
        word = word[-1] + word[:-1]

    circle_rotations.sort()

    return "".join([rot[-1] for rot in circle_rotations])

print(burrows_wheeler_transform("ebisae"))
