# Import pandas as pd
import pandas as pd

from matplotlib import pyplot as plt

# Load the 'Salaries.csv' into a DataFrame
#df = pd.read_csv('Salaries.csv')
df = pd.read_csv('Book1.csv')

# Display DataFrame with all columns
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)

# Then just print your dataframe
print(df.info()) # will show the columns name
#print(df.head()) # will show the first five rows of the data

# selecting a particular column
items = df.EmployeeName  #dot method
# items = df['EmployeeName'] #bracket method
#print(items)


# Select the OvertimePay that  is equal to zero
equal_to_zero = df[df.OvertimePay == 0.00]
#print(equal_to_zero)


# plotting graph
# plt.plot(df.EmployeeName, df.TotalPay, label ="totalPay", color ="orange", linewidth ="2", marker ="x", linestyle ="-")
# plt.plot(df.EmployeeName, df.OtherPay, label ="otherPay", color ="violet", linewidth ="3", marker ="o", linestyle ="--")
# plt.scatter(df.EmployeeName, df.TotalPay, color ="orange", marker ="s", alpha=0.5)
# plt.bar(df.EmployeeName, df.TotalPay,label='TotalPay')
# plt.bar(df.EmployeeName, df.OtherPay,bottom=df.TotalPay,label='OtherPay')
plt.hist(df.OtherPay, bins=40)
plt.xlabel("name")
plt.ylabel("pay")
plt.title("company data")
plt.style.use('ggplot')
#plt.legend()
plt.show()
