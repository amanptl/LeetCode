def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import defaultdict
        
        d = defaultdict(int)
        
        for task in tasks:
            d[task] += 1
        
        max_occ = max(d.values())
        
        task_with_max_occ = sum((1 for task, occ in d.items() if occ == max_occ))
        
        schedule = (max_occ - 1) * (n + 1) + task_with_max_occ
        
        #print(task_with_max_occ)
        
        return max(len(tasks), schedule)