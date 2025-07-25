import pyautogui
import time
import subprocess

# 1. 메모장 실행
subprocess.Popen("notepad.exe")
time.sleep(2)

# 2. "Hello World" 입력
pyautogui.write("Hello World!", interval=0.1)

# 3. 저장 단축키 (Ctrl+S)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

# 4. 파일명 입력 후 저장
pyautogui.write("sample.txt")
pyautogui.press('enter')
time.sleep(1)

# 5. 메모장 종료  
pyautogui.hotkey('alt', 'f4')
