import yfinance as yf
from curl_cffi import requests

# "Too Many Requests. Rate limited, Try after a while." 오류 해결
session = requests.Session(impersonate="chrome")

# 티커설정
ticker = yf.Ticker("SLDP", session=session)

############
# 주요통계 
############

import pandas as pd

# 해당 종목의 재무, 기업정보, 주요통계등 상세한 데이터를 딕셔너리 형태로 제공
key_stats = ticker.info

# key_stats는 딕셔너리 형태인데 출력하면 지저분하게 나오므로 데이터 프레임으로 변환
key_stats_df = pd.DataFrame.from_dict(key_stats, orient='index', columns=['Value'])

# 기본적으로 pandas는 행이 많은 경우 중간생략하고 처음과 끝만 보여주므로 모든정보 보기위함
pd.set_option('display.max_rows', None)

print(key_stats_df)

############
# 재무상태표 가져오기
############

balance_sheet = ticker.balance_sheet
pd.set_option('display.max_rows', None) # 생략없이 전체보기
print(balance_sheet) 