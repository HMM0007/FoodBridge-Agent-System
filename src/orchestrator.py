"""
orchestrator.py
---------------
Combines all agent outputs into a unified pipeline.
"""

from agents import (
    SurplusIntakeAgent,
    NGOMatchingAgent,
    LogisticsAgent,
    ImpactEstimationAgent
)

class FoodBridgeOrchestrator:
    """Controls the full multi-agent workflow."""

    def __init__(self):
        self.intake = SurplusIntakeAgent()
        self.matching = NGOMatchingAgent()
        self.logistics = LogisticsAgent()
        self.impact = ImpactEstimationAgent()

    def run(self, request: dict) -> dict:
        # Step 1: Intake processing
        intake_result = self.intake.validate(request)

        # Step 2: NGO matchmaking
        match = self.matching.match(
            intake_result["food_type"], intake_result["quantity"]
        )

        if "error" in match:
            return match

        # Step 3: Logistics planning
        logistics = self.logistics.plan_pickup(match["ngo_name"])

        # Step 4: Impact calculation
        impact = self.impact.compute_impact(intake_result["quantity"])

        # Final response
        return {
            "intake": intake_result,
            "ngo_match": match,
            "logistics": logistics,
            "impact": impact
        }
