# infrastructure/policies/order_policy.rego
package order.policy

default allow_close = false

allow_close {
    input.user.role == "admin"
}

allow_close {
    input.order.status == "completed"
    time.now_ns() - input.order.completed_at < 3*3600*1e9
}