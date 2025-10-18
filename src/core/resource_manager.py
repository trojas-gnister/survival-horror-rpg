"""Resource management and calculations."""

from typing import Dict, Any


class ResourceManager:
    """
    Manages resource calculations and drain rates.

    START HERE:
    1. Handles resource drain calculations
    2. Validates resource changes
    3. Checks critical levels
    4. Calculates consequences
    """

    # Resource limits
    MAX_FUEL = 100.0
    MAX_BATTERY = 100.0
    MAX_SANITY = 100.0
    MAX_TRUST = 100.0
    MIN_TRUST = -100.0

    # Critical thresholds
    CRITICAL_FUEL = 20.0
    CRITICAL_BATTERY = 30.0
    CRITICAL_SANITY = 40.0
    CRITICAL_TRUST = -50.0

    def calculate_call_fuel_cost(self, duration_seconds: int) -> float:
        """
        Calculate fuel cost for a radio call.

        START HERE:
        1. Base rate: ~2% per minute during calls
        2. Convert duration to minutes
        3. Calculate fuel cost
        4. Return the cost

        Args:
            duration_seconds: Call duration in seconds

        Returns:
            Fuel cost percentage
        """
        # TODO: Implement fuel cost calculation
        return 0.0

    def calculate_nightly_drain(self, night: int) -> Dict[str, float]:
        """
        Calculate nightly resource drain.

        START HERE:
        1. Fuel drains ~0.5% per minute ambient
        2. Sanity may decrease based on events
        3. Difficulty scaling: harder = more drain
        4. Later nights = increased drain
        5. Return dict with drain amounts

        Args:
            night: Current night number

        Returns:
            Dict with resource drain amounts
        """
        # TODO: Implement nightly drain calculation
        return {
            "fuel": 0.0,
            "battery": 0.0,
            "sanity": 0.0,
        }

    def clamp_value(self, value: float, min_val: float, max_val: float) -> float:
        """
        Clamp a value between min and max.

        START HERE:
        1. Use min() and max() to clamp
        2. Return clamped value

        Args:
            value: Value to clamp
            min_val: Minimum value
            max_val: Maximum value

        Returns:
            Clamped value
        """
        # TODO: Implement clamp_value
        return value

    def is_critical_fuel(self, fuel: float) -> bool:
        """Check if fuel is at critical level."""
        return fuel <= self.CRITICAL_FUEL

    def is_critical_battery(self, battery: float) -> bool:
        """Check if battery is at critical level."""
        return battery <= self.CRITICAL_BATTERY

    def is_critical_sanity(self, sanity: float) -> bool:
        """Check if sanity is at critical level."""
        return sanity <= self.CRITICAL_SANITY

    def is_critical_trust(self, trust: float) -> bool:
        """Check if trust is at critical level."""
        return trust <= self.CRITICAL_TRUST

    def check_game_over_conditions(
        self,
        fuel: float,
        sanity: float,
        food: int,
    ) -> tuple[bool, str]:
        """
        Check if any game over conditions are met.

        START HERE:
        1. Check if fuel <= 0 (freeze to death)
        2. Check if sanity <= 0 (breakdown)
        3. Check if food <= 0 (starvation)
        4. Return (is_game_over, reason)

        Args:
            fuel: Current fuel level
            sanity: Current sanity level
            food: Days of food remaining

        Returns:
            Tuple of (game_over: bool, reason: str)
        """
        # TODO: Implement game over check
        return (False, "")


# Global resource manager instance
resource_manager = ResourceManager()
