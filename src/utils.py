"""
utils.py
--------
Helper functions, safe logging, dataset loading etc.
"""

import json
import datetime

def log_event(message: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[FoodBridge LOG {timestamp}] {message}")

def load_json(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)
