# csv library
import csv
# import tableHash file
from tableHash import HashTable
# import datetime
from datetime import datetime as dt

# Replace method
EOD = dt.now().replace(hour=23, minute=59, second=0)

# Class Package
class Package:
    '''Used to bundle package related info into an object.'''

    def __init__(self, id: str, address: str, city: str, state: str, zip: str, deadline: str, weight: str, note: str = ''):
        '''Will cast args to their appropriate data types'''
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = float(weight)
        self.note = note

        self.status: str = 'Pending'
        self.truck: int = 0
        self.stateDeliv: str = ''
        self.locAdd: str = ''

        today = dt.now()
        if deadline.upper() == 'EOD':
            self.deadline = EOD
        else:
            parsed_deadline = dt.strptime(deadline, '%I:%M:%S')
            hour, minute = parsed_deadline.hour, parsed_deadline.minute
            self.deadline = today.replace(hour=hour, minute=minute, second=0)
    # Package Status
    @property
    def delivered(self):
        return self.status.lower() == 'delivered'
    # Setting the different attributes
    def __repr__(self):
        return f'- Package {self.id} Info -\n' \
               f'Weight: {self.weight}\n' \
               f'Deadline: {self.deadline}\n' \
               f'Status: {self.status}\n' \
               f'Destination: {self.address}\n' \
               f'             {self.city}, {self.state}, {self.zip}\n' \
               f'Notes: {self.note}\n'

    # The following functions are used to sort the packages

    def __lt__(self, other):
        return int(self.id) < int(other.id) if other.__class__ is self.__class__ else NotImplemented

    def __le__(self, other):
        return int(self.id) <= int(other.id) if other.__class__ is self.__class__ else NotImplemented

    def __gt__(self, other):
        return int(self.id) > int(other.id) if other.__class__ is self.__class__ else NotImplemented

    def __ge__(self, other):
        return int(self.id) >= int(other.id) if other.__class__ is self.__class__ else NotImplemented

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.address, self.city, self.state, self.zip, self.weight, self.note) \
                == (other.id, other.address, other.city, other.state, other.zip, other.weight, other.note)
        else:
            return NotImplemented

# Open file
with open('packets_data.csv') as f:
    data = [*csv.reader(f)]

pkgs: HashTable = HashTable()
listFirstTrPk:  list[Package] = []
listSecondTrPk: list[Package] = []
listThirdTrPk:  list[Package] = []

for row in data:  # O (n)
    pkg = Package(*row)

    # pkg_id: str = row[0]
    # pkg_street: str = row[1]
    # pkg_city: str = row[2]
    # pkg_state: str = row[3]
    # pkg_zip: str = row[4]
    # pkg_deadline: str = row[5]
    # pkg_weight: float = float(row[6])
    # pkg_note: str = row[7]

    # stateDeliv: str = ''
    # locAdd: str = ''
    # pkg_status: str = 'At HUB'
    # val = [pkg_id, locAdd, pkg_street, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_weight, pkg_note,
    #             stateDeliv, pkg_status]

    if pkg.deadline != EOD:
        if 'Delayed on flight---will not arrive to depot until 9:05 am' in pkg.note or '3365 S 900 W' in pkg.address:
            listSecondTrPk.append(pkg)
        elif '3365 S 900 W' in pkg.address:
            listSecondTrPk.append(pkg)
        else:
            listFirstTrPk.append(pkg)
    elif (pkg.deadline == EOD) and ('none' not in pkg.note):
        if 'Wrong address listed' in pkg.note:
            listThirdTrPk.append(pkg)
        elif '84103' in pkg.zip:
            listThirdTrPk.append(pkg)
        else:
            listSecondTrPk.append(pkg)
    elif (pkg.deadline == EOD) and ('none' in pkg.note):
        if pkg.address in ('177 W Price Ave', '2010 W 500 S', '1330 2100 S', '3575 W Valley Central Station bus Loop', '3148 S 1100 W'):
            listFirstTrPk.append(pkg)
        else:
            if pkg.zip in ('84103', '84111', '84117', '84119'):
                if '300 State St' in pkg.address:
                    listThirdTrPk.append(pkg)
                else:
                    listSecondTrPk.append(pkg)
            else:
                listThirdTrPk.append(pkg)
    pkgs.insert(pkg.id, pkg)

# These methods return the list of packages
def get_listFirstTrPk() -> list[Package]:
    return listFirstTrPk


def get_listSecondTrPk() -> list[Package]:
    return listSecondTrPk


def get_listThirdTrPk() -> list[Package]:
    return listThirdTrPk


def get_pkg_db() -> HashTable:
    '''Returns a Hashtable Containing Packages'''
    return pkgs
