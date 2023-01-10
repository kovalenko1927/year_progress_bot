import datetime

def progress_bar(iteration=(365 - (datetime.date(2023, 12, 31) - datetime.date.today()).days) / 3.65, total=100,
                 prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    date_today = datetime.date.today()
    days_progress = 365 - (datetime.date(2023, 12, 31) - datetime.date.today()).days
    return f'\r{prefix}\n{date_today} \n|{bar}| \n{percent}% {suffix} \n{days_progress} / 365'