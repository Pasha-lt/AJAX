def convert(DD):
    """
    Convert DD coordinate format to DDM coordinate format.
    :param DD - Decimal Degrees.
    :return DDM - Degrees Decimal Minutes.
    """
    DD = float(DD)
    hemisphere = "W" if DD < 0 else "E"
    integer_part, decimal_part = [i for i in str(abs(DD)).split(".")]
    decimal_part = str(round(float(str(f"0.{decimal_part}")) * 60, 4)).rstrip("0").rstrip(".")
    DDM = f"{integer_part}^{decimal_part}{hemisphere}"
    return DDM
