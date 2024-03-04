from datetime import datetime

start_date = list(map(int, input().split()))
end_date = list(map(int, input().split()))

days = (end_date[0] - start_date[0]) * 365

start_date[0], end_date[0] = 2009, 2009

start_datetime, end_datetime = datetime(*start_date), datetime(*end_date)

delta = end_datetime - start_datetime

print(delta.days + days, delta.seconds)
