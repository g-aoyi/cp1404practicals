from prac_07.project import Project
import datetime
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ").lower()
    filename = "projects.txt"
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            print(f"Now loading projects from {filename}")
        elif choice == "s":
            filename = input("Filename: ")
            print(f"Now saving projects to {filename}")
        elif choice == "d":
            incomplete_projects = []
            completed_projects = []
            in_file = open(filename, 'r')
            in_file.readline()
            for line in in_file:
                parts = line.strip().split("\t")
                project = Project(parts[0], parts[1], parts[2], float(parts[3]), parts[4])
                if int(parts[4]) == 100:
                    completed_projects.append(project)
                else:
                    incomplete_projects.append(project)
            in_file.close()
            incomplete_projects.sort()
            completed_projects.sort()
            print("Incomplete projects:")
            for project in incomplete_projects:
                print(project)
            print("Completed projects:")
            for project in completed_projects:
                print(project)
        elif choice == "f":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            projects = []
            with open(filename, 'r') as in_file:
                in_file.readline()
                for i, line in enumerate(in_file):
                    parts = line.strip().split("\t")
                    project_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
                    project = Project(parts[0], parts[1], parts[2], float(parts[3]), parts[4])
                    if project_date >= date:
                        projects.append(project)
            for i in range(0, len(projects)):
                for j in range(i+1, len(projects)):
                    if projects[i].start_date >= projects[j].start_date:
                        projects[i].start_date, projects[j].start_date = projects[j].start_date, projects[i].start_date
            for project in projects:
                print(project)
        elif choice == "a":
            print("Let's add a new project")
            name = input("Name: ")
            if name == "":
                pass
            start = get_nonempty_string("Start date (dd/mm/yy): ", "Invalid input")
            priority = get_nonempty_string("Priority: ", "Invalid input")
            cost = get_nonempty_string("Cost estimate: ", "Invalid input")
            completion = get_nonempty_string("Percent complete: ", "Invalid input")
            out_file = open(filename, 'a')
            print(f"{name}\t{start}\t{priority}\t{float(cost):1f}\t{completion}", file=out_file)
            out_file.close()
        elif choice == "u":
            data = []
            with open(filename, 'r') as in_file:
                header = in_file.readline()
                for i, line in enumerate(in_file):
                    print(f"{i} {line.strip()}")
                    data.append(f"{line}")
            project_choice = int(input("Project choice: "))
            print(data[project_choice].strip())
            new_completion = int(input("New Percentage: "))
            new_priority = input("New Priority: ")
            parts = data[project_choice].split("\t")
            if new_completion != "":
                data[project_choice] = f"{parts[0]}\t{parts[1]}\t{parts[2]}\t{parts[3]}\t{new_completion}\n"
            if new_priority != "":
                data[project_choice] = f"{parts[0]}\t{parts[1]}\t{int(new_priority)}\t{parts[3]}\t{new_completion}\n"
            with open(filename, 'w') as out_file:
                out_file.write(header)
                out_file.writelines(data)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")


def get_nonempty_string(prompt, error):
    user_input = input(prompt)
    while user_input == "":
        print(error)
        user_input = input(prompt)
    return user_input


main()
