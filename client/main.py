from participants import knowledge_distribuition, experience, specific_knowledge_by_time
from results import boxplotLLM, positive_usage_llm
from categorization import open_coding_categorization
from sankey import sankey_interaction_flows

if __name__ == "__main__":
    print("This is the main entry point for the client API.")

    while True:
        graph = input(
            "\nDo you want to generate any graph?\n"
            "1 - Knowledge Distribution\n"
            "2 - Experience Distribution\n"
            "3 - Boxplot LLM usage by time\n"
            "4 - Boxplot LLM usage by grade\n"
            "5 - Specific Knowledge by Topic\n"
            "6 - Positive LLM usage diagram\n"
            "7 - Boxplot LLM usage by LLM grade\n"
            "8 - Open Coding Categorization\n"
            "9 - Sankey Diagram\n"
            "0 - Exit\n"
        )

        if graph == "1":
            print("Generating Knowledge Distribution graph...")
            knowledge_distribuition()

        elif graph == "2":
            print("Generating Experience Distribution graph...")
            experience()

        elif graph == "3":
            print("Generating Boxplot for LLM usage by time...")
            boxplotLLM("time")

        elif graph == "4":
            print("Generating Boxplot for LLM usage by grade...")
            boxplotLLM("grad_mean")

        elif graph == "5":
            topic = "requirements"
            print(f"Generating Specific Knowledge by Time graph for topic: {topic}...")
            specific_knowledge_by_time(topic)

        elif graph == "6":
            print("Generating Positive LLM usage diagram...")
            positive_usage_llm()

        elif graph == "7":
            print("Generating Boxplot for LLM usage by LLM grade...")
            boxplotLLM("grad_llm")
        
        elif graph == "8":
            print("Generating Open Coding Categorization graph...")
            open_coding_categorization()
        
        elif graph == "9":
            print("Generating Sankey Diagram...")
            sankey_interaction_flows()

        elif graph == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose a valid number.")
    

