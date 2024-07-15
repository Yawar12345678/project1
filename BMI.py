def calculate_bmi():
    weight = input("Enter your weight in kg :")
    height = input("Enter your height in meters:")
    
    weight = float(weight)
    height = float(height)
    bmi = weight / (height * height)
    return weight, height, bmi
def main():
    weight, height, bmi = calculate_bmi()
    print ("Weight:", weight)
    print ("Height:", height)
    print ("BMI :", bmi)

main()