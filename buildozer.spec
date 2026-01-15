[app]

# (str) Title of your application
title = Multi IP Ping Master

# (str) Package name
package.name = ping_latency_pro

# (str) Package domain (needed for android packaging)
package.domain = org.adityaverma

# (str) Source code where the main.py live
source.dir = .

# (str) Application version (Professional start) [cite: 2026-01-06]
version = 1.0

# (list) Application requirements
# Ping logic aur UI ke liye zaroori libraries [cite: 2025-12-14]
requirements = python3,kivy==2.3.0,kivymd,pillow

# (list) Permissions
# Network analysis aur report save karne ke liye [cite: 2026-01-14, 2025-12-14]
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
# API 31 sabse stable hai GitHub Actions ke liye [cite: 2026-01-14]
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (leave empty to download)
android.ndk_path = 

# (str) Android SDK directory (leave empty to download)
android.sdk_path = 

# (bool) Use --copy-libs instead of packaging them in the APK
android.copy_libs = 1

# (str) The Android arch to build for
android.archs = arm64-v8a

# (bool) automatically accept SDK license
# Isse "Broken pipe" error nahi aayegi [cite: 2026-01-14]
android.accept_sdk_license = True

# (int) Log level (2 = error only, 1 = info, 0 = debug)
log_level = 2

# (str) Android entry point, default is to use PythonActivity
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
# (int) Log level (2 = error only)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
