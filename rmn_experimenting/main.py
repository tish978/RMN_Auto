from fastapi import FastAPI, Body, Form, Request, File, UploadFile
from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Bank, Customer, Employee, ItemsCovered, PaymentHistory, PurchasedCar, Purchaser, Sale, Salesperson, SoldCar, carProblems, soldWarranty, employmentInfo
from database import engine
from sqlmodel import Session, select
from typing import Optional, List
from sqlalchemy import func
import datetime
import database

app = FastAPI()

session=Session(bind=engine)
templates = Jinja2Templates(directory="htmlDirectory")

@app.get("/tables")
async def get_all_tables():
    pass

#                           get functions                       #
####################################################################################
@app.get("/banks", response_model=List[Bank])
async def get_all_banks():
    statement=select(Bank)
    results=session.exec(statement).all()
    return results

@app.get("/customers", response_model=List[Customer])
async def get_all_customers():
    statement=select(Customer)
    results=session.exec(statement).all()
    return results

@app.get("/employees", response_model=List[Employee])
async def get_all_employees():
    statement=select(Employee)
    results=session.exec(statement).all()
    return results

@app.get("/itemsCovered", response_model=List[ItemsCovered])
async def get_all_itemsCovered():
    statement=select(ItemsCovered)
    results=session.exec(statement).all()
    return results

@app.get("/paymentHistories", response_model=List[PaymentHistory])
async def get_all_paymentHistories():
    statement=select(PaymentHistory)
    results=session.exec(statement).all()
    return results

@app.get("/purchasedCars", response_model=List[PurchasedCar])
async def get_all_purchasedCars():
    statement=select(PurchasedCar)
    results=session.exec(statement).all()
    return results

@app.get("/purchaser", response_model=List[Purchaser])
async def get_all_purchasers():
    statement=select(Purchaser)
    results=session.exec(statement).all()
    return results

@app.get("/sale", response_model=List[Sale])
async def get_all_sales():
    statement=select(Sale)
    results=session.exec(statement).all()
    return results

@app.get("/salesperson", response_model=List[Salesperson])
async def get_all_salespersons():
    statement=select(Salesperson)
    results=session.exec(statement).all()
    return results

@app.get("/soldCars", response_model=List[SoldCar])
async def get_all_soldCars():
    statement=select(SoldCar)
    results=session.exec(statement).all()
    return results

@app.get("/warranties", response_model=List[soldWarranty])
async def get_all_warranties():
    statement=select(soldWarranty)
    results=session.exec(statement).all()
    return results



#                           post functions                       #
####################################################################################
@app.post("/banks", response_model=Bank,
          status_code=status.HTTP_201_CREATED)
async def create_a_bank(bank: Bank):
    new_bank = Bank(bankAcct=bank.bankAcct, due=bank.due, amount=bank.amount)
    session.add(new_bank)
    session.commit()
    return new_bank

@app.post("/createBank", response_class=HTMLResponse)
def create_bank(request: Request, bankAcct: int = Form(...), due: float = Form(...), amount: float = Form(...)):
    print("bankAcct :" + str(bankAcct) + ", due:" + str(due) + ", amount:" + str(amount))
    new_bank = Bank(bankAcct=bankAcct, due=due, amount=amount)
    session.add(new_bank)
    session.commit()
    print("Successfully made new bank!")
    statement = select(Bank).where(Bank.bankAcct == bankAcct)
    results=session.exec(statement).all()
    return templates.TemplateResponse("bankFormOutput.html", {"request": request, "results": results})


