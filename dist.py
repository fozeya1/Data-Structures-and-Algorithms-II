# Import csv library
import csv
# For date and time functionality
import datetime
# Import file and its packages
from read_csv_file import Package

# get address
def get_addrs() -> list[list[str]]:
    '''Returns Address list from address_data.csv'''
    return addr_data

# get total distance covered
def get_total_dist(row: int, col: int, total: float) -> float:
    distance = dist_data[row][col]
    if not distance:
        distance = dist_data[col][row]

    return total + float(distance)


def get_dist(row: int, col: int) -> float:
    distance = dist_data[row][col]
    if distance == '':
        distance = dist_data[col][row]
    return float(distance)
# Get time methods that distance conversion
def timeGet(distance: float, truck_list: list[str]) -> datetime.timedelta:
    distance_in_minutes: str = '{0:02.0f}:{1:02.0f}'.format(
        *divmod((distance / 18) * 60, 60))
    truck_list.append(distance_in_minutes + str(':00'))
    total = datetime.timedelta()
    for _time in truck_list:
        (hrs, mins, secs) = map(int, _time.split(':'))
        total += datetime.timedelta(hours=hrs,
                                    minutes=mins, seconds=secs)
    return total

# fast route finding
def fastRouteFind(pkg_list: list, truck_id: int, curr_location: int):  # O(2n) = O(n)
    if not pkg_list:
        return pkg_list
    lowest_value = 50.0
    location = 0

    for pkg in pkg_list:  # O(n)
        pkg_loc = int(pkg.locAdd)
        if get_dist(curr_location, pkg_loc) <= lowest_value:  # Get lowest value in list
            lowest_value = get_dist(curr_location, pkg_loc)
            location = pkg_loc

    for pkg_idx, pkg in enumerate(pkg_list):  # O(n)
        if get_dist(curr_location, int(pkg.locAdd)) == lowest_value:
            if truck_id == 1:
                sortListFirstTr.append(pkg)
                sortIndicesFirstTr.append(pkg.locAdd)
                pkg_list.pop(pkg_idx)  # remove pkg from pkg_list
                curr_location = location
                fastRouteFind(pkg_list, 1, curr_location)
            elif truck_id == 2:
                sortListSecondTr.append(pkg)
                sortIndicesSecondTr.append(pkg.locAdd)
                pkg_list.pop(pkg_idx)
                curr_location = location
                fastRouteFind(pkg_list, 2, curr_location)
            elif truck_id == 3:
                sortListThirdTr.append(pkg)
                sortIndicesThirdTr.append(pkg.locAdd)
                pkg_list.pop(pkg_idx)
                curr_location = location
                fastRouteFind(pkg_list, 3, curr_location)


# TODO: Rename these getters
def sortIndexFirstTrGet():
    return sortIndicesFirstTr


def sortListFirstTrGet() -> list[Package]:
    return sortListFirstTr


def sortIndexSecondTrGet():
    return sortIndicesSecondTr


def sortListSecondTrGet() -> list[Package]:
    return sortListSecondTr


def sortIndexThirdTrGet():
    return sortIndicesThirdTr


def sortListThirdTrGet() -> list[Package]:
    return sortListThirdTr


# Import distance and address data
with open('distance_data.csv') as f:
    dist_data: list[list[str]] = [*csv.reader(f)]

with open('address_data.csv') as f:
    addr_data: list[list[str]] = [*csv.reader(f)]

# TODO: Check if adding '0's inside lists broke anything else, uncomment the last 3 lines where the 0's are inserted
sortListFirstTr: list[Package] = []
sortIndicesFirstTr = ['0']

sortListSecondTr: list[Package] = []
sortIndicesSecondTr = ['0']

sortListThirdTr: list[Package] = []
sortIndicesThirdTr = ['0']

# sortIndicesFirstTr.insert(0, '0')
# sortIndicesSecondTr.insert(0, '0')
# sortIndicesThirdTr.insert(0, '0')
