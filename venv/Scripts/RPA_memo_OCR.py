#####################################
# ; ✅ 문자 기반 처리란?
# ; 화면에서 "파일", "인쇄", "취소" 등의 텍스트를 인식(OCR) 하여 해당 위치를 찾아 클릭하는 방식입니다.

# ; 이런 기능은 pyautogui 단독으로는 불가능하며, 아래 라이브러리가 필요합니다:

# ; ✅ 필요한 라이브러리
# ; 라이브러리	설명
# ; pyautogui	마우스 클릭 및 스크린샷
# ; pytesseract	OCR(글자 인식)
# ; Pillow	이미지 처리
# ; tesseract	Google의 OCR 엔진, 따로 설치 필요

# ; ✅ 설치 명령어
# ; bash
# ; 복사
# ; 편집
# ; pip install pyautogui pytesseract pillow
# ; 그리고 아래도 설치해야 합니다:

# ; 🔧 Tesseract OCR 설치 (Windows)
# ; https://github.com/tesseract-ocr/tesseract 접속

# ; "tesseract-ocr-w64-setup" 다운로드 및 설치

# ; 설치 경로 확인 (예: C:\Program Files\Tesseract-OCR\tesseract.exe)

# ; ✅ 환경설정 코드에 추가
# ; python
# ; 복사
# ; 편집
# ; import pytesseract
# ; pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
################################################


import pyautogui
import pytesseract
from PIL import Image
import time
import pyperclip
import subprocess
import pygetwindow as gw

# tesseract 설치 경로 설정
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 텍스트 위치 찾기 함수
def find_text_on_screen(target_text):
    screenshot = pyautogui.screenshot()
    data = pytesseract.image_to_data(screenshot, lang='kor+eng', output_type=pytesseract.Output.DICT)

    for i, text in enumerate(data['text']):
        if target_text in text:
            x = data['left'][i] + data['width'][i] // 2
            y = data['top'][i] + data['height'][i] // 2
            return (x, y)
    return None

# 1. 메모장 실행
subprocess.Popen("notepad.exe")
time.sleep(2)

# 2. 메모장 창 찾고 포커스
notepad_window = None
for w in gw.getWindowsWithTitle("메모장"):
    if w.isVisible and "메모장" in w.title:
        notepad_window = w
        break

if notepad_window:
    notepad_window.activate()
    time.sleep(1)

# 3. "파일" 메뉴 클릭
file_pos = find_text_on_screen("파일")
if file_pos:
    pyautogui.click(file_pos)
    time.sleep(1)
else:
    print("파일 메뉴를 찾을 수 없습니다.")
    exit()

# 4. "인쇄" 메뉴 클릭
print_pos = find_text_on_screen("인쇄")
if print_pos:
    pyautogui.click(print_pos)
    time.sleep(2)
else:
    print("인쇄 메뉴를 찾을 수 없습니다.")
    exit()

# 5. "취소" 버튼 클릭
cancel_pos = find_text_on_screen("취소")
if cancel_pos:
    pyautogui.click(cancel_pos)
    time.sleep(1)
else:
    print("취소 버튼을 찾을 수 없습니다.")
    exit()

# 6. 본문 클릭하여 커서 확보
notepad_window.activate()
time.sleep(0.5)
pyautogui.click(notepad_window.left + 200, notepad_window.top + 200)
time.sleep(0.5)

# 7. 클립보드 붙여넣기 방식으로 "완료" 입력
pyperclip.copy("완료")
pyautogui.hotkey("ctrl", "v")
