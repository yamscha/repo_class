# Dependencies
from matplotlib import pyplot as plt
from scipy import stats

import numpy as np
import pandas as pd


crime_data = pd.read_csv("../Resources/crime_data.csv")

year = crime_data.iloc[:, 0]

violent_crime_rate = crime_data.iloc[:, 3]
vc_slope, vc_int, vc_r, vc_p, vc_std_err = stats.linregress(
    year, violent_crime_rate)
vc_fit = vc_slope * year + vc_int

murder_rate = crime_data.iloc[:, 5]
m_slope, m_int, m_r, m_p, m_std_err = stats.linregress(year, murder_rate)
m_fit = m_slope * year + m_int

aggravated_assault_rate = crime_data.iloc[:, 9]
aa_slope, aa_int, aa_r, aa_p, aa_std_err = stats.linregress(
    year, aggravated_assault_rate)
aa_fit = aa_slope * year + aa_int

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True)
fig.suptitle("Crime Rates Over Time", fontsize=16, fontweight="bold")

ax1.set_xlim(min(year), max(year))
ax1.plot(year, violent_crime_rate, linewidth=1, marker="o")
ax1.plot(year, vc_fit, "b--", linewidth=1)
ax1.set_ylabel("Violent Crime Rate")

ax2.plot(year, murder_rate, linewidth=1, marker="o", color="r")
ax2.plot(year, m_fit, "r--", linewidth=1)
ax2.set_ylabel("Murder Rate")

ax3.plot(year, aggravated_assault_rate, linewidth=1, marker="o", color="g")
ax3.plot(year, aa_fit, "g--", linewidth=1)
ax3.set_ylabel("Aggravated Assault Rate")
ax3.set_xlabel("Year")

year = 2019
print("The violent crime rate in 2019 will be " +
      str(vc_slope * year + vc_int) + ".")
print("The murder rate in 2019 will be " + str(m_slope * year + m_int) + ".")
print("The aggravated assault rate in 2019 will be " +
      str(aa_slope * year + aa_int) + ".")

plt.savefig("../../../Images/18-final-plot.png")
plt.show()
