import os
from tqdm import tqdm
from datetime import datetime
import csv

################################################################################
#                          read WIDEFIELD IMAGING DATA
################################################################################

# moved to preproceessWidefield.py

################################################################################
#                         read BONSAI CSV
################################################################################
 
def load_bonsai_timestamps(file_path, timestamp_column=0):
    # load bonsai timestamp and return the array of timestamps
    # file_path: bonsai timestamp csv file
    # timestamp_column: column number of bonsai timestamp

    assert os.path.isfile(file_path), "The path specified does not exist."
    state = []
    ts = []

    with open(file_path) as f:
        reader = csv.reader(f)
        for row in reader:
            state_text = row[0]
            timestamp_text = row[timestamp_column]
            timestamp_text_parts = timestamp_text.split(".")
            microsecond_text = int(timestamp_text_parts[1][0:6])
            fixed_timestamp_text = f"{timestamp_text_parts[0]}.{microsecond_text:06}"

            state.append(state_text)
            try:
                ts.append(datetime.strptime(fixed_timestamp_text, "%Y-%m-%dT%H:%M:%S.%f"))
            except ValueError:
                print(f'invalid timestamp: {timestamp_text}')
                break

    return ts, state

def detect_bonsai_state_change(file_path, timestamp_column=1):
    # detect bonsai state change False-to-True and return the array of timestamps
    # file_path: bonsai timestamp csv file

    state_change = []

    ts, state = load_bonsai_timestamps(file_path, timestamp_column)

    for i in tqdm(range(1, len(ts))):
        if state[i].lower() == 'true' and state[i-1].lower() == 'false':
            state_change.append(ts[i])

    return state_change        



################################################################################
#                          read BEHAVIORAL VIDEO
################################################################################
def load_behavior_video_individual_frame(file_path, frame_idx = 0):
    # load behavior video frames (.mp4) and return the array of frames
    # file_path: behavior video file
    # frame_idx: frame index to be loaded

    assert os.path.isfile(file_path), "The path specified does not exist."
    cap = cv2.VideoCapture(str(file_path))
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
    im = cap.read()[1] 
    return im











