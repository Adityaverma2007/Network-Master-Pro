[app]
title = NetworkMasterPro
package.name = networkmasterpro
package.domain = org.aditya.net
source.dir = .
version = 1.1

# Original requirements only [cite: 2025-12-14]
requirements = python3,kivy==2.3.0

android.permissions = INTERNET
# API 30 is more stable for ping subprocess [cite: 2026-01-14]
android.api = 30
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
log_level = 2
