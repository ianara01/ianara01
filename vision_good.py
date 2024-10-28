import cv2

# 동영상 파일 열기
cap = cv2.VideoCapture("lion.mp4")
edge_bool = False
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 그레이스케일 변환
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Canny edge detection 적용
    edges = cv2.Canny(image=gray_img, threshold1=100, threshold2=200)

    if edge_bool:
        image = edges
    else:
        image = frame
    cv2.imshow("Video", image)
    key = cv2.waitKey(1)
    if key == ord("q"):break
    elif key == ord("b"):
        edge_bool = not edge_bool


# 외부 자원은 반환
cap.release()
cv2.destroyAllWindows()
