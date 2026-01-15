[app]
title = Network Master Pro
package.name = netpro_master_scan
package.domain = org.networkpro
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.3

# आवश्यकताओं में 'requests' और 'threading' के लिए 'python3' पर्याप्त है
requirements = python3, kivy==2.3.0, kivymd, pillow

# Mi मोबाइल और रिपोर्ट डाउनलोड के लिए जरूरी परमिशन
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_NETWORK_STATE

# Mi मोबाइल (Android 11-14) के लिए सही API लेवल्स
android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# सबसे महत्वपूर्ण: Mi मोबाइल के लिए Architecture
android.archs = arm64-v8a, armeabi-v7a

# पिंग कमांड चलाने के लिए सिस्टम एक्सेस (Mi Policy Fix)
android.allow_backup = True

# लॉग्स को छोटा रखने के लिए ताकि बिल्ड फेल न हो
log_level = 1

[buildozer]
warn_on_root = 1
