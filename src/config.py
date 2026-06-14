# import os
# import sys
#
# if getattr(sys, 'frozen', False):
#     BASE_DIR = os.path.dirname(sys.executable)
# else:
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# MODEL_PATH = os.path.join(BASE_DIR, 'Artifacts', 'spam_model.pkl')
# DATA_PATH = os.path.join(BASE_DIR, 'Data', 'SMSSpamCollection')
# ARTIFACTS_DIR = os.path.join(BASE_DIR, 'Artifacts')
# os.makedirs(ARTIFACTS_DIR, exist_ok=True)


import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = os.path.join(BASE_DIR, 'Artifacts', 'spam_model.pkl')
DATA_PATH = os.path.join(BASE_DIR, 'Data', 'SMSSpamCollection')
ARTIFACTS_DIR = os.path.join(BASE_DIR, 'Artifacts')
os.makedirs(ARTIFACTS_DIR, exist_ok=True)

print(f"BASE_DIR: {BASE_DIR}")
print(f"DATA_PATH: {DATA_PATH}")
print(f"File exists: {os.path.exists(DATA_PATH)}")