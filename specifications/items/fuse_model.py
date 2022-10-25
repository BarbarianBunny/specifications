from specifications.doc import Doc
from specifications.enums.fuse import FuseMake, FuseClass, FuseSpeed
from specifications.item import Item
from specifications.spec import Spec


class FuseModel(Item):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, make: FuseMake, model: str, class_: FuseClass, speed: FuseSpeed = None, vac_rating: int = None,
                 indicating: bool = None, manual: Doc = None,
                 mersen_equivalent=None, bussmann_equivalent=None, littelfuse_equivalent=None,
                 mersen_upgrade=None, bussmann_upgrade=None, littelfuse_upgrade=None):
        super().__init__()
        self.make = Spec("Make", make)
        self.model = Spec("Model", model)
        self.class_ = Spec("Class", class_)
        self.speed = Spec("Speed", speed)
        self.vac_rating = Spec("VAC Rating", vac_rating)
        self.indicating = Spec("Indicating", indicating)
        self.manual = Spec("Manual", manual)
        self.mersen_equivalent = Spec("Mersen Equivalent", mersen_equivalent)
        self.bussmann_equivalent = Spec("Bussmann Equivalent", bussmann_equivalent)
        self.littelfuse_equivalent = Spec("Littelfuse Equivalent", littelfuse_equivalent)
        self.mersen_upgrade = Spec("Mersen Upgrade", mersen_upgrade)
        self.bussmann_upgrade = Spec("Bussmann Upgrade", bussmann_upgrade)
        self.littelfuse_upgrade = Spec("Littelfuse Upgrade", littelfuse_upgrade)

    def __str__(self):
        return f"{self.model}"


# FuseModel.blank = FuseModel(FuseMake.make, "model", FuseClass.class, FuseSpeed.speed)

# FuseModel.blank = FuseModel(FuseMake.mersen, "model", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, int, bool)
# FuseModel.blank = FuseModel(FuseMake.bussmann, "model", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, int, bool)
# FuseModel.blank = FuseModel(FuseMake.littelfuse, "model", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, int, bool)
#
# FuseModel.blank.mersen_equivalent.value = FuseModel.blank
# FuseModel.blank.bussmann_equivalent.value = FuseModel.blank
# FuseModel.blank.littelfuse_equivalent.value = FuseModel.blank
#
# FuseModel.blank.mersen_upgrade.value = FuseModel.blank
# FuseModel.blank.bussmann_upgrade.value = FuseModel.blank
# FuseModel.blank.littelfuse_upgrade.value = FuseModel.blank

# TODO: Add manual Doc references to fuses


