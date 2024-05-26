from timeit import default_timer as timer
from datetime import timedelta
import random

def countOccurrences(numbers: list[int]) -> bool: 
    """
    The function uses a nested loop where the outer loop iterates through each value in the list, 
    and the inner loop iterates through the list again to count the occurrences of the current value.
    It uses the 'checked_numbers' list to avoid checking the same value several times.

    Time Complexity: O(n^2)

    Parameters:
    numbers: list[int]: list of integer numbers

    Returns:
    bool: true if the function ends
    """
    checkedNumbers = list()
    occurrencesResult = list()

    for i in range(len(numbers)):
        currentValue = numbers[i]
        if currentValue not in checkedNumbers:
            checkedNumbers.append(currentValue)
            count = 1
            for j in range(len(numbers)):
                if currentValue == numbers[j] and i != j:
                    count += 1
            occurrencesResult.append(f"{currentValue}: {count}")
    
    print(f"Output: {', '.join(occurrencesResult)}")

    return True


def countOccurrences_Optimized(numbers: list[int]) -> bool:
    """
    The function iterates through the list only once, checking for each value in the list.
    It uses the 'occurrences' dictionary to check and count each value in constant time.

    Time Complexity: O(n)

    Parameters:
    numbers: list[int]: list of integer numbers

    Returns:
    bool: true if the function ends
    """
    occurrences = dict()

    for i in range(len(numbers)):
        currentValue = numbers[i]
        if currentValue not in occurrences:
            occurrences[currentValue] = 1
        else:
            occurrences[currentValue] += 1
    
    print(f"Output: {occurrences}")

    return True


def generateRandomList(startValue: int, endValue: int, size: int) -> list[int]:
    """
    The function generates a random list of integer numbers by using random.randint().

    Parameters:
    startValue: start value to generate random numbers
    endValue: end value to generate random numbers
    size: length of the list to be generated

    Returns:
    test_numbers: list[int]: list of random integer numbers
    """
    numbers = list()

    for i in range(size):
        numbers.append(random.randint(startValue, endValue))

    return numbers


def main():
    print("Performance Test of three different functions to count occurrences of each value in a list\n")

    # Set startValue, endValue, size and call generateRandomList to get the list for the tests
    startValue = 1
    endValue = 10
    size = 1000
    test_numbers = generateRandomList(startValue, endValue, size)
    print(f"Generated list: {test_numbers}", end="\n\n")
    
    # First function's performance test
    startTime = timer()
    countOccurrences(test_numbers)
    endTime = timer()
    timeDelta = timedelta(seconds = endTime - startTime)
    print(f"The first function took {timeDelta} to complete", end="\n\n")
    
    # Second function's performance test
    startTime = timer()
    countOccurrences_Optimized(test_numbers)
    endTime = timer()
    timeDelta = timedelta(seconds = endTime - startTime)
    print(f"The second function took {timeDelta} to complete", end="\n\n")


if __name__ == "__main__":
    main()
