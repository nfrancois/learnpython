hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter rate:")
r = float(rate)

pay = 0.0

if h > 40:
    dif = h - 40
    effective_time = dif * 1.5 + 40
    pay = r * effective_time
else:
    pay = h*r

print(pay)
