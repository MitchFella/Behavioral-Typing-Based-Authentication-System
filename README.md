# Behavioral-Typing-Based-Authentication-System
This repository contains the implementation of a Behavioral Typing Based Authentication System. The system leverages behavioral typing techniques to enhance the security and reliability of user authentication processes.
# How It Works

During calibration, the program measures your typing speed (words per minute).

During monitoring, it compares your new typing speed to your baseline.

If your typing speed differs by more than 25%, the system locks.
# Future Improvements
System-wide Monitoring:
Extend the program to run in the background and monitor typing activity across all applications, not just during the test window.

Password Re-authentication:
Instead of locking the workstation, prompt the user to re-enter their password or use multi-factor authentication when anomalies are detected.

Typing Pattern Analysis:
Track keypress intervals, rhythm, and error rates for more accurate behavioral profiling instead of relying only on WPM.

GUI Interface:
Add a small desktop interface for calibration, status monitoring, and sensitivity adjustment.