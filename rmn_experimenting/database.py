from sqlmodel import SQLModel, create_engine
import os
import mysql.connector
import main
import models
from sqlalchemy import create_engine, MetaData

#engine = create_engine("mysql+pymysql://testuser:RMN123@192.168.1.84:3306/rmn_records", echo=True)
engine = create_engine("mysql+pymysql://testuser:RMN123@192.168.254.130:3306/rmn_records", echo=True)

def createBank(bankAcct : int, due : float, amount : float):
    new_bank = models.Bank()
    new_bank.bankAcct = bankAcct
    new_bank.due = due
    new_bank.amount = amount
    main.session.add(new_bank)
    #main.session.commit()
    print("bank")
    return new_bank

