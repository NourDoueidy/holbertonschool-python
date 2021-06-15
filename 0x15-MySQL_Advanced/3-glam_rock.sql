-- Old school bands 
-- List all bands with Glam as their main style, ranked by their longevity
SELECT band_name, COALESCE(split, 2021) - formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam%' ORDERED BY lifespan DESC;
