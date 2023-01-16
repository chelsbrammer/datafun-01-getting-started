"""
Complete the script.
"""
print('What were the top 3 times from the barrel race?')
racer1_time = int(input('Enter the number of seconds of first barrel race: '))
print()
racer2_time = int(input('Enter the number of seconds of second barrel race: '))
print()
racer3_time = float(input('Enter the number of seconds of third barrel race: '))
print()

type(racer1_time)

racer1_time = float(racer1_time)
racer2_time = float(racer2_time)


quickest_run = min(racer1_time, racer2_time, racer3_time)
print('Quickest run was:', quickest_run)

longest_run = max(racer1_time, racer2_time, racer3_time)
print('Longest run was:', longest_run)

racer_average_run = round((racer1_time + racer2_time + racer3_time) / 3)
print('Average run was:', racer_average_run)

print('Range:', quickest_run, '-', longest_run)

Barrel_1_Penalty = float('5')
Barrel_2_Penalty = float('10')
Barrel_3_Penalty = float('15')

print('If racer knocks down 1 barrel,', Barrel_1_Penalty, 'seconds penalty is added')
print('If racer knocks down 2 barrels,', Barrel_2_Penalty, 'seconds penalty is added')
print('If racer knocks over all barrels,', Barrel_3_Penalty, 'seconds penalty is added')

if racer1_time + Barrel_1_Penalty:
    print('The first racer knocked down 1 barrel during their run')

if racer2_time + Barrel_2_Penalty:
    print('The second racer knocked down 2 barrels during their run')

if racer3_time + Barrel_3_Penalty:
    print('The third racer knocked down all 3 barrels during their run')

