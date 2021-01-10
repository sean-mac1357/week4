# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.
# candies = [2,3,5,1,3]
# extraCandies = 3
# Expected output: [true, true, true, false, true]

candies = [2, 3, 5, 1, 3, 8, 2, 6, 4, 1, 3]
extraCandies = 3


def get_highest_candy(list):
    i = 0
    highest_candies = 0
    while i < len(list):
        if list[i] > highest_candies:
            highest_candies = candies[i]
        i += 1
    return highest_candies

def check_each_kid(list, highest, extra_candies):
    i = 0
    new_highest_list = []
    while i < len(candies):
        if list[i] + extra_candies >= highest:
            new_highest_list.append(True)
        else:
            new_highest_list.append(False)
        i += 1
    return(new_highest_list)

highest_candies = get_highest_candy(candies)

new_highest_list = check_each_kid(candies, highest_candies, extraCandies)

print(new_highest_list)