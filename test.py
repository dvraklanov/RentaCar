import logging
from vehicles import Vehicles


if __name__ == '__main__':
    veh = Vehicles()
    logging.info(veh.add_veh(veh_data={'name': 'Ford Focus', 'number_plate': 'num123',
                                       'body_type': 'Седан', 'wheel_drive': 'RWD',
                                       'fuel_type': 'Бензин', 'power_hp': 120, 'n_seat': 5,
                                       'rental_price': 3500, 'gearbox_type': 'Ручная'}))



    #logging.info(veh.get_all_veh())
    #logging.info(veh.get_spec(id=11))
    #logging.info(veh.del_veh(id=13))
