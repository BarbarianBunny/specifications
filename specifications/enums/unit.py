from specifications.enums.ordered_str_enum import OrderedStrEnum


class Unit(OrderedStrEnum):
    # Electrical
    milliamp = " mA"
    amp = " A"
    hertz = " Hz"
    phase = " PH"
    volt = " V"
    volt_ampere = " VA"
    kilowatt = " KW"

    # Frequency of Occurrence
    rotations_per_minute = " RPM"
    stroke_per_minute = " SPM"

    # Temperature
    degree_celsius = "°C"
    degree_fahrenheit = "°F"

    # Pressure
    pounds_per_square_inch = " psi"
    inches_of_water_column = '"WC'
    feet_of_water_column = "'WC"
    centimeter_of_water_column = "cmWC"
    inches_of_mercury = '"Hg'
    millimeters_of_mercury = " mmHg"
    kilopascal = " kPa"
    millibar = " mbar"
    bar = "bar"
    kilograms_per_square_centimeter = "kg/cm<sup>2</sup>"
    ounces_per_square_inch = " ozin<sup>2</sup>"

    # Distance
    inch = '"'
    feet = " ft"

    # Volume
    gallon = " gal"

    # Angle
    degree = "°"

    # Power
    horse_power = " HP"
    boiler_horse_power = " BHP"
    british_thermal_unit = " BTU"
    british_thermal_units_per_hour = " BTU/hr"
    thousand_british_thermal_units_per_hour = " MBH"

    # Flow
    gallon_per_hour = " GPH"
    gallon_per_minute = " GPM"
    pounds_per_hour = " lbs/hr"

    # Time
    hour = " hr"
    second = " s"

    # Weight
    pounds = " lbs"
