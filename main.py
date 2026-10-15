"""Minimal API scaffold. Add authentication/authorisation before exposing real data."""
from datetime import datetime, timezone
import os, sqlite3
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DB_PATH = Path(os.getenv('LOLOS_DB_PATH', str(Path(__file__).parent / 'lolos.db')))
app = FastAPI(title="LoLo's Scrap Collect API", version="0.1.0", description="Development scaffold; not production-secured.")

class Intake(BaseModel):
    seller_ref: str = Field(min_length=2, max_length=80)
    material_code: str = Field(min_length=2, max_length=80)
    received_date: str
    gross_kg: float = Field(gt=0)
    tare_kg: float = Field(ge=0)
    buy_rate_zar_kg: float = Field(ge=0)
    payment_method: str
    counterparty_verified: bool
    provenance_status: str = "unknown"

@app.on_event('startup')
def setup():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DB_PATH) as db:
        db.execute('''CREATE TABLE IF NOT EXISTS intake (id INTEGER PRIMARY KEY, created_utc TEXT, seller_ref TEXT, material_code TEXT, received_date TEXT, gross_kg REAL, tare_kg REAL, net_kg REAL, buy_rate REAL, estimated_value REAL, payment_method TEXT, provenance_status TEXT, status TEXT)''')
        db.execute('''CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY, created_utc TEXT, action TEXT, record_id INTEGER, details TEXT)''')

@app.get('/health')
def health(): return {'status':'ok','service':"LoLo's Scrap Collect API",'mode':'development scaffold'}

@app.get('/api/intakes')
def list_intakes():
    with sqlite3.connect(DB_PATH) as db:
        db.row_factory=sqlite3.Row
        return [dict(r) for r in db.execute('SELECT * FROM intake ORDER BY id DESC LIMIT 500')]

@app.post('/api/intakes', status_code=201)
def create_intake(item: Intake):
    net = round(item.gross_kg - item.tare_kg, 3)
    if net <= 0: raise HTTPException(422, 'Net weight must be greater than zero.')
    if not item.counterparty_verified: raise HTTPException(409, 'Counterparty verification must be completed before this demo API accepts an intake.')
    if item.payment_method not in {'EFT','Instant EFT','Approved provider'}: raise HTTPException(409, 'Use an approved electronic payment method in this prototype.')
    if item.provenance_status != 'documented': status = 'review'
    else: status = 'received'
    now = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(DB_PATH) as db:
        cur = db.execute('INSERT INTO intake (created_utc,seller_ref,material_code,received_date,gross_kg,tare_kg,net_kg,buy_rate,estimated_value,payment_method,provenance_status,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', (now,item.seller_ref,item.material_code,item.received_date,item.gross_kg,item.tare_kg,net,item.buy_rate_zar_kg,round(net*item.buy_rate_zar_kg,2),item.payment_method,item.provenance_status,status))
        rec_id = cur.lastrowid
        db.execute('INSERT INTO audit (created_utc,action,record_id,details) VALUES (?,?,?,?)',(now,'CREATE_INTAKE',rec_id,f'material={item.material_code}; net_kg={net}; status={status}'))
    return {'id':rec_id,'net_kg':net,'estimated_value_zar':round(net*item.buy_rate_zar_kg,2),'status':status,'note':'Development API only; verify legal controls before production.'}
