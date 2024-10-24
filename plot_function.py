import matplotlib.pyplot as plt

def plot(gdp_data):
    plt.figure(figsize=(10, 6))
    for country in gdp_data.columns:
        plt.plot(gdp_data.index, gdp_data[country],label = country)
    
    plt.title("2000-2022 Yearly GDP")
    plt.xlabel("Year")
    plt.ylabel("GDP(billions)")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()
