[app]
# (str) ऐप का नाम
title = Network Master Pro

# (str) पैकेज का नाम (बिना स्पेस के)
package.name = networkmasterpro

# (str) डोमेन नाम
package.domain = org.aditya

# (str) सोर्स कोड की लोकेशन
source.dir = .

# (list) शामिल की जाने वाली फाइलें
source.include_exts = py,png,jpg,kv,atlas,json

# (str) वर्जन
version = 1.0

# (list) ज़रूरी लाइब्रेरीज़ (Professional Ping Analysis के लिए idna, certifi ज़रूरी हैं)
requirements = python3,kivy==2.3.0,kivymd,certifi,pillow,idna

# (str) स्क्रीन ओरिएंटेशन
orientation = portrait

# (bool) फुलस्क्रीन मोड
fullscreen = 0

# (list) अनुमतियाँ (Network Analysis के लिए ज़रूरी)
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE

# (int) Android API Level (Play Store के लिए 34 अनिवार्य है)
android.api = 34

# (int) Minimum API support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) SDK लाइसेंस स्वीकार करें
android.accept_sdk_license = True

# (list) आर्किटेक्चर (यहाँ केवल एक बार लिखा है ताकि Duplicate error न आए)
android.archs = arm64-v8a, armeabi-v7a

# (bool) लाइब्रेरी कॉपी करने की सेटिंग
android.copy_libs = 1

[buildozer]
# (int) लॉग लेवल (2 का मतलब है पूरी जानकारी दिखाना)
log_level = 2

# (int) इसे 0 रखने से "Are you sure?" वाला Root सवाल नहीं आएगा
warn_on_root = 0
