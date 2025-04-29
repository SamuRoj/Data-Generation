import unittest
from generator import data_generator
from generator import constants
from datetime import datetime
from datetime import timedelta
from faker import Faker

fake = Faker()

class DataGeneratorTest(unittest.TestCase):
    def test_generate_data(self):
        N = 500
        data = data_generator.generate_data(N)
        self.assertTrue(N == len(data))

    def test_generator_product_code(self):
        N = 12
        code = data_generator.generate_product_code()
        self.assertTrue(N == len(code))
        self.assertTrue(code.isascii())

    def test_generator_tier(self):
        tier = data_generator.generate_tier()
        self.assertTrue(tier in constants.TIER)
    
    def test_generator_category(self):
        category = data_generator.generate_category()
        self.assertTrue(category in constants.CATEGORIES)

    def test_generator_brand(self):
        mobile_brand = data_generator.generate_brand("Mobile")
        self.assertTrue(mobile_brand in constants.MOBILE_BRANDS)
        computer_brand = data_generator.generate_brand("Laptop")
        self.assertTrue(computer_brand in constants.LAPTOP_BRANDS)

    def test_generator_price(self):
        categories = ["Mobile", "Laptop"]
        tiers = ["Low", "Mid", "High"]
        mobile_prices = [80, 200, 200, 500, 600, 1500]
        laptop_prices = [200, 500, 500, 1000, 1100, 3000]
        for category in categories:
            for j in range(len(tiers)):
                price = data_generator.generate_price(category, tiers[j])
                if category == "Mobile":
                    self.assertTrue(mobile_prices[j*2] <= price <= mobile_prices[j*2 + 1])
                else:
                    self.assertTrue(laptop_prices[j*2] <= price <= laptop_prices[j*2 + 1])

    def test_generator_inward_date(self):
        inward_date = data_generator.generate_inward_date()
        today = datetime.today().date()
        self.assertGreaterEqual(today - inward_date, timedelta(days=10))
        self.assertLessEqual(today - inward_date, timedelta(days=7300))

    def test_generator_dispatch_date(self):
        inward_date = data_generator.generate_inward_date()
        dispatch_date = data_generator.generate_dispatch_date(inward_date)

        self.assertGreaterEqual(dispatch_date, inward_date + timedelta(days=3))
        self.assertLessEqual(dispatch_date, inward_date + timedelta(days=30))

    def test_generator_core_specification(self):
        category = ["Mobile", "Laptop"]
        tier = ["Low", "Mid", "High"]
        date = fake.date_between(start_date="-7300d", end_date="-10d")
        years = sorted(constants.CORE_SPECIFICATION.keys())
        year = date.year
        key = max([a for a in years if a <= year])
        for i in category:
            for j in range(len(tier)):
                core_specification = data_generator.generate_core_specification(i, tier[j], date)
                if i == "Mobile":
                    self.assertTrue(core_specification == "N/A")
                else:
                    self.assertTrue(core_specification in constants.CORE_SPECIFICATION[key][j * 2: (j + 1) * 2])

    def test_generator_ram(self):
        categories = ["Mobile", "Laptop"]
        tiers = ["Low", "Mid", "High"]
        date = fake.date_between(start_date="-7300d", end_date="-10d")
        for category in categories:
            for tier in tiers:
                ram = data_generator.generate_ram(category, tier, date)
                self.assertTrue(ram % 2 == 0)
                if category == "Mobile":
                    self.assertGreaterEqual(ram, 128)
                    self.assertLessEqual(ram, 12288)
                else:
                    self.assertGreaterEqual(ram, 128)
                    self.assertLessEqual(ram, 65536)

    def test_generator_storage(self):
        category = ["Mobile", "Laptop"]
        tier = ["Low", "Mid", "High"]
        date = fake.date_between(start_date="-7300d", end_date="-10d")
        for i in category:
            for j in range(len(tier)):
                storage = data_generator.generate_storage(i, tier[j], date)
                self.assertTrue(storage % 2 == 0)
                if i == "Mobile": 
                    self.assertGreaterEqual(storage, 2000)
                    self.assertLessEqual(storage, 1024000)
                else:
                    self.assertGreaterEqual(storage, 8000)
                    self.assertLessEqual(storage, 4096000)

    def test_generator_battery(self):
        category = ["Mobile", "Laptop"]
        tier = ["Low", "Mid", "High"]
        date = fake.date_between(start_date="-7300d", end_date="-10d")
        for i in category:
            for j in range(len(tier)):
                battery = data_generator.generate_battery(i, tier[j], date)
                if i == "Mobile":
                    self.assertGreaterEqual(battery, 186)
                    self.assertLessEqual(battery, 7000)
                else:
                    self.assertGreaterEqual(battery, 250)
                    self.assertLessEqual(battery, 9000)

    def test_generator_processor_specification(self):
        processor_specification = data_generator.generate_processor_specification("Laptop", 
                                                                                  "Samsung",
                                                                                  "",
                                                                                  "Intel i3")
        self.assertTrue(processor_specification == "Intel i3")
        date = fake.date_between(start_date='-7300d', end_date='-10d')

        for brand in constants.MOBILE_BRANDS:
            processor = str(data_generator.generate_processor_specification("Mobile", brand, date))
            if brand == "Apple":
                self.assertTrue(processor.startswith("Apple"))
            elif brand == "Samsung":
                self.assertTrue(processor.startswith("Samsung") or processor.startswith("Exynos"))
            elif brand == "Xiaomi" or brand == "OnePlus" or brand == "Realme":
                self.assertTrue(processor.startswith("MediaTek"))
            else:
                self.assertTrue(processor.startswith("Qualcomm"))

    def test_generator_screen_size(self):
        screen_size = data_generator.generate_screen_size("Mobile")
        self.assertTrue(5.5 <= screen_size <= 6.9)

        screen_size = data_generator.generate_screen_size("Laptop")
        self.assertTrue(11 <= screen_size <= 17)

    def test_generator_operating_system(self):
        for brand in constants.MOBILE_BRANDS:
            operating_system = data_generator.generate_operating_system("Mobile", brand)
            if brand == "Apple":
                self.assertTrue(operating_system == "iOS")
            elif brand == "Huawei":
                self.assertTrue(operating_system == "HarmonyOS")
            else:
                self.assertTrue(operating_system == "Android")
        for brand in constants.LAPTOP_BRANDS:
            operating_system = data_generator.generate_operating_system("Laptop", brand)
            if brand == "Apple":
                self.assertTrue(operating_system == "MacOS")
            else:
                self.assertTrue(operating_system == "Windows")

    def test_generator_gender(self):
        gender = data_generator.generate_gender()
        self.assertTrue(gender in constants.GENDER)

    def test_generator_name(self):
        name = data_generator.generate_name('Male')
        self.assertTrue(2 == len(name.split()))

        name = data_generator.generate_name('Female')
        self.assertTrue(2 == len(name.split()))

    def test_generator_age(self):
        age = data_generator.generate_age()
        self.assertTrue(18 <= age <= 60)

    def test_generator_region(self):
        region = data_generator.generate_region()
        self.assertTrue(region in constants.REGIONS)

    def test_generator_location(self):
        for i in constants.REGIONS:
            location = data_generator.generate_location(i)
            self.assertTrue(location in constants.LOCATIONS[i])

    def test_generator_email(self):
        name = data_generator.generate_name("Male")
        email = data_generator.generate_email(name)

        self.assertTrue(name.split()[0].lower() == email.split(".")[0])
        self.assertTrue(name.split()[1].lower() == email.split(".")[1].split("@")[0])
        self.assertTrue(email.endswith("@example.com"))

    def test_generator_quantity_sold(self):
        quantity_sold = data_generator.generate_quantity_sold()
        self.assertTrue(1 <= quantity_sold <= 10)

    def test_generator_warranty_years(self):
        warranty_years = data_generator.generate_warranty_years()
        self.assertTrue(1 <= warranty_years <= 2)

    def test_generator_rating(self):
        rating = data_generator.generate_rating()
        self.assertTrue(1 <= rating <= 5)

    def test_generator_channel(self):
        channel = data_generator.generate_channel()
        self.assertTrue(channel in constants.CHANNELS)

    def test_generator_payment_method(self):
        payment_method = data_generator.generate_payment_method()
        self.assertTrue(payment_method in constants.PAYMENT_METHODS)

    def test_generator_shipping_method(self):
        shipping_method = data_generator.generate_shipping_method()
        self.assertTrue(shipping_method in constants.SHIPPING_METHODS)

    def test_generator_has_5g(self):
        has_5g = data_generator.generate_has_5g()
        self.assertTrue(has_5g in [True, False])

    def test_generator_has_touchscreen(self):
        has_touchscreen = data_generator.generate_has_touchscreen("Mobile")
        self.assertTrue(has_touchscreen)

        has_touchscreen = data_generator.generate_has_touchscreen("Laptop")
        self.assertTrue(has_touchscreen in [True, False])

    def test_generator_currency(self):
        currency = data_generator.generate_currency()
        self.assertTrue(currency in constants.CURRENCIES)
