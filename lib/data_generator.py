import random
import pandas as pd
import numpy as np
from faker import Faker
from tqdm import tqdm
from datetime import timedelta, datetime
from constants.categories import product_categories_list, product_categories_weights
from constants.coupons import special_events
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

fake = Faker("en_US")
total_weight = sum(product_categories_weights)
product_categories_weights = [w / total_weight for w in product_categories_weights]


def is_special_event(date):
    return date in (event_date.date() for event_date in special_events.values())


def generate_synthetic_data(num_rows=1000, month=None, year=None):
    data = []
    existing_users = {}

    logging.info("Generating User Profiles")
    for _ in range(num_rows):
        user_id = f"****{random.randint(1000000, 9999999)}"
        phone_number = f"+63{random.randint(1000000, 9999999)}"
        age = np.random.randint(18, 65)
        sex = np.random.choice(["M", "F", "O"])
        join_date = fake.date_between(start_date="-5y", end_date="today")
        payment_method = np.random.choice(
            [
                "GCash",
                "Maya",
                "GrabPay",
                "ShopeePay",
                "Coins.ph",
                "Visa (Credit)",
                "Mastercard (Credit)",
                "American Express",
                "Visa (Debit)",
                "Mastercard (Debit)",
                "Cash",
                "Bank Transfer",
                "Over-the-counter (OTC)",
            ]
        )
        loyalty_program_member = np.random.choice([0, 1])
        loyalty_tier = (
            np.random.choice([0, 1, 2, 3, 4]) if loyalty_program_member else None
        )

        existing_users[user_id] = {
            "phone_number": phone_number,
            "age": age,
            "sex": sex,
            "join_date": join_date,
            "country": "Philippines",
            "payment_method": payment_method,
            "loyalty_program_member": loyalty_program_member,
            "loyalty_tier": loyalty_tier,
        }

    logging.info("Starting data generation loop")
    for _ in tqdm(range(num_rows), desc="Generating data", unit="record"):
        if np.random.random() < 0.1 and existing_users:
            user_id = random.choice(list(existing_users.keys()))
        else:
            user_id = f"****{random.randint(1000000, 9999999)}"
            phone_number = f"+63{random.randint(1000000, 9999999)}"
            age = np.random.randint(18, 65)
            sex = np.random.choice(["M", "F", "O"])
            join_date = fake.date_between(start_date="-5y", end_date="today")
            payment_method = np.random.choice(["credit", "debit", "cash"])
            loyalty_program_member = np.random.choice([0, 1])
            loyalty_tier = (
                np.random.choice([0, 1, 2, 3, 4]) if loyalty_program_member else None
            )

            existing_users[user_id] = {
                "phone_number": phone_number,
                "age": age,
                "sex": sex,
                "join_date": join_date,
                "country": "Philippines",
                "payment_method": payment_method,
                "loyalty_program_member": loyalty_program_member,
                "loyalty_tier": loyalty_tier,
            }

        user_profile = existing_users[user_id]
        order_id = f"******{np.random.randint(1000, 9999)}"
        total_purchase = round(np.random.uniform(100, 10000), 2)
        tier_discount_percentage = {0: 0, 1: 3, 2: 5, 3: 7, 4: 10}.get(
            user_profile["loyalty_tier"], 0
        )
        coupon_discount_percentage = (
            np.random.randint(2, 5)
            if is_special_event(fake.date_between(start_date="-5y", end_date="today"))
            else 0
        )
        total_discount_percentage = (
            tier_discount_percentage + coupon_discount_percentage
        )
        total_discount = round(total_purchase * (total_discount_percentage / 100), 2)
        total_purchase_after_discount = round(total_purchase - total_discount, 2)
        product_category = np.random.choice(
            product_categories_list, p=product_categories_weights
        )
        purchase_medium = np.random.choice(["online", "in-store"])
        customer_exp_rating = np.random.randint(1, 5)

        if year and month:
            start_date = datetime(year, month, 1)
            end_date = (
                (datetime(year, month + 1, 1) - timedelta(days=1))
                if month < 12
                else datetime(year, 12, 31)
            )
            purchase_date = fake.date_between(start_date=start_date, end_date=end_date)
        elif year:
            start_date = datetime(year, 1, 1)
            end_date = datetime(year, 12, 31)
            purchase_date = fake.date_between(start_date=start_date, end_date=end_date)
        else:
            purchase_date = fake.date_between(
                start_date=user_profile["join_date"], end_date="today"
            )

        purchase_time = fake.time()
        purchased_at = f"{purchase_date} {purchase_time}"

        release_date = fake.date_between(
            start_date=purchase_date, end_date=purchase_date + timedelta(days=3)
        )
        estimated_delivery_date = fake.date_between(
            start_date=release_date, end_date=release_date + timedelta(days=7)
        )
        received_date = fake.date_between(
            start_date=estimated_delivery_date,
            end_date=estimated_delivery_date + timedelta(days=2),
        )

        data.append(
            {
                "user_id": user_id,
                "age": user_profile["age"],
                "sex": user_profile["sex"],
                "phone_number": user_profile["phone_number"],
                "join_date": user_profile["join_date"],
                "country": user_profile["country"],
                "payment_method": user_profile["payment_method"],
                "loyalty_program_member": user_profile["loyalty_program_member"],
                "loyalty_tier": user_profile["loyalty_tier"],
                "tier_discount_percentage": tier_discount_percentage,
                "coupon_discount_percentage": coupon_discount_percentage,
                "total_discount_percentage": total_discount_percentage,
                "total_discount": total_discount,
                "total_purchase": total_purchase,
                "total_purchase_after_discount": total_purchase_after_discount,
                "purchased_at": purchased_at,
                "product_category": product_category,
                "purchase_medium": purchase_medium,
                "order_id": order_id,
                "release_date": release_date.strftime("%Y-%m-%d"),
                "estimated_delivery_date": estimated_delivery_date.strftime("%Y-%m-%d"),
                "received_date": received_date.strftime("%Y-%m-%d"),
                "customer_exp_rating": customer_exp_rating,
            }
        )

    logging.info("Data generation complete")
    return pd.DataFrame(data)
