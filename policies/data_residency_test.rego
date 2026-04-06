package canada.data_residency_test

import rego.v1

import data.canada.data_residency

# Should pass - resource in Canada.
test_valid_canadian_region if {
  data_residency.allow with input as {
    "resource": {
      "id": "prod-db-01",
      "region": "ca-central-1",
      "replication": [],
    },
  } with data.allowed_regions.canadian_regions as ["ca-central-1", "ca-west-1"]
}

# Should fail - resource outside Canada.
test_invalid_region_violation if {
  violations := data_residency.violation with input as {
    "resource": {
      "id": "prod-db-01",
      "region": "us-east-1",
      "replication": [],
    },
  } with data.allowed_regions.canadian_regions as ["ca-central-1", "ca-west-1"]

  count(violations) == 1
}