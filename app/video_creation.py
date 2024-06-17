import cv2

def create_video(image, duration):
    # Initialize video writer
    video_writer = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (image.shape[1], image.shape[0]))

    # Write frames to video
    for _ in range(duration * 30):  # 30 frames per second
        video_writer.write(image)

    video_writer.release()
    return 'output_video.mp4'