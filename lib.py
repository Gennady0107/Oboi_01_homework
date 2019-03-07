def perimeter(leng_of_room, width_of_room, wigth_of_wallpaper):
    """
    >>> perimeter(6,8,0.75)
    37
    """
    wallpaper_in_perimeter_room = round((leng_of_room + width_of_room) * 2) / wigth_of_wallpaper
    return round(wallpaper_in_perimeter_room)


def ceiling_heights_in_roll(lengh_of_wallpaper, ceiling_heigt):
    """
    >>> ceiling_heights_in_roll(6,3)
    2
    >>> ceiling_heights_in_roll(12,3)
    4
    """
    roll_in_room = round(lengh_of_wallpaper / ceiling_heigt)
    return roll_in_room


def rolls_all(perimeter, ceiling_heights_in_roll):
    """
    >>> rolls_all(6,3)
    2
    """
    rolls = perimeter / ceiling_heights_in_roll
    return round(rolls)
