import pyautogui
import subprocess
import time
import pygetwindow as gw
import pyperclip

# 1. 메모장 실행
subprocess.Popen("notepad.exe")
time.sleep(2)

# 2. 메모장 창 찾기
notepad_window = None
for w in gw.getWindowsWithTitle("메모장"):
    if w.visible and "메모장" in w.title:
        notepad_window = w
        break

if notepad_window is None:
    print("메모장을 찾을 수 없습니다.")
    exit()

# 3. 메모장 포커스
notepad_window.activate()
time.sleep(1)

# 4. 인쇄 메뉴 실행
pyautogui.hotkey('alt', 'f')
time.sleep(0.5)
pyautogui.press('p')
time.sleep(1.5)

# 5. 인쇄창 닫기
pyautogui.press('esc')
time.sleep(1)

# 6. 다시 메모장 포커스 및 중앙 클릭
notepad_window.activate()
time.sleep(0.5)

center_x = notepad_window.left + notepad_window.width // 2
center_y = notepad_window.top + notepad_window.height // 2

print(f"클릭 위치: ({center_x}, {center_y})")
pyautogui.click(center_x, center_y)
time.sleep(0.5)

# 7. 커서 활성화 보조 입력
pyautogui.press('home')  # 홈으로 이동
pyautogui.press('left')  # 커서 살짝 움직여 인식 유도
pyautogui.press('right')
time.sleep(0.2)

# 8. 글자 입력
pyautogui.typewrite("OK완료", interval=0.2)  #한글은 처리되지 않음


# pyperclip.copy("완료")
# pyautogui.hotkey("ctrl", "v")
