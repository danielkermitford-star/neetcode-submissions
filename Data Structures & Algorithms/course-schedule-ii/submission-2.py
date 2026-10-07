class Solution:
    # topological sort - Kahn's Algorithm.  Like Course Schedule, but you need to return the 
    # topologically sorted list of vertices instead of a bool
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        counts = [0 for i in range(numCourses)] # the number of courses that this is a prereq for 
        # i.e. the number of times this course is in a list of prereqs for another course
        prereqs = {}        
        for a,b in prerequisites: # b is a prereq for a
            prereqs.setdefault(a, []).append(b) # prereq[a] = [b,]
            counts[b] += 1
        
        queue_order = []
        # no_prerequisites: list of all courses that are not a prereq for any other course
        no_prerequisites = [i for i,c in enumerate(counts) if c == 0]  
        queue = deque(no_prerequisites)
        while queue:
            # for all prereqs decrease count; add to queue if count becomes 0
            course = queue.popleft()
            queue_order.append(course)
            if course in prereqs:
                for p in prereqs[course]:
                    counts[p] -= 1
                    if counts[p] == 0:
                        queue.append(p)
        
        if len(queue_order) != numCourses:
            return []
        else:
            queue_order.reverse()
            return queue_order


        