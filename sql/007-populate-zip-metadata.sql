-- CX-08 / 007
-- Derived from: middle-math/schemas/zip-metadata-schema.md (population script)

INSERT INTO zip_metadata (zip_code, order_position, axis_position, type_position, color_position)
SELECT
  CONCAT(o::text, a::text, t::text, c::text) AS zip_code,
  o AS order_position,
  a AS axis_position,
  t AS type_position,
  c AS color_position
FROM
  generate_series(1, 7) AS o,
  generate_series(1, 6) AS a,
  generate_series(1, 5) AS t,
  generate_series(1, 8) AS c
ON CONFLICT (zip_code) DO NOTHING;

-- Verification query (should return 1680 after a clean first run)
SELECT COUNT(*) AS zip_metadata_count FROM zip_metadata;
