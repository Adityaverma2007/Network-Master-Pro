[app]

# (string) Title of your application
title = NetworkMasterPro

# (string) Package name
package.name = netmasterpro

# (string) Package domain (needed for android packaging)
package.domain = org.aditya

# (string) Source code where the main.py is located
source.dir = .

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (int) Android API to use
android.api = 30

# (int) Minimum API your APK will support.
android.minapi = 21

# (string) Android NDK version to use
android.ndk = 25b

# (bool) Use the official google play services
android.accept_sdk_license = True

# (list) Permissions
android.permissions = INTERNET

# (list) Supported architectures
android.archs = arm64-v8a

# (int) Log level (1 = error only, 2 = all)
log_level = 2
