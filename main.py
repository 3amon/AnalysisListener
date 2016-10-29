import os
import subprocess
import time
import shutil

WATCH_DIR = "./uploads"

PROCESSING_DIR = "./processing"

OUTPUT_DIR = "./output"

def moveDir(src, dest):
    w = os.walk(src)
    for root, dirs, files in os.walk(src):
        for file in files:
            shutil.move(os.path.join(src, file), os.path.join(dest, file))

while True:
    time.sleep(10)
    print "Looking for new files!"
    moveDir(WATCH_DIR, PROCESSING_DIR);
    # python ./pyAudioAnalysis/audioAnalysis.py featureExtractionDir -i ./output -mw 50.0 -ms 25.0
    subprocess.Popen(
        ['python', './pyAudioAnalysis/audioAnalysis.py', 'featureExtractionDir', "-i", PROCESSING_DIR, '-mw', "50.0",
         "-ms", "25.0"]).wait()
    moveDir(PROCESSING_DIR, OUTPUT_DIR);