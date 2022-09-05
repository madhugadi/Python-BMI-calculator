import json
from bmi import BMI_CALCLULATOR
from  plot_results import PLOT_RESULTS

if __name__ == "__main__":

    f = open('data.json')

    data = json.load(f)

    data = data['details']

    BMI_Category, BMI_value, Health_Risk = BMI_CALCLULATOR(data)

    table = PLOT_RESULTS(BMI_Category, BMI_value, Health_Risk)

    print(table)

    f.close()



