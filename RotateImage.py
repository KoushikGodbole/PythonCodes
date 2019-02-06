def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    matrix.reverse()
    for i in range(0,len(matrix)):
        for j in range(i+1,len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)







ex = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

rotate(ex)