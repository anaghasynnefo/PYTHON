def find_max(numbers):
    if not numbers:
        return None
    max_number=numbers[0]
    for num in numbers:
        if num>max_number:
            max_number=num
        return max_number
       