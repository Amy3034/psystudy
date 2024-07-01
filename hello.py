burger1 = 461
burger2 = 431
burger3 = 420
burger4 = 0

burger_selection = int(input())
if burger_selection == 1:
    burger_calorie = burger1
elif burger_selection == 2:
    burger_calorie = burger2
elif burger_selection == 3:
    burger_calorie = burger3
else:
    burger_selection = burger4

side1 = 100
side2 = 57
side3 = 70
side4 = 0

side_selection = int(input())
if side_selection == 1:
    side_calorie = side1
elif side_selection == 2:
    side_calorie = side2
elif side_selection == 3:
    side_calorie = side3
else:
    side_selection = side4

drink1 = 130
drink2 = 160
drink3 = 118
drink4 = 0

drink_selection = int(input())
if drink_selection == 1:
    drink_calorie = drink1
elif drink_selection == 2:
    drink_calorie = drink2
elif drink_selection == 3:
    drink_calorie = drink3
else:
    drink_selection = drink4

dessert1 = 130
dessert2 = 160
dessert3 = 118
dessert4 = 0

dessert_selection = int(input())
if dessert_selection == 1:
    dessert_calorie = dessert1
elif dessert_selection == 2:
    dessert_calorie = dessert2
elif dessert_selection == 3:
    dessert_calorie = dessert3
else:
    dessert_selection = dessert4

total_calorie = burger_calorie + side_calorie + drink_calorie + dessert_calorie
print('Your total calorie count is' + str(total_calorie) + '.')