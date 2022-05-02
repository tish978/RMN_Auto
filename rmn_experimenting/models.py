from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Bank(SQLModel, table=True):
    bankAcct: Optional[int] = Field(primary_key=True)
    pmt_date: str
    due: float
    paid_date: str
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
    DOB: str
    creditScore: int
    taxpayerID: int


class employmentInfo(SQLModel, table=True):
    employmentID: Optional[int] = Field(primary_key=True)
    employerName: str
    jobTitle: str
    supervisorName: str
    supervisorPhone: str
    employmentAddress: str
    employmentStartDate: str
    customerID: int



class Employee(SQLModel, table=True):
    empID: Optional[int] = Field(primary_key=True)
    first_name: str
    last_name: str
    username: str
    password: str
    commission: int
    customer_ID: int


class ItemsCovered(SQLModel, table=True):
    item_ID: Optional[int] = Field(primary_key=True)
    #start_date: date
    length: str
    #cost: double
    #deductible: double


class PaymentHistory(SQLModel, table=True):
    taxpayerID: Optional[int] = Field(primary_key=True)
    number_late_payments: Optional[int]
    average_number_days_late: Optional[int]
    bank: Optional[int]


class PurchasedCar(SQLModel, table=True):
    VIN: Optional[int] = Field(primary_key=True)
    make: Optional[str]
    model: str
    year: str
    color: str
    miles: int
    book_price: int
    price_paid: int



class carProblems(SQLModel, table=True):
    problemID: Optional[int] = Field(primary_key=True)
    problem_description: str
    est_repair_cost: int
    actual_cost: int
    VIN: int
    car_problem_number: int



class Purchaser(SQLModel, table=True):
    taxID: Optional[int] = Field(primary_key=True)
    date: str
    location: str
    auction: str
    seller_dealer: str
    VIN: int


class Sale(SQLModel, table=True):
    sale_ID: Optional[int] = Field(primary_key=True)
    total_price: int
    down_payment: int
    financed_amount: int
    date: str
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
    list_price: int
    sale_price: int
    style: str
    interior_color: str
    warranty_ID: int


class soldWarranty(SQLModel, table=True):
    warranty_ID: Optional[int] = Field(primary_key=True)
    co_signer: str
    warranty_sale_date: date
    total_cost: int
    monthly_cost: int
    customer_warranty_number: int
    warranty_start_date: date
    warranty_length: str
    warranty_cost: int
    warranty_deductible: int
    items_covered: str
    VIN: int
    customerID: int
