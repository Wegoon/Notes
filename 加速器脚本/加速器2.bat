adb shell input swipe 828 2403 828 791 200
echo 从：828 2403 滑动到 828 791，持续 200 毫秒

adb shell input tap 1210 2254
echo 点击：1210 2254

echo 延时63秒
choice /t 63 /d y /n >nul 

adb shell input swipe 828 2403 828 791 200
echo 从：828 2403 滑动到 828 791，持续 200 毫秒

adb shell input tap 1539 110
echo 点击：1539 110

echo 延时7秒
choice /t 7 /d y /n >nul 

adb shell input tap 1519 104
echo 点击：1519 104