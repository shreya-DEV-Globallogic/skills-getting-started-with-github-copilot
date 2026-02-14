"""Test configuration and fixtures for FastAPI tests."""
import pytest
import sys
from pathlib import Path

# Add the src directory to the path so we can import app.py
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from fastapi.testclient import TestClient
from app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the activities database before each test."""
    # Store original state
    original_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for varsity and intramural play",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["alex@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Learn tennis skills and participate in friendly matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["james@mergington.edu", "lucy@mergington.edu"]
        },
        "Drama Club": {
            "description": "Perform in theatrical productions and develop acting skills",
            "schedule": "Saturdays, 2:00 PM - 4:00 PM",
            "max_participants": 25,
            "participants": ["grace@mergington.edu", "noah@mergington.edu"]
        },
        "Photography Club": {
            "description": "Explore photography techniques and create artistic visual content",
            "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
            "max_participants": 18,
            "participants": ["ava@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and critical thinking through competitive debate",
            "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
            "max_participants": 14,
            "participants": ["mason@mergington.edu", "harper@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore scientific concepts through hands-on projects",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["ethan@mergington.edu"]
        }
    }
    
    # Reset activities dict to original state
    activities.clear()
    activities.update(original_activities)
    
    yield
    
    # Cleanup after test
    activities.clear()
    activities.update(original_activities)
