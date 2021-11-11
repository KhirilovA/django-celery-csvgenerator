import csv
import os

from celery import shared_task
from django.core.files.storage import default_storage
from faker import Faker

from .models import Scheme


@shared_task(bind=True)
def create_csv(self, names: list, types: list, scheme_id: int, *args, **kwargs):
	"""
	names - list of column names
	types - list of types
	creates a csv with given number of rows, header and types of data
	"""

	scheme = Scheme.objects.get(pk=scheme_id)
	filename = f'fakecsv-{scheme.scheme_name}.csv'

	scheme.task_progress = "Processing"
	scheme.save()
	
	with default_storage.open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=names)
		writer.writeheader()

		for row in range(scheme.rows):
			data_dict = {}
			for column_name, data_type in zip(names, types):
				data_dict[column_name] = generate_fake_element(data_type, scheme_id)

			writer.writerow(data_dict)

	filename = f'fakecsv-{scheme.scheme_name}.csv'
	scheme.upload = filename
	scheme.task_progress = "Ready"
	scheme.save()


def generate_fake_element(data_type, scheme_id):
	"""
	generates one fake element based on its type
	"""
	fake = Faker()
	scheme = Scheme.objects.get(pk=scheme_id)
	number_of_sentences = scheme.quantity_of_sentences			
	if data_type == '2':
		return fake.name()
	if data_type == '3':
		return fake.job()
	if data_type == '4':
		return fake.email()
	if data_type == '5':
		return fake.domain_name()
	if data_type == '6':
		return fake.phone_number()
	if data_type == '7':
		return fake.company()
	if data_type == '8':
		sentences = fake.sentences(number_of_sentences)
		return ' '.join(sentences)
	if data_type == '9':
		return fake.random_int(min=scheme.min_age,
                               max=scheme.max_age)
	if data_type == '10':
		return ' '.join(fake.address().split())
	if data_type == '11':
		return fake.date()


def make_csv(scheme_id):
	"""
	makes lists of names and types and orders them
	also clears the data from unfilled fields
	"""
	scheme = Scheme.objects.get(pk=scheme_id)
	
	types = [scheme.choice1, scheme.choice2, scheme.choice3, scheme.choice4,
			scheme.choice5, scheme.choice6, scheme.choice7, scheme.choice8,
			scheme.choice9, scheme.choice10]

	names = [scheme.name1, scheme.name2, scheme.name3, scheme.name4,
			scheme.name5, scheme.name6, scheme.name7, scheme.name8,
			scheme.name9, scheme.name10]

	orders = [scheme.order1, scheme.order2, scheme.order3, scheme.order4,
			scheme.order5, scheme.order6, scheme.order7, scheme.order8,
			scheme.order9, scheme.order10]

	while '1' in types:
		types.remove('1')
	while 'None' in names:
		names.remove('None')
	while 0 in orders:
		orders.remove(0)


	types = [value for order, value in sorted(zip(orders,types))]
	names = [value for order, value in sorted(zip(orders,names))]


	create_csv.delay(names=names, types=types, scheme_id=scheme_id)









	
