from services.database_service import DatabaseService
from views.menu import Menu


def main():

    # ==========================
    # Initialize Database
    # ==========================
    DatabaseService.initialize_database()

    # ==========================
    # Main Loop
    # ==========================
    while True:

        choice = Menu.show_main_menu()

        try:

            if choice == "1":
                Menu.add_book()

            elif choice == "2":
                Menu.view_books()

            elif choice == "3":
                Menu.search_by_id()

            elif choice == "4":
                Menu.search_by_title()

            elif choice == "5":
                Menu.sort_books()

            elif choice == "6":
                Menu.update_book_info()

            elif choice == "7":
                Menu.update_stock()

            elif choice == "8":
                Menu.delete_book()

            elif choice == "9":
                Menu.create_transaction()

            elif choice == "10":
                Menu.view_transactions()

            elif choice == "11":
                Menu.show_report()

            elif choice == "12":
                Menu.export_csv()

            elif choice == "0":

                print("\nThank you for using Digital Library System!")
                break

            else:

                print("\nInvalid choice. Please try again.")

        except ValueError:

            print("\nInput error: Please enter valid data.")

        except Exception as e:

            print("\nUnexpected error:", e)


if __name__ == "__main__":
    main()