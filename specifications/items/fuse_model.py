from specifications.doc import Doc
from specifications.enums.fuse import FuseMake, FuseClass, FuseSpeed
from specifications.enums.unit import Unit
from specifications.item import Item
from specifications.spec import Spec


class FuseModel(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: FuseMake, model: str, class_: FuseClass, speed: FuseSpeed = None, vac_rating: int = None,
                 indicating: bool = None, manual: Doc = None, manual2: Doc = None,
                 mersen_equivalent=None, bussmann_equivalent=None, littelfuse_equivalent=None,
                 mersen_upgrade=None, bussmann_upgrade=None, littelfuse_upgrade=None):
        super().__init__()
        self.make = Spec("Make", make)
        self.model = Spec("Model", model)
        self.class_ = Spec("Class", class_)
        self.speed = Spec("Speed", speed)
        self.vac_rating = Spec("VAC Rating", vac_rating, Unit.volt)
        self.indicating = Spec("Indicating", indicating)
        self.mersen_equivalent = Spec("Mersen Equivalent", mersen_equivalent)
        self.bussmann_equivalent = Spec("Bussmann Equivalent", bussmann_equivalent)
        self.littelfuse_equivalent = Spec("Littelfuse Equivalent", littelfuse_equivalent)
        self.mersen_upgrade = Spec("Mersen Upgrade", mersen_upgrade)
        self.bussmann_upgrade = Spec("Bussmann Upgrade", bussmann_upgrade)
        self.littelfuse_upgrade = Spec("Littelfuse Upgrade", littelfuse_upgrade)
        self.manual = Spec("Manual", manual)
        self.manual2 = Spec("Manual2", manual2)

    def __str__(self):
        return f"{self.model}"


