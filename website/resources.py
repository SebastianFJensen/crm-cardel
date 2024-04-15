from import_export import resources
from .models import Record

class RecordResource(resources.ModelResource):
	class meta:
		model = Record