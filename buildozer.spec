[app]

# (str) Title of your application
title = English Learning App

# (str) Package name
package.name = englishlearning

# (str) Package domain (needed for android/ios packaging)
package.domain = org.englishlearning

# (source.dir) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.png

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,flask,flask-cors,requests

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based app
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation
# android.version_code = 1

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) explicitly set numeric Android ApplicationVesionCode -> method a
#android.numeric_version = 1

# (list) patterns used to whitelist font files
#android.whitelist = lib-dynload/termios.so

# (list) MD5 sums of Java files to keep to prevent false jar signing warning
# List can be empty to disable the verification
#android.Java_files_to_keep = None

# (list) copy files to delete after the build the APK (only for build.sub only
;android.delete_src = bin, build, buildozer.spec

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup agent class. See the documentation to understand this file.
# android.backup_agent_class = com.example.myapp.CustomBackupAgent

# (str) The Java package used to override the default ApplicationId compat value
# android.application_id = org.englishlearning.englishlearning

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file for custom backup schemes.
# android.fullbackup_content = %(source.dir)s/mybackup.xml

# (list) An optional list of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow down the
# build process. Allows wildcards matching with * and ?.
# OUYA Console icon. It must be a 732x412 png image.
#android.add_src =

# (list) Pattern to whitelist (only used if build.uses_split_resources is true)
#android.whitelist = lib-dynload/termios.so

# (str) Path to the Android SDK used by android-configure
#android.sdk_path = /opt/android-sdk

# (str) Path to the Android NDK used by android-configure
#android.ndk_path = /opt/android-ndk

# (bool) automatically accept Android SDK licenses (Android15:+)
android.accept_sdk_license = True

# (bool) Enable AndroidX support. With this enabled you must have the Android
# SDK API >= 28 installed. Defaults to False
android.enable_androidx = True

# (bool) enable Android auto backup feature (Android API >=23)
# android.allow_backup = True

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# android.archs = arm64-v8a

# (bool) enable AndroidX support
# android.enable_androidx = True

# (bool) It is used for Android project creation.
android.gradle_dependencies =

# (list) Pattern to whitelist (only used if build.uses_split_resources is true)
#android.whitelist = lib-dynload/termios.so

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning (1) or not (0)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = .buildozer

# (str) Path to build output (i.e. where to put the built APK)
bin_dir = ./bin
