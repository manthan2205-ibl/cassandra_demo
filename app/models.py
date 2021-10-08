from django.db import models

# Create your models here.

import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class ExampleModel(DjangoCassandraModel):
    example_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
    example_type = columns.Integer(index=True)
    created_at   = columns.DateTime()
    description  = columns.Text(required=False)



from cassandra.cqlengine.models import Model
class Person(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    first_name  = columns.Text()
    last_name = columns.Text()


# kevin = Person.create(first_name="Kevin", last_name="Deldycke")
# dict(kevin)  # returns {'first_name': 'Kevin', 'last_name': 'Deldycke'}
# kevin['first_name']  # returns 'Kevin'
# kevin.keys()  # returns ['first_name', 'last_name']
# kevin.values()  # returns ['Kevin', 'Deldycke']
# kevin.items()  # returns [('first_name', 'Kevin'), ('last_name', 'Deldycke')]

# kevin['first_name'] = 'KEVIN5000'  # changes the models first name