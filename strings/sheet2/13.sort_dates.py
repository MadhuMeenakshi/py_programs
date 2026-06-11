from datetime import datetime

def sort_dates(dates: list[str]) -> list[str]:
    return sorted(dates, key=lambda d: datetime.strptime(d, "%Y-%m-%d"))

result = sort_dates(["2021-05-21", "2019-01-12", "2020-12-15"])
