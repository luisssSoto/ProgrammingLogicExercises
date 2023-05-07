def solution(year):
	century=year%100
	if century == 0:
		century=year//100
		return century
	else:
		century=year//100+1
		return century