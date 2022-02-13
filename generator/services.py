import csv
import os

from celery import shared_task
from django.core.files.storage import default_storage
from faker import Faker

from .models import Scheme, SchemeColumn


@shared_task(bind=True)
def create_csv(self, scheme_id: int, *args, **kwargs):
	"""
	names - list of column names
	types - list of types
	creates a csv with given number of rows, header and types of data
	"""

	scheme = Scheme.objects.get(id=scheme_id)
	filename = f'fakecsv-{scheme.scheme_name}.csv'

	scheme.task_progress = "Processing"
	scheme.save()
	
	columns = SchemeColumn.objects.filter(scheme=scheme_id).order_by('order')

	with default_storage.open(filename, 'w') as csvfile:
		writer = csv.writer(csvfile)

		# header
		writer.writerow([column.name for column in columns])

		# generating fake elements
		for row in range(scheme.rows):
			writer.writerow([generate_fake_element(column.column_type, scheme_id) for column in columns])

	filename = f'fakecsv-{scheme.scheme_name}.csv'
	scheme.upload = filename
	scheme.task_progress = "Ready"
	scheme.save()


def generate_fake_element(data_type, scheme_id):
	"""
	generates one fake element based on its type
	"""
	fake = Faker()			
	if data_type == 1:
		return fake.name()
	if data_type == 2:
		return fake.job()
	if data_type == 3:
		return fake.email()
	if data_type == 4:
		return fake.domain_name()
	if data_type == 5:
		return fake.phone_number()
	if data_type == 6:
		return fake.company()
	if data_type == 7:
		scheme = Scheme.objects.get(id=scheme_id)
		number_of_sentences = scheme.quantity_of_sentences
		sentences = fake.sentences(number_of_sentences)
		return ' '.join(sentences)
	if data_type == 8:
		scheme = Scheme.objects.get(id=scheme_id)
		return fake.random_int(min=scheme.min_age,
                               max=scheme.max_age)
	if data_type == 9:
		return ' '.join(fake.address().split())
	if data_type == 10:
		return fake.date()


def make_csv(scheme_id):
	scheme = Scheme.objects.get(id=scheme_id)
	create_csv.delay(scheme_id=scheme_id)









	
