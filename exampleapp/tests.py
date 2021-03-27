from django.test import TestCase
import pytest
from .models import Something


@pytest.fixture
def something():
    return Something.objects.create(message="That's something!")


@pytest.mark.django_db
def test_cheating(something):
    assert something is not None
