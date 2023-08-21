def edit_distance(source, target):

	matrix = [[0 for i in range(len(source) + 1)] for j in range(len(target) + 1)]
	
	for i in range(len(target) + 1):
		matrix[i][0] = i

	for i in range(len(source) + 1):
		matrix[0][i] = i

	for i in range(1, len(target) + 1):
		for j in range(1, len(source) + 1):
			if source[j - 1] == target[i - 1]:
				matrix[i][j] = matrix[i - 1][j - 1]
			else:
				matrix[i][j] = min(
					matrix[i - 1][j],
					matrix[i][j - 1],
					matrix[i - 1][j - 1]
				) + 1

	return matrix[i][j]


source = 'replace'
target = 'delete'

edit_dist = edit_distance(source, target)
print(edit_dist)
