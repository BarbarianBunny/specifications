from specifications.enums.ordered_str_enum import OrderedStrEnum


class FuseSpeed(OrderedStrEnum):
    fast_acting = "Fast-Acting"
    time_delay = "Time-Delay"
    varies_by_amp_rating = "Varies by Amp Rating"


class FuseClass(OrderedStrEnum):
    cc = "CC"
    ceramic_5mmx20mm = "Ceramic 5mm x 20mm"
    g = "G"
    glass_1_4x1_1_4 = 'Glass 1/4" x 1 1/4"'
    glass_5mmx20mm = "Glass 5mm x 20mm"
    h = "H"
    j = "J"
    k5 = "K5"
    midget_13_32x1_1_2 = 'MIDGET 13/32" x 1 1/2"'
    rk5 = "RK5"
