import logging

logger = logging.getLogger(__name__)

class SecurityScorecard:
    """
    Generates a high-level scorecard for the DevSecOps pipeline and runtime health.
    """

    def __init__(self, tracker):
        self.tracker = tracker

    def generate_report(self) -> str:
        metrics = self.tracker.get_metrics()
        
        total = metrics["total_requests"]
        if total == 0:
            return "No data to generate scorecard."

        intercept_rate = (metrics["security_intercepts"] / total) * 100
        failover_rate = (metrics["reliability_failovers"] / total) * 100
        circuit_break_rate = (metrics["resilience_circuit_breaks"] / total) * 100
        
        report = f"""
        ========================================
        🛡️  AI-Model-Atlas Security Scorecard 🛡️
        ========================================
        Total Requests: {total}
        Average Latency: {metrics["average_latency_ms"]:.2f} ms
        
        Security Intercept Rate: {intercept_rate:.2f}%
        Reliability Failover Rate: {failover_rate:.2f}%
        Resilience Circuit Break Rate: {circuit_break_rate:.2f}%
        ========================================
        """
        logger.info("Scorecard generated.")
        return report
