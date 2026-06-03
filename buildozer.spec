[app]
title = SpeedCar
package.name = speedcar
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3

version = 1.0

requirements = python3,kivy,hostpython3

orientation = portrait
fullscreen = 1
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# این خط بسیار حیاتی است؛ جایگزین دستور yes قدیمی شده و لایسنس‌ها را خودکار قبول می‌کند
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
