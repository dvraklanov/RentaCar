from app.vehicles import Vehicles
from app.database import Database

db = Database("app/data/test_db")
vehicle_data = Vehicles(db)

print(vehicle_data.get_uniq_spec('fuel_type'))

