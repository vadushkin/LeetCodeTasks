import os
import pathlib
from pathlib import Path
import sys
import time

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

load_dotenv()

ABSOLUTE_PATH = os.getenv("ABSOLUTE_PATH")
# why just don't language? because it's already taken
LANGUAGE = os.getenv("YOUR_FAVORITE_LANGUAGE")

NAMES_OF_FOLDERS = {1: "1-100", **{int(f"{i}00"): f"{i}00-{i + 1}00" for i in range(1, 40)}}

DICTIONARY_OF_LANGUAGES_WITH_FILE_EXTENSIONS = {
    "Python": ".py",
    "Pytho3": ".py",
    "Java": ".java",
    "C": ".c",
    "C++": ".cpp",
    "C#": ".cs",
    "Visual Basic": ".vb",
    "JavaScript": ".js",
    "PHP": ".php",
    "SQL": ".sql",
    "Objective-C": ".m",
    "Swift": ".swift",
    "GO": ".go",
    "Ruby": ".rb",
    "Perl": ".pl",
    "MATLAB": ".m",
    "R": ".r",
    "Scala": ".scala",
    "Kotlin": ".kt",
    "TypeScript": ".ts"
}


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function <{func.__name__}> Start!")
        result = func(*args, **kwargs)
        print(f"Function <{func.__name__}> Done!")
        return result

    return wrapper


@print_decorator
def change_work_directory(path: Path) -> Path:
    """Change work directory"""

    current_directory = Path(path)
    os.chdir(current_directory)

    return current_directory


@print_decorator
def get_html_for_all_problems(all_problems_url: str) -> webdriver.Chrome.page_source:
    """Return html page for all problems"""

    # hide the window
    options = Options()
    options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)

    browser.get(all_problems_url)
    # download a whole page
    time.sleep(5)

    # get html and exit
    html = browser.page_source
    browser.quit()

    return html


@print_decorator
def get_html_for_the_next_50_problems(number: int) -> webdriver.Chrome.page_source:
    """Return html page for one problem"""
    pagination_number = number // 50 + 1 if number % 50 != 0 else number // 50

    url_of_task = f"https://leetcode.com/problemset/all/?page={pagination_number}"

    # hide the window
    options = Options()
    options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)

    browser.get(url_of_task)
    # download a whole page
    time.sleep(7)

    # get html and exit
    html = browser.page_source
    browser.quit()

    return html


@print_decorator
def get_html_for_task(task_url: str, language: str) -> webdriver.Chrome.page_source:
    # hide the window
    options = Options()
    options.add_argument("--headless")

    browser = webdriver.Chrome(options=options)

    browser.get(task_url)
    # more size to get a line of an example code
    browser.set_window_size(1800, 1000)

    # sleep for downloading a whole page
    time.sleep(7)

    # browser.find_element("xpath", '//*[@id="headlessui-listbox-button-:ri:"]').click()
    # this div changes every time             ---------------------------~~--- especially the last letter
    # for example:
    # headlessui-listbox-button-:r1:
    # headlessui-listbox-button-:r4:
    # headlessui-listbox-button-:rs: etc...

    # full xpath because leetcode.
    xpath = "/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div/button"
    browser.find_element("xpath", xpath).click()

    # all buttons of languages
    elements = browser.find_elements("class name", "whitespace-nowrap")

    # search python or java or php
    for element in elements:
        if element.text == language:
            element.click()
            break

    # sleeping
    time.sleep(5)

    # get html and exit
    html = browser.page_source
    browser.quit()

    return html


@print_decorator
def get_link_and_name_of_your_task(html: webdriver.Chrome.page_source, number: int) -> tuple[str, str]:
    """Get link and name of your task"""

    soup = BeautifulSoup(html, "lxml")

    tasks_row = soup.find("div", role="rowgroup")
    # 50 is default pagination
    index = number % 50 - 1 if number > 50 else number
    task_line = tasks_row.find_all("div", role="row")[index].find_all("div", class_="mx-2 py-[11px]")

    data = task_line[1].find("a")

    # new link for your task
    task_link = "https://leetcode.com" + data.get("href")
    task_name = data.text

    return task_link, task_name


@print_decorator
def get_link_and_name_of_today_task(html: webdriver.Chrome.page_source) -> tuple[str, str]:
    """Get link and name of today task"""

    soup = BeautifulSoup(html, "lxml")

    tasks_row = soup.find("div", role="rowgroup")
    task_line = tasks_row.find("div", role="row").find_all("div", class_="mx-2 py-[11px]")

    # first task == daily task
    data = task_line[1].find("a")

    # new link for daily task
    task_link = "https://leetcode.com" + data.get("href")
    task_name = data.text

    return task_link, task_name


@print_decorator
def add_to_string_python_code(code: str, name_of_function: str, one_example: str) -> str:
    """Add to str main function and tests"""

    code += " " * 8 + "pass" + "\n\n"

    code += f"""
def main():
    s = Solution()
    print(s.{name_of_function}({one_example}))


if __name__ == '__main__':
    main()

\"\"\"Tests:
1. 

2. 
\"\"\"
"""
    return code


