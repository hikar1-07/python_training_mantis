from conftest import app
import pytest
from model.project import Project
from data.project import testdata


@pytest.mark.parametrize("project", testdata, ids = [repr(x) for x in testdata])
def test_add_project(app, project):
    old_projects = app.project.get_project_list()
    app.project.create_project(project)
    old_projects.append(project)
    new_projects = app.project.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)