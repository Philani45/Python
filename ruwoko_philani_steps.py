def feet_to_steps(feet):
    steps = feet / 2.5  
    return int(steps)

def main():
    feet_walked = float(input("Enter the distance walked in feet: "))
    steps_walked = feet_to_steps(feet_walked)
    print(f"You have walked approximately {steps_walked} steps.")

if __name__ == "__main__":
    main()
