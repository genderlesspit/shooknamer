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
    open(csdfp) #"r" doesn't need to be specified because it's assumed in the function
    #Define sought after variables
    
    class csdfp_properties:
        def __init__(self, sender, recipient, date, subject):
            self.sender = sender
            self.recipient = recipient
            self.date = date
            self.subject = subject
    def find_metadata(this_document):
        file_metadata_list = ["F r o m :   ", "T o :   ", "D a t e :   ", "S u b j e c t :   "]
        find_sender_string = file_metadata_list(0)
        find_recipient_string = file_metadata_list(1)
        find_date_string = file_metadata_list(2)
        find_subject_string = file_metadata_list(3)
        open(this_document)
        while = most_recent_email_found < 3:
            most_recent_email_found = x
            x = 0
            for line in this_document:
               str(line)
               if find_sender_string in line:
                   print(str(line))
                   csdfp_properties.sender = line
                    most_recent_email = x + 1
                if find_recipient_string in line:
                   print(str(line))
                   csdfp_properties.recipient = line
                    most_recent_email = x + 1
                if find_date_string in line:
                   print(str(line))
                   csdfp_properties.date = line
                    most_recent_email = x + 1
                if find_subject_string in line:
                   print(str(line))
                   csdfp_properties.subject = line
                    most_recent_email = x + 1
            print(csdfp_properties(this_document))
    find_metadata(csdfp)
