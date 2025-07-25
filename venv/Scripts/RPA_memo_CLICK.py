import sys
import time
from pywinauto import Application, Desktop

# 메모장 실행
app = Application(backend="uia").start("notepad.exe")
# CPU 사용량이 낮아질 때까지 대기 (초기화 안정화)
app.wait_cpu_usage_lower(threshold=5, timeout=30)
time.sleep(2)

# 바탕화면에 있는 메모장 창들 목록 가져오기
windows = Desktop(backend="uia").windows(title_re=".*메모장.*", top_level_only=True)

if len(windows) >= 1:
    target_win = windows[0]
    app = Application(backend="uia").connect(handle=target_win.handle)
    dlg = app.window(handle=target_win.handle)

# 내용 입력
dlg.type_keys("Hello, this is a test.", with_spaces=True)

# # '다른 이름으로 저장' 호출
# dlg.menu_select("파일(F)->다른 이름으로 저장(A)...")
# time.sleep(1)  # 저장창이 뜨도록 대기

# 파일메뉴 클릭
file_menu = dlg.child_window(title_re="파일", control_type="MenuItem")
file_menu.click_input()
time.sleep(1)

# 저장메뉴 클릭
save_menu = dlg.child_window(title_re="저장", control_type="MenuItem")
save_menu.click_input()
save_menu.invoke()    
time.sleep(1)

# 기존파일명으로 작업가능
resave_dlg = None
try : 
    # "다른 이름으로 저장" 창 처리는 top-level이 아닌 자식창이므로 Desktop이 아니라 dlg에서 검색
    save_dlg = dlg.child_window(title_re=".*저장.*", control_type="Window")
    save_dlg.wait('visible', timeout=5)
except :
    print("기존파일 오픈후 저장")
    sys.exit()

# 파일명 입력창에 이름 입력
filename_edit = save_dlg.child_window(auto_id="1001", control_type="Edit")
filename_edit.wait('ready', timeout=2)
filename_edit.set_edit_text("test_saving.txt")

# 저장 버튼 클릭
save_button = save_dlg.child_window(title="저장(S)", control_type="Button")
save_button.wait('enabled', timeout=5)
save_button.click_input()

#기존파일존재 : 다른 이름으로 저장 확인창이 뜨는지 확인
resave_dlg = None
try : 
    # "다른 이름으로 저장 확인" 창 처리는 top-level이 아닌 자식창이므로 Desktop이 아니라 dlg에서 검색
    resave_dlg = dlg.child_window(title_re=".*확인", control_type="Window")
    resave_dlg.wait('visible', timeout=10)
except:
    print("저장시 기존파일이 존재함")

if resave_dlg:    
    # 예/아니오 버튼선택
    yes_button = resave_dlg.child_window(title="예(Y)", control_type="Button")
    yes_button.wait('enabled', timeout=5)
    yes_button.click_input()
