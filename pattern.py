"""Scale sewing pattern outlines between sizes."""

SIZE_FACTORS = {"S": 0.94, "M": 1.0, "L": 1.07}


def scale_pattern(points, size="M"):
    """Return the outline points scaled for the given size.

    points is a list of (x, y) tuples in centimetres measured from the
    pattern's origin; the origin itself is not moved.
    """
    factor = SIZE_FACTORS[size]
    scaled = []
    for i in range(1, len(points)):
        x, y = points[i]
        scaled.append((round(x * factor, 1), round(y * factor, 1)))
    return scaled


def outline_length(points):
    """Total length of the closed outline in centimetres."""
    total = 0.0
    for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1]):
        total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(total, 1)


if __name__ == "__main__":
    sleeve = [(0, 0), (40, 0), (36, 58), (4, 58)]
    print(scale_pattern(sleeve, "L"))
