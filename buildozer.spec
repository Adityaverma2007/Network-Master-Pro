[app]

# (str) Title of your application
title = Network Master Pro

# (str) Package name
package.name = networkmasterpro

# (str) Package domain (needed for android packaging)
package.domain = org.aditya

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 0.1

# (list) Application requirements
# हमने इसमें kivymd और certifi जोड़ दिया है ताकि पिंग एनालिसिस सही से चले
requirements = python3,kivy==2.3.0,kivymd,certifi,pillow,idna

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
# नेटवर्क और पिंग के लिए ये परमिशन बहुत ज़रूरी हैं
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# (int) Android API to use (34 is latest for Play Store)
android.api = 34

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
# GitHub के साथ टकराव रोकने के लिए हमने इसे फिक्स कर दिया है
android.ndk = 25b

# (bool) Use the shared SDK/NDK
android.accept_sdk_license = True

# (str) Android architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) skip update of the android toolchain
android.skip_update = False

# (bool) Copy library instead of making a lib dir
android.copy_libs = 1

# (list) The Android architectures for which to build
# Play Store के लिए arm64-v8a ज़रूरी है
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
