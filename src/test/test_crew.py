import pytest

from flask import url_for

def test_show(client):
    res = client.get(url_for('crew.show'))
    assert res.status_code == 200
