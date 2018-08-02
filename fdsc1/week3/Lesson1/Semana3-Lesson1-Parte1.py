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

## Find any one student enrollments where the student is missing from the daily engagement table.
## Output that enrollment.

# not_in = []
#
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

problem = []
for students in enrollments:
    if not students['account_key'] in unique_daily and students['join_date'] != students['cancel_date']:
        problem.append(students['account_key'])
print len(problem)


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

print len(non_udacity_enrollments)
print len(non_udacity_engagement)
print len(non_udacity_submissions)


#####################################
#                 6                 #
#####################################

## Create a dictionary named paid_students containing all students who either
## haven't canceled yet or who remained enrolled for more than 7 days. The keys
## should be account keys, and the values should be the date the student enrolled.

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