@app.post("/createCarSale", response_class=HTMLResponse)
def create_carSale(request: Request, empID: int = Form(...), e_first_name: str = Form(...), e_last_name: str = Form(...), e_phone: str = Form(...), customer_ID: int = Form(...), c_phone: str = Form(...), c_last_name: str = Form(...), c_first_name: str = Form(...), city: str = Form(...), state: str = Form(...), zip: int = Form(...), gender: str = Form(...), creditScore: int = Form(...), VIN: int = Form(...), miles: int = Form(...), condition: str = Form(...), style: str = Form(...), interior_color: str = Form(...), employerName: str = Form(...), jobTitle: str = Form(...), supervisorName: str = Form(...), supervisorPhone: str = Form(...), employmentAddress: str = Form(...)):
    print("empID :" + str(empID) + ", e_first_name:" + str(e_first_name) + ", e_last_name:" + str(e_last_name) + "e_phone:" + str(e_phone) + ", customer_ID:" + str(customer_ID) + ", c_phone:" + str(c_phone) + "c_last_name :" + str(c_last_name) + ", c_first_name:" + str(c_first_name) + ", city:" + str(city) + ", state:" + str(state) + ", ZIP :" + str(zip) + ", gender:" + str(gender) + "creditScore :" + str(creditScore) + ", VIN :" + str(VIN) + ", miles:" + str(miles) + "condition :" + str(condition) + ", style :" + str(style) + ", interior_color:" + str(interior_color))
    saleIDQuery = session.query(func.max(Sale.sale_ID)).first()
    new_saleID: int = 0
    for saleID in saleIDQuery:
        new_saleID = saleID + 1
        print(new_saleID)
    print(new_saleID)
    new_sale = Sale(sale_ID=new_saleID, employee_ID=empID)

    empIDQuery = session.query(func.max(employmentInfo.employmentID)).first()
    new_empID: int = 0
    for empID in empIDQuery:
        new_empID = empID + 1
        print(new_empID)
    print(new_empID)
    new_employmentInfo = employmentInfo(employmentID=new_empID, employerName=employerName, jobTitle=jobTitle, supervisorName=supervisorName, supervisorPhone=supervisorPhone, employmentAddress=employmentAddress, customerID=customer_ID)

    purchasedCar = select(PurchasedCar).where(PurchasedCar.VIN == VIN)
    pCarResult: PurchasedCar = session.exec(purchasedCar).first()
    pCarVIN: int = pCarResult.VIN
    print("pCarResult: " + str(pCarResult))
    print("pCarVIN: " + str(pCarVIN))

    statement = select(Employee).where(Employee.empID == empID)
    result = session.exec(statement).first()
    print("Found employee is: " + str(result))
    result.customer_ID = customer_ID
    print("Updated employee is: + " + str(result))
    new_customer = Customer(customer_ID=customer_ID, c_phone=c_phone, c_last_name=c_last_name, c_first_name=c_first_name, city=city, state=state, zip=zip, gender=gender, creditScore=creditScore)
    print("New customer is: " + str(new_customer))
    new_soldcar = SoldCar(customer_ID=customer_ID, VIN=pCarVIN, miles=miles, condition=condition, style=style, interior_color=interior_color)
    #new_soldcar.VIN = pCarResult.VIN
    print("New sold car is: " + str(new_soldcar))
    session.add(new_sale)
    #session.add(new_employee)
    session.add(result)
    session.add(new_customer)
    session.add(new_soldcar)
    session.add(new_employmentInfo)
    print("New employmentInfo: " + str(new_employmentInfo))
    session.commit()

    saleResults = select(Sale).where(Sale.sale_ID == saleID)
    results1 = session.exec(saleResults).first()

    employeeResults = select(Employee).where(Employee.empID == empID)
    results2 = session.exec(employeeResults).first()

    customerResults = select(Customer).where(Customer.customer_ID == customer_ID)
    results3 = session.exec(customerResults).first()

    soldCarResults = select(SoldCar).where(SoldCar.VIN == VIN)
    results4 = session.exec(soldCarResults).first()


    return templates.TemplateResponse("carSaleOutput.html", {"request": request, "results1": new_sale, "results2": result, "results3": new_customer, "results4": new_soldcar})



@app.post("/createWarrantySale", response_class=HTMLResponse)
def create_warranty():
    pass


@app.post("/getBank", response_class=HTMLResponse)
def get_bank(request: Request, bankAcct: int = Form(...)):
    statement=select(Bank).where(Bank.bankAcct == bankAcct)
   # gotBank: Bank = session.exec(statement).first()
    results=session.exec(statement).all()
    print(results)
    return templates.TemplateResponse("bankReportOutput.html", {"request": request, "results": results})



@app.get("/getBank/{bankAcct}", response_model=List[Bank])
def get_bank(request: Request, bankAcct: int):
    print("Find fish called with bankAcct: " + str(bankAcct))
    result = select(Bank).having({"bankAcct" : bankAcct})
    print(result["bankAcct"])
    return



