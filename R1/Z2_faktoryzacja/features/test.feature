Feature: z2_tests

Scenario: test_functionality
  Given test_not_a_number with 'asr'
  Given test_null with ''
  Given test_not_a_int with '{}"|:"|:"'
  Given test_zero with 0
  Given test_negative_int with -18
  Given test_prime_number with 11
  Given test_not_a_prime_number with 3958159172
