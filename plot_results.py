import pandas as pd

def PLOT_RESULTS(BMI_Category, BMI_value, Health_Risk):
    table = pd.DataFrame(
        {'BMI_Category': BMI_Category,
        'BMI_value': BMI_value,
        'Health_Risk': Health_Risk
        })
    return table
    
