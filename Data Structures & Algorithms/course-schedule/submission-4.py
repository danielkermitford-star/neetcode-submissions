class Solution:
    # checking for cycles
    # note that a non-tree doesn't necessarily contain a cycle, i.e. there may 
    # be more than a single path to a specific prereq.  
    # to check for cycles need to create a list of all the prereqs and see if the 
    # list contains itself.  Hence the list of prereqs needs to be flattened, so
    # we must build it up by working backward - e.g. 'up from the leaves'.  
    # In other words we need to start with a course that has no prereqs. 
    # We can either try to iterate backwards flattening all the recursive prerequistes
    # But the problems, is that we don't want to proceed, i.e. add it to the queue
    # until we've done this for all prerequisites.  So we can either keep track of all 
    # the prereqs and remove the one we're coming from - or just keep a counter of the 
    # the number of them and decrease this by 1 - Kahn's Algorithm. 
    # the following uses Kahn's algorithm.  Alternatively we could use DFS
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        counts = [0 for i in range(numCourses)] # the number of courses that this is a prereq for 
        # i.e. the number of times this course is in a list of prereqs for another course
        prereqs = {}        
        for a,b in prerequisites: # b is a prereq for a
            prereqs.setdefault(a, []).append(b) # prereq[a] = [b,]
            counts[b] += 1
        
        
        n_visited = 0
        # no_prerequisites: list of all courses that are not a prereq for any other course
        no_prerequisites = [i for i,c in enumerate(counts) if c == 0]  
        queue = deque(no_prerequisites)
        while queue:
            # for all prereqs decrease count; add to queue if count becomes 0
            course = queue.popleft()
            n_visited += 1
            if course in prereqs:
                for p in prereqs[course]:
                    counts[p] -= 1
                    if counts[p] == 0:
                        queue.append(p)
        
        return n_visited == numCourses


        