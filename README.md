# Data Generator of Mobiles and Laptop Sales

A Python-based project designed to generate synthetic data for testing and development purposes about the sales of laptops and mobiles. This tool simplifies the process of creating structured datasets for various use cases.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Requirements for the software and other tools to build, test, and run the project:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/installation/)  

### Installing

Follow these steps to set up the development environment:

1. Clone the repository:  
    ```bash
    git clone https://github.com/SamuRoj/Data-Generation
    cd data-generator
    ```

2. Install dependencies:  
    ```bash
    pip install matplotlib numpy pandas Faker coverage openpyxl

    pip install -r requirements.txt
    ```

3. Run the application:  
    ```bash
    python main.py
    python graphics.py
    ```

## Dataset Explanation

| Column Name              | Description                                                                 | Data Type                       |
|--------------------------|-----------------------------------------------------------------------------|----------------------------------|
| **Sale Id**              | Unique identifier for each sale.                                           | String                          |
| **Product Code**         | Code representing the specific product.                                    | String                          |
| **Category**             | Category of the product (e.g., Laptop, Mobile).                           | String                          |
| **Tier**                 | Product tier (e.g., Low, Mid, High).                                      | String                          |
| **Brand**                | Brand name of the product.                                                 | String                          |
| **Price (USD)**          | Price of the product in USD.                                               | Float                           |
| **Inward Date**          | Date when the product was added to inventory.                              | Date                            |
| **Dispatch Date**        | Date when the product was dispatched to the customer.                      | Date                            |
| **Core Specification**   | Details about the product's core specifications.                          | String                          |
| **RAM**                  | Amount of RAM in the product (e.g., 8GB, 16GB).                            | String                          |
| **Storage (GB)**         | Storage capacity of the product in gigabytes.                              | Integer                         |
| **Battery (mAh)**        | Battery capacity of the product in milliampere-hours.                      | Integer                         |
| **Processor Specification** | Details about the processor used in the product.                        | String                          |
| **Screen Size**          | Size of the product's screen in inches.                                    | Float                           |
| **Operating System**     | Operating system installed on the product.                                 | String                          |
| **Customer Name**        | Name of the customer who purchased the product.                           | String                          |
| **Customer Age**         | Age of the customer.                                                       | Integer                         |
| **Customer Region**      | Region where the customer resides.                                         | String                          |
| **Customer Location**    | Specific location of the customer.                                         | String                          |
| **Customer Gender**      | Gender of the customer.                                                    | String                          |
| **Customer Email**       | Email address of the customer.                                             | String                          |
| **Quantity Sold**        | Number of units sold in the transaction.                                   | Integer                         |
| **Warranty Years**       | Warranty period provided for the product in years.                        | Integer                         |
| **Rating**               | Customer rating for the product (e.g., 1-5 stars).                        | Integer                           |
| **Channel**              | Sales channel used (e.g., Online, Store).                                | String                          |
| **Payment Method**       | Payment method used by the customer (e.g., Credit Card, PayPal).           | String                          |
| **Shipping Method**      | Shipping method used for delivery (e.g., Standard, Express).               | String                          |
| **Has 5G**               | Indicates if the product supports 5G connectivity (Yes/No).               | Boolean                         |
| **Has Touchscreen**      | Indicates if the product has a touchscreen feature (Yes/No).               | Boolean                         |
| **Currency**             | Currency used for the transaction.                                         | String                          |


## Running the tests

To ensure the project works as expected, run the automated tests.

### Sample Tests

Run the unit tests to verify the functionality of the data generator:  
```bash
python -m unittest discover -v
```

### Current Coverage

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
generator\__init__.py             0      0   100%
generator\constants.py           19      0   100%
generator\data_generator.py     189      0   100%
test\__init__.py                  0      0   100%
test\test_data_generator.py     171      0   100%
-------------------------------------------------
TOTAL                           379      0   100%
```

## Built With

- [Python](https://www.python.org/) - Programming language  

## Authors

- **Samuel Rojas** - - [GitHub Profile](https://github.com/SamuRoj)

