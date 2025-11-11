#MapPlot.py
#Name: Gareth Moodley
#Date: 11-10-25
#Assignment: Matplotlib visualization of data

import matplotlib.pyplot as plt
import energy

#avg price of different fuel types per industry, per state, 1960-2019

avg_prices_per_year = {
    "Coal": [],
    "Petroleum": [],
    "Kerosene": [],
    "Natural Gas": []
}
fuel_types = ['Coal', 'Petroleum', "Kerosene", "Natural Gas"]
industries = ['Commercial', 'Electric Power', 'Industrial', 'Transportation']
years = []

def main():
    reports = energy.get_report()
    for r in reports:
        if r['State'] == "Nebraska":
            avg_prices = {"Coal": {"total": 0, "num": 0}, "Petroleum": {"total": 0, "num": 0}, "Kerosene": {"total": 0, "num": 0}, "Natural Gas": {"total": 0, "num": 0}}
            for i in industries:
                for f in fuel_types:
                    #print(r['Price'][i])
                    if f in r['Price'][i]:# and r['Price'][i][f] > 0:
                        avg_prices[f]['total'] += r['Price'][i][f]
                        avg_prices[f]['num'] += 1
            for f in fuel_types:
                if avg_prices[f]['num'] > 0:
                    avg_prices_per_year[f].append(round(avg_prices[f]['total']/avg_prices[f]['num'], 2))
            #if avg_prices['Petroleum']['num'] > 0:
            #    avg_prices_per_year["Petroleum"].append(round(avg_prices['Petroleum']['total']/avg_prices['Petroleum']['num'], 2))
            years.append(r['Year'])
    #print(len(avg_prices_per_year['Coal']))
    #print(len(years))
    fig, ax = plt.subplots()
    ax.plot(years, avg_prices_per_year["Coal"], label="Coal")
    ax.plot(years,  avg_prices_per_year["Petroleum"], label="Petroleum")
    ax.plot(years, avg_prices_per_year["Kerosene"], label="Kerosene")
    ax.plot(years, avg_prices_per_year["Natural Gas"], label="Natural Gas")
    ax.legend(title="Fuel Type")
    plt.show()


if __name__ == "__main__":
    main()
