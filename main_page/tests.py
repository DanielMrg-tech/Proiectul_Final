import pytest
from django.template.defaultfilters import title

from main_page.models import Meniu
from django.contrib.auth import get_user_model

# Create your tests here.

@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username="daniel", password="daniel123456789")


@pytest.fixture
def logged_in_client(client, user):
    client.login(username="daniel", password="daniel123456789")
    return client

def test_meniu_creation(db, user):
    saved_meniu = Meniu.objects.create(title="Meniu basic", produs = "Test", meniu_number = 2, created_by = user)

    db_meniu = Meniu.objects.first()
    assert saved_meniu.title == db_meniu.title


@pytest.fixture
def meniu_obj(user):
    meniu1 = Meniu(title="Paste Carbonara", produs = "rosi", meniu_number = 2, created_by = user)
    meniu1.save()
    return meniu1

def test_check_thing1(meniu_obj):
    assert meniu_obj.title == "Paste Carbonara"
    assert True

def test_check_meniu(meniu_obj):
    assert meniu_obj.produs == "rosi"

def test_delete_meniu_confirm_page(logged_in_client, meniu_obj):
    url = '/meniu/{}/delete/'.format(meniu_obj.pk)

    response = logged_in_client.get(url)
    print(response)

@pytest.mark.django_db
def test_cannot_edit_without_login(client, meniu_obj):
    url = '/meniu/{}/edit/'.format(meniu_obj.pk)
    response = client.get(url)
    assert response.status_code in [302, 403]

def test_meniu_str(user):
    meniu = Meniu.objects.create(
        title="Salată Caesar",
        produs="salată",
        meniu_number=5,
        created_by=user
    )
    assert str(meniu) == "Salată Caesar, by salată, number 5"