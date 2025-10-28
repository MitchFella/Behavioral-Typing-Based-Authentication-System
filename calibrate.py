import time
import json
import keyboard

def calculate_wpm(start_time, end_time, words):
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60
    wpm = words / minutes if minutes > 0 else 0
    return round(wpm, 2)

def calibrate():
    print("=== TypeLock Calibration ===")
    print("Type the following sentence as fast and accurately as you can:")
    sentence = "The quick brown fox jumps over the lazy dog"
    print(f"\n> {sentence}\n")
    input("Press Enter when ready...")

    print("\nStart typing now!")

    start_time = None
    typed = ""
    while len(typed) < len(sentence):
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if start_time is None:
                start_time = time.time()
            if event.name == "space":
                typed += " "
            elif len(event.name) == 1:
                typed += event.name

    end_time = time.time()
    words = len(sentence.split())
    wpm = calculate_wpm(start_time, end_time, words)

    profile = {"avg_wpm": wpm}
    with open("user_profile.json", "w") as f:
        json.dump(profile, f)

    print(f"\nCalibration complete. Your average typing speed: {wpm} WPM")
    print("Profile saved to user_profile.json")

if __name__ == "__main__":
    calibrate()
