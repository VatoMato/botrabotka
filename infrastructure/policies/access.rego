# infrastructure/policies/access.rego
package httpapi.authz

default allow = false

allow {
    input.method == "GET"
    allowed_paths[input.path]
}

allowed_paths = {
    "/healthz",
    "/metrics"
}