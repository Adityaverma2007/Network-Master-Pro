[app]
title = Network Master Pro
package.name = networkmasterpro
package.domain = org.aditya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0,kivymd,certifi,pillow,idna
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE
android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
# यहाँ केवल एक बार archs है, DuplicateOptionError नहीं आएगा
android.archs = arm64-v8a, armeabi-v7a
android.copy_libs = 1

[buildozer]
log_level = 2
# इसे 0 रखने से Root वाला सवाल नहीं आता
warn_on_root = 0
