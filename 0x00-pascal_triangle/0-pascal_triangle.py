def pascal_triangle(n):
    """
    Generates Pascal's Triangle of n rows.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # Edge case: first element is always 1
        for j in range(1, i):
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        row.append(1)  # Edge case: last element is always 1
        triangle.append(row)
    return triangle
