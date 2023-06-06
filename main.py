from gooey import Gooey, GooeyParser

@Gooey(program_name="Gooey Form")
def main():
    parser = GooeyParser()

    # Getting input from user to calculate sum
    parser.add_argument("num_1", action="store", help="First number of sum", metavar="First number")
    parser.add_argument("num_2", action="store", help="Second number of sum", metavar="Second number")

    # Optional argument
    parser.add_argument("--num_3", action="store")

    # Checkboxes
    parser.add_argument("--checkbox", action="store_true", help="Example of checkbox")

    # Dropdown
    parser.add_argument("option", choices=["Option 1", "Option 2"], metavar="Dropdown", help="Example of a dropdown")

    # Radio Buttons
    group = parser.add_mutually_exclusive_group("selection")
    group.add_argument("--selection_1", action="store_true", help="First radio button")
    group.add_argument("--selection_2", action="store_true", help="Second radio button")

    # Custom Widgets
    parser.add_argument("file_chooser", widget="FileChooser", metavar="Select file", help="Select a file on your system")
    parser.add_argument("color_picker", widget="ColourChooser", metavar="Color Picker", help="Select any color")
    parser.add_argument("date_picker", widget="DateChooser", metavar="Date Picker", help="Pick a Date")
    parser.add_argument("password", widget="PasswordField", metavar="Password", help="Enter the password")

    args = parser.parse_args()

    print(int(args.num_1) + int(args.num_2))

main()