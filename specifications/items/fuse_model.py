from specifications.doc import Doc
from specifications.items.make import Make
from specifications.enums.fuse import FuseClass, FuseSpeed
from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class FuseModel(Item):
    atm_r = None
    ktk_r = None
    klk_r = None
    atm = None
    ktk = None
    klk = None
    klm = None
    dcm = None
    otm = None
    baf = None
    bln = None
    blf = None
    mic = None
    ban = None
    atq_r = None
    fnq_r = None
    kld_r = None
    atq = None
    fnq = None
    kld = None
    trm = None
    fnm = None
    flm = None
    gfn = None
    fna = None
    fla = None
    atd_r = None
    lp_cc = None
    ccmr = None
    s505 = None
    _215 = None
    ag = None
    sc = None
    slc = None
    ggc = None
    agc = None
    _312 = None
    gsc = None
    gmd = None
    _239 = None
    ajt_n = None
    lpj_sp = None
    jtd = None
    ajt = None
    lpj_spi = None
    jtd_id = None
    tr_r = None
    frn_r = None
    flnr = None
    tr_r_id = None
    frn_r_id = None
    flnr_id = None
    ot = None
    non = None
    nln = None
    rf = None
    ren = None
    rln = None
    non_class_h = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: Make, model: str, class_: FuseClass, speed: FuseSpeed = None, vac_rating: int = None,
                 indicating: bool = None, manual: str = None, manual2: str = None,
                 mersen_equivalent=None, bussmann_equivalent=None, littelfuse_equivalent=None,
                 mersen_upgrade=None, bussmann_upgrade=None, littelfuse_upgrade=None):
        super().__init__()
        self.make = make
        self.model = Spec("Model", model)
        self.class_ = Spec("Class", class_)
        self.speed = Spec("Speed", speed)
        self.vac_rating = Spec("VAC Rating", vac_rating, Unit.volt)
        self.indicating = Spec("Indicating", indicating)

        # FuseModels
        self.mersen_equivalent = mersen_equivalent
        self.bussmann_equivalent = bussmann_equivalent
        self.littelfuse_equivalent = littelfuse_equivalent
        self.mersen_upgrade = mersen_upgrade
        self.bussmann_upgrade = bussmann_upgrade
        self.littelfuse_upgrade = littelfuse_upgrade

        # Docs
        self.manual = Spec("Manual", Doc(manual))
        self.manual2 = Spec("Manual2", Doc(manual2))

    @item_property
    def make(self):
        return self._make

    @make.setter
    def make(self, item):
        self._make = Spec("Make", item)

    @item_property
    def mersen_equivalent(self):
        return self._mersen_equivalent

    @mersen_equivalent.setter
    def mersen_equivalent(self, item):
        self._mersen_equivalent = Spec("Mersen Equivalent", item)

    @item_property
    def bussmann_equivalent(self):
        return self._bussmann_equivalent

    @bussmann_equivalent.setter
    def bussmann_equivalent(self, item):
        self._bussmann_equivalent = Spec("Bussmann Equivalent", item)

    @item_property
    def littelfuse_equivalent(self):
        return self._littelfuse_equivalent

    @littelfuse_equivalent.setter
    def littelfuse_equivalent(self, item):
        self._littelfuse_equivalent = Spec("Littelfuse Equivalent", item)

    @item_property
    def mersen_upgrade(self):
        return self._mersen_upgrade

    @mersen_upgrade.setter
    def mersen_upgrade(self, item):
        self._mersen_upgrade = Spec("Mersen Upgrade", item)

    @item_property
    def bussmann_upgrade(self):
        return self._bussmann_upgrade

    @bussmann_upgrade.setter
    def bussmann_upgrade(self, item):
        self._bussmann_upgrade = Spec("Bussmann Upgrade", item)

    @item_property
    def littelfuse_upgrade(self):
        return self._littelfuse_upgrade

    @littelfuse_upgrade.setter
    def littelfuse_upgrade(self, item):
        self._littelfuse_upgrade = Spec("Littelfuse Upgrade", item)

    def __str__(self):
        return f"{self.class_} - {self.model}"


