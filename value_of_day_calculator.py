#introduction
print("Welcome to the Value of Your Day quiz! This quiz will help you determine the worth of your day through analyzing )

day_rating = 0
bonus_points = 0
total_points = 0

# base factors

rate_your_sleep = int(input("Rate your sleep on a scale of 1-10. 1 shows a bad night of sleep while 10 shows good sleep:  "))
day_rating += int(rate_your_sleep)
total_points += 10
 
rate_your_breakfast = int(input("Rate your breakfast on a scale of 1-5. 1 indicating a bad breakfast/no breakfast and 5 being the best breakfast ever:  "))
day_rating += int(rate_your_breakfast)
total_points += 5

rate_your_lunch = int(input("Rate your lunch on a scale of 1-5. 1 indicating a bad lunch/no lunch and 5 being the best lunch ever:  "))
day_rating += int(rate_your_lunch)
total_points += 5

rate_your_dinner = int(input("Rate your dinner on a scale of 1-5. 1 indicating a bad dinner/no dinner and 5 being the best dinner ever:  "))
day_rating += int(rate_your_dinner)
total_points += 5

rate_your_exercise = int(input("Please rate how your exercise effected your day on a scale of -5 to 5. -5 to -1 indicates negative impact and 1 to 5 to indicates positive impact. 0 shows that exercise had no impact.  "))
day_rating += int(rate_your_exercise)
total_points += 5

rate_your_commute = int(input("Please rate how your commute effected your day.  -5 to -1 indicates negative impact and 1 to 5 indicates positive impact. 0 indicates no impact.  "))
day_rating += int(rate_your_commute)
total_points += 5

rate_your_poductivity = int(input("Please rate how your productivity effected your day. -5 to -1 indicates negative impact (low productivity) and 1 to 5 indicates positive impact (high productivity). 0 indicates no impact (level of productivity is not a determining factor in your day).  "))
day_rating += int(rate_your_poductivity)
total_points += 10


rate_your_social_interations = int(input("Please rate how your social interations have effected your day. -5 to -1 indicates a negative impact of social interactions on your day, and 1 to 5 indicates a positive impact. 0 indicates no impact.  "))
day_rating += int(rate_your_social_interations)
total_points += 5

rate_pride_in_achievements = int(input("Please rate your pride in today's achievements. Answering 1 indicates a low/nonexistent level of pride in achieving your goals, while 10 shows a high level of pride in achieving your goals.  "))
day_rating += int(rate_pride_in_achievements)
total_points += 10

rate_enjoyment_in_activities = int(input("Please rate your enjoyment of today's activities. Answering 1 indicates a low/nonexistent level of enjoyment in what you did today, while 10 shows a high level of enjoyment in your activities.  "))
day_rating += int(rate_enjoyment_in_activities)
total_points += 10


#bonus factors
optional_snacks = int(input("If you had a snack, please respond with the level of enjoyment the snack brought to your day on a range of 1 to 5. If you did not have a snack, please respond with 0.  "))
bonus_points += int(optional_snacks)


optional_nap = int(input("If you took a nap, please respond with the level of enjoyment the nap brought to your day on a range of 1 to 5. If you did not take a nap, please respond with 0.  "))
bonus_points += int(optional_nap)


optional_humor =  int(input("If humor impacted your day, please respond with the level of cheer the humor brought to your day on a range of 1 to 5. If humor did not affect your day, please respond with 0.  "))
bonus_points += int(optional_humor)


optional_new_experiences = int(input("Please indicate on a scale of 1 to 5 if new experiences positively impacted your day. If there was no impact, please respond with 0.  "))
bonus_points += int(optional_new_experiences)


optional_downtime = int(input("Please rate how downtime effected your day. A scale of -5 to -1 indicates a negative impact of downtime on your day, and 1 to 5 indicates a positive impact. 0 indicates no impact.  "))
bonus_points += int(optional_downtime)


from decimal import Decimal
day_rating += bonus_points
gross_percentage = float(day_rating / total_points) * 100
fine_percentage = round(gross_percentage, 2)


print("Your day is a " + str(day_rating) + " out of " + str(total_points) + "!")
print("You got " + str(bonus_points) + " bonus points, which may have contributed positively to your day.")
print("In other words, your day was " + str(fine_percentage) + "% fantastic.")
