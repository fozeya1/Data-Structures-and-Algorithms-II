# Data Structures and Algorithms II
# Student Name: Fozeya Chowdhury


from read_csv_file import get_pkg_db
from modules import get_total_trks_distance
import datetime as dt


def showStatus(pkg_id): #shows file status
    print(
        f'Package ID: {get_pkg_db().search(str(pkg_id)).id}',
        f'\tTruck load time: {get_pkg_db().search(str(pkg_id)).stateDeliv}',
        f'\tDelivery status: {get_pkg_db().search(str(pkg_id)).status}'
    )


def showPkDetail(pkg_id): #show package details w.r.t id
    print(get_pkg_db().search(str(pkg_id)))

class Main:
    # page header
    print("*"*100)
    print("-----------------------------WGUPS Packet Tracking Console-----------------------------",sep='\n')
    print("*"*100)

    # Total delivery package for all 40 packets
    distance=get_total_trks_distance()
    print("Complete delivery of all 40 packets was accomplished at",distance,"miles\n")

class Main:  #Main Class
    print('\n\n-------------------- Packet Tracking --------------------\n')
    now = dt.datetime.now()
    cur_time: str = now.strftime("%H:%M:%S")   # shows current time in hour,minute and seconds format
    cur_date: str = now.strftime("%Y-%m-%d")   # Shows current date
    print("Date: ", cur_date)                  # Print current time
    print("Time: ", cur_time)                  # Print current time
    in_user = int(input("\nPress 1 to list all packages\nPress 2 to search for package by ID\n"))
    if in_user not in (1, 2):                  # If checks
        print("Invalid entry")
        exit()
    while in_user != 'quit':
        try:
            hrs, mins, secs = map(int, input('Enter a time to search report in format-->(HH:MM:SS):\n').split(':'))
        except ValueError:
            print('[!] Wrong format! Please try again...\n')
            continue
        print('-' * 100)

        time_query = dt.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        if in_user == 1:
            try:
                for pkg in get_pkg_db():
                    try:
                        # stateDeliv
                        hrs, mins, secs = map(int, pkg.stateDeliv.split(':'))  # FIXME: pkg.stateDeliv is blank
                        pkg_load_time = dt.timedelta(hours=hrs, minutes=mins, seconds=secs)

                        # Status
                        hrs, mins, secs = map(int, pkg.status.split(':'))
                        pkg_delivery = dt.timedelta(hours=hrs, minutes=mins, seconds=secs)
                    except ValueError as VE:
                        print(VE)
                    else:  # if no exceptions, display correct status based on truck load time
                        if time_query <= pkg_load_time:
                            pkg.status = 'At Hub'    # Pkg Status
                        elif time_query > pkg_load_time:
                            if time_query < pkg_delivery:
                                pkg.status = 'In transit'  # Status
                            else:
                                pkg.status = f'Delivered at {pkg.status}'
                        showStatus(pkg.id)
                break
            # Exception Errors
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Entry not exist!')
                continue
        elif in_user == 2:
            try:
                pkg_id: str = input('Enter a existing package ID: \n')
                pkg = get_pkg_db()[pkg_id]

                # Truck Load Time to timedelta
                hrs, mins, secs = map(int, pkg.stateDeliv.split(':'))
                trk_load_time = dt.timedelta(hours=hrs, minutes=mins, seconds=secs)

                # Delivery Time to timedelta
                hrs, mins, secs = map(int, pkg.status.split(':'))
                pkg_delivery = dt.timedelta(hours=hrs, minutes=mins, seconds=secs)

                showPkDetail(pkg_id)

                if time_query <= trk_load_time:        # Load time query
                    pkg.status = 'At Hub'
                elif time_query > trk_load_time:
                    if time_query < pkg_delivery:
                        pkg.status = 'In Transit'
                    else:
                        pkg.status = f'Delivered at {pkg.status}'   # Pkg status
                showStatus(pkg_id)
            except ValueError:
                print('Entry not exist!')
                exit()
        else:
            print('Entry not exist!')
            exit()
