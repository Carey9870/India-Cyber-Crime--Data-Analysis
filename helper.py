def RateOfTotalCyberCrimes(cyber_C):
    cyber_C = cyber_C.groupby('State/UT')['Rate of Total Cyber Crimes (2018)++'].sum().reset_index()
    return cyber_C

def categoryPerRateOfTotalCyberCrimesPerState(cyber_C):
    cyber_C= cyber_C.groupby('Category')['Rate of Total Cyber Crimes (2018)++'].sum().reset_index()
    return cyber_C

def Mid_Year_Projected_Population_per_State(cyber_C):
    cyber_C = cyber_C.groupby(['Category','State/UT'])['Mid-Year Projected Population (in Lakhs) (2018)+'].sum().reset_index()
    return cyber_C

def PercentageCrimeSharePerState(cyber_C):
    cyber_C = cyber_C.groupby(['Category','State/UT'])['Percentage Share of State/UT (2018)'].sum().reset_index()
    return cyber_C

def Crimes_Per_State_in_2016_2017_2018(cyber_C):
    cyber_C = cyber_C.groupby(['Category','State/UT'])[['2016',	'2017',	'2018']].sum().reset_index()
    return cyber_C