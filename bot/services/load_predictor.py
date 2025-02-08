# bot/services/load_predictor.py
import numpy as np
import tensorflow as tf
from prometheus_api_client import PrometheusConnect

class LoadPredictor:
    def __init__(self):
        self.model = tf.keras.models.load_model('models/load_forecast.h5')
        self.prom = PrometheusConnect(url="http://prometheus:9090")
    
    def get_metrics(self):
        cpu_query = 'sum(rate(container_cpu_usage_seconds_total{container="bot"}[5m]))'
        return self.prom.custom_query([cpu_query])
    
    async def predict_load(self):
        metrics = self.get_metrics()
        sequence = np.array([m['value'] for m in metrics]).reshape(1, -1, 1)
        prediction = self.model.predict(sequence)
        return prediction[0][0]