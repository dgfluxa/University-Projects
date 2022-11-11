from apscheduler.schedulers.background import BackgroundScheduler
from proyectogrupo2_api.Views.utilities import *
from proyectogrupo2_api.Views.ingredients import Ingredientes
import proyectogrupo2_api.sftp as sftp

scheduler = BackgroundScheduler()

Ingredientes = Ingredientes()

scheduler.add_job(Ingredientes.order_ingredients_from_factory, trigger='interval', minutes=7)
scheduler.add_job(Ingredientes.from_recepcion_to_general, trigger='interval', minutes=1)
scheduler.add_job(sftp.save_db, trigger='interval', minutes=1)
scheduler.add_job(sftp.check_new_orders, trigger='interval', minutes=3)
scheduler.add_job(Ingredientes.handler_order_manager, trigger='interval', minutes=5)

def start():
    #sftp.update_old_orders()
    #Ingredientes._from_x_to_y()
    sftp.check_new_orders()
    sftp.save_db()
    Ingredientes.handler_order_manager()

    print("\nSTARTING SCHEDULER\n")
    scheduler.start()
