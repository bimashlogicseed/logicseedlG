banner = "Welcome to the Python REPL. Type 'exit()' or 'quit()' to exit."
exit_commands = ('exit()', 'quit()')

print(banner)
while True:
    try:
        user_input = input(">>> ")
        if user_input in exit_commands:
            print("Exiting REPL. Goodbye!")
            break

        try:
            # First, try to evaluate the user input
            result = eval(user_input)
            if result is not None:
                print(result)
        except:
            # If eval fails, it might be a statement, so we use exec
            exec(user_input)
    except KeyboardInterrupt:
        print("\nExiting REPL. Goodbye!")
        break
    except Exception as e:
        print(f"Error: {e}")
