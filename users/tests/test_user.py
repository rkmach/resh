import pytest

from ..models import User   #testando o Usuario q eu criei

pytestmark = pytest.mark.django_db    #essa linha permite q o pytest tenha acesso ao BD. Sem isso aqui não funciona!

def test_create_user():
    user = User.objects.create_user(username = "milho", email = "milho@email.com", password = "1234")

    #checando se os dados que eu passei com a API de acesso são os dados que estão no banco
    assert user.username == "milho"
    assert user.email == "milho@email.com"

    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser


def test_create_superUser():
    superU = User.objects.create_superuser(username = "milho_adm", email = "milho_adm@email.com", password = "1234")

    assert superU.username == "milho_adm"
    assert superU.email == "milho_adm@email.com"

    assert superU.is_active
    assert superU.is_staff
    assert superU.is_superuser