team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использую %
print('В команде Мастера кода участников: %(team1)s !' % {'team1' : team1_num})
print('Итого сегодня в командах участников: %(team1)s и %(team2)s !' % {'team1' : team1_num, 'team2' : team2_num})

#Использование format():
print('Команда Волшебники данных решила задач: {0} !'.format(score_1))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

#Использую f-строки
print(f'Команды решили {score_1} и {score_2} задач')

if score_1>score_2 or (score_1==score_2 and team1_time<team2_time):
    challenge_result='Волшебники данных'
elif score_1<score_2 or (score_1==score_2 and team2_time<team1_time):
    challenge_result = 'Мастера кода'
else:
    challenge_result = 'Ничья'

print(f'Результат битвы: {challenge_result}')


sumScore=score_1+score_2
avgTime=(team1_time+team2_time)/sumScore
print(f'Сегодня было решено {sumScore} задач, в среднем по {avgTime} секунды на задачу!')