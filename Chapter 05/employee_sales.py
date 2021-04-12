from typing import List
# Definition for Employee.
class Employee:
    def __init__(self, id: int, sales: int, subordinates: List[int]):
        self.id = id
        self.sales = sales
        self.subordinates = subordinates
class Solution:
    def getSales(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        employee = emap[id]
        #ei=employee.id             #For debugging
        #es=employee.subordinates   #For debugging
        total_sales = employee.sales    
        for id in employee.subordinates:
            total_sales += self.getSales(employees, id)
        return total_sales
#Driver code
sol = Solution()
emps,id=[[1, 5, [2, 3]], [2, 3, [4]], [3, 3, []],
          [4,6,[]]],1
emp_list = []
for el in emps:
    emp_list.append(Employee(el[0],el[1],el[2]))
print(sol.getSales(emp_list,id))
