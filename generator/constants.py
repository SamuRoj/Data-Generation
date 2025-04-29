MOBILE_BRANDS = [
    'Apple', 'Samsung', 'Xiaomi', 'OnePlus', 'Realme',
    'Motorola', 'Huawei', 'Google', 'Nokia'
]

LAPTOP_BRANDS = [
    'Apple', 'Samsung', 'Lenovo', 'HP', 'Dell',
    'Asus', 'Acer', 'Huawei', 'MSI'
]

CATEGORIES = ['Mobile', 'Laptop']
TIER = ['Low', 'Mid', 'High']

PC_RAM = [2048, 4096, 8192, 16384, 32768, 65536]
MOBILE_RAM = [2048, 3072, 4096, 6144, 8192, 12288]

PC_STORAGE = [128000, 256000, 512000, 1024000, 2048000, 4096000]
MOBILE_STORAGE = [32000, 64000, 128000, 256000, 512000, 1024000]

PC_BATTERY = [4000, 5000, 6000, 7000, 8000, 9000]
MOBILE_BATTERY = [3000, 4000, 4500, 5000, 6000, 7000]

CORE_SPECIFICATION = {
    2005: [
        'Intel Celeron M', 'AMD Sempron',
        'Intel Pentium M', 'AMD Turion 64',
        'Intel Pentium 4', 'AMD Athlon 64'
    ],
    2010: [
        'Intel Celeron', 'AMD Athlon II',
        'Intel Core i3', 'Intel Core i5',
        'Intel Core i7', 'AMD Phenom II'
    ],
    2015: [
        'Intel Celeron N3050', 'AMD A4-5000',
        'Intel Core i3-6100U', 'AMD A8-7410',
        'Intel Core i7-6500U', 'AMD FX-8800P'
    ],
    2020: [
        'Intel Celeron N4000', 'AMD Athlon 300U',
        'Intel Core i5-1035G1', 'AMD Ryzen 5 3500U',
        'Intel Core i7-1065G7', 'AMD Ryzen 7 4700U'
    ],
    2025: [
        'Intel Core i3-1215U', 'AMD Ryzen 3 7600U',
        'Intel Core i5-13500H', 'AMD Ryzen 5 7600U',
        'Intel Core i7-13700H', 'AMD Ryzen 7 7800U'
    ],
}

PROCESSOR_SPECIFICATION = {
    2005: {
        'Apple': ['Apple A6'],
        'MediaTek': ['MediaTek MT6253'],
        'Samsung': ['Samsung Exynos 3 Single'],
        'Others': ['Qualcomm Snapdragon 200']
    },
    2010: {
        'Apple': ['Apple A4'],
        'MediaTek': ['MediaTek MT6573'],
        'Samsung': ['Samsung Exynos 4'],
        'Others': ['Qualcomm Snapdragon S1', 'Qualcomm Snapdragon S2', 'Qualcomm Snapdragon S3']
    },
    2015: {
        'Apple': ['Apple A9'],
        'MediaTek': ['MediaTek MT6732'],
        'Samsung': ['Samsung Exynos 7 Octa'],
        'Others': ['Qualcomm Snapdragon 410', 'Qualcomm Snapdragon 615', 'Qualcomm Snapdragon 820']
    },
    2020: {
        'Apple': ['Apple A14 Bionic'],
        'MediaTek': ['MediaTek Helio G80'],
        'Samsung': ['Exynos 9611'],
        'Others': ['Qualcomm Snapdragon 460', 'Qualcomm Snapdragon 732G', 'Qualcomm Snapdragon 865']
    },
    2025: {
        'Apple': ['Apple A17 Bionic'],
        'MediaTek': ['MediaTek Dimensity 700'],
        'Samsung': ['Exynos 1280'],
        'Others': ['Qualcomm Snapdragon 695', 'Qualcomm Snapdragon 778G', 'Qualcomm Snapdragon 8 Gen 3']
    },
}

GENDER = ["Male", "Female"]

REGIONS = ['North', 'South', 'East', 'West']
LOCATIONS = {
    'North': [
        'New York City', 'Buffalo', 'Chicago', 'Detroit', 'Cleveland', 
        'Milwaukee', 'Minneapolis', 'Cincinnati', 'Pittsburgh', 'Indianapolis'
    ],
    'South': [
        'Houston', 'Miami', 'Atlanta', 'Dallas', 'New Orleans', 
        'Charlotte', 'Orlando', 'Tampa', 'Austin', 'Nashville'
    ],
    'East': [
        'Washington D.C.', 'Baltimore', 'Richmond', 'Boston', 'Philadelphia', 
        'Newark', 'Hartford', 'Albany', 'Providence', 'Trenton'
    ],
    'West': [
        'Los Angeles', 'San Francisco', 'Seattle', 'Phoenix', 'Denver', 
        'Portland', 'Las Vegas', 'San Diego', 'Salt Lake City', 'Sacramento'
    ]
}

CHANNELS = ['Store', 'Online', 'Supplier']
PAYMENT_METHODS = [
    'Cash', 
    'Credit Card', 
    'Paypal', 
    'Debit Card', 
    'Apple Pay / Google Pay', 
    'Cash on Delivery'
]
SHIPPING_METHODS = [
    'Standard', 
    'Express', 
    'In-store Pickup', 
    'International Shipping'
]
CURRENCIES = ['USD', 'EUR']