# def generate_cc_fa():
# CC F-A 600VAC
FuseModel.atm_r = FuseModel(Make.mersen, "ATM-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, "CC, ATMR .1-30A, Mersen manual.pdf")
FuseModel.ktk_r = FuseModel(Make.bussmann, "KTK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, "CC, KTKR .1-30A, Bussmann manual.pdf")
FuseModel.klk_r = FuseModel(Make.littelfuse, "KLK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, "CC, KLKR .1-30A, Littelfuse manual.pdf")


FuseModel.atm_r.bussmann_equivalent = FuseModel.ktk_r
FuseModel.atm_r.littelfuse_equivalent = FuseModel.klk_r

FuseModel.ktk_r.mersen_equivalent = FuseModel.atm_r
FuseModel.ktk_r.littelfuse_equivalent = FuseModel.klk_r

FuseModel.klk_r.mersen_equivalent = FuseModel.atm_r
FuseModel.klk_r.bussmann_equivalent = FuseModel.ktk_r


# def generate_midget_fa_600():
# MIDGET 13/32" x 1 1/2" F-A 600VAC
FuseModel.atm = FuseModel(Make.mersen, "ATM", FuseClass.midget, FuseSpeed.fast_acting, 600, False, "MIDGET, ATM .1-50A, Mersen manual.pdf")
FuseModel.ktk = FuseModel(Make.bussmann, "KTK", FuseClass.midget, FuseSpeed.fast_acting, 600, False, "MIDGET, KTK .1-30A, Bussmann manual.pdf")
FuseModel.klk = FuseModel(Make.littelfuse, "KLK", FuseClass.midget, FuseSpeed.fast_acting, 600, False, "MIDGET, KLK .1-30A, Littelfuse manual.pdf")

FuseModel.klm = FuseModel(Make.bussmann, "KLM", FuseClass.midget, FuseSpeed.fast_acting, 600, False, "MIDGET, KLM .1-30A, Bussmann manual.pdf")
FuseModel.dcm = FuseModel(Make.bussmann, "DCM", FuseClass.midget, FuseSpeed.fast_acting, 600, False, "MIDGET, DCM .1-30A, Bussmann manual.pdf")


FuseModel.atm.bussmann_equivalent = FuseModel.ktk
FuseModel.atm.littelfuse_equivalent = FuseModel.klk
FuseModel.atm.mersen_upgrade = FuseModel.atm_r
FuseModel.atm.bussmann_upgrade = FuseModel.ktk_r
FuseModel.atm.littelfuse_upgrade = FuseModel.klk_r

FuseModel.ktk.mersen_equivalent = FuseModel.atm
FuseModel.ktk.littelfuse_equivalent = FuseModel.klk
FuseModel.ktk.mersen_upgrade = FuseModel.atm_r
FuseModel.ktk.bussmann_upgrade = FuseModel.ktk_r
FuseModel.ktk.littelfuse_upgrade = FuseModel.klk_r

FuseModel.klk.mersen_equivalent = FuseModel.atm
FuseModel.klk.bussmann_equivalent = FuseModel.ktk
FuseModel.klk.mersen_upgrade = FuseModel.atm_r
FuseModel.klk.bussmann_upgrade = FuseModel.ktk_r
FuseModel.klk.littelfuse_upgrade = FuseModel.klk_r


FuseModel.klm.mersen_upgrade = FuseModel.atm_r
FuseModel.klm.bussmann_upgrade = FuseModel.ktk_r
FuseModel.klm.littelfuse_upgrade = FuseModel.klk_r

FuseModel.dcm.bussmann_upgrade = FuseModel.klm


# def generate_midget_fa_250():
# MIDGET 13/32" x 1 1/2" F-A 250VAC
FuseModel.otm = FuseModel(Make.mersen, "OTM", FuseClass.midget, FuseSpeed.fast_acting, 250, False, "MIDGET, OTM 1-30A, Mersen manual.pdf")
FuseModel.baf = FuseModel(Make.bussmann, "BAF", FuseClass.midget, FuseSpeed.fast_acting, 250, False, "MIDGET, BAF .25-30A, Bussmann manual.pdf")
FuseModel.bln = FuseModel(Make.littelfuse, "BLN", FuseClass.midget, FuseSpeed.fast_acting, 250, False, "MIDGET, BLN 1-30, Littelfuse manual.pdf")

FuseModel.blf = FuseModel(Make.littelfuse, "BLF", FuseClass.midget, FuseSpeed.fast_acting, 250, False, "MIDGET, BLF .5-30A, Littelfuse manual.pdf")
FuseModel.mic = FuseModel(Make.bussmann, "MIC", FuseClass.midget, FuseSpeed.fast_acting, 250, True, "MIDGET, MIC 1-30A, Bussmann manual.pdf")
FuseModel.ban = FuseModel(Make.bussmann, "BAN", FuseClass.midget, FuseSpeed.fast_acting, 250, False, "MIDGET, BAN 1-30A, Bussmann manual.pdf")


FuseModel.otm.bussmann_equivalent = FuseModel.baf
FuseModel.otm.littelfuse_equivalent = FuseModel.bln
FuseModel.otm.mersen_upgrade = FuseModel.atm_r
FuseModel.otm.bussmann_upgrade = FuseModel.ktk_r
FuseModel.otm.littelfuse_upgrade = FuseModel.klk_r

FuseModel.baf.mersen_equivalent = FuseModel.otm
FuseModel.baf.littelfuse_equivalent = FuseModel.bln
FuseModel.baf.mersen_upgrade = FuseModel.atm_r
FuseModel.baf.bussmann_upgrade = FuseModel.ktk_r
FuseModel.baf.littelfuse_upgrade = FuseModel.klk_r

FuseModel.bln.mersen_equivalent = FuseModel.otm
FuseModel.bln.bussmann_equivalent = FuseModel.baf
FuseModel.bln.mersen_upgrade = FuseModel.atm_r
FuseModel.bln.bussmann_upgrade = FuseModel.ktk_r
FuseModel.bln.littelfuse_upgrade = FuseModel.klk_r


FuseModel.blf.mersen_upgrade = FuseModel.otm
FuseModel.blf.bussmann_upgrade = FuseModel.baf
FuseModel.blf.littelfuse_upgrade = FuseModel.bln

FuseModel.mic.mersen_upgrade = FuseModel.otm
FuseModel.mic.bussmann_upgrade = FuseModel.baf
FuseModel.mic.littelfuse_upgrade = FuseModel.bln

FuseModel.ban.mersen_upgrade = FuseModel.otm
FuseModel.ban.bussmann_upgrade = FuseModel.baf
FuseModel.ban.littelfuse_upgrade = FuseModel.bln


# def generate_cc_td_transformers():
# CC T-D for Transformers 600VAC
FuseModel.atq_r = FuseModel(Make.mersen, "ATQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, ATQR .1-30A, Mersen manual.pdf")
FuseModel.fnq_r = FuseModel(Make.bussmann, "FNQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, FNQR .25-30A, Bussmann manual.pdf")
FuseModel.kld_r = FuseModel(Make.littelfuse, "KLD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, KLDR .1-30A, Littelfuse manual.pdf")


FuseModel.atq_r.bussmann_equivalent = FuseModel.fnq_r
FuseModel.atq_r.littelfuse_equivalent = FuseModel.kld_r

FuseModel.fnq_r.mersen_equivalent = FuseModel.atq_r
FuseModel.fnq_r.littelfuse_equivalent = FuseModel.kld_r

FuseModel.kld_r.mersen_equivalent = FuseModel.atq_r
FuseModel.kld_r.bussmann_equivalent = FuseModel.fnq_r



# def generate_midget_td():
# MIDGET 13/32" x 1 1/2" T-D ___VAC
FuseModel.atq = FuseModel(Make.mersen, "ATQ", FuseClass.midget, FuseSpeed.time_delay, 500, False, "MIDGET, ATQ .1-30A, Mersen manual.pdf")
FuseModel.fnq = FuseModel(Make.bussmann, "FNQ", FuseClass.midget, FuseSpeed.time_delay, 500, False, "MIDGET, FNQ .1-30A, Bussmann manual.pdf")
FuseModel.kld = FuseModel(Make.littelfuse, "KLD", FuseClass.midget, FuseSpeed.time_delay, 500, False)

FuseModel.trm = FuseModel(Make.mersen, "TRM", FuseClass.midget, FuseSpeed.time_delay, 250, False, "MIDGET, TRM .1-30A, Mersen manual.pdf")
FuseModel.fnm = FuseModel(Make.bussmann, "FNM", FuseClass.midget, FuseSpeed.time_delay, 250, False, "MIDGET, FNM .1-30A, Bussmann manual.pdf")
FuseModel.flm = FuseModel(Make.littelfuse, "FLM", FuseClass.midget, FuseSpeed.time_delay, 250, False, "MIDGET, FLM .1-30A, Littelfuse manual.pdf")

FuseModel.gfn = FuseModel(Make.mersen, "GFN", FuseClass.midget, FuseSpeed.time_delay, 250, True, "MIDGET, GFN .1-30A, Mersen manual.pdf")
FuseModel.fna = FuseModel(Make.bussmann, "FNA", FuseClass.midget, FuseSpeed.time_delay, 250, True, "MIDGET, FNA .1-30A, Bussmann manual.pdf")
FuseModel.fla = FuseModel(Make.littelfuse, "FLA", FuseClass.midget, FuseSpeed.time_delay, 250, True)


FuseModel.atq.bussmann_equivalent = FuseModel.fnq
FuseModel.atq.littelfuse_equivalent = FuseModel.kld
FuseModel.atq.mersen_upgrade = FuseModel.atq_r
FuseModel.atq.bussmann_upgrade = FuseModel.fnq_r
FuseModel.atq.littelfuse_upgrade = FuseModel.kld_r

FuseModel.fnq.mersen_equivalent = FuseModel.atq
FuseModel.fnq.littelfuse_equivalent = FuseModel.kld
FuseModel.fnq.mersen_upgrade = FuseModel.atq_r
FuseModel.fnq.bussmann_upgrade = FuseModel.fnq_r
FuseModel.fnq.littelfuse_upgrade = FuseModel.kld_r

FuseModel.kld.mersen_equivalent = FuseModel.atq
FuseModel.kld.bussmann_equivalent = FuseModel.fnq
FuseModel.kld.mersen_upgrade = FuseModel.atq_r
FuseModel.kld.bussmann_upgrade = FuseModel.fnq_r
FuseModel.kld.littelfuse_upgrade = FuseModel.kld_r


FuseModel.trm.bussmann_equivalent = FuseModel.fnm
FuseModel.trm.littelfuse_equivalent = FuseModel.flm
FuseModel.trm.mersen_upgrade = FuseModel.atq
FuseModel.trm.bussmann_upgrade = FuseModel.fnq
FuseModel.trm.littelfuse_upgrade = FuseModel.kld

FuseModel.fnm.mersen_equivalent = FuseModel.trm
FuseModel.fnm.littelfuse_equivalent = FuseModel.flm
FuseModel.fnm.mersen_upgrade = FuseModel.atq
FuseModel.fnm.bussmann_upgrade = FuseModel.fnq
FuseModel.fnm.littelfuse_upgrade = FuseModel.kld

FuseModel.flm.mersen_equivalent = FuseModel.trm
FuseModel.flm.bussmann_equivalent = FuseModel.fnm
FuseModel.flm.mersen_upgrade = FuseModel.atq
FuseModel.flm.bussmann_upgrade = FuseModel.fnq
FuseModel.flm.littelfuse_upgrade = FuseModel.kld


FuseModel.gfn.bussmann_equivalent = FuseModel.fna
FuseModel.gfn.littelfuse_equivalent = FuseModel.fla
FuseModel.gfn.mersen_upgrade = FuseModel.atq
FuseModel.gfn.bussmann_upgrade = FuseModel.fnq
FuseModel.gfn.littelfuse_upgrade = FuseModel.kld

FuseModel.fna.mersen_equivalent = FuseModel.gfn
FuseModel.fna.littelfuse_equivalent = FuseModel.fla
FuseModel.fna.mersen_upgrade = FuseModel.atq
FuseModel.fna.bussmann_upgrade = FuseModel.fnq
FuseModel.fna.littelfuse_upgrade = FuseModel.kld

FuseModel.fla.mersen_equivalent = FuseModel.gfn
FuseModel.fla.bussmann_equivalent = FuseModel.fna
FuseModel.fla.mersen_upgrade = FuseModel.atq
FuseModel.fla.bussmann_upgrade = FuseModel.fnq
FuseModel.fla.littelfuse_upgrade = FuseModel.kld


# def generate_cc_td_motors():
# CC T-D for Motors 600VAC
FuseModel.atd_r = FuseModel(Make.mersen, "ATD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, ATDR .25-30A, Mersen manual.pdf")
FuseModel.lp_cc = FuseModel(Make.bussmann, "LP-CC", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, LPCC .25-30A, Bussmann manual.pdf")
FuseModel.ccmr = FuseModel(Make.littelfuse, "CCMR", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC CD, CCMR .2-60, Littelfuse manual.pdf")


FuseModel.atd_r.bussmann_equivalent = FuseModel.lp_cc
FuseModel.atd_r.littelfuse_equivalent = FuseModel.ccmr

FuseModel.lp_cc.mersen_equivalent = FuseModel.atd_r
FuseModel.lp_cc.littelfuse_equivalent = FuseModel.ccmr

FuseModel.ccmr.mersen_equivalent = FuseModel.atd_r
FuseModel.ccmr.bussmann_equivalent = FuseModel.lp_cc


# def generate_ceramic_td():
# Ceramic T-D 250VAC
FuseModel.s505 = FuseModel(Make.bussmann, "S505", FuseClass.ceramic_5mmx20mm, FuseSpeed.time_delay, 250, True, "Ceramic, S505 .5-12A, Bussmann manual.pdf")
FuseModel._215 = FuseModel(Make.littelfuse, "215", FuseClass.ceramic_5mmx20mm, FuseSpeed.time_delay, 250, True, "Ceramic, 215 .125-20A, Littelfuse manual.pdf")


FuseModel.s505.littelfuse_equivalent = FuseModel._215
FuseModel._215.bussmann_equivalent = FuseModel.s505


# def generate_g():
# G Speed & VAC varies by amp rating
FuseModel.ag = FuseModel(Make.mersen, "AG", FuseClass.g, indicating=False, manual="G, AG .5-60A, Mersen manual.pdf")
FuseModel.sc = FuseModel(Make.bussmann, "SC", FuseClass.g, indicating=False, manual="G, SC .5-60A, Bussmann manual.pdf")
FuseModel.slc = FuseModel(Make.littelfuse, "SLC", FuseClass.g, indicating=False, manual="G, SLC .5-60A, Littelfuse manual.pdf")


FuseModel.ag.bussmann_equivalent = FuseModel.sc
FuseModel.ag.littelfuse_equivalent = FuseModel.slc

FuseModel.sc.mersen_equivalent = FuseModel.ag
FuseModel.sc.littelfuse_equivalent = FuseModel.slc

FuseModel.slc.mersen_equivalent = FuseModel.ag
FuseModel.slc.bussmann_equivalent = FuseModel.sc


# def generate_glass_fa():
# Glass 1/4" x 1 1/4" F-A, VAC varies by amp rating
FuseModel.ggc = FuseModel(Make.mersen, "GGC", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual="Glass, GGC .1-30A, GGC-V .1-30, GGM .0625-15A, GGM-V .0625-15A, Mersen manual.pdf")
FuseModel.agc = FuseModel(Make.bussmann, "AGC", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual="Glass, AGC .1-40A, AGC-V .1-40A, Bussmann manual.pdf")
FuseModel._312 = FuseModel(Make.littelfuse, "312", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual="Glass, 312 .0625-35A, 318 .0625-35A, Littelfuse manual.pdf")


FuseModel.ggc.bussmann_equivalent = FuseModel.agc
FuseModel.ggc.littelfuse_equivalent = FuseModel._312

FuseModel.agc.mersen_equivalent = FuseModel.ggc
FuseModel.agc.littelfuse_equivalent = FuseModel._312

FuseModel._312.mersen_equivalent = FuseModel.ggc
FuseModel._312.bussmann_equivalent = FuseModel.agc


# def generate_glass_td():
# Glass 5mm x 20mm T-D VAC varies by amp rating
FuseModel.gsc = FuseModel(Make.mersen, "GSC", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual="Glass, Ceramic, GGA .1-5A, GGA-V .1-5A, GSC .1-10A, GSC-V .1-10A, Mersen manual.pdf")
FuseModel.gmd = FuseModel(Make.bussmann, "GMD", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual="Glass, GMA .063-15A, GMA-V .063-15A, Bussmann manual.pdf")
FuseModel._239 = FuseModel(Make.littelfuse, "239", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual="Glass, 239 .08-7A, 239-XE .08-7A, Littelfuse manual.pdf")


FuseModel.gsc.bussmann_equivalent = FuseModel.gmd
FuseModel.gsc.littelfuse_equivalent = FuseModel._239

FuseModel.gmd.mersen_equivalent = FuseModel.gsc
FuseModel.gmd.littelfuse_equivalent = FuseModel._239

FuseModel._239.mersen_equivalent = FuseModel.gsc
FuseModel._239.bussmann_equivalent = FuseModel.gmd


# def generate_j():
# J T-D 600VAC
FuseModel.ajt_n = FuseModel(Make.mersen, "AJT-N", FuseClass.j, FuseSpeed.time_delay, 600, False, "J, AJTN 1-600A, AJT 8-600A, Mersen manual.pdf")
FuseModel.lpj_sp = FuseModel(Make.bussmann, "LPJ-SP", FuseClass.j, FuseSpeed.time_delay, 600, False, "J, LPJ-SP 1-60A, LPJ-SPI 6-60A, Bussmann manual.pdf")
FuseModel.jtd = FuseModel(Make.littelfuse, "JTD", FuseClass.j, FuseSpeed.time_delay, 600, False, "J, JTD .8-600A, JTD-ID .8-600A, Littelfuse manual.pdf")

FuseModel.ajt = FuseModel(Make.mersen, "AJT", FuseClass.j, FuseSpeed.time_delay, 600, True, "J, AJTN 1-600A, AJT 8-600A, Mersen manual.pdf")
FuseModel.lpj_spi = FuseModel(Make.bussmann, "LPJ-SPI", FuseClass.j, FuseSpeed.time_delay, 600, True, "J, LPJ-SP 1-60A, LPJ-SPI 6-60A, Bussmann manual.pdf")
FuseModel.jtd_id = FuseModel(Make.littelfuse, "JTD-ID", FuseClass.j, FuseSpeed.time_delay, 600, True, "J, JTD .8-600A, JTD-ID .8-600A, Littelfuse manual.pdf")


FuseModel.ajt_n.bussmann_equivalent = FuseModel.lpj_sp
FuseModel.ajt_n.littelfuse_equivalent = FuseModel.jtd

FuseModel.lpj_sp.mersen_equivalent = FuseModel.ajt_n
FuseModel.lpj_sp.littelfuse_equivalent = FuseModel.jtd

FuseModel.jtd.mersen_equivalent = FuseModel.ajt_n
FuseModel.jtd.bussmann_equivalent = FuseModel.lpj_sp


FuseModel.ajt.bussmann_equivalent = FuseModel.lpj_spi
FuseModel.ajt.littelfuse_equivalent = FuseModel.jtd_id
FuseModel.ajt.mersen_upgrade = FuseModel.ajt_n
FuseModel.ajt.bussmann_upgrade = FuseModel.lpj_sp
FuseModel.ajt.littelfuse_upgrade = FuseModel.jtd

FuseModel.lpj_spi.mersen_equivalent = FuseModel.ajt
FuseModel.lpj_spi.littelfuse_equivalent = FuseModel.jtd_id
FuseModel.lpj_spi.mersen_upgrade = FuseModel.ajt_n
FuseModel.lpj_spi.bussmann_upgrade = FuseModel.lpj_sp
FuseModel.lpj_spi.littelfuse_upgrade = FuseModel.jtd

FuseModel.jtd_id.mersen_equivalent = FuseModel.ajt
FuseModel.jtd_id.bussmann_equivalent = FuseModel.lpj_spi
FuseModel.jtd_id.mersen_upgrade = FuseModel.ajt_n
FuseModel.jtd_id.bussmann_upgrade = FuseModel.lpj_sp
FuseModel.jtd_id.littelfuse_upgrade = FuseModel.jtd


# def generate_rk5():
# RK5 T-D 250VAC
FuseModel.tr_r = FuseModel(Make.mersen, "TR-R", FuseClass.rk5, FuseSpeed.time_delay, 250, False, "RK5, TR-R .1-600A, TR-R-ID 8-600A, TRS-R .1-600A, TRS-R-ID 8-600A, Mersen manual.pdf")
FuseModel.frn_r = FuseModel(Make.bussmann, "FRN-R", FuseClass.rk5, FuseSpeed.time_delay, 250, False, "RK5, FRN-R .1-60A, FRN-R-ID 8-60A, Bussmann manual.pdf", "RK5, FRN-R 70-600A, Bussmann manual.pdf")
FuseModel.flnr = FuseModel(Make.littelfuse, "FLNR", FuseClass.rk5, FuseSpeed.time_delay, 250, False, "RK5, FLNR .1-600A, FLNR-ID 35-600A, FLSR .1-600A, FLSR-ID .1-600, Littelfuse manual.pdf")

FuseModel.tr_r_id = FuseModel(Make.mersen, "TR-R-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, "RK5, TR-R .1-600A, TR-R-ID 8-600A, TRS-R .1-600A, TRS-R-ID 8-600A, Mersen manual.pdf")
FuseModel.frn_r_id = FuseModel(Make.bussmann, "FRN-R-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, "RK5, FRN-R .1-60A, FRN-R-ID 8-60A, Bussmann manual.pdf", "RK5, FRN-R 70-600A, Bussmann manual.pdf")
FuseModel.flnr_id = FuseModel(Make.littelfuse, "FLNR-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, "RK5, FLNR .1-600A, FLNR-ID 35-600A, FLSR .1-600A, FLSR-ID .1-600, Littelfuse manual.pdf")


FuseModel.tr_r.bussmann_equivalent = FuseModel.frn_r
FuseModel.tr_r.littelfuse_equivalent = FuseModel.flnr

FuseModel.frn_r.mersen_equivalent = FuseModel.tr_r
FuseModel.frn_r.littelfuse_equivalent = FuseModel.flnr

FuseModel.flnr.mersen_equivalent = FuseModel.tr_r
FuseModel.flnr.bussmann_equivalent = FuseModel.frn_r


FuseModel.tr_r_id.bussmann_equivalent = FuseModel.frn_r_id
FuseModel.tr_r_id.littelfuse_equivalent = FuseModel.flnr_id
FuseModel.tr_r_id.mersen_upgrade = FuseModel.tr_r
FuseModel.tr_r_id.bussmann_upgrade = FuseModel.frn_r
FuseModel.tr_r_id.littelfuse_upgrade = FuseModel.flnr

FuseModel.frn_r_id.mersen_equivalent = FuseModel.tr_r_id
FuseModel.frn_r_id.littelfuse_equivalent = FuseModel.flnr_id
FuseModel.frn_r_id.mersen_upgrade = FuseModel.tr_r
FuseModel.frn_r_id.bussmann_upgrade = FuseModel.frn_r
FuseModel.frn_r_id.littelfuse_upgrade = FuseModel.flnr

FuseModel.flnr_id.mersen_equivalent = FuseModel.tr_r_id
FuseModel.flnr_id.bussmann_equivalent = FuseModel.frn_r_id
FuseModel.flnr_id.mersen_upgrade = FuseModel.tr_r
FuseModel.flnr_id.bussmann_upgrade = FuseModel.frn_r
FuseModel.flnr_id.littelfuse_upgrade = FuseModel.flnr


# def generate_k5():
# K5 F-A 250VAC
FuseModel.ot = FuseModel(Make.mersen, "OT", FuseClass.k5, FuseSpeed.fast_acting, 250, False, "K5, OT 1-600A, OTN 15-60A, OTS 1-600A, Mersen manual.pdf")
FuseModel.non = FuseModel(Make.bussmann, "NON", FuseClass.k5, FuseSpeed.fast_acting, 250, False, "K5 H, NON .125-600A, NOS 1-600A, Bussmann manual.pdf")
FuseModel.nln = FuseModel(Make.littelfuse, "NLN", FuseClass.k5, FuseSpeed.fast_acting, 250, False, "K5, NLN 1-600A, NLS 1-600A, Littelfuse manual.pdf")


FuseModel.ot.bussmann_equivalent = FuseModel.non
FuseModel.ot.littelfuse_equivalent = FuseModel.nln
FuseModel.ot.mersen_upgrade = FuseModel.tr_r
FuseModel.ot.bussmann_upgrade = FuseModel.frn_r
FuseModel.ot.littelfuse_upgrade = FuseModel.flnr

FuseModel.non.mersen_equivalent = FuseModel.ot
FuseModel.non.littelfuse_equivalent = FuseModel.nln
FuseModel.non.mersen_upgrade = FuseModel.tr_r
FuseModel.non.bussmann_upgrade = FuseModel.frn_r
FuseModel.non.littelfuse_upgrade = FuseModel.flnr

FuseModel.nln.mersen_equivalent = FuseModel.ot
FuseModel.nln.bussmann_equivalent = FuseModel.non
FuseModel.nln.mersen_upgrade = FuseModel.tr_r
FuseModel.nln.bussmann_upgrade = FuseModel.frn_r
FuseModel.nln.littelfuse_upgrade = FuseModel.flnr


# def generate_h():
# H F-A 250VAC
FuseModel.rf = FuseModel(Make.mersen, "RF", FuseClass.h, FuseSpeed.fast_acting, 250, False, "H, RF 1-600A, RFS 1-600A, Mersen manual.pdf")
FuseModel.ren = FuseModel(Make.bussmann, "REN", FuseClass.h, FuseSpeed.fast_acting, 250, False, "H, REN 1-60A, RES 1-60A, Bussmann manual.pdf")
FuseModel.rln = FuseModel(Make.littelfuse, "RLN", FuseClass.h, FuseSpeed.fast_acting, 250, False, "H, RLN 1-600A, RLS 1-600A, Littelfuse manual.pdf")

FuseModel.non_class_h = FuseModel(Make.bussmann, "NON", FuseClass.h, FuseSpeed.fast_acting, 250, False, "K5 H, NON .125-600A, NOS 1-600A, Bussmann manual.pdf")


FuseModel.rf.bussmann_equivalent = FuseModel.ren
FuseModel.rf.littelfuse_equivalent = FuseModel.rln
FuseModel.rf.mersen_upgrade = FuseModel.tr_r
FuseModel.rf.bussmann_upgrade = FuseModel.frn_r
FuseModel.rf.littelfuse_upgrade = FuseModel.flnr

FuseModel.ren.mersen_equivalent = FuseModel.rf
FuseModel.ren.littelfuse_equivalent = FuseModel.rln
FuseModel.ren.mersen_upgrade = FuseModel.tr_r
FuseModel.ren.bussmann_upgrade = FuseModel.frn_r
FuseModel.ren.littelfuse_upgrade = FuseModel.flnr

FuseModel.rln.mersen_equivalent = FuseModel.rf
FuseModel.rln.bussmann_equivalent = FuseModel.ren
FuseModel.rln.mersen_upgrade = FuseModel.tr_r
FuseModel.rln.bussmann_upgrade = FuseModel.frn_r
FuseModel.rln.littelfuse_upgrade = FuseModel.flnr


FuseModel.non_class_h.mersen_upgrade = FuseModel.tr_r
FuseModel.non_class_h.bussmann_upgrade = FuseModel.frn_r
FuseModel.non_class_h.littelfuse_upgrade = FuseModel.flnr
