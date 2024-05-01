"""Arquivo que estudantes devem editar"""


def bar_char_counter(pwd: str) -> int:
    count = 0
    for char in pwd:
        if char == "/":
            count += 1
    return count


def show_deepest_file(context):
    if not context["all_files"]:
        print("No files found")
    else:
        deepest_file = max(context["all_files"], key=bar_char_counter)
        print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