def generate_cc_fa():
    # CC F-A 600VAC
    FuseModel.atm_r = FuseModel(FuseMake.mersen, "ATM-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, Doc("CC, ATMR .1-30A, Mersen manual.pdf"))
    FuseModel.ktk_r = FuseModel(FuseMake.bussmann, "KTK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, Doc("CC, KTKR .1-30A, Bussmann manual.pdf"))
    FuseModel.klk_r = FuseModel(FuseMake.littelfuse, "KLK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False, Doc("CC, KLKR .1-30A, Littelfuse manual.pdf"))
    
    
    FuseModel.atm_r.bussmann_equivalent.value = FuseModel.ktk_r
    FuseModel.atm_r.littelfuse_equivalent.value = FuseModel.klk_r
    
    FuseModel.ktk_r.mersen_equivalent.value = FuseModel.atm_r
    FuseModel.ktk_r.littelfuse_equivalent.value = FuseModel.klk_r
    
    FuseModel.klk_r.mersen_equivalent.value = FuseModel.atm_r
    FuseModel.klk_r.bussmann_equivalent.value = FuseModel.ktk_r


def generate_midget_fa_600():
    # MIDGET 13/32" x 1 1/2" F-A 600VAC
    FuseModel.atm = FuseModel(FuseMake.mersen, "ATM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False, Doc("MIDGET, ATM .1-50A, Mersen manual.pdf"))
    FuseModel.ktk = FuseModel(FuseMake.bussmann, "KTK", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False, Doc("MIDGET, KTK .1-30A, Bussmann manual.pdf"))
    FuseModel.klk = FuseModel(FuseMake.littelfuse, "KLK", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False, Doc("MIDGET, KLK .1-30A, Littelfuse manual.pdf"))
    
    FuseModel.klm = FuseModel(FuseMake.bussmann, "KLM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False, Doc("MIDGET, KLM .1-30A, Bussmann manual.pdf"))
    FuseModel.dcm = FuseModel(FuseMake.bussmann, "DCM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False, Doc("MIDGET, DCM .1-30A, Bussmann manual.pdf"))
    
    
    FuseModel.atm.bussmann_equivalent.value = FuseModel.ktk
    FuseModel.atm.littelfuse_equivalent.value = FuseModel.klk
    FuseModel.atm.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.atm.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.atm.littelfuse_upgrade.value = FuseModel.klk_r
    
    FuseModel.ktk.mersen_equivalent.value = FuseModel.atm
    FuseModel.ktk.littelfuse_equivalent.value = FuseModel.klk
    FuseModel.ktk.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.ktk.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.ktk.littelfuse_upgrade.value = FuseModel.klk_r
    
    FuseModel.klk.mersen_equivalent.value = FuseModel.atm
    FuseModel.klk.bussmann_equivalent.value = FuseModel.ktk
    FuseModel.klk.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.klk.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.klk.littelfuse_upgrade.value = FuseModel.klk_r
    
    
    FuseModel.klm.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.klm.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.klm.littelfuse_upgrade.value = FuseModel.klk_r
    
    FuseModel.dcm.bussmann_upgrade.value = FuseModel.klm


def generate_midget_fa_250():
    # MIDGET 13/32" x 1 1/2" F-A 250VAC
    FuseModel.otm = FuseModel(FuseMake.mersen, "OTM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False, Doc("MIDGET, OTM 1-30A, Mersen manual.pdf"))
    FuseModel.baf = FuseModel(FuseMake.bussmann, "BAF", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False, Doc("MIDGET, BAF .25-30A, Bussmann manual.pdf"))
    FuseModel.bln = FuseModel(FuseMake.littelfuse, "BLN", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False, Doc("MIDGET, BLN 1-30, Littelfuse manual.pdf"))
    
    FuseModel.blf = FuseModel(FuseMake.littelfuse, "BLF", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False, Doc("MIDGET, BLF .5-30A, Littelfuse manual.pdf"))
    FuseModel.mic = FuseModel(FuseMake.bussmann, "MIC", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, True, Doc("MIDGET, MIC 1-30A, Bussmann manual.pdf"))
    FuseModel.ban = FuseModel(FuseMake.bussmann, "BAN", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False, Doc("MIDGET, BAN 1-30A, Bussmann manual.pdf"))
    
    
    FuseModel.otm.bussmann_equivalent.value = FuseModel.baf
    FuseModel.otm.littelfuse_equivalent.value = FuseModel.bln
    FuseModel.otm.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.otm.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.otm.littelfuse_upgrade.value = FuseModel.klk_r
    
    FuseModel.baf.mersen_equivalent.value = FuseModel.otm
    FuseModel.baf.littelfuse_equivalent.value = FuseModel.bln
    FuseModel.baf.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.baf.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.baf.littelfuse_upgrade.value = FuseModel.klk_r
    
    FuseModel.bln.mersen_equivalent.value = FuseModel.otm
    FuseModel.bln.bussmann_equivalent.value = FuseModel.baf
    FuseModel.bln.mersen_upgrade.value = FuseModel.atm_r
    FuseModel.bln.bussmann_upgrade.value = FuseModel.ktk_r
    FuseModel.bln.littelfuse_upgrade.value = FuseModel.klk_r
    
    
    FuseModel.blf.mersen_upgrade.value = FuseModel.otm
    FuseModel.blf.bussmann_upgrade.value = FuseModel.baf
    FuseModel.blf.littelfuse_upgrade.value = FuseModel.bln
    
    FuseModel.mic.mersen_upgrade.value = FuseModel.otm
    FuseModel.mic.bussmann_upgrade.value = FuseModel.baf
    FuseModel.mic.littelfuse_upgrade.value = FuseModel.bln
    
    FuseModel.ban.mersen_upgrade.value = FuseModel.otm
    FuseModel.ban.bussmann_upgrade.value = FuseModel.baf
    FuseModel.ban.littelfuse_upgrade.value = FuseModel.bln


def generate_cc_td_transformers():
    # CC T-D for Transformers 600VAC
    FuseModel.atq_r = FuseModel(FuseMake.mersen, "ATQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, Doc("CC, ATQR .1-30A, Mersen manual.pdf"))
    FuseModel.fnq_r = FuseModel(FuseMake.bussmann, "FNQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, Doc("CC, FNQR .25-30A, Bussmann manual.pdf"))
    FuseModel.kld_r = FuseModel(FuseMake.littelfuse, "KLD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, Doc("CC, KLDR .1-30A, Littelfuse manual.pdf"))
    
    
    FuseModel.atq_r.bussmann_equivalent.value = FuseModel.fnq_r
    FuseModel.atq_r.littelfuse_equivalent.value = FuseModel.kld_r
    
    FuseModel.fnq_r.mersen_equivalent.value = FuseModel.atq_r
    FuseModel.fnq_r.littelfuse_equivalent.value = FuseModel.kld_r
    
    FuseModel.kld_r.mersen_equivalent.value = FuseModel.atq_r
    FuseModel.kld_r.bussmann_equivalent.value = FuseModel.fnq_r



def generate_midget_td():
    # MIDGET 13/32" x 1 1/2" T-D ___VAC
    FuseModel.atq = FuseModel(FuseMake.mersen, "ATQ", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 500, False, Doc("MIDGET, ATQ .1-30A, Mersen manual.pdf"))
    FuseModel.fnq = FuseModel(FuseMake.bussmann, "FNQ", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 500, False, Doc("MIDGET, FNQ .1-30A, Bussmann manual.pdf"))
    FuseModel.kld = FuseModel(FuseMake.littelfuse, "KLD", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 500, False)
    
    FuseModel.trm = FuseModel(FuseMake.mersen, "TRM", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, False, Doc("MIDGET, TRM .1-30A, Mersen manual.pdf"))
    FuseModel.fnm = FuseModel(FuseMake.bussmann, "FNM", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, False, Doc("MIDGET, FNM .1-30A, Bussmann manual.pdf"))
    FuseModel.flm = FuseModel(FuseMake.littelfuse, "FLM", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, False, Doc("MIDGET, FLM .1-30A, Littelfuse manual.pdf"))
    
    FuseModel.gfn = FuseModel(FuseMake.mersen, "GFN", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, True, Doc("MIDGET, GFN .1-30A, Mersen manual.pdf"))
    FuseModel.fna = FuseModel(FuseMake.bussmann, "FNA", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, True, Doc("MIDGET, FNA .1-30A, Bussmann manual.pdf"))
    FuseModel.fla = FuseModel(FuseMake.littelfuse, "FLA", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, True)
    
    
    FuseModel.atq.bussmann_equivalent.value = FuseModel.fnq
    FuseModel.atq.littelfuse_equivalent.value = FuseModel.kld
    FuseModel.atq.mersen_upgrade.value = FuseModel.atq_r
    FuseModel.atq.bussmann_upgrade.value = FuseModel.fnq_r
    FuseModel.atq.littelfuse_upgrade.value = FuseModel.kld_r
    
    FuseModel.fnq.mersen_equivalent.value = FuseModel.atq
    FuseModel.fnq.littelfuse_equivalent.value = FuseModel.kld
    FuseModel.fnq.mersen_upgrade.value = FuseModel.atq_r
    FuseModel.fnq.bussmann_upgrade.value = FuseModel.fnq_r
    FuseModel.fnq.littelfuse_upgrade.value = FuseModel.kld_r
    
    FuseModel.kld.mersen_equivalent.value = FuseModel.atq
    FuseModel.kld.bussmann_equivalent.value = FuseModel.fnq
    FuseModel.kld.mersen_upgrade.value = FuseModel.atq_r
    FuseModel.kld.bussmann_upgrade.value = FuseModel.fnq_r
    FuseModel.kld.littelfuse_upgrade.value = FuseModel.kld_r
    
    
    FuseModel.trm.bussmann_equivalent.value = FuseModel.fnm
    FuseModel.trm.littelfuse_equivalent.value = FuseModel.flm
    FuseModel.trm.mersen_upgrade.value = FuseModel.atq
    FuseModel.trm.bussmann_upgrade.value = FuseModel.fnq
    FuseModel.trm.littelfuse_upgrade.value = FuseModel.kld
    
    FuseModel.fnm.mersen_equivalent.value = FuseModel.trm
    FuseModel.fnm.littelfuse_equivalent.value = FuseModel.flm
    FuseModel.fnm.mersen_upgrade.value = FuseModel.atq
    FuseModel.fnm.bussmann_upgrade.value = FuseModel.fnq
    FuseModel.fnm.littelfuse_upgrade.value = FuseModel.kld
    
    FuseModel.flm.mersen_equivalent.value = FuseModel.trm
    FuseModel.flm.bussmann_equivalent.value = FuseModel.fnm
    FuseModel.flm.mersen_upgrade.value = FuseModel.atq
    FuseModel.flm.bussmann_upgrade.value = FuseModel.fnq
    FuseModel.flm.littelfuse_upgrade.value = FuseModel.kld
    
    
    FuseModel.gfn.bussmann_equivalent.value = FuseModel.fna
    FuseModel.gfn.littelfuse_equivalent.value = FuseModel.fla
    FuseModel.gfn.mersen_upgrade.value = FuseModel.atq
    FuseModel.gfn.bussmann_upgrade.value = FuseModel.fnq
    FuseModel.gfn.littelfuse_upgrade.value = FuseModel.kld
    
    FuseModel.fna.mersen_equivalent.value = FuseModel.gfn
    FuseModel.fna.littelfuse_equivalent.value = FuseModel.fla
    FuseModel.fna.mersen_upgrade.value = FuseModel.atq
    FuseModel.fna.bussmann_upgrade.value = FuseModel.fnq
    FuseModel.fna.littelfuse_upgrade.value = FuseModel.kld
    
    FuseModel.fla.mersen_equivalent.value = FuseModel.gfn
    FuseModel.fla.bussmann_equivalent.value = FuseModel.fna
    FuseModel.fla.mersen_upgrade.value = FuseModel.atq
    FuseModel.fla.bussmann_upgrade.value = FuseModel.fnq
    FuseModel.fla.littelfuse_upgrade.value = FuseModel.kld


def generate_cc_td_motors():
    # CC T-D for Motors 600VAC
    FuseModel.atd_r = FuseModel(FuseMake.mersen, "ATD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False, Doc("CC, ATDR .25-30A, Mersen manual.pdf"))
    FuseModel.lp_cc = FuseModel(FuseMake.bussmann, "LP-CC", FuseClass.cc, FuseSpeed.time_delay, 600, False, Doc("CC, LPCC .25-30A, Bussmann manual.pdf"))
    FuseModel.ccmr = FuseModel(FuseMake.littelfuse, "CCMR", FuseClass.cc, FuseSpeed.time_delay, 600, False, Doc("CC CD, CCMR .2-60, Littelfuse manual.pdf"))
    
    
    FuseModel.atd_r.bussmann_equivalent.value = FuseModel.lp_cc
    FuseModel.atd_r.littelfuse_equivalent.value = FuseModel.ccmr
    
    FuseModel.lp_cc.mersen_equivalent.value = FuseModel.atd_r
    FuseModel.lp_cc.littelfuse_equivalent.value = FuseModel.ccmr
    
    FuseModel.ccmr.mersen_equivalent.value = FuseModel.atd_r
    FuseModel.ccmr.bussmann_equivalent.value = FuseModel.lp_cc


def generate_ceramic_td():
    # Ceramic T-D 250VAC
    FuseModel.s505 = FuseModel(FuseMake.bussmann, "S505", FuseClass.ceramic_5mmx20mm, FuseSpeed.time_delay, 250, True, Doc("Ceramic, S505 .5-12A, Bussmann manual.pdf"))
    FuseModel._215 = FuseModel(FuseMake.littelfuse, "215", FuseClass.ceramic_5mmx20mm, FuseSpeed.time_delay, 250, True, Doc("Ceramic, 215 .125-20A, Littelfuse manual.pdf"))
    
    
    FuseModel.s505.littelfuse_equivalent.value = FuseModel._215
    FuseModel._215.bussmann_equivalent.value = FuseModel.s505


def generate_g():
    # G Speed & VAC varies by amp rating
    FuseModel.ag = FuseModel(FuseMake.mersen, "AG", FuseClass.g, indicating=False, manual=Doc("G, AG .5-60A, Mersen manual.pdf"))
    FuseModel.sc = FuseModel(FuseMake.bussmann, "SC", FuseClass.g, indicating=False, manual=Doc("G, SC .5-60A, Bussmann manual.pdf"))
    FuseModel.slc = FuseModel(FuseMake.littelfuse, "SLC", FuseClass.g, indicating=False, manual=Doc("G, SLC .5-60A, Littelfuse manual.pdf"))
    
    
    FuseModel.ag.bussmann_equivalent.value = FuseModel.sc
    FuseModel.ag.littelfuse_equivalent.value = FuseModel.slc
    
    FuseModel.sc.mersen_equivalent.value = FuseModel.ag
    FuseModel.sc.littelfuse_equivalent.value = FuseModel.slc
    
    FuseModel.slc.mersen_equivalent.value = FuseModel.ag
    FuseModel.slc.bussmann_equivalent.value = FuseModel.sc


def generate_glass_fa():
    # Glass 1/4" x 1 1/4" F-A, VAC varies by amp rating
    FuseModel.ggc = FuseModel(FuseMake.mersen, "GGC", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual=Doc("Glass, GGC .1-30A, GGC-V .1-30, GGM .0625-15A, GGM-V .0625-15A, Mersen manual.pdf"))
    FuseModel.agc = FuseModel(FuseMake.bussmann, "AGC", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual=Doc("Glass, AGC .1-40A, AGC-V .1-40A, Bussmann manual.pdf"))
    FuseModel._312 = FuseModel(FuseMake.littelfuse, "312", FuseClass.glass_1_4x1_1_4, FuseSpeed.fast_acting, indicating=True, manual=Doc("Glass, 312 .0625-35A, 318 .0625-35A, Littelfuse manual.pdf"))
    
    
    FuseModel.ggc.bussmann_equivalent.value = FuseModel.agc
    FuseModel.ggc.littelfuse_equivalent.value = FuseModel._312
    
    FuseModel.agc.mersen_equivalent.value = FuseModel.ggc
    FuseModel.agc.littelfuse_equivalent.value = FuseModel._312
    
    FuseModel._312.mersen_equivalent.value = FuseModel.ggc
    FuseModel._312.bussmann_equivalent.value = FuseModel.agc


def generate_glass_td():
    # Glass 5mm x 20mm T-D VAC varies by amp rating
    FuseModel.gsc = FuseModel(FuseMake.mersen, "GSC", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual=Doc("Glass, Ceramic, GGA .1-5A, GGA-V .1-5A, GSC .1-10A, GSC-V .1-10A, Mersen manual.pdf"))
    FuseModel.gmd = FuseModel(FuseMake.bussmann, "GMD", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual=Doc("Glass, GMA .063-15A, GMA-V .063-15A, Bussmann manual.pdf"))
    FuseModel._239 = FuseModel(FuseMake.littelfuse, "239", FuseClass.glass_5mmx20mm, FuseSpeed.time_delay, indicating=True, manual=Doc("Glass, 239 .08-7A, 239-XE .08-7A, Littelfuse manual.pdf"))
    
    
    FuseModel.gsc.bussmann_equivalent.value = FuseModel.gmd
    FuseModel.gsc.littelfuse_equivalent.value = FuseModel._239
    
    FuseModel.gmd.mersen_equivalent.value = FuseModel.gsc
    FuseModel.gmd.littelfuse_equivalent.value = FuseModel._239
    
    FuseModel._239.mersen_equivalent.value = FuseModel.gsc
    FuseModel._239.bussmann_equivalent.value = FuseModel.gmd


def generate_j():
    # J T-D 600VAC
    FuseModel.ajt_n = FuseModel(FuseMake.mersen, "AJT-N", FuseClass.j, FuseSpeed.time_delay, 600, False, Doc("J, AJTN 1-600A, AJT 8-600A, Mersen manual.pdf"))
    FuseModel.lpj_sp = FuseModel(FuseMake.bussmann, "LPJ-SP", FuseClass.j, FuseSpeed.time_delay, 600, False, Doc("J, LPJ-SP 1-60A, LPJ-SPI 6-60A, Bussmann manual.pdf"))
    FuseModel.jtd = FuseModel(FuseMake.littelfuse, "JTD", FuseClass.j, FuseSpeed.time_delay, 600, False, Doc("J, JTD .8-600A, JTD-ID .8-600A, Littelfuse manual.pdf"))
    
    FuseModel.ajt = FuseModel(FuseMake.mersen, "AJT", FuseClass.j, FuseSpeed.time_delay, 600, True, Doc("J, AJTN 1-600A, AJT 8-600A, Mersen manual.pdf"))
    FuseModel.lpj_spi = FuseModel(FuseMake.bussmann, "LPJ-SPI", FuseClass.j, FuseSpeed.time_delay, 600, True, Doc("J, LPJ-SP 1-60A, LPJ-SPI 6-60A, Bussmann manual.pdf"))
    FuseModel.jtd_id = FuseModel(FuseMake.littelfuse, "JTD-ID", FuseClass.j, FuseSpeed.time_delay, 600, True, Doc("J, JTD .8-600A, JTD-ID .8-600A, Littelfuse manual.pdf"))
    
    
    FuseModel.ajt_n.bussmann_equivalent.value = FuseModel.lpj_sp
    FuseModel.ajt_n.littelfuse_equivalent.value = FuseModel.jtd
    
    FuseModel.lpj_sp.mersen_equivalent.value = FuseModel.ajt_n
    FuseModel.lpj_sp.littelfuse_equivalent.value = FuseModel.jtd
    
    FuseModel.jtd.mersen_equivalent.value = FuseModel.ajt_n
    FuseModel.jtd.bussmann_equivalent.value = FuseModel.lpj_sp
    
    
    FuseModel.ajt.bussmann_equivalent.value = FuseModel.lpj_spi
    FuseModel.ajt.littelfuse_equivalent.value = FuseModel.jtd_id
    FuseModel.ajt.mersen_upgrade.value = FuseModel.ajt_n
    FuseModel.ajt.bussmann_upgrade.value = FuseModel.lpj_sp
    FuseModel.ajt.littelfuse_upgrade.value = FuseModel.jtd
    
    FuseModel.lpj_spi.mersen_equivalent.value = FuseModel.ajt
    FuseModel.lpj_spi.littelfuse_equivalent.value = FuseModel.jtd_id
    FuseModel.lpj_spi.mersen_upgrade.value = FuseModel.ajt_n
    FuseModel.lpj_spi.bussmann_upgrade.value = FuseModel.lpj_sp
    FuseModel.lpj_spi.littelfuse_upgrade.value = FuseModel.jtd
    
    FuseModel.jtd_id.mersen_equivalent.value = FuseModel.ajt
    FuseModel.jtd_id.bussmann_equivalent.value = FuseModel.lpj_spi
    FuseModel.jtd_id.mersen_upgrade.value = FuseModel.ajt_n
    FuseModel.jtd_id.bussmann_upgrade.value = FuseModel.lpj_sp
    FuseModel.jtd_id.littelfuse_upgrade.value = FuseModel.jtd


def generate_rk5():
    # RK5 T-D 250VAC
    FuseModel.tr_r = FuseModel(FuseMake.mersen, "TR-R", FuseClass.rk5, FuseSpeed.time_delay, 250, False, Doc("RK5, TR-R .1-600A, TR-R-ID 8-600A, TRS-R .1-600A, TRS-R-ID 8-600A, Mersen manual.pdf"))
    FuseModel.frn_r = FuseModel(FuseMake.bussmann, "FRN-R", FuseClass.rk5, FuseSpeed.time_delay, 250, False, Doc("RK5, FRN-R .1-60A, FRN-R-ID 8-60A, Bussmann manual.pdf"), Doc("RK5, FRN-R 70-600A, Bussmann manual.pdf"))
    FuseModel.flnr = FuseModel(FuseMake.littelfuse, "FLNR", FuseClass.rk5, FuseSpeed.time_delay, 250, False, Doc("RK5, FLNR .1-600A, FLNR-ID 35-600A, FLSR .1-600A, FLSR-ID .1-600, Littelfuse manual.pdf"))
    
    FuseModel.tr_r_id = FuseModel(FuseMake.mersen, "TR-R-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, Doc("RK5, TR-R .1-600A, TR-R-ID 8-600A, TRS-R .1-600A, TRS-R-ID 8-600A, Mersen manual.pdf"))
    FuseModel.frn_r_id = FuseModel(FuseMake.bussmann, "FRN-R-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, Doc("RK5, FRN-R .1-60A, FRN-R-ID 8-60A, Bussmann manual.pdf"), Doc("RK5, FRN-R 70-600A, Bussmann manual.pdf"))
    FuseModel.flnr_id = FuseModel(FuseMake.littelfuse, "FLNR-ID", FuseClass.rk5, FuseSpeed.time_delay, 250, True, Doc("RK5, FLNR .1-600A, FLNR-ID 35-600A, FLSR .1-600A, FLSR-ID .1-600, Littelfuse manual.pdf"))
    
    
    FuseModel.tr_r.bussmann_equivalent.value = FuseModel.frn_r
    FuseModel.tr_r.littelfuse_equivalent.value = FuseModel.flnr
    
    FuseModel.frn_r.mersen_equivalent.value = FuseModel.tr_r
    FuseModel.frn_r.littelfuse_equivalent.value = FuseModel.flnr
    
    FuseModel.flnr.mersen_equivalent.value = FuseModel.tr_r
    FuseModel.flnr.bussmann_equivalent.value = FuseModel.frn_r
    
    
    FuseModel.tr_r_id.bussmann_equivalent.value = FuseModel.frn_r_id
    FuseModel.tr_r_id.littelfuse_equivalent.value = FuseModel.flnr_id
    FuseModel.tr_r_id.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.tr_r_id.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.tr_r_id.littelfuse_upgrade.value = FuseModel.flnr
    
    FuseModel.frn_r_id.mersen_equivalent.value = FuseModel.tr_r_id
    FuseModel.frn_r_id.littelfuse_equivalent.value = FuseModel.flnr_id
    FuseModel.frn_r_id.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.frn_r_id.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.frn_r_id.littelfuse_upgrade.value = FuseModel.flnr
    
    FuseModel.flnr_id.mersen_equivalent.value = FuseModel.tr_r_id
    FuseModel.flnr_id.bussmann_equivalent.value = FuseModel.frn_r_id
    FuseModel.flnr_id.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.flnr_id.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.flnr_id.littelfuse_upgrade.value = FuseModel.flnr


def generate_k5():
    # K5 F-A 250VAC
    FuseModel.ot = FuseModel(FuseMake.mersen, "OT", FuseClass.k5, FuseSpeed.fast_acting, 250, False, Doc("K5, OT 1-600A, OTN 15-60A, OTS 1-600A, Mersen manual.pdf"))
    FuseModel.non = FuseModel(FuseMake.bussmann, "NON", FuseClass.k5, FuseSpeed.fast_acting, 250, False, Doc("K5 H, NON .125-600A, NOS 1-600A, Bussmann manual.pdf"))
    FuseModel.nln = FuseModel(FuseMake.littelfuse, "NLN", FuseClass.k5, FuseSpeed.fast_acting, 250, False, Doc("K5, NLN 1-600A, NLS 1-600A, Littelfuse manual.pdf"))
    
    
    FuseModel.ot.bussmann_equivalent.value = FuseModel.non
    FuseModel.ot.littelfuse_equivalent.value = FuseModel.nln
    FuseModel.ot.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.ot.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.ot.littelfuse_upgrade.value = FuseModel.flnr
    
    FuseModel.non.mersen_equivalent.value = FuseModel.ot
    FuseModel.non.littelfuse_equivalent.value = FuseModel.nln
    FuseModel.non.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.non.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.non.littelfuse_upgrade.value = FuseModel.flnr
    
    FuseModel.nln.mersen_equivalent.value = FuseModel.ot
    FuseModel.nln.bussmann_equivalent.value = FuseModel.non
    FuseModel.nln.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.nln.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.nln.littelfuse_upgrade.value = FuseModel.flnr


def generate_h():
    # H F-A 250VAC
    FuseModel.rf = FuseModel(FuseMake.mersen, "RF", FuseClass.h, FuseSpeed.fast_acting, 250, False, Doc("H, RF 1-600A, RFS 1-600A, Mersen manual.pdf"))
    FuseModel.ren = FuseModel(FuseMake.bussmann, "REN", FuseClass.h, FuseSpeed.fast_acting, 250, False, Doc("H, REN 1-60A, RES 1-60A, Bussmann manual.pdf"))
    FuseModel.rln = FuseModel(FuseMake.littelfuse, "RLN", FuseClass.h, FuseSpeed.fast_acting, 250, False, Doc("H, RLN 1-600A, RLS 1-600A, Littelfuse manual.pdf"))
    
    FuseModel.non_class_h = FuseModel(FuseMake.bussmann, "NON", FuseClass.h, FuseSpeed.fast_acting, 250, False, Doc("K5 H, NON .125-600A, NOS 1-600A, Bussmann manual.pdf"))
    
    
    FuseModel.rf.bussmann_equivalent.value = FuseModel.ren
    FuseModel.rf.littelfuse_equivalent.value = FuseModel.rln
    FuseModel.rf.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.rf.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.rf.littelfuse_upgrade.value = FuseModel.flnr
    
    FuseModel.ren.mersen_equivalent.value = FuseModel.rf
    FuseModel.ren.littelfuse_equivalent.value = FuseModel.rln
    FuseModel.ren.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.ren.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.ren.littelfuse_upgrade.value = FuseModel.flnr
    
    FuseModel.rln.mersen_equivalent.value = FuseModel.rf
    FuseModel.rln.bussmann_equivalent.value = FuseModel.ren
    FuseModel.rln.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.rln.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.rln.littelfuse_upgrade.value = FuseModel.flnr
    
    
    FuseModel.non_class_h.mersen_upgrade.value = FuseModel.tr_r
    FuseModel.non_class_h.bussmann_upgrade.value = FuseModel.frn_r
    FuseModel.non_class_h.littelfuse_upgrade.value = FuseModel.flnr


# Generate Fuse Models
generate_cc_fa()
generate_midget_fa_600()
generate_midget_fa_250()
generate_cc_td_transformers()
generate_midget_td()
generate_cc_td_motors()
generate_ceramic_td()
generate_g()
generate_glass_fa()
generate_glass_td()
generate_j()
generate_rk5()
generate_k5()
generate_h()