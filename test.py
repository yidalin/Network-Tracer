from functions import *

sqlite_connnect('tracer.sqlite')

sqlite_query_all('tracer')

print(sqlite_query('select count from tracer')[0][1])
