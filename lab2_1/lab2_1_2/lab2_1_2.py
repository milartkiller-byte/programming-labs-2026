from typing import List


def max_hamsters(S: int, hamsters: List[List[int]]) -> int:

    n = len(hamsters)

    def can_feed(k: int) -> bool:
        if k == 0:
            return True

        costs = []
        neighbours = k - 1

        for a, b in hamsters:
            costs.append(a + b * neighbours)

        costs.sort()
        return sum(costs[:k]) <= S

    left, right = 0, n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if can_feed(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer


if __name__ == "__main__":
  
    print(max_hamsters(7, [[1, 2], [2, 2], [3, 1]]))              
    print(max_hamsters(19, [[5, 0], [2, 2], [1, 4], [5, 1]]))     
    print(max_hamsters(2, [[1, 50000], [1, 60000]]))              