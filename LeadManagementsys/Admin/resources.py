from import_export import resources
from SuperAdmin.models import LeadCreate

class LeadResource(resources.ModelResource):
    class Meta:
        model = LeadCreate