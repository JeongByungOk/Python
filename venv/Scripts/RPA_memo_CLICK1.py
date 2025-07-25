from pywinauto import Desktop, Application
import time

# 바탕화면에 있는 메모장 창들 목록 가져오기
windows = Desktop(backend="uia").windows(title_re=".*메모장.*", top_level_only=True)

# 여러 창이 있을 때 첫 번째 창만 연결
if len(windows) >= 1:
    target_win = windows[0]
    app = Application(backend="uia").connect(handle=target_win.handle)
    dlg = app.window(handle=target_win.handle)
    dlg.set_focus()

    # 내용 입력
    dlg.type_keys("Hello, this is a test.", with_spaces=True)

    # 이후 자동화 로직 예시 (파일 메뉴 클릭)
    file_menu = dlg.child_window(title="파일", control_type="MenuItem")
    file_menu.click_input()
    time.sleep(1)

    # 저장 클릭
    save_menu = dlg.child_window(title="저장", control_type="MenuItem")
    save_menu.click_input()
    save_menu.invoke()
    time.sleep(1)


    # "다른 이름으로 저장" 창 찾기
    # 저장창은 top-level이 아닌 자식창이므로 Desktop이 아니라 dlg에서 검색
    save_dlg = dlg.child_window(title_re=".*다른 이름으로 저장.*", control_type="Window")
    save_dlg.wait('visible', timeout=10)
    #save_dlg = Desktop(backend="uia").window(title_re=".*다른 이름으로 저장.*")

    # 현재 떠 있는 모든 창 제목 확인
    windows = Desktop(backend="uia").windows()
    for win in windows:
        title = win.window_text()
        if title.strip():  # 빈 제목 제외
            print(title)

    save_dlg.wait('visible', timeout=10)

    # 저장 버튼 클릭
    save_button = save_dlg.child_window(title="저장(S)", control_type="Button")
    save_button.wait('enabled', timeout=5)
    save_button.click_input()
    save_menu.invoke()
    
    
    # save_button = save_dlg.child_window(title=".*저장.*", control_type="Button")
    # save_button.print_control_identifiers
    # save_button.click_input()
    # time.sleep(1)

else:
    print("메모장 창이 없습니다.")