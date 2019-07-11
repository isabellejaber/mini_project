day_rating = 0
bonus_points = 0

# base factors
rate_your_sleep = int(input("Rate your sleep. 1 being the worst and 10 being the best:"))
day_rating += int(rate_your_sleep)
        
rate_your_breakfast = int(input("Rate your breakfast. 1 being the worst and 5 being the best:"))
day_rating += int(rate_your_breakfast)

rate_your_lunch = int(input("Rate your lunch. 1 being the worst and 5 being the best:"))
day_rating += int(rate_your_lunch)

rate_your_dinner = int(input("Rate your dinner. 1 being the worst and 5 being the best:"))
day_rating += int(rate_your_dinner)

rate_your_exercise = int(input("Please rate how your exercise effected your day with -5 to -1 to indicate the degree of negative impact and 1 to 5 to indicate the degree of positive impact and 0 being no impact"))
day_rating += int(rate_your_exercise)

rate_your_commute = int(input("Please rate how your commute effected your day with -5 to -1 to indicate the degree of negative impact and 1 to 5 to indicate the degree of positive impact and 0 being no impact"))
day_rating += int(rate_your_commute)

rate_your_poductivity = int(input("Please rate how your productivity effected your day with -5 to -1 to indicate the degree of negative impact and 1 to 5 to indicate the degree of positive impact and 0 being no impact"))
day_rating += int(rate_your_commute)


rate_your_social_interations = int(input("Please rate how your social interations effected your day with -5 to -1 to indicate the degree of negative impact and 1 to 5 to indicate the degree of positive impact and 0 being no impact"))
day_rating += int(rate_your_social_interations)

#bonus factors
optional_snacks = int(input("If you had a snack please respond with the level of enjoyment it brought to your day with 1 being the worst and 5 being the best. However, if you did not have a snack please respond with 0."))
bonus_points += int(optional_snacks)
day_rating += int(optional_snacks)

optional_nap = int(input("If you had a nap please respond with the level of enjoyment it brought to your day with 1 being the worst and 5 being the best. However, if you did not have a nap please respond with 0."))
bonus_points += int(optional_nap)
day_rating += int(optional_nap)


print("Your day is a " + str(day_rating) + " out of 10")
print("You got " + str(bonus_points) + " bonus points !")