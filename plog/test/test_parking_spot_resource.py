def test_get_parking_spot(client):
    response = client.get("/api/v1/spot")
    assert response.status_code == 200
    print(response.text)
