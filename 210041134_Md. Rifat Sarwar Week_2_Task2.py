import cv2 as cv
import numpy as np

def detect_red_and_white_regions(image):

    #bgr to hsv
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    lower_red = np.array([157, 130, 80])
    upper_red = np.array([180, 255, 255])

    mask1 = cv.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([0, 200, 70])
    upper_red = np.array([12, 255, 255])

    mask2 = cv.inRange(hsv, lower_red, upper_red)

    lower_white = np.array([0, 0, 150])
    upper_white = np.array([255, 30, 255])

    mask_white = cv.inRange(hsv, lower_white, upper_white)


    mask_red = mask1 + mask2
    mask = mask_red + mask_white

    processed_image = cv.bitwise_and(image, image, mask=mask)

    return processed_image

def analyze_goat(image_array):


    min_pixval = np.min(image_array)
    max_pixval = np.max(image_array)
    avg_pixval = np.mean(image_array)

    non_zero_pixval = np.count_nonzero(image_array)
    zero_pixval = np.sum(image_array == 0)

    print(min_pixval)
    print(max_pixval)
    print(zero_pixval)
    print(non_zero_pixval)
    print(non_zero_pixval + zero_pixval)

    font = cv.FONT_HERSHEY_DUPLEX
    font_scale = 1
    color = (20, 255, 57)
    thickness = 2

    new_image = cv.putText(image, f"Min Pixel Value: {min_pixval}", (10,40),font, font_scale, color,thickness)
    new_image = cv.putText(image, f"Max Pixel Value: {max_pixval}", (10, 80), font, font_scale, color, thickness)
    new_image = cv.putText(image, f"Average Pixel Value: {avg_pixval}", (10, 120), font, font_scale, color, thickness)
    new_image = cv.putText(image, f"Total number of Non Zero Pixel: {non_zero_pixval}", (10, 160), font, font_scale, color, thickness)
    new_image = cv.putText(image, f"Total number of Zero Pixel: {zero_pixval}", (10, 200), font, font_scale, color, thickness)

    return new_image


image = cv.imread("GOAT.jpg")
cv.imshow("Image", image)

gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
processed_image = detect_red_and_white_regions(image)

analyzed_image = analyze_goat(gray_image)

cv.imshow("Processed Image", processed_image)
cv.imshow("Analyzed Image", analyzed_image)

cv.waitKey()
cv.destroyAllWindows()