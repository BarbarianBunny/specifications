from specifications.doc import Doc
from specifications.items.make import Make
from specifications.enums.fuse import FuseClass, FuseSpeed
from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.spec import Spec
from specifications.support_modules.item_property import item_property


class Fuse(Item):
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
    flq = None
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
Fuse.atm_r = Fuse(Make.mersen, "ATM-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, "CC, ATMR .1-30A, Mersen manual.pdf")
Fuse.ktk_r = Fuse(Make.bussmann, "KTK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, "CC, KTKR .1-30A, Bussmann manual.pdf")
Fuse.klk_r = Fuse(Make.littelfuse, "KLK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, "CC, KLKR .1-30A, Littelfuse manual.pdf")


Fuse.atm_r.bussmann_equivalent = Fuse.ktk_r
Fuse.atm_r.littelfuse_equivalent = Fuse.klk_r

Fuse.ktk_r.mersen_equivalent = Fuse.atm_r
Fuse.ktk_r.littelfuse_equivalent = Fuse.klk_r

Fuse.klk_r.mersen_equivalent = Fuse.atm_r
Fuse.klk_r.bussmann_equivalent = Fuse.ktk_r


# def generate_midget_fa_600():
# MIDGET 13/32" x 1 1/2" F-A 600VAC
Fuse.atm = Fuse(Make.mersen, "ATM", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 600, False, "MIDGET, ATM .1-50A, Mersen manual.pdf")
Fuse.ktk = Fuse(Make.bussmann, "KTK", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 600, False, "MIDGET, KTK .1-30A, Bussmann manual.pdf")
Fuse.klk = Fuse(Make.littelfuse, "KLK", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 600, False, "MIDGET, KLK .1-30A, Littelfuse manual.pdf")

Fuse.klm = Fuse(Make.bussmann, "KLM", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 600, False, "MIDGET, KLM .1-30A, Bussmann manual.pdf")
Fuse.dcm = Fuse(Make.bussmann, "DCM", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 600, False, "MIDGET, DCM .1-30A, Bussmann manual.pdf")


Fuse.atm.bussmann_equivalent = Fuse.ktk
Fuse.atm.littelfuse_equivalent = Fuse.klk
Fuse.atm.mersen_upgrade = Fuse.atm_r
Fuse.atm.bussmann_upgrade = Fuse.ktk_r
Fuse.atm.littelfuse_upgrade = Fuse.klk_r

Fuse.ktk.mersen_equivalent = Fuse.atm
Fuse.ktk.littelfuse_equivalent = Fuse.klk
Fuse.ktk.mersen_upgrade = Fuse.atm_r
Fuse.ktk.bussmann_upgrade = Fuse.ktk_r
Fuse.ktk.littelfuse_upgrade = Fuse.klk_r

Fuse.klk.mersen_equivalent = Fuse.atm
Fuse.klk.bussmann_equivalent = Fuse.ktk
Fuse.klk.mersen_upgrade = Fuse.atm_r
Fuse.klk.bussmann_upgrade = Fuse.ktk_r
Fuse.klk.littelfuse_upgrade = Fuse.klk_r


Fuse.klm.mersen_upgrade = Fuse.atm_r
Fuse.klm.bussmann_upgrade = Fuse.ktk_r
Fuse.klm.littelfuse_upgrade = Fuse.klk_r

Fuse.dcm.bussmann_upgrade = Fuse.klm


# def generate_midget_fa_250():
# MIDGET 13/32" x 1 1/2" F-A 250VAC
Fuse.otm = Fuse(Make.mersen, "OTM", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 250, False, "MIDGET, OTM 1-30A, Mersen manual.pdf")
Fuse.baf = Fuse(Make.bussmann, "BAF", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 250, False, "MIDGET, BAF .25-30A, Bussmann manual.pdf")
Fuse.bln = Fuse(Make.littelfuse, "BLN", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 250, False, "MIDGET, BLN 1-30, Littelfuse manual.pdf")

Fuse.blf = Fuse(Make.littelfuse, "BLF", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 250, False, "MIDGET, BLF .5-30A, Littelfuse manual.pdf")
Fuse.mic = Fuse(Make.bussmann, "MIC", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 250, True, "MIDGET, MIC 1-30A, Bussmann manual.pdf")
Fuse.ban = Fuse(Make.bussmann, "BAN", FuseClass.midget_1_1_2, FuseSpeed.fast_acting, 250, False, "MIDGET, BAN 1-30A, Bussmann manual.pdf")


Fuse.otm.bussmann_equivalent = Fuse.baf
Fuse.otm.littelfuse_equivalent = Fuse.bln
Fuse.otm.mersen_upgrade = Fuse.atm_r
Fuse.otm.bussmann_upgrade = Fuse.ktk_r
Fuse.otm.littelfuse_upgrade = Fuse.klk_r

Fuse.baf.mersen_equivalent = Fuse.otm
Fuse.baf.littelfuse_equivalent = Fuse.bln
Fuse.baf.mersen_upgrade = Fuse.atm_r
Fuse.baf.bussmann_upgrade = Fuse.ktk_r
Fuse.baf.littelfuse_upgrade = Fuse.klk_r

Fuse.bln.mersen_equivalent = Fuse.otm
Fuse.bln.bussmann_equivalent = Fuse.baf
Fuse.bln.mersen_upgrade = Fuse.atm_r
Fuse.bln.bussmann_upgrade = Fuse.ktk_r
Fuse.bln.littelfuse_upgrade = Fuse.klk_r


Fuse.blf.mersen_upgrade = Fuse.otm
Fuse.blf.bussmann_upgrade = Fuse.baf
Fuse.blf.littelfuse_upgrade = Fuse.bln

Fuse.mic.mersen_upgrade = Fuse.otm
Fuse.mic.bussmann_upgrade = Fuse.baf
Fuse.mic.littelfuse_upgrade = Fuse.bln

Fuse.ban.mersen_upgrade = Fuse.otm
Fuse.ban.bussmann_upgrade = Fuse.baf
Fuse.ban.littelfuse_upgrade = Fuse.bln


# def generate_cc_td_transformers():
# CC T-D for Transformers 600VAC
Fuse.atq_r = Fuse(Make.mersen, "ATQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, ATQR .1-30A, Mersen manual.pdf")
Fuse.fnq_r = Fuse(Make.bussmann, "FNQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, FNQR .25-30A, Bussmann manual.pdf")
Fuse.kld_r = Fuse(Make.littelfuse, "KLD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, KLDR .1-30A, Littelfuse manual.pdf")


Fuse.atq_r.bussmann_equivalent = Fuse.fnq_r
Fuse.atq_r.littelfuse_equivalent = Fuse.kld_r

Fuse.fnq_r.mersen_equivalent = Fuse.atq_r
Fuse.fnq_r.littelfuse_equivalent = Fuse.kld_r

Fuse.kld_r.mersen_equivalent = Fuse.atq_r
Fuse.kld_r.bussmann_equivalent = Fuse.fnq_r



# def generate_midget_td():
# MIDGET 13/32" x 1 1/2" T-D ___VAC
Fuse.atq = Fuse(Make.mersen, "ATQ", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 500, False, "MIDGET, ATQ .1-30A, Mersen manual.pdf")
Fuse.fnq = Fuse(Make.bussmann, "FNQ", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 500, False, "MIDGET, FNQ .1-30A, Bussmann manual.pdf")
Fuse.flq = Fuse(Make.littelfuse, "FLQ", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 500, False, "MIDGET, FLQ .1-30A, Littelfuse manual.pdf")

Fuse.trm = Fuse(Make.mersen, "TRM", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 250, False, "MIDGET, TRM .1-30A, Mersen manual.pdf")
Fuse.fnm = Fuse(Make.bussmann, "FNM", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 250, False, "MIDGET, FNM .1-30A, Bussmann manual.pdf")
Fuse.flm = Fuse(Make.littelfuse, "FLM", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 250, False, "MIDGET, FLM .1-30A, Littelfuse manual.pdf")

Fuse.gfn = Fuse(Make.mersen, "GFN", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 250, True, "MIDGET, GFN .1-30A, Mersen manual.pdf")
Fuse.fna = Fuse(Make.bussmann, "FNA", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 250, True, "MIDGET, FNA .1-30A, Bussmann manual.pdf")
Fuse.fla = Fuse(Make.littelfuse, "FLA", FuseClass.midget_1_1_2, FuseSpeed.time_delay, 250, True, "MIDGET, BLS .2-10A, FLA .1-30A, Littelfuse manual.pdf")


Fuse.atq.bussmann_equivalent = Fuse.fnq
Fuse.atq.littelfuse_equivalent = Fuse.flq
Fuse.atq.mersen_upgrade = Fuse.atq_r
Fuse.atq.bussmann_upgrade = Fuse.fnq_r
Fuse.atq.littelfuse_upgrade = Fuse.kld_r

Fuse.fnq.mersen_equivalent = Fuse.atq
Fuse.fnq.littelfuse_equivalent = Fuse.flq
Fuse.fnq.mersen_upgrade = Fuse.atq_r
Fuse.fnq.bussmann_upgrade = Fuse.fnq_r
Fuse.fnq.littelfuse_upgrade = Fuse.kld_r

Fuse.flq.mersen_equivalent = Fuse.atq
Fuse.flq.bussmann_equivalent = Fuse.fnq
Fuse.flq.mersen_upgrade = Fuse.atq_r
Fuse.flq.bussmann_upgrade = Fuse.fnq_r
Fuse.flq.littelfuse_upgrade = Fuse.kld_r


Fuse.trm.bussmann_equivalent = Fuse.fnm
Fuse.trm.littelfuse_equivalent = Fuse.flm
Fuse.trm.mersen_upgrade = Fuse.atq
Fuse.trm.bussmann_upgrade = Fuse.fnq
Fuse.trm.littelfuse_upgrade = Fuse.flq

Fuse.fnm.mersen_equivalent = Fuse.trm
Fuse.fnm.littelfuse_equivalent = Fuse.flm
Fuse.fnm.mersen_upgrade = Fuse.atq
Fuse.fnm.bussmann_upgrade = Fuse.fnq
Fuse.fnm.littelfuse_upgrade = Fuse.flq

Fuse.flm.mersen_equivalent = Fuse.trm
Fuse.flm.bussmann_equivalent = Fuse.fnm
Fuse.flm.mersen_upgrade = Fuse.atq
Fuse.flm.bussmann_upgrade = Fuse.fnq
Fuse.flm.littelfuse_upgrade = Fuse.flq


Fuse.gfn.bussmann_equivalent = Fuse.fna
Fuse.gfn.littelfuse_equivalent = Fuse.fla
Fuse.gfn.mersen_upgrade = Fuse.atq
Fuse.gfn.bussmann_upgrade = Fuse.fnq
Fuse.gfn.littelfuse_upgrade = Fuse.flq

Fuse.fna.mersen_equivalent = Fuse.gfn
Fuse.fna.littelfuse_equivalent = Fuse.fla
Fuse.fna.mersen_upgrade = Fuse.atq
Fuse.fna.bussmann_upgrade = Fuse.fnq
Fuse.fna.littelfuse_upgrade = Fuse.flq

Fuse.fla.mersen_equivalent = Fuse.gfn
Fuse.fla.bussmann_equivalent = Fuse.fna
Fuse.fla.mersen_upgrade = Fuse.atq
Fuse.fla.bussmann_upgrade = Fuse.fnq
Fuse.fla.littelfuse_upgrade = Fuse.flq


# def generate_cc_td_motors():
# CC T-D for Motors 600VAC
Fuse.atd_r = Fuse(Make.mersen, "ATD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, ATDR .25-30A, Mersen manual.pdf")
Fuse.lp_cc = Fuse(Make.bussmann, "LP-CC", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC, LPCC .25-30A, Bussmann manual.pdf")
Fuse.ccmr = Fuse(Make.littelfuse, "CCMR", FuseClass.cc, FuseSpeed.time_delay, 600, False, "CC CD, CCMR .2-60, Littelfuse manual.pdf")


Fuse.atd_r.bussmann_equivalent = Fuse.lp_cc
Fuse.atd_r.littelfuse_equivalent = Fuse.ccmr

Fuse.lp_cc.mersen_equivalent = Fuse.atd_r
Fuse.lp_cc.littelfuse_equivalent = Fuse.ccmr

Fuse.ccmr.mersen_equivalent = Fuse.atd_r
Fuse.ccmr.bussmann_equivalent = Fuse.lp_cc


# def generate_ceramic_td():
# Ceramic T-D 250VAC
Fuse.s505 = Fuse(Make.bussmann, "S505", FuseClass.ceramic_5mmx20mm, FuseSpeed.time_delay, 250, True, "Ceramic, S505 .5-12A, Bussmann manual.pdf")
Fuse._215 = Fuse(Make.littelfuse, "215", FuseClass.ceramic_5mmx20mm, FuseSpeed.time_delay, 250, True, "Ceramic, 215 .125-20A, Littelfuse manual.pdf")


Fuse.s505.littelfuse_equivalent = Fuse._215
Fuse._215.bussmann_equivalent = Fuse.s505


# def generate_g():
# G Speed & VAC varies by amp rating
Fuse.ag = Fuse(Make.mersen, "AG", FuseClass.g, indicating=False, manual="G, AG .5-60A, Mersen manual.pdf")
Fuse.sc = Fuse(Make.bussmann, "SC", FuseClass.g, indicating=False, manual="G, SC .5-60A, Bussmann manual.pdf")
Fuse.slc = Fuse(Make.littelfuse, "SLC", FuseClass.g, indicating=False, manual="G, SLC .5-60A, Littelfuse manual.pdf")


Fuse.ag.bussmann_equivalent = Fuse.sc
Fuse.ag.littelfuse_equivalent = Fuse.slc

Fuse.sc.mersen_equivalent = Fuse.ag
Fuse.sc.littelfuse_equivalent = Fuse.slc

Fuse.slc.mersen_equivalent = Fuse.ag
Fuse.slc.bussmann_equivalent = Fuse.sc


# def generate_glass_fa():
# Glass 1/4" x 1 1/4" F-A, VAC varies by amp rating
Fuse.ggc = Fuse(Make.mersen, "GGC", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual="Glass, GGC .1-30A, GGC-V .1-30, GGM .0625-15A, GGM-V .0625-15A, Mersen manual.pdf")
Fuse.agc = Fuse(Make.bussmann, "AGC", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual="Glass, AGC .1-40A, AGC-V .1-40A, Bussmann manual.pdf")
Fuse._312 = Fuse(Make.littelfuse, "312", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual="Glass, 312 .0625-35A, 318 .0625-35A, Littelfuse manual.pdf")


Fuse.ggc.bussmann_equivalent = Fuse.agc
Fuse.ggc.littelfuse_equivalent = Fuse._312

Fuse.agc.mersen_equivalent = Fuse.ggc
Fuse.agc.littelfuse_equivalent = Fuse._312

Fuse._312.mersen_equivalent = Fuse.ggc
Fuse._312.bussmann_equivalent = Fuse.agc


# def generate_glass_td():
# Glass 5mm x 20mm T-D VAC varies by amp rating
Fuse.gsc = Fuse(Make.mersen, "GSC", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual="Glass, Ceramic, GGA .1-5A, GGA-V .1-5A, GSC .1-10A, GSC-V .1-10A, Mersen manual.pdf")
Fuse.gmd = Fuse(Make.bussmann, "GMD", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual="Glass, GMA .063-15A, GMA-V .063-15A, Bussmann manual.pdf")
Fuse._239 = Fuse(Make.littelfuse, "239", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual="Glass, 239 .08-7A, 239-XE .08-7A, Littelfuse manual.pdf")


Fuse.gsc.bussmann_equivalent = Fuse.gmd
Fuse.gsc.littelfuse_equivalent = Fuse._239

Fuse.gmd.mersen_equivalent = Fuse.gsc
Fuse.gmd.littelfuse_equivalent = Fuse._239

Fuse._239.mersen_equivalent = Fuse.gsc
Fuse._239.bussmann_equivalent = Fuse.gmd


# def generate_j():
# J T-D 600VAC
Fuse.ajt_n = Fuse(Make.mersen, "AJT-N", FuseClass.j, FuseSpeed.time_delay, 600, False, "J, AJTN 1-600A, AJT 8-600A, Mersen manual.pdf")
Fuse.lpj_sp = Fuse(Make.bussmann, "LPJ-SP", FuseClass.j, FuseSpeed.time_delay, 600, False, "J, LPJ-SP 1-60A, LPJ-SPI 6-60A, Bussmann manual.pdf")
Fuse.jtd = Fuse(Make.littelfuse, "JTD", FuseClass.j, FuseSpeed.time_delay, 600, False, "J, JTD .8-600A, JTD-ID .8-600A, Littelfuse manual.pdf")

Fuse.ajt = Fuse(Make.mersen, "AJT", FuseClass.j, FuseSpeed.time_delay, 600, True, "J, AJTN 1-600A, AJT 8-600A, Mersen manual.pdf")
Fuse.lpj_spi = Fuse(Make.bussmann, "LPJ-SPI", FuseClass.j, FuseSpeed.time_delay, 600, True, "J, LPJ-SP 1-60A, LPJ-SPI 6-60A, Bussmann manual.pdf")
Fuse.jtd_id = Fuse(Make.littelfuse, "JTD-ID", FuseClass.j, FuseSpeed.time_delay, 600, True, "J, JTD .8-600A, JTD-ID .8-600A, Littelfuse manual.pdf")


Fuse.ajt_n.bussmann_equivalent = Fuse.lpj_sp
Fuse.ajt_n.littelfuse_equivalent = Fuse.jtd

Fuse.lpj_sp.mersen_equivalent = Fuse.ajt_n
Fuse.lpj_sp.littelfuse_equivalent = Fuse.jtd

Fuse.jtd.mersen_equivalent = Fuse.ajt_n
Fuse.jtd.bussmann_equivalent = Fuse.lpj_sp


Fuse.ajt.bussmann_equivalent = Fuse.lpj_spi
Fuse.ajt.littelfuse_equivalent = Fuse.jtd_id
Fuse.ajt.mersen_upgrade = Fuse.ajt_n
Fuse.ajt.bussmann_upgrade = Fuse.lpj_sp
Fuse.ajt.littelfuse_upgrade = Fuse.jtd

Fuse.lpj_spi.mersen_equivalent = Fuse.ajt
Fuse.lpj_spi.littelfuse_equivalent = Fuse.jtd_id
Fuse.lpj_spi.mersen_upgrade = Fuse.ajt_n
Fuse.lpj_spi.bussmann_upgrade = Fuse.lpj_sp
Fuse.lpj_spi.littelfuse_upgrade = Fuse.jtd

Fuse.jtd_id.mersen_equivalent = Fuse.ajt
Fuse.jtd_id.bussmann_equivalent = Fuse.lpj_spi
Fuse.jtd_id.mersen_upgrade = Fuse.ajt_n
Fuse.jtd_id.bussmann_upgrade = Fuse.lpj_sp
Fuse.jtd_id.littelfuse_upgrade = Fuse.jtd


# def generate_rk5():
# RK5 T-D 250VAC
Fuse.tr_r = Fuse(Make.mersen, "TR-R", FuseClass.rk5, FuseSpeed.time_delay, 250, False, "RK5, TR-R .1-600A, TR-R-ID 8-600A, TRS-R .1-600A, TRS-R-ID 8-600A, Mersen manual.pdf")
Fuse.frn_r = Fuse(Make.bussmann, "FRN-R", FuseClass.rk5, FuseSpeed.time_delay, 250, False, "RK5, FRN-R .1-60A, FRN-R-ID 8-60A, Bussmann manual.pdf", "RK5, FRN-R 70-600A, Bussmann manual.pdf")
Fuse.flnr = Fuse(Make.littelfuse, "FLNR", FuseClass.rk5, FuseSpeed.time_delay, 250, False, "RK5, FLNR .1-600A, FLNR-ID 35-600A, FLSR .1-600A, FLSR-ID .1-600, Littelfuse manual.pdf")

Fuse.tr_r_id = Fuse(Make.mersen, "TR-R-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, "RK5, TR-R .1-600A, TR-R-ID 8-600A, TRS-R .1-600A, TRS-R-ID 8-600A, Mersen manual.pdf")
Fuse.frn_r_id = Fuse(Make.bussmann, "FRN-R-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, "RK5, FRN-R .1-60A, FRN-R-ID 8-60A, Bussmann manual.pdf", "RK5, FRN-R 70-600A, Bussmann manual.pdf")
Fuse.flnr_id = Fuse(Make.littelfuse, "FLNR-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, "RK5, FLNR .1-600A, FLNR-ID 35-600A, FLSR .1-600A, FLSR-ID .1-600, Littelfuse manual.pdf")


Fuse.tr_r.bussmann_equivalent = Fuse.frn_r
Fuse.tr_r.littelfuse_equivalent = Fuse.flnr

Fuse.frn_r.mersen_equivalent = Fuse.tr_r
Fuse.frn_r.littelfuse_equivalent = Fuse.flnr

Fuse.flnr.mersen_equivalent = Fuse.tr_r
Fuse.flnr.bussmann_equivalent = Fuse.frn_r


Fuse.tr_r_id.bussmann_equivalent = Fuse.frn_r_id
Fuse.tr_r_id.littelfuse_equivalent = Fuse.flnr_id
Fuse.tr_r_id.mersen_upgrade = Fuse.tr_r
Fuse.tr_r_id.bussmann_upgrade = Fuse.frn_r
Fuse.tr_r_id.littelfuse_upgrade = Fuse.flnr

Fuse.frn_r_id.mersen_equivalent = Fuse.tr_r_id
Fuse.frn_r_id.littelfuse_equivalent = Fuse.flnr_id
Fuse.frn_r_id.mersen_upgrade = Fuse.tr_r
Fuse.frn_r_id.bussmann_upgrade = Fuse.frn_r
Fuse.frn_r_id.littelfuse_upgrade = Fuse.flnr

Fuse.flnr_id.mersen_equivalent = Fuse.tr_r_id
Fuse.flnr_id.bussmann_equivalent = Fuse.frn_r_id
Fuse.flnr_id.mersen_upgrade = Fuse.tr_r
Fuse.flnr_id.bussmann_upgrade = Fuse.frn_r
Fuse.flnr_id.littelfuse_upgrade = Fuse.flnr


# def generate_k5():
# K5 F-A 250VAC
Fuse.ot = Fuse(Make.mersen, "OT", FuseClass.k5, FuseSpeed.fast_acting, 250, False, "K5, OT 1-600A, OTN 15-60A, OTS 1-600A, Mersen manual.pdf")
Fuse.non = Fuse(Make.bussmann, "NON", FuseClass.k5, FuseSpeed.fast_acting, 250, False, "K5 H, NON .125-600A, NOS 1-600A, Bussmann manual.pdf")
Fuse.nln = Fuse(Make.littelfuse, "NLN", FuseClass.k5, FuseSpeed.fast_acting, 250, False, "K5, NLN 1-600A, NLS 1-600A, Littelfuse manual.pdf")


Fuse.ot.bussmann_equivalent = Fuse.non
Fuse.ot.littelfuse_equivalent = Fuse.nln
Fuse.ot.mersen_upgrade = Fuse.tr_r
Fuse.ot.bussmann_upgrade = Fuse.frn_r
Fuse.ot.littelfuse_upgrade = Fuse.flnr

Fuse.non.mersen_equivalent = Fuse.ot
Fuse.non.littelfuse_equivalent = Fuse.nln
Fuse.non.mersen_upgrade = Fuse.tr_r
Fuse.non.bussmann_upgrade = Fuse.frn_r
Fuse.non.littelfuse_upgrade = Fuse.flnr

Fuse.nln.mersen_equivalent = Fuse.ot
Fuse.nln.bussmann_equivalent = Fuse.non
Fuse.nln.mersen_upgrade = Fuse.tr_r
Fuse.nln.bussmann_upgrade = Fuse.frn_r
Fuse.nln.littelfuse_upgrade = Fuse.flnr


# def generate_h():
# H F-A 250VAC
Fuse.rf = Fuse(Make.mersen, "RF", FuseClass.h, FuseSpeed.fast_acting, 250, False, "H, RF 1-600A, RFS 1-600A, Mersen manual.pdf")
Fuse.ren = Fuse(Make.bussmann, "REN", FuseClass.h, FuseSpeed.fast_acting, 250, False, "H, REN 1-60A, RES 1-60A, Bussmann manual.pdf")
Fuse.rln = Fuse(Make.littelfuse, "RLN", FuseClass.h, FuseSpeed.fast_acting, 250, False, "H, RLN 1-600A, RLS 1-600A, Littelfuse manual.pdf")

Fuse.non_class_h = Fuse(Make.bussmann, "NON", FuseClass.h, FuseSpeed.fast_acting, 250, False, "K5 H, NON .125-600A, NOS 1-600A, Bussmann manual.pdf")


Fuse.rf.bussmann_equivalent = Fuse.ren
Fuse.rf.littelfuse_equivalent = Fuse.rln
Fuse.rf.mersen_upgrade = Fuse.tr_r
Fuse.rf.bussmann_upgrade = Fuse.frn_r
Fuse.rf.littelfuse_upgrade = Fuse.flnr

Fuse.ren.mersen_equivalent = Fuse.rf
Fuse.ren.littelfuse_equivalent = Fuse.rln
Fuse.ren.mersen_upgrade = Fuse.tr_r
Fuse.ren.bussmann_upgrade = Fuse.frn_r
Fuse.ren.littelfuse_upgrade = Fuse.flnr

Fuse.rln.mersen_equivalent = Fuse.rf
Fuse.rln.bussmann_equivalent = Fuse.ren
Fuse.rln.mersen_upgrade = Fuse.tr_r
Fuse.rln.bussmann_upgrade = Fuse.frn_r
Fuse.rln.littelfuse_upgrade = Fuse.flnr


Fuse.non_class_h.mersen_upgrade = Fuse.tr_r
Fuse.non_class_h.bussmann_upgrade = Fuse.frn_r
Fuse.non_class_h.littelfuse_upgrade = Fuse.flnr
