from specifications.enums.item_group import ItemGroup
from specifications.item import Item
from specifications.link import Link
from specifications.spec import Spec


class Make(Item):
    item_group = ItemGroup.specs

    antunes = None
    asco = None
    bussmann = None
    cleveland_controls = None
    honeywell = None
    littelfuse = None
    mersen = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, name: str, website: str = None):
        super().__init__()
        self.name = Spec("Name", name)
        self.website = Spec("Website", Link(website))

    def __str__(self):
        return f"{self.name}"


Make.ao_smith_corporation = Make("A.O. Smith Corporation", "https://www.aosmith.com/")
Make.acetank = Make("Acetank", "https://www.acetank.com/")
Make.alcon = Make("Alcon", "https://www.rotork.com/en")
Make.allanson = Make("Allanson", "http://allanson.com/")
Make.american_meter_company = Make("American Meter Company", "https://www.elster-americanmeter.com/en/index")
Make.antunes = Make("Antunes")
Make.apollo = Make("Apollo", "http://www.apollovalves.com/")
Make.asco = Make("Asco", "https://www.emerson.com/en-us/automation/asco")
Make.ashcroft = Make("Ashcroft", "https://www.ashcroft.com/")
Make.aurora_pumps = Make("Aurora Pumps", "https://www.pentair.com/en-us/brands/aurora.html")
Make.badger_meter = Make("Badger Meter", "https://www.badgermeter.com")
Make.baldor = Make("Baldor", "https://www.baldor.com/")
Make.barnes_and_jones = Make("Barnes & Jones", "https://barnesandjones.com/")
Make.bfs_industries = Make("BFS Industries", "https://bfs-ind.com/")
Make.bluffton_motor_works = Make("Bluffton Motor Works", "http://weg-cm.com/")
Make.bryan = Make("Bryan", "https://bryanboilers.com/")
Make.burnham = Make("Burnham", "https://www.burnhamcommercial.com/")
Make.bussmann = Make("Bussmann")
Make.carlon_meter = Make("Carlon Meter", "http://www.carlonmeter.com/")
Make.cascadian = Make("Cascadian", "https://www.cascadianwater.com/")
Make.cash_valve = Make("Cash Valve", "https://cashvalve.com/en-us")
Make.cleaver_brooks = Make("Cleaver Brooks", "https://cleaverbrooks.com/")
Make.cleveland_controls = Make("Cleveland Controls", "https://unicontrolinc.com")
Make.conbu = Make("Combu")
Make.danfoss = Make("Danfoss", "https://www.danfoss.com/en-us/")
Make.dayton = Make("Dayton", "https://daytonwatersystems.com/")
Make.dietz = Make("Dietz")
Make.dongan = Make("Dongan", "https://dongan.com")
Make.ecodyne_industrial = Make("Ecodyne Industrial", "https://ecodyne.com/")
Make.ecowater_systems = Make("Ecowater Systems", "https://www.ecowater.com/")
Make.emerson = Make("Emerson", "https://www.emerson.com/en-us")
Make.equimeter = Make("Equimeter", "https://sensus.com")
Make.fabtek_aero = Make("Fabtek Aero", "https://fabtekaero.com/")
Make.fireye = Make("Fireye", "https://www.fireye.com/")
Make.franklin_electric = Make("Franklin Electric", "https://franklin-electric.com/")
Make.fulflo = Make("Fulflo", "http://www.fulflo.com/")
Make.general_electric = Make("General Electric", "https://www.ge.com/")
Make.gordon_piatt = Make("Gordon Piatt", "https://www.gordonpiatt.com/")
Make.goulds = Make("Goulds", "https://goulds.com/")
Make.grundfos = Make("Grundfos", "https://www.grundfos.com/us")
Make.hoffman = Make("Hoffman")
Make.honeywell = Make("Honeywell", "https://customer.honeywell.com/en-US/Pages/default.aspx")
Make.hurst = Make("Hurst", "https://www.hurstboiler.com/")
Make.itt_general_controls = Make("ITT General Controls", "https://ittcontrols.com")
Make.kewanee = Make("Kewanee", "https://www.oemboilerparts.com/parts-kewanee-boilers.html")
Make.kinetico = Make("Kinetico", "https://www.kinetico.com/")
Make.kunkle = Make("Kunkle", "https://www.emerson.com/en-us/automation/valves-actuators-regulators/kunkle")
Make.leeson = Make("Leeson", "https://www.regalbeloit.com/brands/LEESON/Products")
Make.lowara = Make("Lowara", "https://www.xylem.com/en-uk/brands/lowara/")




Make.littelfuse = Make("Littelfuse")
Make.mersen = Make("Mersen")

# for var in vars(Make):
#     print(var)
