from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            soap_projects = client.service.mc_projects_get_user_accessible(username, password)
            projects = []
            for soap_project in soap_projects:
                projects.append(
                    Project(
                        name=soap_project.name,
                        description=soap_project.description,
                        id=str(soap_project.id)
                    )
                )
            return projects

        except WebFault:
            return None