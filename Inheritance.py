# Base class
class Notification:
    def __init__(self, message):
        self.message = message  # The message to be displayed

    def display(self):
        print(f"Notification: {self.message}")

# Derived class
class EmailNotification(Notification):
    def __init__(self, message, email_address):
        # Call the parent class constructor to initialize message
        super().__init__(message)
        self.email_address = email_address  # Email address for the email notification

    def show_email(self):
        print(f"Sending email to {self.email_address} with message: {self.message}")

# Create an object of the derived class
email = EmailNotification("Hello!!!.", "user@example.com")

# Call methods from both base and derived class
email.display()       # Inherited from Notification
email.show_email()    # Defined in EmailNotification
