def median(lst):
	n = len(lst)
	s = sorted(lst)
	return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n%2] if n else None

lst = [3,5,2,52,5,32,4,5,23,4,23,]

print(median(lst))