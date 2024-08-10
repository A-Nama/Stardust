import ee

# Initialize Earth Engine
ee.Initialize()

def get_light_pollution_data(bounds):
    # Fetch the VIIRS Nighttime Lights image collection
    image = ee.ImageCollection('NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG') \
        .filterBounds(bounds) \
        .filterDate('2024-01-01', '2024-08-01')  # Adjust date range as needed
        .mean()  # Compute the mean value over the date range

    # Extract light pollution data by reducing over the region
    light_pollution_stats = image.reduceRegion(
        reducer=ee.Reducer.mean(),  # Calculate mean light pollution
        geometry=bounds,             # Use the provided bounds
        scale=1000,                  # Scale in meters (adjust based on desired resolution)
        maxPixels=1e13               # Maximum number of pixels to process
    )
    
    # Get the light pollution value (assuming 'avg_rad' is the relevant band)
    light_pollution_value = light_pollution_stats.get('avg_rad').getInfo()

    return {
        'light_pollution': light_pollution_value
    }

# Example usage
light_pollution_data = get_light_pollution_data(bounds)
print(light_pollution_data)
