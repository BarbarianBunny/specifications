from specifications.enums.item_group import ItemGroup
from specifications.item import Item
from specifications.link import Link
from specifications.spec import Spec


class Make(Item):
    item_group = ItemGroup.specs

    ao_smith_corporation = None
    acetank = None
    alcon = None
    allanson = None
    american_meter_company = None
    antunes = None
    apollo = None
    asco = None
    ashcroft = None
    aurora_pumps = None
    badger_meter = None
    baldor = None
    barnes_and_jones = None
    bfs_industries = None
    bluffton_motor_works = None
    bryan = None
    burnham = None
    bussmann = None
    carlon_meter = None
    cascadian = None
    cash_valve = None
    cleaver_brooks = None
    cleveland_controls = None
    combu = None
    danfoss = None
    dayton = None
    dietz = None
    dongan = None
    ecodyne_industrial = None
    ecowater_systems = None
    emerson = None
    equimeter = None
    extech = None
    fabtek_aero = None
    fireye = None
    franklin_electric = None
    fulflo = None
    general_electric = None
    gordon_piatt = None
    goulds = None
    grundfos = None
    hoffman = None
    honeywell = None
    hurst = None
    itt_general_controls = None
    kewanee = None
    kinetico = None
    kunkle = None
    leeson = None
    littelfuse = None
    lowara = None
    marathon = None
    marlo = None
    master_meter = None
    maxitrol = None
    mcdonnell_miller = None
    mercoid = None
    mersen = None
    neptune = None
    pentair = None
    power_flame = None
    pulsafeeder = None
    sea_metrics = None
    siemens = None
    sensus = None
    skidmore = None
    square_d = None
    sterlco = None
    suntec = None
    topog_e = None
    tuthill = None
    united_electric_controls = None
    us_motors = None
    walchem = None
    warrick_controls = None
    watts = None
    webster = None
    weg = None
    western_water_products = None

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
Make.combu = Make("Combu")
Make.danfoss = Make("Danfoss", "https://www.danfoss.com/en-us/")
Make.dayton = Make("Dayton", "https://daytonwatersystems.com/")
Make.dietz = Make("Dietz")
Make.dongan = Make("Dongan", "https://dongan.com")
Make.ecodyne_industrial = Make("Ecodyne Industrial", "https://ecodyne.com/")
Make.ecowater_systems = Make("Ecowater Systems", "https://www.ecowater.com/")
Make.emerson = Make("Emerson", "https://www.emerson.com/en-us")
Make.equimeter = Make("Equimeter", "https://sensus.com")
Make.extech = Make("Extech", "https://extech.com/")
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
Make.littelfuse = Make("Littelfuse", "https://m.littelfuse.com/")
Make.lowara = Make("Lowara", "https://www.xylem.com/en-uk/brands/lowara/")
Make.marathon = Make("Marathon", "https://www.regalbeloit.com/brands/Marathon-Motors")
Make.marlo = Make("Marlo", "https://www.marlo-inc.com/")
Make.master_meter = Make("Master Meter", "https://www.mastermeter.com/")
Make.maxitrol = Make("Maxitrol", "https://www.maxitrol.com/")
Make.mcdonnell_miller = Make("McDonnell & Miller", "https://mcdonnellmiller.com/")
Make.mercoid = Make("Mercoid", "https://www.dwyer-inst.com/division/mercoid")
Make.mersen = Make("Mersen", "https://www.mersen.us/")
Make.neptune = Make("Neptune", "https://www.neptunetg.com")
Make.pentair = Make("Pentair", "https://www.pentair.com/")
Make.power_flame = Make("Power Flame", "https://www.powerflame.com/")
Make.pulsafeeder = Make("Pulsafeeder", "https://www.pulsa.com/")
Make.sea_metrics = Make("SeaMetrics", "https://www.seametrics.com/")
Make.siemens = Make("Siemens", "https://www.siemens.com/global/en.html")
Make.sensus = Make("Sensus", "https://sensus.com")
Make.skidmore = Make("Skidmore", "http://skidmorepump.com/")
Make.square_d = Make("Square D", "https://www.se.com/us/en/brands/squared/products-and-services/")
Make.sterlco = Make("Sterlco", "https://www.sterlco.com")
Make.suntec = Make("Suntec", "http://www.suntec.fr/en/")
Make.topog_e = Make("Topog-E", "http://www.topog-e.com/")
Make.tuthill = Make("Tuthill", "https://www.tuthill.com/")
Make.united_electric_controls = Make("United Electric Controls", "https://www.ueonline.com/")
Make.us_motors = Make("US Motors", "https://usmotor.com")
Make.walchem = Make("Walchem", "https://www.walchem.com")
Make.warrick_controls = Make("Warrick Controls", "https://www.gemssensors.com/product/warrick/conductivity-liquid-level-controls")
Make.watts = Make("Watts", "https://www.watts.com/")
Make.webster = Make("Webster", "https://www.webstercombustion.com/")
Make.weg = Make("WEG", "https://www.weg.net/institutional/US/en/")
Make.western_water_products = Make("Western Water Products")





# for var in vars(Make):
#     print(var)
