[app]
title = Ping Latency Master
package.name = pingmaster_pro
package.domain = org.adityaverma
source.dir = .
version = 1.0

# Ping analysis ke liye requirements [cite: 2025-12-14]
requirements = python3,kivy==2.3.0,kivymd,pillow

# Permissions (Internet aur Storage) [cite: 2026-01-14]
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Final Stable API Settings [cite: 2026-01-14]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# License accept karne ki setting [cite: 2026-01-14]
android.accept_sdk_license = True

# Copy libraries for stability [cite: 2026-01-14]
android.copy_libs = 1

# Log level professional rakhein [cite: 2026-01-14]
log_level = 2
