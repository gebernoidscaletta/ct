import json
import os
import datetime
from pathlib import Path
from util.utilLogging import Log

log = Log()

class builderGeofence:

    @staticmethod
    def convertToPayload(inputPath, outputPath):
        try:
            with open(inputPath,'r') as f:
                geojsonData = json.load(f)
            
            areaName = inputPath.stem
            folderPath = str(inputPath.parent)

        except Exception as e:
            log.error("Error Processing")
            log.error(f"Error Message : {e}")
            return 0
        