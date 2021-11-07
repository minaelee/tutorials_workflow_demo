from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial


@pytest.mark.django_db
def test_homepage_access(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial


@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# @pytest.mark.django_db
# def test_create_tutorial(tutorial):
    # tutorial = Tutorial.objects.create(
    #     title='Pytest',
    #     tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
    #     description='Tutorial on how to apply pytest to a Django application',
    #     published=True
    # )
    # assert tutorial.title == "Pytest"


def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()


def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()


def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk
