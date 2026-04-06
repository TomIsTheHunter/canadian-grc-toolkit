package canada.data_residency

import rego.v1

default allow := false

allow if {
  count(violation) == 0
}

violation contains {
  "msg": msg,
  "resource_id": resource.id,
} if {
  resource := input.resource
  not resource.region in data.allowed_regions.canadian_regions
  msg := sprintf("resource region %q is outside approved Canadian regions", [resource.region])
}

violation contains {
  "msg": msg,
  "resource_id": resource.id,
  "replication_region": replica,
} if {
  resource := input.resource
  replica := resource.replication[_]
  not replica in data.allowed_regions.canadian_regions
  msg := sprintf("replication region %q is outside approved Canadian regions", [replica])
}