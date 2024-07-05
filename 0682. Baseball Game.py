# Runtime: O(n)
# Space: O(n)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for operation in operations:
            if operation == '+':
                new = record[-2] + record[-1]
                record.append(new)
            elif operation == 'D':
                new = 2 * record[-1]
                record.append(new)
            elif operation == 'C':
                record.pop()
            else:
                record.append(int(operation))
        
        f_sum = 0
        for i in range(len(record)):
            f_sum += record[i]
        return f_sum
