n = 4
arr[] = {1, 2, 3, 4}
k = 2

m = {}
ans = 0
        
for i in arr:
  if (i%k) in m:
    ans += m[i%k]
    m[i%k] += 1
  else:
    m[i%k] = 1
        
print(ans)
