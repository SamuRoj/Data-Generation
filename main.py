from generator import data_generator
import pandas as pd

def main():
    ROWS = 10000000
    data = data_generator.generate_data(ROWS)
    df = pd.DataFrame(data)
    # df.to_excel('data.xlsx', index=False)
    df.to_csv('data_big.csv', index=False)

if __name__ == "__main__":
    main()