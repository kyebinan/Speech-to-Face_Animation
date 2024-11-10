#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <input_video> <segment_file> <output_dir> <counter>"
    exit 1
fi

# Assign command-line arguments to variables
input_video="$1"
segment_file="$2"
output_dir="$3"
counter="$4"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Counter to keep track of segment numbers
segment_number="$counter"

# Loop through each line in the segment file
while IFS=, read -r start_time duration; do
    output_file="${output_dir}/biden_${segment_number}.mp4"
    echo "Extracting segment ${segment_number}: start at ${start_time} for duration ${duration}"

    # Use ffmpeg to extract the segment with specified start time and duration
    ffmpeg -i "$input_video" -ss "$start_time" -t "$duration" -c copy "$output_file" -y

    echo "Segment ${segment_number} saved as ${output_file}"
    ((segment_number++))
done < "$segment_file"

echo "All segments extracted to $output_dir"
