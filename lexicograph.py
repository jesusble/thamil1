def lexicograph_sort(s):
  return sorted(sorted(s),key=str.upper)
s1=input()
print(lexicograph_sort(s1))
