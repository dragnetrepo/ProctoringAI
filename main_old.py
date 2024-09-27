from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles

from eye_tracker import track_eye
from head_pose_estimation import detect_head_pose
from mouth_opening_detector import mouth_opening_detector
from person_and_phone import detect_phone_and_person


app = FastAPI()


@app.post("/analyze_video")
def read_root(video_urls: str=None):
    video_url = "http://localhost:8000/static/loom-video.mp4"
    track_eye(video_url)
    detect_head_pose(video_url)
    mouth_opening_detector(video_url)
    detect_phone_and_person(video_url)


    return {"message": "Success"}

app.mount("/static", StaticFiles(directory="devdata/"), name="static")