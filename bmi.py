def calculateBMI(weight,height):
    BMI = weight/(height*height)
    BMI = round(BMI, 1)
    return BMI
    


def BMI_CALCLULATOR(data):
    BMI_Category=[]
    BMI_value=[]
    Health_Risk=[]
    for details in data:
        weight = details['WeightKg']
        height = details['HeightCm'] * 0.01
        BMI = calculateBMI(weight,height)
        if BMI < 18.5:
            BMI_Category.append("Underweight")
            BMI_value.append( BMI)
            Health_Risk.append( "Malnutrition risk")
        elif BMI >= 18.5 and BMI < 25:
            BMI_Category.append("Normalweight")
            BMI_value.append( BMI)
            Health_Risk.append( "Low risk")
        elif BMI >= 25 and BMI < 30:
            BMI_Category.append("Overweight")
            BMI_value.append( BMI)
            Health_Risk.append( "Enhanced risk")
        elif BMI >= 30 and BMI < 35:
            BMI_Category.append("Underweight")
            BMI_value.append( BMI)
            Health_Risk.append( "Malnutrition risk")
        elif BMI >= 35 and BMI < 40:
            BMI_Category.append("Severely obese")
            BMI_value.append( BMI)
            Health_Risk.append( "High risk")
        elif BMI >= 40:
            BMI_Category.append("Very severely obese")
            BMI_value.append( BMI)
            Health_Risk.append( "Very High risk")
    return BMI_Category, BMI_value, Health_Risk