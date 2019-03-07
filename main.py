from lib import perimeter, ceiling_heights_in_roll, rolls_all

length_room = float(input("Длина комнаты: "))
width_room = float(input("Ширина комнаты: "))
ceiling_heigt = float(input("Высота потолка: "))
width_rool = float(input("Ширина рулона обоев: "))
length_rool = float(input("Длина рулона: "))

print(perimeter(length_room, width_room, width_rool))
print(ceiling_heights_in_roll(12, ceiling_heigt))
print("Кол. рулонов",
      (rolls_all(perimeter(length_room, width_room, width_rool), ceiling_heights_in_roll(12, ceiling_heigt))))

