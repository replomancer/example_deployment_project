import pytest
from .models import Something


@pytest.fixture(autouse=True)
def _use_static_files_storage(settings):
    settings.STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )


@pytest.fixture
def something():
    return Something.objects.create(message="That's something!")


@pytest.mark.django_db()
def test_sanity_check(something):
    assert something is not None


def test_view(client):
    response = client.get('/')
    assert response.status_code == 200
    assert '<img src="/static/images/python.gif">' in str(response.content)
