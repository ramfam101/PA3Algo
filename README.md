Jeevan Munnangi 

26233363

Compilation instructions

can run the python file with the command

``` bash
python ./HighestValueSequence.py
```

can modify the file being tested by changing the index of the number in inputs array in the main function. 

Question 2

In this oslution dp[i][j] is the maximum value of a subsequence in both A and B up to lenghts i and j respectively. dp[0][j] are all 0 and dp[i][0] are all 0

Basically 1 of 2 options comes up. if the values of A and B are the same A[i] == B[j] we can mark the dp cell dp[i][j] as the prior diagonal dp celldp[i-1]dp[j-1] + the value of the char in the string we are on v(A[i]). If they are not equal we are going to skip the current charcachter in either A or B based on which is better to use, the more expensive one.

Question 3

HVLCS(A,B, v):
    m = len(A)
    n = len(B)

    dp array [0 ... m][0 ... n]
    for i in range(0,m):
        dp[i][0] = 0
    for j in range(0,n):
        dp[0][j] = 0
    
    for i = 1 to m:
        for j = 1 to n:
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + v(A[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

runtime of this algorithim is 0(mn)
each cell does a comparison and one max or addition.