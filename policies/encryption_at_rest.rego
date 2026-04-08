package canada.encryption_at_rest

import rego.v1

approved_algorithms := {
  "AES256",
  "aws:kms",
}

default allow := false

allow if {
  count(violation) == 0
}

violation contains {"msg": msg} if {
  resource := input.resource
  not resource.encryption.enabled
  msg := "encryption at rest must be enabled"
}

violation contains {"msg": msg} if {
  resource := input.resource
  algo := resource.encryption.algorithm
  not algo in approved_algorithms
  msg := sprintf("algorithm %q is not approved", [algo])
}

violation contains {"msg": msg} if {
  resource := input.resource
  resource.sensitive == true
  resource.encryption.cmk != true
  msg := "sensitive resources must use customer-managed keys (CMK)"
}

violation contains {"msg": msg} if {
  resource := input.resource
  resource.encryption.rotation_enabled != true
  msg := "key rotation must be enabled"
}