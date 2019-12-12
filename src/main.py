import sys
import WebScraping as ws
import DataStoring as ds
import DataModeling as dm
import DataVisualization as dv


# Driver function
def main(argv):
    # Set up two paramaeters that execute the progeam remotely and locally
    if len(argv) == 2:
        # Remote paramater requires the program to gather data from web scraping and complete steps including stroing data, modeling data, and visualizing data
        if argv[1] == '-source=remote':
            print('Gathering data from web...')
            records = ws.scrape_all()
            ds.DataStoring(records)
            dfs = dm.DataModeling()
            dv.DataVisualization(dfs)
            print('All done! Please check the graph in the folder.')
            print('Please see the conclusion in liu_jiacheng.ipynb.')
        # Local parameter requires the program to access data on disk and complete steps only including modeling data and visualizing data
        elif argv[1] == '-source=local':
            print('Gathering data on disk...')
            dfs = dm.DataModeling()
            dv.DataVisualization(dfs)
            print('All done! Please check the graph in the folder.')
            print('Please see the conclusion in liu_jiacheng.ipynb.')
        else: 
            print('Please enter a valid parameter: -source=remote / -source=local.')
    else:
        print('Please enter a valid parameter: -source=remote / -source=local.')

if __name__ == '__main__':
    main(sys.argv)