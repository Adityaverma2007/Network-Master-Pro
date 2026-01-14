[app]

# (str) Title of your application
title = Network Master Pro

# (str) Package name
package.name = networkmasterpro

# (str) Package domain (needed for android packaging)
package.domain = org.aditya

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0

# (list) Application requirements
# प्रोफेशनल पिंग रिपोर्ट के लिए idna और certifi ज़रूरी हैं
requirements = python3,kivy==2.3.0,kivymd,certifi,pillow,idna

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
# नेटवर्क एनालिसिस के लिए ये परमिशन अनिवार्य हैं
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# (int) Android API to use (34 is required for Play Store)
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use the shared SDK/NDK
android.accept_sdk_license = True

# (list) The Android architectures for which to build
# यहाँ केवल एक बार archs लिखा है, ताकि DuplicateOptionError न आए
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy library instead of making a lib dir
android.copy_libs = 1

[buildozer]
# (int) Log level (2 = debug)
log_level = 2

# (int) इसे 0 रखने से Root वाला सवाल नहीं पूछा जाएगा और EOFError नहीं आएगा
warn_on_root = 0
