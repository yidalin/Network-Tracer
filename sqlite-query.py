from functions import *

sqlite_connnect('tracer.sqlite')

#print(sqlite_query_all('tracer')[2])
print(sqlite_query('select count, latency_avg from tracer where datetime="2017-09-22 01:03"'))

sqlite_close()

