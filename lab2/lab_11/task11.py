from sortedcontainers import SortedList
sl = SortedList()
import sys
input_data = sys.stdin.read().split()
i = 0
out = []
while i < len(input_data):
    op = input_data[i]; x = int(input_data[i+1]); i += 2
    if op == "insert":
        if x not in sl: sl.add(x)
    elif op == "delete":
        if x in sl: sl.remove(x)
    elif op == "exists":
        out.append("true" if x in sl else "false")
    elif op == "next":
        idx = sl.bisect_right(x)
        out.append(str(sl[idx]) if idx < len(sl) else "none")
    elif op == "prev":
        idx = sl.bisect_left(x) - 1
        out.append(str(sl[idx]) if idx >= 0 else "none")
print("\n".join(out))
