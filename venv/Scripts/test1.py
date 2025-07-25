from pywinauto import Application
import time

app = Application(backend="uia").start("notepad.exe")
dlg = app.window(title_re=".*메모장")
#dlg.wait("visible")
time.sleep(2)

# 텍스트 입력
dlg.Edit.type_keys("자동화된 테스트입니다!", with_spaces=True)

# 저장 (메뉴 접근 예시)
dlg.menu_select("파일->다른 이름으로 저장")
