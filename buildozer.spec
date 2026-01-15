[app]
title = Ping Latency Master
package.name = ping_master_pro
package.domain = org.adityaverma
source.dir = .
version = 1.0

# Professional requirements [cite: 2025-12-14]
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

# Essential Network Permissions [cite: 2026-01-14]
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Stable Build Settings [cite: 2026-01-14]
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.copy_libs = 1
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
