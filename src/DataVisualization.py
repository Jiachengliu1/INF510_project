import matplotlib.pyplot as plt
import numpy as np


def DataVisualization(dfs): 

    ## Data Visualization
    fig, axes = plt.subplots(2, 2, figsize = (25, 10))
    fig.subplots_adjust(wspace = 0.2, hspace = 0.5)

    ## Set up legend
    positions = ['C', 'F', 'G']

    for i in range(3):
        axes[0, 0].plot(dfs[0].iloc[:,i], label=positions[i])
        axes[0, 1].plot(dfs[1].iloc[:,i], label=positions[i])
        axes[1, 0].plot(dfs[2].iloc[:,i], label=positions[i])
        axes[1, 1].plot(dfs[3].iloc[:,i], label=positions[i])

    ## Upper left, visualize players' average field goal attempts vs position over year
    axes[0, 0].legend()
    axes[0, 0].set_title('Average Field Goal Attempt vs Position over year')
    axes[0, 0].set_xlabel('year')
    axes[0, 0].set_ylabel('average FGA')
    x_ticks_1 = np.arange(1998, 2019, 1)
    y_ticks_1 = np.arange(6, 11, 0.5)
    axes[0, 0].set_xticks(x_ticks_1)
    axes[0, 0].set_yticks(y_ticks_1)

    ## Upper right, visualize players' average usage percentange vs position over year 
    axes[0, 1].legend()
    axes[0, 1].set_title('Average Usage Percentange vs Position over year')
    axes[0, 1].set_xlabel('year')
    axes[0, 1].set_ylabel('average USG%')
    x_ticks_2 = np.arange(1998, 2019, 1)
    y_ticks_2 = np.arange(15, 22, 1)
    axes[0, 1].set_xticks(x_ticks_2)
    axes[0, 1].set_yticks(y_ticks_2)

    ## Bottom left, visualize players' average salaries vs position over year 
    axes[1, 0].legend()
    axes[1, 0].set_title('Average Salary vs Position over year')
    axes[1, 0].set_xlabel('year')
    axes[1, 0].set_ylabel('average salary (ten million dollars)')
    x_ticks_3 = np.arange(1998, 2019, 1)
    y_ticks_3 = np.arange(5000000, 25000000, 1000000)
    axes[1, 0].set_xticks(x_ticks_3)
    axes[1, 0].set_yticks(y_ticks_3)

    ## Bottom right, visualize sum of players' expected values in draft vs position over year 
    axes[1, 1].legend()
    axes[1, 1].set_title("Sum of Draft's Expected Value vs Position over year")
    axes[1, 1].set_xlabel('year')
    axes[1, 1].set_ylabel('sum of EV')
    x_ticks_4 = np.arange(1998, 2019, 1)
    y_ticks_4 = np.arange(100, 1000, 100)
    axes[1, 1].set_xticks(x_ticks_4)
    axes[1, 1].set_yticks(y_ticks_4)

    ## Export figure 
    #fig.show()
    fig.savefig('Visualization')