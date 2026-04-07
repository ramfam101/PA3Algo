import time
import matplotlib.pyplot as plt

def readinput(filename):
    with open(filename, 'r') as f:
        K = int(f.readline())
        values = {}
        for _ in range(K):
            parts = f.readline().split()
            values[parts[0]] = int(parts[1])
        A = f.readline().strip()
        B = f.readline().strip()
    return values, A, B

def dpcalc(values, A, B):
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values.get(A[i - 1], 0)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp

def getstring(dp, A, B):
    i, j = len(A), len(B)
    result = []
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            result.append(A[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(result))

def plotresults(inputs):
    times = []
    for f in inputs:
        values, A, B = readinput(f)
        starttime = time.time()
        dp = dpcalc(values, A, B)
        times.append(time.time() - starttime)
    plt.bar(inputs, times)
    plt.ylabel("Runtime (s)")
    plt.show()


if __name__ == "__main__":
    inputs = ["input1.txt",
        "input2.txt",   "input3.txt",   "input4.txt",   "input5.txt",
        "input6.txt",   "input7.txt",   "input8.txt",   "input9.txt",   
        "input10.txt"]
    values, A, B = readinput(inputs[1])
    print(values)
    print(A)
    print(B)
    dp = dpcalc(values, A, B)
    print(dp[-1][-1])
    sequence = getstring(dp, A, B)
    print(sequence)
    plotresults(inputs)