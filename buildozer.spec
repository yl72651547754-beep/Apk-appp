[[app]

# (str) Title of your application
title = Hello World Arabic

# (str) Package name
package.name = helloworldarabic

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash color (format #RRGGBB)
android.presplash_color = #FFFFFF

# (str) Supported Android architectures
android.arch = arm64-v8a

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 23b

# (int) Android SDK version to use
android.sdk = 31

# (bool) Use a custom virtualenv path
# android.virtualenv = 

# (str) Android build tools version to use
# android.build_tools_version = 

# (list) Permissions (empty = no permissions)
android.permissions =

# (bool) Allow app backup
android.allow_backup = True

# (bool) Run the app in background
# android.background = False

# (str) Gradle dependencies
android.gradle_dependencies =

# (str) Android logcat filters (for debugging)
android.logcat_filters = *:S python:D

# (bool) Activate debug logging
# android.debug = True

# (bool) Copy library files instead of making lib links
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.arch = arm64-v8a

# (bool) Whether to accept the Android SDK license automatically
android.accept_sdk_license = True

#
# iOS specific
#

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display a warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = .git, __pycache__
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#.git
#__pycache__
#
#    -----------------------------------------------------------------------------