# CC F-A 600VAC
FuseModel.atm_r = FuseModel(FuseMake.mersen, "ATM-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False)
FuseModel.ktk_r = FuseModel(FuseMake.bussmann, "KTK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False)
FuseModel.klk_r = FuseModel(FuseMake.littelfuse, "KLK-R", FuseClass.cc, FuseSpeed.fast_acting, 600, False)


FuseModel.atm_r.bussmann_equivalent.value = FuseModel.ktk_r
FuseModel.atm_r.littelfuse_equivalent.value = FuseModel.klk_r

FuseModel.ktk_r.mersen_equivalent.value = FuseModel.atm_r
FuseModel.ktk_r.littelfuse_equivalent.value = FuseModel.klk_r

FuseModel.klk_r.mersen_equivalent.value = FuseModel.atm_r
FuseModel.klk_r.bussmann_equivalent.value = FuseModel.ktk_r


# MIDGET 13/32" x 1 1/2" F-A 600VAC
FuseModel.atm = FuseModel(FuseMake.mersen, "ATM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False)
FuseModel.ktk = FuseModel(FuseMake.bussmann, "KTK", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False)
FuseModel.klk = FuseModel(FuseMake.littelfuse, "KLK", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False)

FuseModel.klm = FuseModel(FuseMake.bussmann, "KLM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False)
FuseModel.dcm = FuseModel(FuseMake.bussmann, "DCM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 600, False)


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


# MIDGET 13/32" x 1 1/2" F-A 250VAC
FuseModel.otm = FuseModel(FuseMake.mersen, "OTM", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False)
FuseModel.baf = FuseModel(FuseMake.bussmann, "BAF", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False)
FuseModel.bln = FuseModel(FuseMake.littelfuse, "BLN", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False)

FuseModel.blf = FuseModel(FuseMake.littelfuse, "BLF", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False)
FuseModel.mic = FuseModel(FuseMake.bussmann, "MIC", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, True)
FuseModel.ban = FuseModel(FuseMake.bussmann, "BAN", FuseClass.midget_13_32x1_1_2, FuseSpeed.fast_acting, 250, False)


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


# CC T-D for Transformers 600VAC
FuseModel.atq_r = FuseModel(FuseMake.mersen, "ATQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False)
FuseModel.fnq_r = FuseModel(FuseMake.bussmann, "FNQ-R", FuseClass.cc, FuseSpeed.time_delay, 600, False)
FuseModel.kld_r = FuseModel(FuseMake.littelfuse, "KLD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False)


FuseModel.atq_r.bussmann_equivalent.value = FuseModel.fnq_r
FuseModel.atq_r.littelfuse_equivalent.value = FuseModel.kld_r

FuseModel.fnq_r.mersen_equivalent.value = FuseModel.atq_r
FuseModel.fnq_r.littelfuse_equivalent.value = FuseModel.kld_r

FuseModel.kld_r.mersen_equivalent.value = FuseModel.atq_r
FuseModel.kld_r.bussmann_equivalent.value = FuseModel.fnq_r


# MIDGET 13/32" x 1 1/2" T-D ___VAC
FuseModel.atq = FuseModel(FuseMake.mersen, "ATQ", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 500, False)
FuseModel.fnq = FuseModel(FuseMake.bussmann, "FNQ", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 500, False)
FuseModel.kld = FuseModel(FuseMake.littelfuse, "KLD", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 500, False)

FuseModel.trm = FuseModel(FuseMake.mersen, "TRM", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, False)
FuseModel.fnm = FuseModel(FuseMake.bussmann, "FNM", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, False)
FuseModel.flm = FuseModel(FuseMake.littelfuse, "FLM", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, False)

FuseModel.gfn = FuseModel(FuseMake.mersen, "GFN", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, True)
FuseModel.fna = FuseModel(FuseMake.bussmann, "FNA", FuseClass.midget_13_32x1_1_2, FuseSpeed.time_delay, 250, True)
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


# CC T-D for Motors 600VAC
FuseModel.atd_r = FuseModel(FuseMake.mersen, "ATD-R", FuseClass.cc, FuseSpeed.time_delay, 600, False)
FuseModel.lp_cc = FuseModel(FuseMake.bussmann, "LP-CC", FuseClass.cc, FuseSpeed.time_delay, 600, False)
FuseModel.ccmr = FuseModel(FuseMake.littelfuse, "CCMR", FuseClass.cc, FuseSpeed.time_delay, 600, False)


FuseModel.atd_r.bussmann_equivalent.value = FuseModel.lp_cc
FuseModel.atd_r.littelfuse_equivalent.value = FuseModel.ccmr

FuseModel.lp_cc.mersen_equivalent.value = FuseModel.atd_r
FuseModel.lp_cc.littelfuse_equivalent.value = FuseModel.ccmr

FuseModel.ccmr.mersen_equivalent.value = FuseModel.atd_r
FuseModel.ccmr.bussmann_equivalent.value = FuseModel.lp_cc


# Ceramic T-D 250VAC


# G Speed & VAC varies by amp rating


# Glass 1/4" x 1 1/4" F-A, VAC varies by amp rating


# Glass 5mm x 20mm T-D VAC varies by amp rating


# J 600VAC


# RK5 T-D 250VAC


# K5 F-A 250VAC


# H F-A 250VAC