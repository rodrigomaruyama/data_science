# -*- coding: utf-8 -*-
#####################################
#                 1                 #
#####################################

## Read in the data from daily_engagement.csv and project_submissions.csv
## and store the results in the below variables.
## Then look at the first row of each table.
import unicodecsv

## ## class csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect=’excel’, *args, **kwds)

## Create an object which operates like a regular reader but maps the information read into a dict whose keys
## are given by the optional fieldnames parameter. The fieldnames parameter is a sequence whose elements are
## associated with the fields of the input data in order. These elements become the keys of the resulting dictionary.
## If the fieldnames parameter is omitted, the values in the first row of the csvfile will be used as the fieldnames.
## If the row read has more fields than the fieldnames sequence, the remaining data is added as a sequence keyed by
## the value of restkey. If the row read has fewer fields than the fieldnames sequence, the remaining keys take the
## value of the optional restval parameter. Any other optional or keyword arguments are passed to the underlying
## reader instance.

## Iniciamos criando uma função que abre um arquivo e depois com o módulo unicodecsv lemos o arquivo CSV e o colocamos emum dicionário

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

# Chamamos a função read_csv para ler os 3 arquivos a serem trabalhados: 1 enrollments contem os dados dos alunos inscritos no curso.
# 2. daily_engagement armazena os progessos do aluno no curso e 3. project_submissions armazena a conclusão dos projetos de
# cada aluno.

enrollments = read_csv('/home/maru/Documents/Semana3/enrollments.csv')
daily_engagement = read_csv('/home/maru/Documents/Semana3/daily-engagement.csv')
project_submissions = read_csv('/home/maru/Documents/Semana3/project-submissions.csv')

##########################
# Estrutura das tabelas  #
##########################

# enrollments
# status | is_udacity | is_canceled | join_date | account_key | cancel_date | days_to_cancel

# daily_engagement
# lessons_completed | num_courses_visited | total_minutes_visited | projects_completed | acct | utc_date

# project_submissions
# lesson_key | processing_state | account_key | assigned_rating | completion_date | creation_date


from datetime import datetime as dt

# Takes a date as a string, and returns a Python datetime object.
# If there is no date given, returns None

# Função que formata o dado como "Date"
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')

# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.

# Função que formata o dado como inteiro ou nulo caso seja a opção
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# Os próximos 3 blocos aplicam as 2 funções anteriores no valores das 3 tabelas
# e atualizam os campos da tabela com os valores formatados

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

# Clean up the data types in the engagement table
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

# Clean up the data types in the submissions table
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

#####################################
#                 2                 #
#####################################

print '########################################################################'
print 'Parte 2\n'


## Find the total number of rows and the number of unique students (account keys)
## in each table.

unique_enrollment = []
for e in enrollments:
    if not e['account_key'] in unique_enrollment:
        unique_enrollment.append(e['account_key'])
print "enrollment: %s" % len(unique_enrollment)

unique_daily = []
for d in daily_engagement:
    if not d['acct'] in unique_daily:
        unique_daily.append(d['acct'])
print "daily_engagement: %s" % len(unique_daily)

unique_project = []
for p in project_submissions:
    if not p['account_key'] in unique_project:
        unique_project.append(p['account_key'])
print "unique_project: %s" % len(unique_project)

#####################################
#                 3                 #
#####################################

print '########################################################################'
print 'Parte 3\n'


## Rename the "acct" column in the daily_engagement table to "account_key".

## Trick to access dictionary values and lables
## >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
## >>> for k, v in knights.iteritems():
## ...     print k, v
## ...
## gallahad the pure
## robin the brave

for d in daily_engagement:
    d['account_key'] = d.pop('acct')

#daily_engagement[1000]

#####################################
#                 4                 #
#####################################

# CODIGO COMENTADO POIS DEMORA UM POUCO PARA RODAR

print '########################################################################'
print 'Parte 4\n'


## Find any one student enrollments where the student is missing from the daily engagement table.
## Output that enrollment.
#

# not_in = []
#

# for ae in enrollments:
#     for ad in daily_engagement:
#         if str(ae['account_key']) == str(ae_daily_engagement)
# for ae in enrollments:
#     for ad in daily_engagement:
#         if str(ad['account_key']) == str(ae['account_key']):
#             if not str(ad['account_key']) in not_in:
#                 not_in.append(str(ad['account_key']))
#             break
#
#
# print len(not_in)


#####################################
#                 5                 #
#####################################

## Find the number of surprising data points (enrollments missing from
## the engagement table) that remain, if any.
print '########################################################################'
print 'Parte 5\n'


problem = []
for students in enrollments:
    if not students['account_key'] in unique_daily and students['join_date'] != students['cancel_date']:
        problem.append(students['account_key'])
print 'problem: %s' % len(problem)


# Create a set of the account keys for all Udacity test accounts
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
len(udacity_test_accounts)

# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


# Remove Udacity test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print 'non_udacity_enrollments: %s' % len(non_udacity_enrollments)
print 'non_udacity_engagement: %s' % len(non_udacity_engagement)
print 'non_udacity_submissions: %s\n' % len(non_udacity_submissions)


#####################################
#                 6                 #
#####################################

## Create a dictionary named paid_students containing all students who either
## haven't canceled yet or who remained enrolled for more than 7 days. The keys
## should be account keys, and the values should be the date the student enrolled.

