try:
    num = int(input("Enter a number: "))
except Exception:
    print("Invalid input.")
else:
    print(f"Input is correct")
finally:
    print("Always runs")