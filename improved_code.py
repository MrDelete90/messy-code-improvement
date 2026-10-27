def classify_product(first_number, second_number, multiplier):
    """Return a size label based on (first_number + second_number) * multiplier.

    The product is classified as:
    - "big" if it is greater than 100
    - "medium" if it is greater than 50
    - "small" otherwise
    """
    total = first_number + second_number
    product = total * multiplier

    if product > 100:
        return "big"
    if product > 50:
        return "medium"
    return "small"


# Sum the sample numbers and classify two example products.
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
print(classify_product(10, 20, 3))
print(classify_product(5, 5, 2))
