degrees_fahrenheit : float = float(input("Enter temperature in Fahrenheit: "))
degrees_celsius : float = (degrees_fahrenheit - 32.0) * 5.0 / 9.0
print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")
