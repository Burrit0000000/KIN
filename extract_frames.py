import cv2
import os
import urllib.request

videos = {
    'mischief': ('https://meetyourkin.com/mischief-video.mp4', 4.0),
    'vortex': ('https://meetyourkin.com/vortex-video.mp4', 4.0),
    'forge': ('https://meetyourkin.com/forge-video.mp4', 3.0),
    'aether': ('https://meetyourkin.com/aether-video.mp4', 3.0),
    'catalyst': ('https://meetyourkin.com/catalyst-video.mp4', 4.0),
    'cipher': ('https://meetyourkin.com/cipher-video.mp4', 4.0)
}

assets_dir = '/Users/xeniabusigin/.gemini/antigravity/scratch/KR8TIV/assets'
os.makedirs(assets_dir, exist_ok=True)

for name, (url, sec) in videos.items():
    print(f"Processing {name} at {sec} seconds...")
    vid_path = f"/tmp/{name}.mp4"
    if not os.path.exists(vid_path):
        urllib.request.urlretrieve(url, vid_path)
    
    cap = cv2.VideoCapture(vid_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps != fps: # NaN
        fps = 30.0
    
    frame_no = int(sec * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
    ret, frame = cap.read()
    
    if ret:
        out_path = os.path.join(assets_dir, f"{name}-video-poster.jpg")
        cv2.imwrite(out_path, frame)
        print(f"Saved {out_path}")
    else:
        print(f"Failed to extract frame for {name}")
    
    cap.release()
