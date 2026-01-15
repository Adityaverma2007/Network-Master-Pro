[app]
title = Network Master Pro
package.name = netpro_master_final
package.domain = org.networkpro
source.dir = .
version = 0.5
requirements = python3, kivy==2.3.0, kivymd, pillow
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, ACCESS_NETWORK_STATE
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
log_level = 1

[buildozer]
warn_on_root = 1
