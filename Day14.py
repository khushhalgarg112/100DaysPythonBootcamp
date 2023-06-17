import random
from data import data
import logo
import os


def celebrity(num):
    result = data[num]
    final = result["name"], result["description"], result["country"]
    return final


print(
    f"""
    {logo.logo}
    """
)

num1 = random.randint(0, len(data))
score = 0
end = True
while end:
    os.system("cls")
    print(
        f"""
    {logo.logo}
    """
    )
    print(f"Your Score is {score}")
    num2 = random.randint(0, len(data))
    if num1 != num2:
        print(f"Compare A : {celebrity(num1)}")
        print(
            f"""
        {logo.vs}
        """
        )
        print(f"Compare B : {celebrity(num2)}")
        ans = input("Compare A or B on the Basis of their followers: ")
        if data[num1]["follower_count"] > data[num2]["follower_count"] and ans == "A":
            score += 1
            num1 = num2
            num2 = random.randint(0, len(data))
        elif data[num1]["follower_count"] < data[num2]["follower_count"] and ans == "B":
            score += 1
            num1 = num2
            num2 = random.randint(0, len(data))
        else:
            os.system("cls")
            print(
                f"Sorry, you choose the wrong option, At Final your score is {score} "
            )
            score = 0
            end = False

    else:
        num2 = random.randint(0, len(data))
