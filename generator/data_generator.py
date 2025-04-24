import random
import numpy as np
from faker import Faker
from datetime import timedelta
from generator import constants
import string

fake = Faker()

def generate_product_code():
    sale_id = ""
    for _ in range(8):
        dataset = np.random.choice([string.ascii_uppercase, string.digits])
        sale_id += np.random.choice(list(dataset))
    return sale_id

def generate_tier():
    return str(np.random.choice(constants.TIER, p=[0.4, 0.4, 0.2]))

def generate_category():
    return str(np.random.choice(constants.CATEGORIES, p=[0.6, 0.4]))

def generate_brand(category):
    if category == "Mobile":
        return str(np.random.choice(constants.MOBILE_BRANDS))
    return str(np.random.choice(constants.LAPTOP_BRANDS))

def generate_price(category, tier):
    if category == "Mobile":
        if tier == "Low":
            return np.random.randint(80, 200)
        elif tier == "Mid":
            return np.random.randint(200, 500)
        return np.random.randint(600, 1500)
    else:
        if tier == "Low":
            return np.random.randint(200, 500)
        elif tier == "Mid":
            return np.random.randint(500, 1000)
        return np.random.randint(1100, 3000)

def generate_inward_date():
    return fake.date_between(start_date='-365d', end_date='-10d')

def generate_dispatch_date(inward_date):
    return inward_date + timedelta(days=random.randint(3, 30))

def generate_core_specification(category, tier):
    if category == "Mobile":
        return "N/A"
    if tier == "Low":
        return str(np.random.choice(constants.CORE_SPECIFICATION[0:2]))
    elif tier == "Mid":
        return str(np.random.choice(constants.CORE_SPECIFICATION[2:4]))
    return str(np.random.choice(constants.CORE_SPECIFICATION[4:]))

def generate_ram(category, tier):
    if category == "Mobile":
        if tier == "Low":
            return int(np.random.choice(constants.MOBILE_RAM[0:2]))
        return int(np.random.choice(constants.MOBILE_RAM[2:]))
    else:
        if tier == "Low":
            return int(np.random.choice(constants.PC_RAM[0:2]))
        return int(np.random.choice(constants.PC_RAM[2:]))
    
def generate_storage(category, tier):
    if category == "Mobile":
        if tier == "Low":
            return int(np.random.choice(constants.MOBILE_STORAGE[0:2]))
        elif tier == "Mid":
            return int(np.random.choice(constants.MOBILE_STORAGE[2:4]))
        return int(np.random.choice(constants.MOBILE_STORAGE[4:]))
    else:
        if tier == "Low":
            return int(np.random.choice(constants.PC_STORAGE[0:2]))
        elif tier == "Mid":
            return int(np.random.choice(constants.PC_STORAGE[2:4]))
        return int(np.random.choice(constants.PC_STORAGE[4:]))

def generate_battery(category, tier):
    if category == "Mobile":
        if tier == "Low":
            return int(np.random.choice(constants.MOBILE_BATTERY[0:2]))
        elif tier == "Mid":
            return int(np.random.choice(constants.MOBILE_BATTERY[2:4]))
        return int(np.random.choice(constants.MOBILE_BATTERY[4:]))
    else:
        if tier == "Low":
            return int(np.random.choice(constants.PC_BATTERY[0:2]))
        elif tier == "Mid":
            return int(np.random.choice(constants.PC_BATTERY[2:4]))
        return int(np.random.choice(constants.PC_BATTERY[4:]))

def generate_processor_specification(category, brand, core_specification=""):
    if category == "Laptop":
        return core_specification
    if brand == "Apple":
        return "Apple A-Series"
    elif brand == "Samsung":
        return "Samsung Exynos"
    elif brand == "Xiaomi" or brand == "OnePlus" or brand == "Realme":
        return "Mediatek Dimensity"
    return str(np.random.choice(constants.PROCESSOR_SPECIFICATION))

def generate_screen_size(category):
    if category == "Mobile":
        return float(np.round(np.random.uniform(5.5, 6.9), 2))
    return float(np.round(np.random.uniform(11, 17), 2))

def generate_operating_system(category, brand):
    if category == "Mobile":
        if brand == "Apple":
            return "iOS"
        elif brand == "Huawei":
            return "HarmonyOS"
        return "Android"
    else:
        if brand == "Apple":
            return "MacOS"
        return "Windows"

def generate_gender():
    return str(np.random.choice(constants.GENDER, p=[0.5, 0.5]))

def generate_name(gender):
    if gender == 'Male':
        first_name = fake.first_name_male()
    else:
        first_name = fake.first_name_female()
    
    last_name = fake.last_name()
    return f"{first_name} {last_name}"

