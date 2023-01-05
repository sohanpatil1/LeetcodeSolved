# https://leetcode.com/problems/flood-fill/description/?orderBy=most_votes
# Flood Fill
import collections

def floodFill(image, sr: int, sc: int, color: int):
        oldcolor = image[sr][sc]
        rows = len(image)
        cols = len(image[0])
        q = collections.deque([(sr,sc)])
        while(q):
            r , c = q.popleft()
            image[r][c] = color
            for x,y in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if(0<=x<rows and 0<=y<cols and (image[x][y] == oldcolor)):
                    q.append((x,y))
        return image


newimage = floodFill(image = [[0,0,0],[0,0,0]], sr = 1, sc = 0, color = 2)
print(newimage)