# 这个文件是为了求每个round中的capacity总和

def calculate_total_capacity(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    round_totals = {}
    current_round = None

    for line in lines:
        line = line.strip()
        if line.startswith("round"):
            parts = line.split(':')
            current_round = int(parts[0].split()[1])
            if current_round not in round_totals:
                round_totals[current_round] = 0
        elif line.startswith("path"):
            parts = line.split(',')
            for part in parts:
                if "capacity" in part:
                    capacity_value = int(part.split(':')[1].strip())
                    round_totals[current_round] += capacity_value

    return round_totals

# Specify the path to your file
file_path = 'margin_athena_3.txt'

# Calculate the total capacity for each round
round_totals = calculate_total_capacity(file_path)

# Print the results
for round_number, total_capacity in round_totals.items():
    print(f"Round {round_number}: Total Capacity = {total_capacity}")

# Optionally, you can save the results to a new file
output_file_path = 'round_totals.txt'
with open(output_file_path, 'w') as output_file:
    for round_number, total_capacity in round_totals.items():
        output_file.write(f"Round {round_number}: Total Capacity = {total_capacity}\n")