#Question =>https://leetcode.com/problems/task-scheduler/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        c = Counter(tasks).most_common()[::-1]
        most_freq_task = c[-1][1] - 1
        idel_slots = most_freq_task * n
        
        for value in c[:len(c)-1]:
            idel_slots -= min(most_freq_task, value[1])
            
        return idel_slots + len(tasks) if idel_slots > 0 else len(tasks)
        
        
        
