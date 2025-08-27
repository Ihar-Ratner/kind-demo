from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Prometheus Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')
ACTIVE_REQUESTS = Gauge('http_requests_in_progress', 'Active HTTP requests')

# Custom business metrics
HELLO_COUNTER = Counter('hello_requests_total', 'Total hello endpoint requests')
TEST_COUNTER = Counter('test_requests_total', 'Total test endpoint requests')

@app.before_request
def before_request():
    """Track request start time and active requests"""
    request.start_time = time.time()
    ACTIVE_REQUESTS.inc()

@app.after_request
def after_request(response):
    """Track request completion metrics"""
    ACTIVE_REQUESTS.dec()
    
    # Calculate request duration
    duration = time.time() - request.start_time
    REQUEST_LATENCY.observe(duration)
    
    # Increment request count
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.endpoint,
        status=response.status_code
    ).inc()
    
    return response

@app.route("/test")
def test():
    TEST_COUNTER.inc()  # Increment the test counter
    return "Test message"

@app.route("/hello")
def hello():
    HELLO_COUNTER.inc()  # Increment the hello counter
    return "Hello message"

@app.route("/metrics")
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
