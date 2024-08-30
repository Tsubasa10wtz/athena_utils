size = 115 * 1024 * 1024
chunks = size / 131072
print(chunks)
time_per_chunk = 24 * 60 / chunks
print(time_per_chunk)