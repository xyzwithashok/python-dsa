#  https://www.geeksforgeeks.org/maximum-value-arri-arrj-j


class Solution:

    def maxValue_Bruteforce(self, arr, N):
        max_value = 0
        for i in range(N):
            for j in range(i, N):
                val = abs(arr[i] - arr[j]) - abs(i - j)
                max_value = max(val, max_value)
        return max_value

    def maxValue_optimal(self, arr, N):
        pass


# def test_solution():
#     arr = [1, 15, 13, 8]
#     # arr = generate_ramdom_array(10, 1, 100)
#     print(Solution.maxValue_Bruteforce(arr, len(arr)))

if __name__ == "__main__":
    arr = [1, 15, 13, 8]
    print(Solution().maxValue_Bruteforce(arr, len(arr)))
