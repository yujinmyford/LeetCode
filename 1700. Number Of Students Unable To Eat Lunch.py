# Runtime: O(n)
# Space: O(1)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cycle = 0
        while len(students) != 0 and len(sandwiches) != 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                cycle = 0
            else:
                val = students.pop(0)
                students.append(val)
                cycle += 1
            
            if cycle == len(students):
                return len(students)

        return 0
