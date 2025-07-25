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
    print("메모장 창을 찾을 수 없습니다.")
    exit()

# 3. 메모장 포커스
notepad_window.activate()
time.sleep(1)

# 4. 메뉴 위치 계산 후 클릭 (좌상단 [파일] 메뉴)
file_menu_x = notepad_window.left + 30   # 대략적인 [파일] 위치
file_menu_y = notepad_window.top + 40
pyautogui.click(file_menu_x, file_menu_y)
time.sleep(0.5)

# 5. 드롭다운된 [인쇄] 메뉴 위치 클릭 (대략 5번째 항목)
print_menu_x = file_menu_x + 30
print_menu_y = file_menu_y + 130
pyautogui.click(print_menu_x, print_menu_y)
time.sleep(1.5)

# 6. 인쇄창의 [취소] 버튼 위치 클릭 (대략 중앙 오른쪽 아래)
screen_width, screen_height = pyautogui.size()
cancel_x = screen_width // 2 + 200
cancel_y = screen_height // 2 + 150
pyautogui.click(cancel_x, cancel_y)
time.sleep(1)

# 7. 메모장 본문 클릭하여 커서 위치 확보
notepad_window.activate()
time.sleep(0.5)
text_x = notepad_window.left + 200
text_y = notepad_window.top + 200
pyautogui.click(text_x, text_y)
time.sleep(0.5)

# 8. 클립보드에 "완료" 복사 후 붙여넣기
pyperclip.copy("완료")
pyautogui.hotkey("ctrl", "v")
