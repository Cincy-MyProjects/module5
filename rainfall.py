years = int(input("Number of years: "))
t_rainfall = 0.0
t_months = 0
for i in range(1,years+1):
    print(f"Year {i}:")
    for m in range(1,13):
        rainfallinch = float(input(f"Inches of rainfall for the month {m}: "))
        t_rainfall += rainfallinch
        t_months+=1

avg_rainfall=t_rainfall/t_months
print(f"Total number of month : {t_months}",)
print(f"Total inches of rainfall : {t_rainfall:.2f}")
print(f"Average rainfall per month : {t_months:.2f} inches")
