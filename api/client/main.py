from participants_characterization import knowledge_distribuition, experience

if __name__ == "__main__":
    print("This is the main entry point for the client API.")
    graph = input("Do you want to generate any graph?\n" \
                    "1 - Knowledge Distribution\n" \
                    "2 - Experience Distribution\n" \
                    "0 - Exit\n")
    if graph == "1":
        print("Generating Knowledge Distribution graph...")
        knowledge_distribuition()
    elif graph == "2":
        print("Generating Experience Distribution graph...")
        experience()
    elif graph == "0":
        print("Exiting...")
