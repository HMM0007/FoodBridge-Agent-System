"""
agents.py
---------
Contains all FoodBridge agent classes used in the multi-agent workflow:
- SurplusIntakeAgent
- NGOMatchingAgent
- LogisticsAgent
- ImpactEstimationAgent
"""

import math
import random

class SurplusIntakeAgent:
    """Extracts and validates surplus food information."""
    
    def validate(self, data: dict) -> dict:
        if not data.get("food_type") or not data.get("quantity"):
            raise ValueError("Invalid input — food_type and quantity required.")
        
        return {
            "food_type": data["food_type"].title(),
            "quantity": int(data["quantity"])
        }


class NGOMatchingAgent:
    """Matches surplus food with a suitable NGO."""

    def __init__(self):
        self.ngo_db = [
            {"name": "Helping Hands", "capacity": 80, "food_needs": ["Rice", "Vegetables"]},
            {"name": "Community Care", "capacity": 120, "food_needs": ["Bread", "Fruits"]},
            {"name": "Hunger Relief Center", "capacity": 150, "food_needs": ["Rice", "Fruits", "Vegetables"]}
        ]
    
    def match(self, food_type: str, quantity: int) -> dict:
        for ngo in self.ngo_db:
            if food_type in ngo["food_needs"] and quantity <= ngo["capacity"]:
                return {
                    "ngo_name": ngo["name"],
                    "capacity": ngo["capacity"],
                    "accepted_food": food_type
                }
        return {"error": "No suitable NGO found"}


class LogisticsAgent:
    """Suggests pickup logistics and estimates delivery time."""
    
    def estimate_eta(self, distance_km: float) -> float:
        return round(distance_km / 25 * 60, 2)  # minutes

    def plan_pickup(self, ngo_name: str) -> dict:
        distance = random.uniform(2.0, 10.0)
        eta = self.estimate_eta(distance)
        return {
            "ngo_name": ngo_name,
            "distance_km": round(distance, 2),
            "eta_minutes": eta
        }


class ImpactEstimationAgent:
    """Estimates meals saved and waste reduced."""
    
    def compute_impact(self, quantity: int) -> dict:
        meals_saved = quantity * 2
        waste_reduced_kg = round(quantity * 0.45, 2)
        return {
            "meals_saved": meals_saved,
            "waste_reduced_kg": waste_reduced_kg
        }
