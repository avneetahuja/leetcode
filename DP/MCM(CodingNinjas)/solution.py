def matrixMultiplication(arr, n):
	# Write your code here.
	t = [[-1 for i in range(n)] for j in range(n)]
	def solve(a,i,j):
		minn = 10**9
		if i==j:
			return 0
		if t[i][j]!=-1:
			return t[i][j]
		
		for k in range(i,j):
			temp = solve(a,i,k) + solve(a,k+1,j) + a[i-1]*a[k]*a[j]
			minn = min(minn,temp)
		t[i][j] = minn
		return minn
	return solve(arr,1,n-1)

