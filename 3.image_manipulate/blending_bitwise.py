import cv2

# Load two images
girl = cv2.imread('../img/wingwall.jpg')
logo = cv2.imread('../img/opencv_logo.png')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = logo.shape
x=10; y=10

roi = girl[y:rows+y, x:cols+x]
cv2.imshow('roi', roi)

# Now create a mask of logo and create its inverse mask also
logo2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
cv2.imshow('logo2gray', logo2gray)

ret, mask = cv2.threshold(logo2gray, 20, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)

# Now black-out the area of logo in ROI
girl_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
cv2.imshow('girl_bg', girl_bg)

# Take only region of logo from logo image.
logo_fg = cv2.bitwise_and(logo,logo,mask = mask)
cv2.imshow('logo_fg', logo_fg)
# Put logo in ROI and modify the main image
dst = cv2.add(girl_bg,logo_fg)
cv2.imshow('add', dst)
girl[x:rows+x, y:cols+y ] = dst
cv2.imshow('imgBitwise',girl)
cv2.waitKey(0)
cv2.destroyAllWindows()