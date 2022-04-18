from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Bank(SQLModel, table=True):
    bankAcct: Optional[int] = Field(primary_key=True)
    #pmt_date: date
    due: float
    #paid_date: date
    amount: float



class Customer(SQLModel, table=True):
    customer_ID: Optional[int] = Field(primary_key=True)
    phone: str
    last_name: str
    first_name: str
    city: str
    state: str
    zip: int
    gender: str
    #DOB: date
    creditScore: int
    #employer: str
    #title: str
    #supervisor: str
    #phone: str
    #address: str
    #start: date


class Employee(SQLModel, table=True):
    empID: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name: str
    #commission: double
    customer_ID: int


class ItemsCovered(SQLModel, table=True):
    item_ID: Optional[int] = Field(primary_key=True)
    #start_date: date
    length: str
    #cost: double
    #deductible: double


class PaymentHistory(SQLModel, table=True):
    taxpayerID: Optional[int] = Field(primary_key=True)
    number_late_payments: int
    average_number_days_late: int
    bank: int


class PurchasedCar(SQLModel, table=True):
    VIN: Optional[int] = Field(primary_key=True)
    make: str
    model: str
    year: str
    color: str
    miles: int
    #book_price: double
    #price_paid: double


class Purchaser(SQLModel, table=True):
    taxID: Optional[int] = Field(primary_key=True)
    #date: date
    location: str
    auction: str
    seller_dealer: str
    VIN: int


class Sale(SQLModel, table=True):
    sale_ID: Optional[int] = Field(primary_key=True)
    #total_price: double
    #down_payment: double
    #financed_amount: double
    #date: date
    employee_ID: int


class Salesperson(SQLModel, table=True):
    salesperson_ID: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name: str
    phone: str
    warranty_ID: int


class SoldCar(SQLModel, table=True):
    customer_ID: Optional[int] = Field(primary_key=True)
    VIN: Optional[int] = Field(primary_key=True)
    miles: int
    condition: str
    #list_price: double
    #sale_price: double
    style: str
    interior_color: str
    warranty_ID: int


class Warranty(SQLModel, table=True):
    warranty_ID: Optional[int] = Field(primary_key=True)
    co_signer: str
    #warranty_sale_date: Date
    #total_cost: double
    #monthly_cost: double
