[app]

# (str) Title of your application
title = Network Master Pro

# (str) Package name
package.name = netpro_master_scan

# (str) Package domain (needed for android packaging)
package.domain = org.networkpro

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.2

# (list) Application requirements
# Mi mobiles par KivyMD aur Pillow crash rokne ke liye
requirements = python3, kivy==2.3.0, kivymd, pillow, requests

# (list) Permissions
# Mi policy ke liye Storage permissions sabse zaroori hain
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) use pose-setup build (needed for modern android)
android.accept_sdk_license = True

# (str) Android architectures to build for
# Mi mobiles ke liye arm64-v8a hona bahut zaroori hai
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Android additionnal libraries to copy into libs/armeabi
# android.add_libs_armeabi = lib/libcrypto.so, lib/libssl.so

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with colors))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
