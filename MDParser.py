import os
import re

class MDParser:

    def __init__(self, directory, ignoredirs=[], only_files=".cs"):
        self.directory = directory
        self.only_files = only_files
        self.contents = {}
        self.ignore_dirs = ignoredirs

        self.__parse_directory()

    def get_parsed_contents(self):
        tmp = []
        tmp = self.contents
        for filename in self.contents:
            tmp[filename]["FUNCTIONS"] = sorted(self.contents[filename]["FUNCTIONS"], key = lambda i: i['function_name'])
            tmp[filename]["DELEGATES"] = sorted(self.contents[filename]["DELEGATES"], key = lambda i: i['parameter_name'])
            tmp[filename]["PARAMETERS"] = sorted(self.contents[filename]["PARAMETERS"], key = lambda i: i['parameter_name'])
        self.contents = tmp
        return self.contents

    def __reset_storage(self):
        return {
            "comment_summary": None,
            "comment_params": [],
            "comment_returns": None,
            "function_name": None,
            "function_overridable": None,
            "function_expose": None,
            "function": None,
            "delegate":None,
            "parameter_name": None,
            "parameter_default_value": None,
            "parameter_type": None,
            "parameter_exposed_value": None,
            "tooltip": None,
            "in_comment_summary": False,
            "in_comment_returns": False,
            "in_tooltip": False,
            "in_custom_class": False,
            "custom_class_line_keeper": 0,
            "type": None
        }
    
    def __parse_file(self, filepath):
        lines = []
        filename = os.path.basename(filepath)
        top_key = filepath.replace(self.directory,"")
        print(f"Reading file: {filename}")
        self.contents[top_key] = {"FUNCTIONS":[],"PARAMETERS":[],"DELEGATES":[]}
        storage = self.__reset_storage()
        with open(filepath, "r") as target:
            lines = target.readlines()
        for line in lines:
            storage = self.__get_file_parameter(storage, line)
            storage = self.__get_delegate(storage, line)
            storage = self.__get_function(storage, line)

            storage = self.__get_tooltip(storage, line)
            storage = self.__get_comment_summary(storage, line)
            storage = self.__get_comment_param(storage, line)
            storage = self.__get_comment_return(storage, line)

            if storage["type"] is not None:
                self.contents[top_key][storage["type"]+"S"].append(storage)
                storage = self.__reset_storage()

    def __get_tooltip(self, storage, line):
        if (("[Tooltip(\"" in line or storage["in_tooltip"] is True) and
        storage["in_comment_summary"] is False and storage["type"] is None and 
        storage["in_comment_returns"] is False):
            storage["in_tooltip"] = True
            tooltip = line.replace("[Tooltip(\"","").replace("\")]","").replace("+","<br>").strip().strip("\"")
            storage["tooltip"] = tooltip if storage["tooltip"] is None else storage["tooltip"] + tooltip
            if line.strip().endswith(")]"):
                storage["in_tooltip"] = False
        return storage

    def __get_file_parameter(self, storage, line):
        if (((storage["type"] is None or storage["type"] is "PARAMETER") and 
        storage["in_tooltip"] is False and storage["tooltip"] is not None) and 
        storage["in_comment_summary"] is False and storage["in_comment_returns"] is False):
            matches = re.search(r'(\w+\s)?([\w,\[,\],<,>]+)\s(\w+)(;|(?:\s=\s(.*);))', line)
            if matches is not None:
                storage["type"] = "PARAMETER"
                storage["parameter_name"] = matches.group(3)
                storage["parameter_default_value"] = matches.group(5) if matches.lastindex == 4 else None
                storage["parameter_exposed_value"] = matches.group(1) if matches.group(1) not in ["public","private","protected"] else "private"
                storage["parameter_type"] = matches.group(2) if matches.lastindex == 3 else matches.group(2)
            
        return storage

    def __get_comment_summary(self, storage, line):
        if (((storage["type"] is None) and storage["in_comment_summary"] is True or 
        "<summary>" in line) and storage["in_tooltip"] is False and 
        storage["in_comment_returns"] is False):
            storage["in_comment_summary"] = True
            formatted = line.strip().replace("///","",1).replace("<summary>","",1).replace("</summary>","",-1)
            storage["comment_summary"] = formatted if storage["comment_summary"] is None else storage["comment_summary"] + formatted
            if "</summary>" in line:
                storage["in_comment_summary"] = False
        return storage

    def __get_comment_param(self, storage, line):
        if (((storage["type"] is None) and "<param" in line) and 
        storage["in_tooltip"] is False and storage["in_comment_summary"] is False and 
        storage["in_comment_returns"] is False):
            matches = re.search(r'<param name=\"(\w+)\">(.+?)?</param>', line)
            storage["comment_params"].append({
                "name": matches.group(1),
                "description": matches.group(2) or None
            })
        return storage

    def __get_comment_return(self, storage, line):
        if (((storage["type"] is None) and storage["in_comment_returns"] is True or 
        "<returns>" in line) and storage["in_tooltip"] is False and 
        storage["in_comment_summary"] is False):
            storage["in_comment_returns"] = True
            formatted = line.strip().replace("///","",1).replace("<returns>","",1).replace("</returns>","",-1)
            storage["comment_returns"] = formatted if storage["comment_returns"] is None else storage["comment_returns"] + formatted
            if "</returns>" in line:
                storage["in_comment_returns"] = False
        return storage

    def __get_delegate(self, storage, line):
        if ((storage["type"] is None) and storage["in_tooltip"] is False and 
        storage["in_comment_summary"] is False and storage["in_comment_returns"] is False and 
        storage["tooltip"] is None and storage["comment_summary"] is not None):
            match = re.search(r'(public|private|protected)\s(\w+)\s(\w+);', line)
            if match is not None:
                storage["type"] = "DELEGATE"
                storage["delegate"] = line.strip().replace(";","")
                storage["parameter_exposed_value"] = match.group(1)
                storage["parameter_type"] = match.group(2)
                storage["parameter_name"] = match.group(3)
        return storage

    def __get_function(self, storage, line):
        if ((storage["type"] is None) and storage["in_tooltip"] is False and 
        storage["in_comment_summary"] is False and storage["in_comment_returns"] is False and 
        storage["tooltip"] is None and storage["comment_summary"] is not None):
            match = re.search(r'(public|private|protected)?\s?(virtual|override|partial)?\s?(\w+)\s(\w+)\((?:.+)?\)', line)
            if match is not None:
                storage["type"] = "FUNCTION"
                storage["function"] = line.strip().replace("{","",-1)
                storage["function_expose"] = match.group(1) if match.group(1) in ["public","private","protected"] else "private"
                storage["function_overridable"] = True if match.group(2) in ["virtual","override","partial"] else False
                storage["function_name"] = match.group(match.lastindex)
        return storage

    def __get_custom_class(self, storage, line, filename):
        if storage["in_custom_class"] is True:
            if "{" in line:
                storage["custom_class_line_keeper"] += 1
            if "}" in line:
                storage["custom_class_line_keeper"] -= 1
            if storage["custom_class_line_keeper"] == 0:
                storage["in_custom_class"] = False
        elif "class" in line:
            match = re.search(r'(public|private)?\s?(partial)?class\s(\w+)', line)
            if match is not None and match.group(1) != filename.replace(self.only_files, "", -1):
                storage["in_custom_class"] = True
        return storage

    def __parse_directory(self):
        for subdir, dirs, files in os.walk(self.directory):
            for filename in files:
                if filename.endswith(self.only_files) and dirs not in self.ignore_dirs:
                    self.__parse_file(subdir+os.sep+filename)

    # For writing the content to files
    def write_contents_to_files(self, parsed_contents, directory_path):
        if directory_path == ".":
            directory_path = os.path.dirname(os.path.realpath(__file__))
        for filename in self.contents:
            full_path = f"{directory_path}/{filename}"
            dirpath = os.path.dirname(full_path)
            if not os.path.exists(dirpath):
                print(f"Directory doesn't exist, making it at:{dirpath}")
                os.makedirs(dirpath)
            print(f"Building File Contents: {full_path}")
            write_lines = []

            # Write Universal Header
            write_lines = self.__write_header(write_lines, filename)
            
            has_contents = False
            # Write Parameters
            write_lines = self._write_parameters_header(write_lines, self.contents[filename])
            for content in self.contents[filename]["PARAMETERS"]:
                has_contents = True
                write_lines = self.__write_parameters_table(write_lines, content)

            # Write Delegates
            write_lines = self._write_delegates_header(write_lines, self.contents[filename])
            for content in self.contents[filename]["DELEGATES"]:
                has_contents = True
                write_lines = self.__write_delegates_table(write_lines, content)
            
            # Write Functions
            write_lines = self.__write_functions_header(write_lines, self.contents[filename]["FUNCTIONS"])
            for content in self.contents[filename]["FUNCTIONS"]:
                has_contents = True
                write_lines = self.__write_functions_table(write_lines, content)

            # Write these lines to the file
            if has_contents is True:
                save_filename = full_path[:full_path.find(self.only_files)]+".md"
                print(f"Writing Contents To: {save_filename}")
                with open(f"{save_filename}", "w") as target:
                    for line in write_lines:
                        target.write(f"{line}\n")

    def __write_header(self, write_lines, filepath):
        count = 0
        for char in filepath:
            if char == "\\":
                count += 1
        back_to_index = ""
        for i in range(count-1):
            back_to_index+="../"
        write_lines.append(f"[Back To Index]({back_to_index}index.md)")
        write_lines.append("")
        filename = filepath.split("\\")[-1].replace(self.only_files,"")
        write_lines.append(f"# {filename}")
        write_lines.append("")
        if len(self.contents[filepath]["PARAMETERS"]) > 0:
            write_lines.append("[Jump To Parameters](#parameter-definitions)<br/>")
        if len(self.contents[filepath]["DELEGATES"]) > 0:
            write_lines.append("[Jump To Delegates](#delegate-definitions)<br/>")
        if len(self.contents[filepath]["FUNCTIONS"]) > 0:
            write_lines.append("[Jump To Function Definitions](#functions-definitions)<br/>")
        write_lines.append("")
        write_lines.append("--------------------------------------------------------")
        return write_lines

    def _write_parameters_header(self, write_lines, file_contents):
        if len(file_contents["PARAMETERS"]) < 1:
            return write_lines

        write_lines.append("## Parameter Definitions<a name=\"parameter-definitions\"></a>")
        write_lines.append("")
        write_lines.append("Select the parameter name from below to jump directly to it on this page.")
        write_lines.append("")
        for delegate in file_contents["PARAMETER"]:
            name = delegate["param_name"]
            write_lines.append(f"[{name}](#parameter-{name})<br>")
        write_lines.append("")
        return write_lines

    def _write_delegates_header(self, write_lines, file_contents):
        if len(file_contents["DELEGATES"]) < 1:
            return write_lines

        write_lines.append("## Delegate Definitions<a name=\"delegate-definitions\"></a>")
        write_lines.append("")
        write_lines.append("Select the delegate name from below to jump directly to it on this page.")
        write_lines.append("")
        for delegate in file_contents["DELEGATES"]:
            name = delegate["parameter_name"]
            write_lines.append(f"[{name}](#delegate-{name})<br>")
        write_lines.append("")
        return write_lines

    def _write_parameters_header(self, write_lines, file_contents):
        if len(file_contents["PARAMETERS"]) < 1:
            return write_lines

        write_lines.append("## Parameter Definitions<a name=\"parameter-definitions\"></a>")
        write_lines.append("")
        write_lines.append("Select the parameter name from below to jump directly to it on this page.")
        write_lines.append("")
        for parameter in file_contents["PARAMETERS"]:
            name = parameter["parameter_name"]
            write_lines.append(f"[{name}](#parameter-{name})<br>")
        write_lines.append("")
        return write_lines

    def __write_functions_header(self, write_lines, file_contents):
        if len(file_contents) < 1:
            return write_lines
        write_lines.append("## Function Definitions<a name=\"functions-definitions\"></a>")
        write_lines.append("")
        write_lines.append("Select the function name from below to jump directly to it on this page.")
        write_lines.append("")
        for content in file_contents:
            function_name = content["function_name"]
            write_lines.append(f"[{function_name}](#{function_name})<br>")
        write_lines.append("")
        return write_lines

    def __write_delegates_table(self, write_lines, content):
        delegate = content["delegate"]
        name = content["parameter_name"]
        desc = content["comment_summary"]
        params = content["comment_params"]
        write_lines.append("------------------")
        write_lines.append(f"### {delegate}<a name=\"delegate-{name}\"></a>")
        write_lines.append("")
        write_lines.append("")
        write_lines.append(f"> {desc}")
        write_lines.append("")
        if len(params) > 0:
            write_lines.append("| Parameter Name | Description")
            write_lines.append("|:---|:---|")
            for param in params:
                name = param["name"]
                desc = param["description"].replace("\\n","\n")
                write_lines.append(f"|{name}|{desc}|")
        else:
            write_lines.append("**No parameters**")
        write_lines.append("")
        write_lines.append("[Back To Top](#)")
        write_lines.append("")

        return write_lines

    def __write_functions_table(self, write_lines, content):
        function_name = content["function_name"]
        function = content["function"]
        expose = content["function_expose"]
        overriable = content["function_overridable"]
        desc = content["comment_summary"]
        params = content["comment_params"]
        returns = content["comment_returns"] or "Does not return anything"
        returns = returns.replace("\\n","<br>")
        write_lines.append("------------------")
        write_lines.append(f"### {function}<a name=\"{function_name}\"></a>")
        write_lines.append("")
        write_lines.append(f"> {desc}")
        write_lines.append("")
        write_lines.append("| Expose Value | Overrideable | Returns |")
        write_lines.append("|:---|:---|---:|")
        write_lines.append(f"|{expose}|{overriable}|{returns}|")
        write_lines.append("")
        if len(params) > 0:
            write_lines.append("| Parameter Name | Description |")
            write_lines.append("|:---|:---|")
            for param in params:
                param_name = param["name"]
                param_desc = param["description"].replace("\\n","\n") if param["description"] is not None else "***No found decription**"
                write_lines.append(f"|{param_name}|{param_desc}|")
        else:
            write_lines.append("**No parameters**")
        write_lines.append("")
        write_lines.append("[Back To Top](#)")
        write_lines.append("")

        return write_lines    

    def __write_parameters_table(self, write_lines, content):
        desc = content["tooltip"]
        name = content["parameter_name"]
        value = content["parameter_default_value"]
        default_type = content["parameter_type"]
        expose = content["parameter_exposed_value"]
        write_lines.append("------------------")
        write_lines.append(f"### {name}<a name=\"parameter-{name}\"></a>")
        write_lines.append("")
        write_lines.append(f"> {desc}")
        write_lines.append("")
        write_lines.append("| Exposed Value | Type | Default Value |")
        write_lines.append("|:---|:---|---:|")
        write_lines.append(f"|{expose}|{default_type}|{value}")
        write_lines.append("")
        write_lines.append("[Back To Top](#)")
        write_lines.append("")

        return write_lines

    # Index File Generation
    def write_index_file(self, contents, directory_path):
        print("Building index file...")
        if directory_path == ".":
            directory_path = os.path.dirname(os.path.realpath(__file__))
        if not os.path.exists(directory_path):
            print("Directory doesn't exist, making it...")
            os.makedirs(directory_path)
        sorted_dict = {}
        for key in sorted(contents):
            build_dict = self.create_dict_from_list(key.replace("\\","",1).split("\\"))
            if sorted_dict is None:
                sorted_dict = build_dict
            else:
                sorted_dict = self.merge_nested_dicts(sorted_dict, build_dict)
        with open(f"{directory_path}/index.md", "w") as target:
            target.write("<p align=\"center\">")
            target.write("<h1> Welcome To The Documentation </h1>")
            target.write("")
            target.write("<img src=\"https://i.imgur.com/e7hkanq.png\" width=\"70%\">")
            target.write("</p>")
            target.write("\n\n")
            target.write(" ## Documentation is available for the following components")
            target.write("\n\n")
            self.write_nested_index(sorted_dict, target, 0)
                
    def write_nested_index(self, sorted_dict, file_handle, indent=0, path=""):
        pad = " "*indent
        for key, value in sorted_dict.items():
            path+=f"{key}/"
            if self.can_print_key(value, path):
                file_handle.write(f"{pad} * {key}\n")
                if isinstance(value, list):
                    self.print_list(value, pad, path, file_handle)
                elif isinstance(value,dict):
                    if "0" in value.keys():
                        self.print_list(value["0"], pad, path, file_handle)
                        value.pop("0")
                    self.write_nested_index(value, file_handle, indent+2, path)
            path = path[:path.find(f"{key}/")]

    def print_list(self, input_list, pad, path, file_handle):
        pad = f"{pad}  "
        tmp_path = path.replace("/","\\")
        for item in input_list:
            if (len(self.contents[f"\\{tmp_path}{item}"]["FUNCTIONS"]) > 0 or 
            len(self.contents[f"\\{tmp_path}{item}"]["DELEGATES"]) > 0 or 
            len(self.contents[f"\\{tmp_path}{item}"]["PARAMETERS"]) > 0):
                display = item.replace(self.only_files,"",1)
                file_handle.write(f"{pad}* [{display}]({path}{display}.md)\n")
    
    def can_print_key(self, value, path):
        if isinstance(value, dict):
            return True
        elif isinstance(value, list):
            tmp_path = path.replace("/","\\")
            for item in value:
                if (len(self.contents[f"\\{tmp_path}{item}"]["FUNCTIONS"]) > 0 or 
                len(self.contents[f"\\{tmp_path}{item}"]["DELEGATES"]) > 0 or 
                len(self.contents[f"\\{tmp_path}{item}"]["PARAMETERS"]) > 0):
                    return True
            return False

    def create_dict_from_list(self, tree_list):
        tree_dict = {}
        tmp_list = []
        for key in reversed(tree_list):
            if key.endswith(self.only_files):
                tmp_list.append(key)
            elif len(tmp_list) > 0:
                tree_dict = {key.replace(self.only_files,""): tmp_list}
                tmp_list = []
            else:
                tree_dict = {key.replace(self.only_files,""): tree_dict}
        return tree_dict

    def merge_nested_dicts(self, a, b, path=None):
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self.merge_nested_dicts(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass # same leaf value
                elif isinstance(a[key], list) and isinstance(b[key], list):
                    for item in b[key]:
                        if item not in a[key]:
                            a[key].append(item)
                elif isinstance(a[key], list) and isinstance(b[key], dict):
                    tmp = {}
                    tmp = a[key]
                    a[key] = b[key]
                    a[key]["0"] = tmp
                elif isinstance(a[key], dict) and isinstance(b[key], list):
                    if "0" not in a[key]:
                        a[key]["0"] = []
                    for item in b[key]:
                        if item not in a[key]["0"]:
                            a[key]["0"].append(item)
                else:
                    print(key)
                    print("A:")
                    print(a[key])
                    print("B:")
                    print(b[key])
                    print("A IS DICT: "+str(isinstance(a[key], dict)))
                    print("B IS DICT: "+str(isinstance(b[key], dict)))
                    print("A IS LIST: "+str(isinstance(a[key], list)))
                    print("B IS LIST: "+str(isinstance(b[key], list)))
                    raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
            else:
                a[key] = b[key]
        return a
