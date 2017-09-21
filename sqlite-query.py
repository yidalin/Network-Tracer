from functions import *

sqlite_connnect('tracer.sqlite')

#print(sqlite_query_all('tracer'))
print(sqlite_query('select count, host, latency_avg from tracer where datetime="2017-09-22 01:59"'))

sqlite_close()

