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

| Column Name              | Description                                                                 | Data Type                       | Statistical Distribution       | Dependency                     |
|--------------------------|-----------------------------------------------------------------------------|----------------------------------|--------------------------------|--------------------------------|
| **Sale Id**              | Unique identifier for each sale.                                           | String                          | Uniform                       | None                           |
| **Product Code**         | Code representing the specific product.                                    | String                          | Uniform                       | None                           |
| **Category**             | Category of the product (e.g., Laptop, Mobile).                           | String                          | Categorical                   | None                           |
| **Tier**                 | Product tier (e.g., Low, Mid, High).                                      | String                          | Categorical                  | None         |
| **Brand**                | Brand name of the product.                                                 | String                          | Categorical                   | Depends on Category            |
| **Price (USD)**          | Price of the product in USD.                                               | Integer                           | Categorical                        | Depends on Category and Tier      |
| **Inward Date**          | Date when the product was added to inventory.                              | Date                            | Uniform                       | None                           |
| **Dispatch Date**        | Date when the product was dispatched to the customer.                      | Date                            | Uniform                       | Depends on Inward Date         |
| **Core Specification**   | Details about the product's core specifications.                          | String                          | Categorical                   | Depends on Category, Tier and Inward Date           |
| **RAM (MB)**                  | Amount of RAM in the product.                            | Integer                          | Categorical                   | Depends on Tier, Category and Inward Date   |
| **Storage (MB)**         | Storage capacity of the product in gigabytes.                              | Integer                         | Categorical              | Depends on Tier, Category and Inward Date            |
| **Battery (mAh)**        | Battery capacity of the product in milliampere-hours.                      | Integer                         | Categorical                        | Depends on Tier, Category and Inward Date            |
| **Processor Specification** | Details about the processor used in the product.                        | String                          | Categorical                   | Depends on Category, Brand, Inward Date and Core Specification   |
| **Screen Size**          | Size of the product's screen in inches.                                    | Float                           | Uniform                        | Depends on Category            |
| **Operating System**     | Operating system installed on the product.                                 | String                          | Categorical                   | Depends on Category and Brand           |
| **Customer Name**        | Name of the customer who purchased the product.                           | String                          | Uniform                       | Depends on Gender                           |
| **Customer Age**         | Age of the customer.                                                       | Integer                         | Normal                        | None                           |
| **Customer Region**      | Region where the customer resides.                                         | String                          | Categorical                   | None                           |
| **Customer Location**    | Specific location of the customer.                                         | String                          | Categorical                       | Depends on Customer Region     |
| **Customer Gender**      | Gender of the customer.                                                    | String                          | Categorical                   | None                           |
| **Customer Email**       | Email address of the customer.                                             | String                          | Uniform                       | Depends on Customer Name                           |
| **Quantity Sold**        | Number of units sold in the transaction.                                   | Integer                         | Categorical                       | None                           |
| **Warranty Years**       | Warranty period provided for the product in years.                        | Integer                         | Categorical              | None            |
| **Rating**               | Customer rating for the product (e.g., 1-5 stars).                        | Integer                         | Categorical                       | None                           |
| **Channel**              | Sales channel used (e.g., Online, Store).                                | String                          | Uniform                   | None                           |
| **Payment Method**       | Payment method used by the customer (e.g., Credit Card, PayPal).           | String                          | Categorical                   | None                           |
| **Shipping Method**      | Shipping method used for delivery (e.g., Standard, Express).               | String                          | Categorical                   | None                           |
| **Has 5G**               | Indicates if the product supports 5G connectivity (Yes/No).               | Boolean                         | Categorical                     | Depends on Inward Date            |
| **Has Touchscreen**      | Indicates if the product has a touchscreen feature (Yes/No).               | Boolean                         | Categorical                     | Depends on Category and Inward Date           |
| **Currency**             | Currency used for the transaction.                                         | String                          | Categorical                   | None     |

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
generator\data_generator.py     190      0   100%
test\__init__.py                  0      0   100%
test\test_data_generator.py     184      2    99%
-------------------------------------------------
TOTAL                           393      2    99%
```

## Built With

- [Python](https://www.python.org/) - Programming language  

## Authors

- **Samuel Rojas** - - [GitHub Profile](https://github.com/SamuRoj)

