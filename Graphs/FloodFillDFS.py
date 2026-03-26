class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if not image:
            return image
        
        if image[sr][sc] == color:
            return image

        start_color = image [sr][sc]
        rows = len (image)
        cols = len (image[0])

        def dfs (r,c):
            if image[r][c] == start_color:
                image[r][c] = color
            
                if r+1 < rows:
                    dfs (r+1,c)
                if r-1 >= 0:
                    dfs (r-1,c)
                if c+1 < cols:
                    dfs (r,c+1)
                if c-1 >= 0:
                    dfs (r,c-1)

        dfs (sr,sc)

        return image