print '########################################################################'
print 'Parte 6\n'


paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
len(paid_students)

# Takes a student's join date and the date of a specific engagement record,
# and returns True if that engagement record happened within one week
# of the student joining.
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7 and time_delta.days >= 0

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

print '########################################################################'
print 'Parte 7\n'

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

# print(len(paid_enrollments))
# print(len(paid_engagement))
# print(len(paid_submissions))
# print '\n'

# paid_students_list=[]
# for key, date in paid_students.items():
#     paid_students_list.append(key)
#
# print len(paid_students_list)

from collections import defaultdict

paid_engagement_in_first_week = []

for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

from collections import defaultdict

# Create a dictionary of engagement grouped by student.
# The keys are account keys, and the values are lists of engagement records.
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)

total_minutes_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

import numpy as np

# Summarize the data about minutes spent in the classroom
total_minutes = total_minutes_by_account.values()
print 'total de minutos\n'
print 'Mean:', np.mean(total_minutes)
print 'Standard deviation:', np.std(total_minutes)
print 'Minimum:', np.min(total_minutes)
print 'Maximum:', np.max(total_minutes)
print '\n'

# print "length paid_engagement_in_first_week: %s" % len(paid_engagement_in_first_week)

print '########################################################################'
print 'Parte 9\n'

lessons_by_account = defaultdict(list)
for lessons_record in paid_engagement_in_first_week:
    account_key = lessons_record['account_key']
    lessons_by_account[account_key].append(lessons_record)

total_lessons_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_lessons = 0
    for lessons_record in engagement_for_student:
        total_lessons += lessons_record['lessons_completed']
    total_lessons_by_account[account_key] = total_lessons


total_lessons = total_lessons_by_account.values()
print 'total de licoes\n'
print 'Mean:', np.mean(total_lessons)
print 'Standard deviation:', np.std(total_lessons)
print 'Minimum:', np.min(total_lessons)
print 'Maximum:', np.max(total_lessons)
print '\n'

print '########################################################################'
print 'Parte 10\n'


def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

import numpy as np

def describe_data(data):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)


for engagement in paid_engagement_in_first_week:
    if engagement['num_courses_visited'] > 0:
        engagement['has_visited'] = 1
    else:
        engagement['has_visited'] = 0

engagement_by_student_first_week = group_data(paid_engagement_in_first_week, 'account_key')

total_days = sum_grouped_items(engagement_by_student_first_week, 'has_visited')
total_days = total_days.values()

print 'total de dias\n'
describe_data(total_days)
print '\n'

## Create two lists of engagement data for paid students in the first week.
## The first list should contain data for students who eventually pass the
## subway project, and the second list should contain data for students
## who do not.

print '########################################################################'
print 'Parte 11\n'

subway_project_lesson_keys = ['746169184', '3176718735']

pass_subway_project = set()

for submission in paid_submissions:
    project = submission['lesson_key']
    rating = submission['assigned_rating']

    if ((project in subway_project_lesson_keys) and
            (rating == 'PASSED' or rating == 'DISTINCTION')):
        pass_subway_project.add(submission['account_key'])

len(pass_subway_project)

passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print len(passing_engagement)
print len(non_passing_engagement)
print '\n'

print '########################################################################'
print 'Parte 12\n'

passing_engagement_by_account = group_data(passing_engagement, 'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')

## minutos
################################################################################
total_minutes_by_account = {}
for account_key, engagement_for_student in passing_engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

total_minutes_passing = total_minutes_by_account.values()
print 'minutes for passing students\n'
describe_data(total_minutes_passing)
print '\n'

total_minutes_by_account = {}
for account_key, engagement_for_student in non_passing_engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

total_minutes_non_passing = total_minutes_by_account.values()
print 'minutes for non passing students\n'
describe_data(total_minutes_non_passing)
print '\n'

## lessons
################################################################################
total_lessons_by_account = {}
for account_key, engagement_for_student in passing_engagement_by_account.items():
    total_lessons = 0
    for lessons_record in engagement_for_student:
        total_lessons += lessons_record['lessons_completed']
    total_lessons_by_account[account_key] = total_lessons

total_lessons_passing = total_lessons_by_account.values()
print 'lessons for passing students\n'
describe_data(total_lessons_passing)
print '\n'

total_lessons_by_account = {}
for account_key, engagement_for_student in non_passing_engagement_by_account.items():
    total_lessons = 0
    for lessons_record in engagement_for_student:
        total_lessons += lessons_record['lessons_completed']
    total_lessons_by_account[account_key] = total_lessons

total_lessons_non_passing = total_lessons_by_account.values()
print 'lessons for non passing students\n'
describe_data(total_lessons_non_passing)
print '\n'
## days
################################################################################
total_days = sum_grouped_items(passing_engagement_by_account, 'has_visited')
total_days = total_days.values()
print 'days for passing students\n'
describe_data(total_days)
print '\n'

total_days = sum_grouped_items(non_passing_engagement_by_account, 'has_visited')
total_days = total_days.values()
print 'days for NON passing students\n'
describe_data(total_days)
print '\n'


for key, records in passing_engagement_by_account.items():
    data = []
    for record in records:
        data.append(record['utc_date'])
    print data
