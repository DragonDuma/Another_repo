# I am weak in the research and planning sections, I need to focus and make a plan for myself before I start coding
# Calculate Area
length = input("Enter your length:")
width = input("Enter the width:")
area = float(length) * float(width)
print(f'The area of your length, {length} times your width {width}, is: {area}')


# calculate tax tip and total
Meal_Cost = input("Cost of meal:")
if Meal_Cost != float and int:
    print("Please enter a whole number or decimal")
tax = float(Meal_Cost) / 10
total_cost_without_tip = tax + int(Meal_Cost)
tip = int(total_cost_without_tip) * 0.15
after_tip_cost = tip + total_cost_without_tip
print(f'Your meal costs {Meal_Cost}, your tax is {tax}, your tip was {tip} and your total plus tip is {after_tip_cost}')


# compound interest  I want to save this for future use
# I need to do the videos version and make a much better version of this one with a for loop

def compound_interest_calculator():  # this only works for 2 years. I will do better.
    invested = input("Enter the amount you have invested:")
    interest_rate = input("Interest Rate as a decimal number (remember to convert that percent!):")
    yearly_increase = float(invested) * float(interest_rate)
    new_amount = yearly_increase + float(invested)
    two_years = (new_amount * float(interest_rate)) + new_amount
    print(f'After 1 year you will have ${yearly_increase} more; and a total of ${new_amount}.')
    print(f'After 2 years you will haves ${two_years}')


compound_interest_calculator()


# videos tutorials version


# my version try a for loop with for years in range 1,2 and 2,3 and 5,6 and 9,10


# Challenge 4: Count the number of consonants and vowels in text


# Challenge 5 Calculate Total Invoice Price:


# Challenge 6 Total Entrance Fee:


# Challenge 7 Find the Largest word in Text: