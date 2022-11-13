from specifications.enums.ordered_str_enum import OrderedStrEnum


class FuseSpeed(OrderedStrEnum):
    fast_acting = "Fast-Acting"
    time_delay = "Time-Delay"
    varies_by_amp_rating = "Varies by Amp Rating"


class FuseClass(OrderedStrEnum):
    cc = "CC"
    ceramic_5mmx20mm = "Ceramic 5x20mm"
    g = "G"
    glass_1_4x1_1_4 = 'Glass 1/4 x 1 1/4"'
    glass_5mmx20mm = "Glass 5x20mm"
    h = "H"
    j = "J"
    k5 = "K5"
    midget = 'MIDGET'
    rk5 = "RK5"
