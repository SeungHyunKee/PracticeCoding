## 6043
# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력해보자. 
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

# f1, f2 = input().split()
# f3 = float(f1)/float(f2)
# print(format(f3,".3f"))







# ###시간대데이터 처리###
# 1
# # 시간대변경시 사용
# import pandas as pd
# # datatime 만들기
# data = pd.Timestamp('2022-12-05 01:40:00')

# data_in_london  =data.tz_localize(tz = 'Europe/London')
# print(data_in_london)

# # 시간대 변경
# data_in_london.tz_convert('Africa/Abidjan')
# dates = pd.Series(pd.data_range('2/2/2022', periods = 3, freq = 'M'))
# temp = dates.dt.tz_localize('Africa/Abidjan')

# print(temp)


# # 2
# import pandas as pd
# from pytz import all_timezone
# from pytz import timezone

# dates = pd.Series(pd.data_range('2/2/2022', periods = 3, freq = 'M'))

# print(all_timezones[0:2])
# dates.dt.tz_localize('dateutil/Aisa/Seoul')
# tz = pytz.timezone('Asia/Seoul')
# temp01 = dates.dt.tz_localize(tz)
# print(temp01)


# 3
# 날짜와 시간 선택하기



# import pandas as pd

# dataframe = pd.DataFrame()
# temp = dataframe['date'] = pd.date_range('1/1/2022', periods=150, freq='w')
# # 년 월 일 시 분에 대한 특성을 만듭니다.
# dataframe['year'] = dataframe['date'].dt.year
# dataframe['month'] = dataframe['date'].dt.month
# dataframe['day'] = dataframe['date'].dt.day
# dataframe['hour'] = dataframe['date'].dt.hour
# dataframe['minute'] = dataframe['date'].dt.minute

# print(dataframe.head(30))


# 12
# 날짜간의 차이계산
# 판다스의 TimeDelta 이용하면 두지점사이의 시간변화를 기록한 특성 계산한다
import pandas as pd

dataframe = pd.DataFrame()
dataframe['Arrived'] = [pd.Timestamp('01-01-2022'), pd.Timestamp('01-04-2022')]
dataframe['Left'] = [pd.Timestamp('01-01-2022'), pd.Timestamp('01-06-2022')]

dataframe['Left'] - dataframe['Arrived']

data = pd.Series(delta.days for delta in (
    dataframe['Left'] - dataframe['Arrived']))
print(data)



# 14
# 시계열 데이터에서 누락된값 처리
# 두 포인트 사이의 직선이 비선형이라고 가정하면 interpolate의 method 매개변수를 사용해 다른 보간방법을 지정할수있다
# 누락된 값의 간격이 커서 전체를 간격을 보간하는것이 좋지않을때는 limit 매개변수를 사용하여 보간값의 개수를 제한하고
# limit_direction매개변수에서 마지막 데이터로 앞쪽방향으로 보간할지 그 반대로 할지 지정할수 있다
import pandas as pd
import numpy as np

time_index = pd.date_range('01/01/2022', periods=5, freq='M')
dataframe = pd.DataFrame(index=time_index)  # 데이터 프레임을 만들고 인덱스를 지정
print(dataframe)

dataframe['Sales'] = [1.0, 2.0, np.nan, np.nan, 5.0]  # 누락된 값이 있는 특성 생성
# data = dataframe.interpolate() # 누락된 값을 보간
data = dataframe.ffill()  # 앞쪽으로 Forward-fill
data01 = dataframe.bfill()  # 뒤쪽으로 Back-fill
data02 = dataframe.interpolate(method='quadratic')
# 보간 방향 지정
data03 = dataframe.interpolate(limit=1, limit_direction='forward')
print(data03)
