import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class TelemetryTracker:
    """
    Real-time tracking of runtime metrics (latency, throughput, errors).
    """

    def __init__(self):
        self.metrics = {
            "total_requests": 0,
            "security_intercepts": 0,
            "reliability_failovers": 0,
            "resilience_circuit_breaks": 0,
            "latency_ms_history": []
        }

    def record_request(self):
        self.metrics["total_requests"] += 1

    def record_intercept(self, category: str):
        if category == "security":
            self.metrics["security_intercepts"] += 1
        elif category == "reliability":
            self.metrics["reliability_failovers"] += 1
        elif category == "resilience":
            self.metrics["resilience_circuit_breaks"] += 1

    def record_latency(self, latency_ms: float):
        self.metrics["latency_ms_history"].append(latency_ms)
        if len(self.metrics["latency_ms_history"]) > 1000:
            self.metrics["latency_ms_history"].pop(0)

    def get_metrics(self) -> Dict[str, Any]:
        avg_latency = 0.0
        if self.metrics["latency_ms_history"]:
            avg_latency = sum(self.metrics["latency_ms_history"]) / len(self.metrics["latency_ms_history"])
            
        return {
            "total_requests": self.metrics["total_requests"],
            "security_intercepts": self.metrics["security_intercepts"],
            "reliability_failovers": self.metrics["reliability_failovers"],
            "resilience_circuit_breaks": self.metrics["resilience_circuit_breaks"],
            "average_latency_ms": avg_latency
        }
