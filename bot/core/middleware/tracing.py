# bot/core/middleware/tracing.py
from opentelemetry import trace
from opentelemetry.semconv.trace import SpanAttributes
from aiogram import Dispatcher
from aiogram.types import Update

class TracingMiddleware:
    async def on_pre_process_update(self, update: Update, data: dict):
        tracer = trace.get_tracer(__name__)
        ctx = trace.get_current_span().get_span_context()
        with tracer.start_as_current_span(
            "telegram_update",
            context=ctx,
            attributes={
                SpanAttributes.MESSAGING_SYSTEM: "telegram",
                "update_type": update.event_type
            }
        ):
            data['span'] = trace.get_current_span()

    @classmethod
    def setup(cls, dp: Dispatcher):
        dp.middleware.setup(cls())