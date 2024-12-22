# Логирование в файл с именем yyyy_mm_dd.log с отметкой времени hh-mm-ss 
# в начале строки
import time

def log_line(ldata):
    t = time.localtime()
    fname = f'{t.tm_year}_{t.tm_mon:02d}_{t.tm_mday:02d}.log'
    tstamp = f'{t.tm_hour:02d}-{t.tm_min:02d}-{t.tm_sec:02d}'
    try:
        with open(fname, 'a') as file:
            file.write(f'{tstamp}: {ldata}\n')
    except:
        pass

if __name__ == '__main__':
    log_line('Hello!')
    log_line('Hello 1')
    log_line('Hello 2')