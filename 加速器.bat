set n=0
:n
set /a n+=1
If %n%==101 goto  nn
echo 第 %n% 次循环

adb shell input tap 846 1345
echo 点击：846 1345

echo 延时55秒
choice /t 55 /d y /n >nul 

adb shell input swipe 526 1248 503 727 200
echo 从：526 1248 滑动到 503 727，持续 200 毫秒

adb shell input tap 973 194
echo 点击：973 194

echo 延时7秒
choice /t 7 /d y /n >nul 

adb shell input tap 987 218
echo 点击：987 218


adb shell input swipe 1066 1706 550 1702 200
echo 从：1066 1706 滑动到 550 1702，持续 200 毫秒

echo 延时1秒
choice /t 1 /d y /n >nul 

adb shell input tap 523 1421
echo 点击：523 1421

echo 延时5秒
choice /t 5 /d y /n >nul 

goto n
:nn