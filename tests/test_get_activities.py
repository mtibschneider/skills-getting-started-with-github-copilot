def test_get_activities_returns_200(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    assert response.status_code == 200


def test_get_activities_returns_expected_count(client):
    # Arrange
    endpoint = "/activities"
    expected_count = 9

    # Act
    response = client.get(endpoint)
    activities = response.json()

    # Assert
    assert response.status_code == 200
    assert len(activities) == expected_count


def test_get_activities_has_required_fields(client):
    # Arrange
    endpoint = "/activities"
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get(endpoint)
    activities = response.json()

    # Assert
    assert response.status_code == 200
    for activity_details in activities.values():
        assert required_fields.issubset(activity_details.keys())
