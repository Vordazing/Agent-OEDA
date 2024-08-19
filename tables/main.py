import httpx
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Record(BaseModel):
    key: str
    hostname: str
    ip: str
    worker: str
    MAC: str
    sn: str
    owner: str

class DataToSend(BaseModel):
    monitoring: str
    records: list[Record]

async def fetch_tags(monitoring_id: str):
    if monitoring_id == "1":
        url = 'http://10.90.90.7:17805/api/tags?key=ad9dabb1ce714d30bde6647f797e7cbf'
    elif monitoring_id == "2":
        url = 'http://10.90.90.8:17805/api/tags?key=53ed7e1f18284012a8b5630923efa306'
    elif monitoring_id == "3":
        url = 'http://10.90.90.9:17805/api/tags?key=3f307beb0d0a422a8aa8feae64c3c84b'
    else:
        raise HTTPException(status_code=400, detail="Invalid monitoring ID")

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Проверка успешности запроса
        return response.json()

@app.post("/submit")
async def submit_data(data: DataToSend):
    print("Полученные данные:", data)

    tags = await fetch_tags(data.monitoring)

    # Создаем словарь сопоставления description -> id
    tag_dict = {tag['description']: tag['id'] for tag in tags}

    if data.monitoring == "1":
        url = 'http://10.90.90.7:17805/api/externalminers?key=ad9dabb1ce714d30bde6647f797e7cbf'
    elif data.monitoring == "2":
        url = 'http://10.90.90.8:17805/api/externalminers?key=53ed7e1f18284012a8b5630923efa306'
    elif data.monitoring == "3":
        url = 'http://10.90.90.9:17805/api/externalminers?key=3f307beb0d0a422a8aa8feae64c3c84b'
    else:
        raise HTTPException(status_code=400, detail="Invalid monitoring ID")

    async with httpx.AsyncClient() as client:
        for record in data.records:
            # Находим ID для владельца
            owner_id = tag_dict.get(record.owner)
            if owner_id is None:
                raise HTTPException(status_code=400, detail=f"Owner '{record.owner}' not found")

            data_list = {
                "description": record.hostname,
                "hostname": record.ip,
                "addToWorkerName": record.worker,
                "macAddress": record.MAC,
                "userNotes": f'SN: {record.sn}',
                "tagList": [owner_id]
            }

            print(f"URL: {url}")
            print(f"Data: {data_list}")

            response = await client.post(url, json=data_list)

            if response.status_code != 200:
                print(f"Ошибка отправки данных: {response.status_code}")
                return {"message": "Ошибка отправки данных", "status_code": response.status_code}

    return {"message": "Данные успешно отправлены"}



DATABASE_URL = "postgresql://maxorder:maxorder404@80.87.110.141/umc"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MonitoringData(Base):
    __tablename__ = "ipbd"

    id = Column(Integer, primary_key=True, index=True)
    ip_address = Column(String, index=True)
    hostname = Column(String)
    whence = Column(String)
    serial_number = Column(String)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/{monitoring_type}/add")
async def add_data(ip_address: str, hostname: str, whence: str, db: Session = Depends(get_db)):
    new_data = MonitoringData(whence=whence, hostname=hostname, ip_address=ip_address)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)


@app.post("/{monitoring_type}/clear")
async def clear_data(monitoring_type: str, db: Session = Depends(get_db)):
    delete_query = delete(MonitoringData).where(MonitoringData.whence == monitoring_type)
    result = db.execute(delete_query)
    db.commit()


@app.get("/{monitoring_type}")
async def get_data(monitoring_type: str, db: Session = Depends(get_db)):
    print(monitoring_type)
    data = db.query(MonitoringData).filter(MonitoringData.whence == monitoring_type).all()
    filtered_data = [
        {
            "ip_address": item.ip_address,
            "hostname": item.hostname,
            "serial_number": item.serial_number
        }
        for item in data
    ]
    print(filtered_data)
    return filtered_data