def generate_age():
    return int(np.clip(np.round(np.random.normal(loc=30, scale=10), 0), 18, 60))

def generate_region():
    probabilities = [0.30, 0.25, 0.25, 0.20]
    return str(np.random.choice(constants.REGIONS, p=probabilities))

def generate_location(region):
    return str(np.random.choice(constants.LOCATIONS[region]))

def generate_email(name):
    values = name.split()
    return str(values[0]).lower() + "." + str(values[1]).lower() + "@example.com"

def generate_quantity_sold():
    quantities_sold = np.arange(1, 11)  

    probabilities = np.zeros(len(quantities_sold)) 
    probabilities[0:2] = 0.6 
    probabilities[2:6] = 0.3 
    probabilities[6:] = 0.1
    probabilities /= np.sum(probabilities)

    return np.random.choice(quantities_sold, p=probabilities)

def generate_warranty_years():
    return np.random.choice([1, 2], p=[0.8, 0.2])

def generate_rating():
    ratings = np.arange(1, 6)  

    probabilities = np.zeros(len(ratings)) 
    probabilities[0:2] = 0.4 
    probabilities[2:] = 0.6 
    probabilities /= np.sum(probabilities)

    return np.random.choice(ratings, p=probabilities)

def generate_channel():
    return str(np.random.choice(constants.CHANNELS))

def generate_payment_method():
    probabilities = [0.10, 0.40, 0.20, 0.15, 0.05, 0.05, 0.03, 0.02]
    return str(np.random.choice(constants.PAYMENT_METHODS, p=probabilities))

def generate_shipping_method():
    probabilities = [0.50, 0.30, 0.10, 0.10]
    return str(np.random.choice(constants.SHIPPING_METHODS, p=probabilities))

def generate_has_5g():
    return bool(np.random.choice([True, False], p=[0.6, 0.4]))

def generate_has_touchscreen(category):
    if category == "Mobile":
        return True
    return bool(np.random.choice([True, False], p=[0.3, 0.7]))

def generate_currency():
    return str(np.random.choice(constants.CURRENCIES, p=[0.85, 0.15]))

def generate_data(n):
    data = []

    for i in range(n):
        print("Row: ", i + 1)

        sale_id = "S" + str(i + 1)
        product_code = generate_product_code()
        tier = generate_tier()
        category = generate_category()
        brand = generate_brand(category)
        price = generate_price(category, tier)
        inward_date = generate_inward_date()
        dispatch_date = generate_dispatch_date(inward_date)
        core_specification = generate_core_specification(category, tier) 
        ram = generate_ram(category, tier) 
        storage = generate_storage(category, tier) 
        battery = generate_battery(category, tier) 
        processor_specification = generate_processor_specification(category, brand, core_specification)
        screen_size = generate_screen_size(category)
        operating_system = generate_operating_system(category, brand)
        customer_gender = generate_gender()
        customer_name = generate_name(customer_gender)
        customer_age = generate_age()
        customer_region = generate_region()
        customer_location = generate_location(customer_region)
        customer_email = generate_email(customer_name)
        quantity_sold = generate_quantity_sold()
        warranty_years = generate_warranty_years()
        rating = generate_rating()
        channel = generate_channel()
        payment_method = generate_payment_method()
        shipping_method = generate_shipping_method()
        has_5g = generate_has_5g()
        has_touchscreen = generate_has_touchscreen(category)
        currency = generate_currency()

        row = {
            "Sale Id": sale_id,
            "Product Code": product_code,
            "Category": category,
            "Tier": tier,
            "Brand": brand,
            "Price (USD)": price,
            "Inward Date": str(inward_date),
            "Dispatch Date": str(dispatch_date),
            "Core Specification": core_specification,
            "RAM": ram,
            "Storage (GB)": storage,
            "Battery (mAh)": battery,
            "Processor Specification": processor_specification,
            "Screen Size": screen_size,
            "Operating System": operating_system,
            "Customer Name": customer_name,
            "Customer Age": customer_age,
            "Customer Region": customer_region,
            "Customer Location": customer_location,
            "Customer Gender": customer_gender,
            "Customer Email": customer_email,
            "Quantity Sold": quantity_sold,
            "Warranty Years": warranty_years,
            "Rating": rating,
            "Channel": channel,
            "Payment Method": payment_method,
            "Shipping Method": shipping_method,
            "Has 5G": has_5g,
            "Has Touchscreen": has_touchscreen,
            "Currency": currency
        }

        data.append(row)

    return data
            