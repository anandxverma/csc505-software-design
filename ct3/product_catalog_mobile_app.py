import Screen as screen

# This program represents a Product Catalog Mobile App
# It documents various screenflows in the app

# List of screens in the app
screen_home = screen.Screen("Home", "This is the home screen of the app. This screen shows the list of recently viewed or updated products in the catalog.")
screen_login = screen.Screen("Login", "This is the Login screen of the app.")
screen_add_product = screen.Screen("Add Product", "This screen allows a user to add a new product to the catalog.")
screen_view_product = screen.Screen("View Product", "This screen displays the details of a product.")
screen_edit_product = screen.Screen("Edit Product", "This screen allows a user to udpate a product's details and save it to the catalog")
screen_search_results = screen.Screen("Search Results", "This screen shows filtered subset of the products based on the search criteria.")
screen_settings = screen.Screen("Settings", "This is the Settins screen. It allows the users to update App settings and preferences.")
screen_about = screen.Screen("About", "This screen shows the About Details of the App.")

# Create an array of screens in the app
list_of_screens = [ screen_login, screen_home, screen_add_product, screen_view_product,
                    screen_edit_product, screen_search_results, screen_settings, screen_about ]

navigations = {
    "Lanuch App": [ screen_login, screen_home ],
    "Add Product": [ screen_home, screen_add_product, screen_home ],
    "View Product": [ screen_home, screen_view_product ],
    "Edit Product": [ screen_home, screen_view_product, screen_edit_product, screen_home ],
    "Search": [ screen_home, screen_search_results ],
    "Settings and About": [ screen_home, screen_settings, screen_about]
}

app_about = "Product Catalog Mobile App v1.0\nDeveloped by: Anand Verma\nLast Updated: Nov 30, 2025\nThis app allows users to view, add, edit, and search products in a catalog."

def display_app_details():
    print()
    print("="*60)
    print("Product Catalog Mobile App Details")
    print("-"*60)
    print("About:", app_about)
    print("-"*60)
    # Display list of screens
    print("Screens in the App:")
    for idx, screen_instance in enumerate(list_of_screens, start=1):
        print(f"{idx}. {screen_instance.name} - {screen_instance.description}")
    # Display number of screens
    print(f"Total Screens in the App: {len(list_of_screens)}")
    print("-"*60)
    print("Screen Flows:")
    # Display each screen flows
    for flow_name, screens in navigations.items():
        print(f"{flow_name}: ", end="")
        for idx, screen_instance in enumerate(screens):
            if idx == 0:
                print(f"{screen_instance.name}", end="")
            else:
                print(f" -> {screen_instance.name}", end="")
        print()
    print("Total Screen Flows: ", len(navigations))
    print("="*60)
    print()

# Call the function to display app details
display_app_details()