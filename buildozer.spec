[app]

# (string) Title of your application
title = NetworkMasterPro

# (string) Package name
package.name = netmasterpro

# (string) Package domain
package.domain = org.aditya

# (string) Source code where the main.py is located
source.dir = .

# (string) Application version (Mandatory line - Fix for your latest error)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0

# (int) Android API 30 is stable for Ping
android.api = 30
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET
android.archs = arm64-v8a
log_level = 2
