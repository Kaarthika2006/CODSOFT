contact={}
def display_contact():
    print("Name \t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice=int(input("1.Add New Contact\n 2. Search Contact \n 3. Display Contact in \n 4. Edit Contact\n 5. Delete Contact \n 6. Exist\n 7. Enter Your Choice"))
    if choice==1:
        name=input("Enter the Contact Name")
        phone=input("Enter the Mobile Number")
        contact[name]=phone
    elif choice==2:
        search_name=input("Enter the Contact Name")
        if search_name in contact:
            print(search_name, "'s Contact Number is", contact [search_name])
        else:
            print("The name is not found in contact")
    elif choice==3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()
    elif choice==4:
        edit_contact=input("Enter the Contact to be Edited!")
        if edit_contact in contact:
            phone=input("Enter the Mobile number")
            contact[edit_contact]=phone
            print ("Contact updated")
            display_contact()
        else:
            print("The Name is not found in Contact Book")
    elif choice==5:
        del_contact=input("Enter the Contact to be Deleted.")
        if del_contact in contact:
            confirm=input("Do You Want to Delete this Contact y/n?")
            if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("The Name it not found in Contact Rock")
    else:
        break
