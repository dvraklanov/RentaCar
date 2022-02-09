import logging
from app.database import Database
from app.vehicles import Vehicles
from app.customer import Customers


if __name__ == '__main__':
    db = Database("app/data/test_db")
    veh = Vehicles(db)
    cust = Customers(db)
    logging.info(veh.add_veh(veh_data={'name': 'Ford Mustang', 'number_plate': 'num2312',
                                       'body_type': 'Седан', 'wheel_drive': 'RWD',
                                       'fuel_type': 'Бензин', 'power_hp': 120, 'n_seat': 5,
                                       'rental_price': 3500, 'gearbox_type': 'Ручная'}))

    #logging.info(veh.get_uniq_spec('number_plate'))
    #logging.info(veh.edit_spec(id=9, new_values={'status': 1}))
    #logging.info(veh.get_all_veh())
    #logging.info(veh.get_spec(id=10))
    #logging.info(veh.del_veh(id=13))
