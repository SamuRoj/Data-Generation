from generator import data_generator
import pandas as pd

def main():
    ROWS = 50000
    data = data_generator.generate_data(ROWS)
    df = pd.DataFrame(data)
    df.to_excel('data.xlsx', index=False)
    df.to_csv('data.csv', index=False)

if __name__ == "__main__":
    main()