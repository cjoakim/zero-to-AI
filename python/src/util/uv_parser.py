import traceback

from src.io.fs import FS
from src.util.counter import Counter

# This class is used to parse various outputs from the uv program -
# such as the 'uv tree' and 'uv pip list' commands.
# Chris Joakim, 3Cloud/Cognizant, 2026


class UVParser:
    def __init__(self):
        self.data = dict()
        self.graph_libs = list()

    def parse_pip_list(self, infile: str = "data/uv/uv-pip-list.txt") -> dict:
        """
        The default input file was created by the venv.sh script.
        """
        try:
            data = dict()
            lines = FS.read_lines(infile)
            in_zone = False
            for line in lines:
                if in_zone:
                    tokens = line.strip().split()
                    name = tokens[0].strip()
                    version = tokens[1].strip()
                    data[name] = version
                if "----" in line:
                    in_zone = True
            return data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def parse_tree(self, infile: str = "data/uv/uv-tree.txt") -> list:
        """
        The default input file was created by the venv.sh script.
        """
        try:
            self.graph_libs = list()
            counter = Counter()
            lines = FS.read_lines(infile)

            # this loop parses the lines of the 'uv tree' output and collects
            # a list of lib dictionaries
            for line_idx, line in enumerate(lines):
                if line_idx > 0:
                    if "─ " in line:
                        indent = line.index("─ ")
                        level = self.indent_to_level(indent)
                        if indent > 0:
                            counter.increment(indent)
                            suffix = line[indent + 1 :].strip()
                            tokens = suffix.split()
                            lib = dict()
                            lib["index"] = 0
                            lib["name"] = tokens[0].strip()
                            lib["version"] = tokens[1].strip()
                            lib["level"] = level
                            lib["indent"] = indent
                            lib["suffix"] = suffix
                            self.graph_libs.append(lib)

            for lib_idx, lib in enumerate(self.graph_libs):
                lib["index"] = lib_idx

            for lib_idx, lib in enumerate(self.graph_libs):
                self.set_dependencies(lib)

            FS.write_json(counter.get_data(), "data/uv/uv-tree-counter.json")
            FS.write_json(self.graph_libs, "data/uv/uv-tree-libs.json", sort_keys=False)
            return self.graph_libs
        except Exception as e:
            print(f"Error: {e}")
            print(traceback.format_exc())
            return None

    def set_dependencies(self, lib: dict) -> dict:
        lib_name = lib["name"]
        lib_index = lib["index"]
        lib_level = lib["level"]
        dep_level = lib_level + 1
        located = False
        dependencies = list()

        for idx, lib in enumerate(self.graph_libs):
            if idx == lib_index:
                if lib["name"] == lib_name:
                    located = True
                    #print(f"located: {lib_name} at index {idx}")
            else:
                if located:
                    if lib["level"] != dep_level:
                        located = False
                        #print(f"dislocated: {lib_name} at index {idx}")
                    else:
                        dep = lib["name"]
                        dep_idx = lib["index"]
                        #print(f"{idx} {lib_index} adding dep: {dep} at index {dep_idx} for lib {lib_name} {lib_index}")
                        dependencies.append(dep)
        lib["dependencies"] = dependencies
        #print(f"lib {lib_name} -> {dependencies}")

    def indent_to_level(self, indent: int) -> int:
        if indent == 2:
            return 1
        elif indent == 6:
            return 2
        elif indent == 10:
            return 3
        elif indent == 14:
            return 4
        elif indent == 18:
            return 5
        elif indent == 22:
            return 6
        elif indent == 26:
            return 7
        elif indent == 30:
            return 8
        elif indent == 34:
            return 9
        elif indent == 38:
            return 10
        elif indent == 42:
            return 11
        elif indent == 46:
            return 12
        else:
            return -1