@app.post("/createCarPurchase", response_class=HTMLResponse)
def create_bank(request: Request, taxID: int = Form(...), location: str = Form(...), auction: str = Form(...), seller_dealer: str = Form(...), VIN: int = Form(...), make: str = Form(...), model: str = Form(...), year: str = Form(...), color: str = Form(...), miles: str = Form(...), car_problem_number: int = Form(...), problem_description: str = Form(...), est_repair_cost: int = Form(...)):
    print("taxID :" + str(taxID) + ", location:" + str(location) + ", auction:" + str(auction) + "seller_dealer :" + str(seller_dealer) + ", VIN:" + str(VIN) + ", make:" + str(make) + "model :" + str(model) + ", year:" + str(year) + ", color:" + str(color) + "miles :" + str(miles))
    new_purchaser = Purchaser(taxID=taxID, location=location, auction=auction, seller_dealer=seller_dealer, VIN=VIN)
    new_purchasedCar = PurchasedCar(VIN=VIN, make=make, model=model, year=year, color=color, miles=miles)

    problemIDQuery = session.query(func.max(carProblems.problemID)).first()
    new_problemID: int = 0
    for problemID in problemIDQuery:
        new_problemID = problemID + 1
        print(new_problemID)
    print(new_problemID)
    new_carProblems = carProblems(problemID=new_problemID, car_problem_number=car_problem_number, problem_description=problem_description, est_repair_cost=est_repair_cost, VIN=VIN)

    session.add(new_purchaser)
    session.add(new_purchasedCar)
    session.add(new_carProblems)
    session.commit()
    print("Successfully made new purchase and purchasedCar and carProblems!")
    return new_purchaser, new_purchasedCar, new_carProblems


@app.get("/createBankForm", response_class=HTMLResponse)
def bankForm_page(request: Request):
    return templates.TemplateResponse("bankForm.html", {"request": request})

@app.get("/readBankForm", response_class=HTMLResponse)
def bankForm_page(request: Request):
    return templates.TemplateResponse("bankReport.html", {"request": request})

@app.get("/createForm1", response_class=HTMLResponse)
def formOne_page(request: Request):
    return templates.TemplateResponse("Car-Purchase-Form.html", {"request": request})


@app.get("/createForm2", response_class=HTMLResponse)
def formTwo_page(request: Request):
    return templates.TemplateResponse("Car-Sale-Form.html", {"request": request})


@app.post("/customers", response_model=Customer,
          status_code=status.HTTP_201_CREATED)
async def create_a_customer(customer: Customer):
    new_customer = Customer(customer_ID=customer.customer_ID, phone=customer.phone, last_name=customer.last_name, first_name=customer.first_name, city=customer.city, state=customer.state, zip=customer.zip, gender=customer.gender, creditScore=customer.creditScore)
    session.add(new_customer)
    session.commit()
    return new_customer

@app.post("/employees", response_model=Employee,
          status_code=status.HTTP_201_CREATED)
async def create_an_employee(employee: Employee):
    new_employee = Employee(empID=employee.empID, first_name=employee.first_name, last_name=employee.last_name, customer_ID=employee.customer_ID)
    session.add(new_employee)
    session.commit()
    return new_employee

@app.post("/items_Covered", response_model= ItemsCovered,
          status_code=status.HTTP_201_CREATED)
async def create_an_itemsCovered(itemsCovered: ItemsCovered):
    new_IC = ItemsCovered(item_ID=itemsCovered.item_ID, length=itemsCovered.length)
    session.add(new_IC)
    session.commit()
    return new_IC


@app.post("/paymentHistories", response_model=PaymentHistory,
          status_code=status.HTTP_201_CREATED)
async def create_a_paymentHisory(paymentHistory: PaymentHistory):
    new_PH = PaymentHistory(taxpayerID=paymentHistory.taxpayerID, number_late_payments=paymentHistory.number_late_payments, average_number_days_late=paymentHistory.average_number_days_late, bank=paymentHistory.bank)
    session.add(new_PH)
    session.commit()
    return new_PH