@print_decorator
def get_example_code_for_task(html: BeautifulSoup, one_example: str) -> str:
    """Return the sample code for task"""

    code = ""

    example_codes = html.find("div", class_="view-lines monaco-mouse-cursor-text").find_all("div", class_="view-line")

    name_of_function = ""

    for index, example_code in enumerate(example_codes):
        if ex := example_code.text.strip().split():
            if ex[0] == "def" and ex[1] != "__init__":
                match LANGUAGE:
                    case "Python3":
                        name_of_function += ex[1][:-6]

        code += example_code.text.replace('\xa0', ' ') + "\n"

    match LANGUAGE:
        case "Python3":
            code = add_to_string_python_code(code, name_of_function, one_example)

    return code


@print_decorator
def get_description_for_task(html: BeautifulSoup) -> tuple[str, str]:
    """Return the description code for task"""

    description = html.find("div", class_="_1l1MA")

    complicated_text = "\"\"\"\n"

    for p in description.find_all("p")[:-5]:
        text = p.text.split()

        for j in range(10, len(text), 10):
            complicated_text += ' '.join(text[j - 10:j]) + "\n"

    examples = description.find_all("pre")

    complicated_text += "\n"

    one_example = ""

    for index, example in enumerate(examples, 1):
        # this for v1.py in Solution.name_of_function(-> args <-)
        if index == 1:
            text = example.text.split("\n")[0].split()[1:]

            for i in range(3, len(text) + 1, 3):
                e = text[i - 3: i][2]

                one_example += e

        complicated_text += f"* Example {index}:" + "\n" + example.text + "\n"

    complicated_text += "Constraints:\n\n"

    constraints = description.find_all("li")

    for index, constraint in enumerate(constraints):
        if constraint.find("code"):
            complicated_text += "* " + constraint.find("code").text + "\n"

    complicated_text += "\"\"\""

    return complicated_text, one_example


@print_decorator
def get_description_and_example_code(task_url: str) -> tuple[str, str]:
    """Return a description and an example code"""

    soup = BeautifulSoup(get_html_for_task(task_url, LANGUAGE), "lxml")

    description, one_example = get_description_for_task(soup)
    example_code = get_example_code_for_task(soup, one_example)

    return description, example_code


@print_decorator
def create_folders_and_files(absolute_path: str, task_link: str, task_name: str):
    """Create folders and files"""
    task_description, example_code = get_description_and_example_code(task_link)

    if not task_link or not task_name or not task_link:
        return

    current_directory = Path(absolute_path)
    os.chdir(current_directory)

    for dir_or_file in current_directory.iterdir():
        if LANGUAGE == "Python3":
            if "Python" == dir_or_file.name:
                break
        elif LANGUAGE == dir_or_file.name:
            break
    else:
        if LANGUAGE == "Python3":
            pathlib.Path(f"Python/").mkdir(parents=True, exist_ok=True)
        else:
            pathlib.Path(f"{LANGUAGE}").mkdir(parents=True, exist_ok=True)

    if LANGUAGE == "Python3":
        current_directory = change_work_directory(current_directory / "Python")
    else:
        current_directory = change_work_directory(current_directory / LANGUAGE)

    task_number = int(task_name.split(".")[0])

    if task_number and task_number > 100:
        task_number = task_number // 100 * 100
    else:
        task_number = 1

    name_of_folder = NAMES_OF_FOLDERS.get(task_number, "4000+")

    pathlib.Path(f"{name_of_folder}/").mkdir(parents=True, exist_ok=True)
    current_directory = change_work_directory(current_directory / name_of_folder)

    pathlib.Path(f"{task_name}/").mkdir(parents=True, exist_ok=True)
    current_directory = change_work_directory(current_directory / task_name)

    file_extension = DICTIONARY_OF_LANGUAGES_WITH_FILE_EXTENSIONS.get(LANGUAGE, '.py')

    if not os.path.exists(current_directory / "name_task.py"):
        with open("name_task.py", "w", encoding="utf-8") as file:
            file.write(task_description)

    if not os.path.exists(current_directory / "v1.py"):
        with open(f"v1{file_extension}", "w", encoding="utf-8") as file:
            file.write(example_code)

    if not os.path.exists(current_directory / "v2.py"):
        with open(f"v2{file_extension}", "w", encoding="utf-8") as file:
            file.write(example_code)


if __name__ == "__main__":
    try:
        if not ABSOLUTE_PATH:
            raise Exception("Please, fill in the ABSOLUTE_PATH")

        if not LANGUAGE:
            raise Exception("Please, fill in the LANGUAGE")

        if not len(sys.argv[1:]):
            url = "https://leetcode.com/problemset/all/"

            all_problems_html = get_html_for_all_problems(url)
            link_of_task, name_of_task = get_link_and_name_of_today_task(all_problems_html)

            create_folders_and_files(ABSOLUTE_PATH, link_of_task, name_of_task)
        else:
            for number_of_task in sys.argv[1:]:
                number_of_task = int(number_of_task)

                html_of_nearest_50_tasks = get_html_for_the_next_50_problems(number_of_task)
                link_of_task, name_of_task = get_link_and_name_of_your_task(html_of_nearest_50_tasks, number_of_task)

                create_folders_and_files(ABSOLUTE_PATH, link_of_task, name_of_task)

        print("\nSuccess!")
    except Exception as _ex:
        print(f"Error: {_ex}")
