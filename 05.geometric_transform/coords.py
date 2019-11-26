import numpy as np
coords = [[ 27,  46], [361, 38], [ 18, 589], [479, 510]]
pts = np.zeros( (4,2), dtype=np.float32)

for i,item in enumerate(coords):
    pts[i] = coords[i]

print(pts, pts.shape)

s = pts.sum(axis=1)
topLeft = pts[np.argmin(s)]
bottomRight = pts[np.argmax(s)]
#print(coords[coords!=topLeft].reshape(-1,2))

diff = np.diff(pts, axis = 1)
topRight = pts[np.argmin(diff)]
bottomLeft = pts[np.argmax(diff)]
pts1 = np.float32([topLeft, topRight, bottomRight , bottomLeft])
print(pts1)

w1 = abs(bottomRight[0] - bottomLeft[0])
w2 = abs(topRight[0] - topLeft[0])
h1 = abs(topRight[1] - bottomRight[1])
h2 = abs(topLeft[1] - bottomLeft[1])
maxWidth = max([w1, w2])
maxHeight = max([h1, h2])

pts2 = np.float32([[0,0], [maxWidth-1,0], 
                    [maxWidth-1,maxHeight-1], [0,maxHeight-1]])
print(pts2)