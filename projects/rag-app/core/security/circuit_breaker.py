import logging
import time

logger = logging.getLogger(__name__)

class CircuitBreaker:
    """
    Rapidly fails requests and sheds load when downstream dependencies become unresponsive.
    Mitigates: cascading_failure, queue_saturation, agent_deadlock
    """

    def __init__(self, failure_threshold: int = 3, reset_timeout: int = 30):
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.state = "HALF_OPEN"
                logger.info("CircuitBreaker transitioned to HALF_OPEN")
            else:
                logger.error("CircuitBreaker OPEN - Fast failing request")
                raise Exception("CircuitBreaker is OPEN. Downstream dependency is unavailable.")

        try:
            result = func(*args, **kwargs)
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
                logger.info("CircuitBreaker transitioned to CLOSED")
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
                logger.warning(f"CircuitBreaker OPENED due to consecutive failures. Threshold: {self.failure_threshold}")
            raise e
