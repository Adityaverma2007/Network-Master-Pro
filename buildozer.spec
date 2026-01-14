[app]

# (str) Title of your application
title = Network Master Pro

# (str) Package name
package.name = networkmasterpro

# (str) Package domain (needed for android packaging)
package.domain = org.networkpro

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.7

# (list) Application requirements
# [cite: 2026-01-06] Added 'android' for storage path access
requirements = python3, kivy==2.3.0, hostpython3, android, pillow

# (list) Permissions
# [cite: 2026-01-06] Crucial for saving reports and network access
android.permissions = INTERNET, ACCESS_NETWORK_STATE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# [cite: 2026-01-06] Play Store 2026 standards
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is to use start.py
android.entrypoint = main.py

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) indicates whether the screen should stay on
android.wakelock = True

# (str) Orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a lib/ folder
android.copy_libs = 1

# [cite: 2026-01-14] Work environment D drive is handled by local runner
# Buildozer settings for build process
build_mode = debug

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build artifacts
bin_dir = ./bin
