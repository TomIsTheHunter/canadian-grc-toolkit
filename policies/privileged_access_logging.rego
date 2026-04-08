package canada.privileged_access_logging

import rego.v1

required_fields := {
  "actor_id",
  "mfa_verified",
  "log_destination",
  "event_type",
  "timestamp",
}

approved_log_destinations := {
  "siem-prod",
  "immutable-audit-store",
}

default allow := false

allow if {
  count(violation) == 0
}

violation contains {"msg": msg} if {
  evt := input.event
  field := required_fields[_]
  not field in object.keys(evt)
  msg := sprintf("missing required field %q", [field])
}

violation contains {"msg": "mfa_verified must be true"} if {
  evt := input.event
  evt.mfa_verified != true
}

violation contains {"msg": msg} if {
  evt := input.event
  not evt.log_destination in approved_log_destinations
  msg := sprintf("unapproved log destination %q", [evt.log_destination])
}