import time
import json
import os
import keyboard

def calculate_wpm(start_time, end_time, words):
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    wpm = words / minutes if minutes > 0 else 0
    return round(wpm, 2)

def load_profile():
    try:
        with open("user_profile.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Run calibrate.py first to create your profile.")
        exit()

def monitor_typing(threshold=0.25):
    profile = load_profile()
    baseline_wpm = profile["avg_wpm"]

    print(f"Monitoring typing... baseline WPM = {baseline_wpm}")
    print("Type any sentence (press Enter when done):")

    while True:
        input("Press Enter to start a typing test... ")
        sentence = input("Type a short sentence: ")
        if not sentence.strip():
            continue

        start_time = time.time()
        print("Start typing:")
        typed = ""
        while len(typed) < len(sentence):
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "space":
                    typed += " "
                elif len(event.name) == 1:
                    typed += event.name

        end_time = time.time()
        words = len(sentence.split())
        wpm = calculate_wpm(start_time, end_time, words)

        deviation = abs(wpm - baseline_wpm) / baseline_wpm
        print(f"\nYour WPM: {wpm} | Deviation: {deviation*100:.1f}%")

        if deviation > threshold:
            print("Typing anomaly detected! Locking workstation...")
            try:
                os.system("rundll32.exe user32.dll,LockWorkStation")
            except Exception as e:
                print("Lock failed:", e)
            break
        else:
            print("Typing matches expected profile.\n")

if __name__ == "__main__":
    monitor_typing()
