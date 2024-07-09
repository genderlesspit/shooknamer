def get_mail_metadata():
    is_readable = False
    while not is_readable:
        currently_selected_document_filepath = input("Paste desired filepath: ")
        print("You have selected " + str(currently_selected_document_filepath))
        csdfp = currently_selected_document_filepath  # Assign the file path to csdfp

        # Check if it's a .msg file
        if csdfp.endswith(".msg"):
            try:
                with open(csdfp, 'r') as file:
                    csd_contents = file.read()  # Read the contents of the file
                    # Process csd_contents here as needed
                is_readable = True  # Set flag to exit the loop
            except IOError:
                print("Error reading the file. Please try again.")
        else:
            print("Error with file type. Please select a .msg file.")

# Call the function to test
get_mail_metadata()
