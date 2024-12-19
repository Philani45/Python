def text_filter(message):
    banned_words = ["Turkey", "Dog", "Fox", "Cat", "Chicken"]
    words = message.split()  
    filtered_words = [word for word in words if word not in banned_words]
    filtered_message = ' '.join(filtered_words)  
    return filtered_message

def main():
    message = input("Enter your message: ")
    filtered_message = text_filter(message)
    print("Filtered message:")
    print(filtered_message)

if __name__ == "__main__":
    main()
