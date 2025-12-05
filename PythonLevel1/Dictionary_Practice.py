def phone_book():

    contacts = {}

    while True:
        print("\n📞 Phone Book Menu")
        print("1. Add Contact")
        print("2. Look Up Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # --- Add Contact --
            name = input("Enter contact name: ").strip()
            print(name)
            phone = input("Enter phone number: ").strip()
            
            if name and phone.isdigit():
                # Add or update the entry
                contacts[name] = phone
                print(f"✅ Contact '{name}' added/updated.")
            elif not name:
                print("❌ Name cannot be empty.")
            else:
                print("❌ Invalid phone number. Please enter digits only.")

        elif choice == '2':
            # --- Look Up Contact ---
            name = input("Enter name to look up: ").strip().title()
            
            # Use .get() method to look up a key safely
            phone = contacts.get(name)
            
            if phone:
                print(f"\n🔎 Contact Found: {name} -> {phone}")
            else:
                print(f"❌ Contact '{name}' not found.")

        elif choice == '3':
            # --- Delete Contact ---
            if not contacts:
                print("The phone book is empty.")
                continue

            name = input("Enter name to delete: ").strip().title()
            
            if name in contacts:
                # Use .pop() to remove the key and get the value (the phone number)
                del contacts[name]
                print(f"🗑️ Contact '{name}' deleted.")
            else:
                print(f"❌ Contact '{name}' not found.")

        elif choice == '4':
            # --- List All Contacts ---
            if contacts:
                print("\n📖 All Contacts:")
                # Iterate over dictionary items (key-value pairs)
                for name, phone in sorted(contacts.items()):
                    print(f"- {name}: {phone}")
            else:
                print("\nThe phone book is empty.")

        elif choice == '5':
            # --- Quit ---
            print("👋 Thank you for using the phone book. Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# Test
# The function will run interactively until the user enters '5'
phone_book()