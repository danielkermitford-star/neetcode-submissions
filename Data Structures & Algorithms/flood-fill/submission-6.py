class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        seen = set()
        originalcolor = image[sr][sc]
        queue = deque()
        queue.append((sr,sc))
        while queue:
            i,j = queue.popleft()

            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) \
            or (i,j) in seen or image[i][j] != originalcolor:
                continue
            else:
                seen.add((i,j))

            image[i][j] = color

            queue.append((i-1,j))
            queue.append((i+1,j))
            queue.append((i,j-1))
            queue.append((i,j+1))

        return image

        