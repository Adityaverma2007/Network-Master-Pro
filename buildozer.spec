[app]
title = Multi IP Ping Master
package.name = ping_latency_pro
package.domain = org.adityaverma
source.dir = .
version = 0.9

# Ping analysis aur report ke liye zaroori requirements [cite: 2025-12-14]
requirements = python3,kivy==2.3.0,kivymd,pillow

# Sirf network aur storage permissions [cite: 2026-01-14]
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Sabse stable API version GitHub build ke liye [cite: 2026-01-14]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# Licenses auto-accept karne ke liye [cite: 2026-01-14]
android.accept_sdk_license = True

# Debugging ke liye professional log level [cite: 2026-01-14]
log_level = 2
