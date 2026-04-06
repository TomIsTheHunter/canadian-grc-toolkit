package canada.encryption_at_rest_test

import rego.v1

import data.canada.encryption_at_rest

test_valid_encryption_configuration if {
  encryption_at_rest.allow with input as {
    "resource": {
      "id": "storage-001",
      "sensitive": true,
      "encryption": {
        "enabled": true,
        "algorithm": "AES256",
        "cmk": true,
        "rotation_enabled": true,
      },
    },
  }
}

test_invalid_sensitive_resource_configuration if {
  violations := encryption_at_rest.violation with input as {
    "resource": {
      "id": "storage-001",
      "sensitive": true,
      "encryption": {
        "enabled": true,
        "algorithm": "DES",
        "cmk": false,
        "rotation_enabled": false,
      },
    },
  }

  count(violations) == 3
}