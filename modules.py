# import dist file
import dist
import read_csv_file
# import read_csv file
from read_csv_file import Package
# List
listfirstTrPk: list[Package] = []
listSecondTrPk: list[Package] = []
listThirdTrPk: list[Package] = []
# Some variables or attributes
distTrFirst = []
distTrSecond = []
distTrThird = []
# Time attributes
startTimeTrFirst = ['8:00:00']
startTimeTrSecond = ['9:10:00']
startTimeTrThird = ['11:00:00']


# Truck No. 1
for pkg in read_csv_file.get_listFirstTrPk():  # Replicating the TrPK list from read_csv???
    pkg.stateDeliv = startTimeTrFirst[0]
    listfirstTrPk.append(pkg)
# Load data into the attributes
for pkg in listfirstTrPk:
    for addr in dist.get_addrs():
        if pkg.address == addr[2]:
            distTrFirst.append(pkg.id)
            pkg.locAdd = addr[0]

dist.fastRouteFind(listfirstTrPk, 1, 0)
tr1TotalDist: float = 0 # Initialization

# TODO: better? -> for idx, idx_nxt, pkg in zip(dist.sortIndexFirstTrGet(), dist.sortIndexFirstGet()[1:], dist.sortListFirstTrGet())
for index in range(len(dist.sortIndexFirstTrGet())):  # index used to look ahead uses pkg and address indexes
    try:
        tr1TotalDist = dist.get_total_dist(
            int(dist.sortIndexFirstTrGet()[index]), int(dist.sortIndexFirstTrGet()[index + 1]),
            tr1TotalDist
        )
# For pkg delivery
        packDeliv = dist.timeGet(
            dist.get_dist(
                int(dist.sortIndexFirstTrGet()[index]), int(dist.sortIndexFirstTrGet()[index + 1])
            ),
            startTimeTrFirst
        )
# Sort pkg status
        dist.sortListFirstTrGet()[index].status = str(packDeliv)
        read_csv_file.get_pkg_db().update(int(dist.sortListFirstTrGet()[index].id), listfirstTrPk)
    except IndexError:
        pass

# Truck No. 2
for pkg in read_csv_file.get_listSecondTrPk():
    pkg.stateDeliv = startTimeTrSecond[0]
    listSecondTrPk.append(pkg)

# Load data into the attributes for append
for pkg in listSecondTrPk:
    for addr in dist.get_addrs():
        if pkg.address == addr[2]:
            distTrSecond.append(pkg.id)
            pkg.locAdd = addr[0]

dist.fastRouteFind(listSecondTrPk, 2, 0)
tr2TotalDist: float = 0

# see comment in line 30
for index in range(len(dist.sortIndexSecondTrGet())):
    try:
        tr2TotalDist = dist.get_total_dist(
            int(dist.sortIndexSecondTrGet()[index]), int(dist.sortIndexSecondTrGet()[index + 1]),
            tr2TotalDist
        )

        packDeliv = dist.timeGet(
            dist.get_dist(
                int(dist.sortIndexSecondTrGet()[index]), int(dist.sortIndexSecondTrGet()[index + 1])
            ),
            startTimeTrSecond
        )
        # Sort pkg status

        dist.sortListSecondTrGet()[index].status = str(packDeliv)
        read_csv_file.get_pkg_db().update(int(dist.sortListSecondTrGet()[index].id), listSecondTrPk)
    except IndexError:
        pass


# Truck No. 3
for pkg in read_csv_file.get_listThirdTrPk():
    pkg.stateDeliv = startTimeTrThird[0]
    listThirdTrPk.append(pkg)

for pkg in listThirdTrPk:
    for addr in dist.get_addrs():
        if pkg.address == addr[2]:
            distTrThird.append(pkg.id)
            pkg.locAdd = addr[0]

dist.fastRouteFind(listThirdTrPk, 3, 0)
tr3TotalDist = 0

# see commen in line 30
for index in range(len(dist.sortIndexThirdTrGet())):
    try:
        tr3TotalDist = dist.get_total_dist(
            int(dist.sortIndexThirdTrGet()[index]), int(dist.sortIndexThirdTrGet()[index + 1]),
            tr3TotalDist
        )

        packDeliv = dist.timeGet(
            dist.get_dist(
                int(dist.sortIndexThirdTrGet()[index]), int(dist.sortIndexThirdTrGet()[index + 1])
            ),
            startTimeTrThird
        )
        # Sort pkg status

        dist.sortListThirdTrGet()[index].status = str(packDeliv)
        read_csv_file.get_pkg_db().update(int(dist.sortListThirdTrGet()[index].id), listThirdTrPk)
    except IndexError:
        pass

# Get total distance <140
def get_total_trks_distance():
    return tr1TotalDist + tr2TotalDist + tr3TotalDist
