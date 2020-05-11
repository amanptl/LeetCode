def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        target = image[sr][sc]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        def traverse(x,y):
            image[x][y] = newColor
            visited.add((x,y))
            for i,j in directions:
                x_ = x + i
                y_ = y + j
                if -1 < x_ < len(image) and -1 < y_ < len(image[0]) and (x_,y_) not in visited and image[x_][y_] == target:
                    traverse(x_,y_)
        
        traverse(sr,sc)
        return image