@app.post("/purchasedCars", response_model=PurchasedCar,
          status_code=status.HTTP_201_CREATED)
async def create_a_purchasedCar(purchasedCar: PurchasedCar):
    new_purchasedCar = PurchasedCar(VIN=purchasedCar.VIN, make=purchasedCar.make, model=purchasedCar.model, year=purchasedCar.year, color=purchasedCar.color, miles=purchasedCar.miles)
    session.add(new_purchasedCar)
    session.commit()
    return new_purchasedCar


@app.post("/purchaser", response_model=Purchaser,
          status_code=status.HTTP_201_CREATED)
async def create_a_purchaser(purchaser: Purchaser):
    new_purchaser = Purchaser(taxID=purchaser.taxID, location=purchaser.location, auction=purchaser.auction, seller_dealer=purchaser.seller_dealer, VIN=purchaser.VIN)
    session.add(new_purchaser)
    session.commit()
    return new_purchaser

@app.post("/sale", response_model=Sale,
          status_code=status.HTTP_201_CREATED)
async def create_a_sale(sale: Sale):
    new_sale = Sale(sale_ID=sale.sale_ID, employee_ID=sale.employee_ID)
    session.add(new_sale)
    session.commit()
    return new_sale


@app.post("/salesperson", response_model=Salesperson,
          status_code=status.HTTP_201_CREATED)
async def create_a_salesPerson(salesPerson: Salesperson):
    new_salesPerson = Salesperson(salesperson_ID=salesPerson.salesperson_ID, first_name=salesPerson.first_name, last_name=salesPerson.last_name, phone=salesPerson.phone, warranty_ID=salesPerson.warranty_ID)
    session.add(new_salesPerson)
    session.commit()
    return new_salesPerson

@app.post("/soldCars", response_model=SoldCar,
          status_code=status.HTTP_201_CREATED)
async def create_a_soldcar(soldCar: SoldCar):
    new_soldCar = SoldCar(customer_ID=soldCar.customer_ID, VIN=soldCar.VIN, miles=soldCar.miles, condition=soldCar.condition, style=soldCar.style, interior_color=soldCar.interior_color, warranty_ID=soldCar.warranty_ID)
    session.add(new_soldCar)
    session.commit()
    return new_soldCar

@app.post("/warranties", response_model=soldWarranty,
          status_code=status.HTTP_201_CREATED)
async def create_a_warranty(warranty: soldWarranty):
    new_warranty = soldWarranty(warranty_ID=warranty.warranty_ID, co_signer=warranty.co_signer)
    session.add(new_warranty)
    session.commit()
    return new_warranty



################    UPDATE FUNCTIONS ##############

@app.put("/bank/{bank_id}")
async def update_a_bank(bankAcct: int, bank: Bank):
    statement=select(Bank).where(Bank.bankAcct == bankAcct)
    result = session.exec(statement).first()
    result.bankAcct = bankAcct
    result.due = bank.due
    result.amount = bank.amount

    session.commit()

    return result


@app.put("/customers/{customer_ID}")
async def update_a_customer(customer_ID: int, customer: Customer):
    statement=select(Customer).where(Customer.customer_ID == customer_ID)
    result = session.exec(statement).first()
    result.customer_ID = customer_ID
    result.phone = customer.phone
    result.last_name = customer.last_name
    result.first_name = customer.first_name
    result.city = customer.city
    result.state = customer.state
    result.zip = customer.zip
    result.gender = customer.gender
    result.creditScore = customer.creditScore

    session.commit()

    return result


@app.put("/employees/{empID}")
async def update_a_employee(empID: int, employee: Employee):
    statement = select(Employee).where(Employee.empID == empID)
    result = session.exec(statement).first()
    result.empID = empID
    result.first_name = employee.first_name
    result.last_name = employee.last_name
    result.customer_ID = employee.customer_ID
    session.commit()
    return result



@app.put("/itemsCovered/{item_ID}")
async def update_an_itemsCovered(item_ID: int, itemsCovered: ItemsCovered):
    statement = select(ItemsCovered).where(ItemsCovered.item_ID == item_ID)
    result = session.exec(statement).first()
    result.item_ID = item_ID
    result.length = itemsCovered.length

    session.commit()

    return result