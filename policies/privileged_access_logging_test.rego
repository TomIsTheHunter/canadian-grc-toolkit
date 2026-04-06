package canada.privileged_access_logging_test

import rego.v1

import data.canada.privileged_access_logging

test_valid_privileged_event if {
  privileged_access_logging.allow with input as {
    "event": {
      "actor_id": "admin-01",
      "mfa_verified": true,
      "log_destination": "siem-prod",
      "event_type": "privileged-login",
      "timestamp": "2026-04-06T12:00:00Z",
    },
  }
}

test_missing_mfa_and_bad_destination if {
  violations := privileged_access_logging.violation with input as {
    "event": {
      "actor_id": "admin-01",
      "mfa_verified": false,
      "log_destination": "local-disk",
      "event_type": "privileged-login",
      "timestamp": "2026-04-06T12:00:00Z",
    },
  }

  count(violations) == 2
}