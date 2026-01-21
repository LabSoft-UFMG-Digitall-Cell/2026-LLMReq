from participants import knowledge_distribuition, experience, specific_knowledge_by_time
from results import boxplotLLM
from categorization import open_coding_categorization
from interactions import sankey_interaction_flows
from perception import build_sankey_negative, build_sankey_positive

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
            "7 - Negative LLM usage diagram\n"
            "8 - Boxplot LLM usage by LLM grade\n"
            "9 - Open Coding Categorization\n"
            "10 - Sankey Diagram\n"
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
            build_sankey_positive()

        elif graph == "7":
            print("Generating Negative LLM usage diagram...")
            build_sankey_negative()

        elif graph == "8":
            print("Generating Boxplot for LLM usage by LLM grade...")
            boxplotLLM("grad_llm")

        elif graph == "9":
            print("Generating Open Coding Categorization graph...")
            open_coding_categorization()

        elif graph == "10":
            print("Generating Sankey Diagram...")
            sankey_interaction_flows()

        elif graph == "0":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose a valid number.")
    

