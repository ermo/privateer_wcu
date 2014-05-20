#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file is a python script called find_vs_config.py part of find_vs_config.
# Copyright (C) 2008  wolphin
# find_vs_config is distributed under the GNU GPL version 3 or later.
# Please see <http://www.gnu.org/licenses/license-list.html>.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import os, os.path, sys, xml.sax.saxutils
manualvsdir = "" # You can manually specify the location of the vegastrike source dir here.
seekdir = "vegastrike/src/"
filedir = os.path.realpath(os.path.dirname(__file__))
basedir = ""
if len(sys.argv) > 1: # Try program argument 1 to find vs dir
    argvsdir = sys.argv[1] # First program argument should be vs dir
    if (os.path.exists(argvsdir) and os.path.isdir(argvsdir)):
        basedir = os.path.realpath(argvsdir)
if basedir == "" and manualvsdir != "": #Try manualvsdir to find vs dir
    if (os.path.exists(manualvsdir) and os.path.isdir(manualvsdir)):
        basedir = os.path.realpath(manualvsdir)
if basedir == "": # Search all parent directories to find vs dir
    basedir = filedir
    while True:
        curdir = os.path.join(basedir, seekdir)
        if os.path.exists(curdir) and os.path.isdir(curdir):
            break
        if basedir == "/":
            print("Could not find vegastrike/src directory anywhere below file location.")
            sys.exit(-1)
        basedir = os.path.dirname(basedir)
if basedir != "":
    curdir = os.path.join(basedir, seekdir)
    if os.path.exists(curdir) and os.path.isdir(curdir):
        basedir = curdir # Found seekdir in basedir, will use that instead
print("Will use vegastrike source at: " + basedir)
vegastrike_dir = os.path.realpath(basedir)
out_file = os.path.join(filedir, "default_values_vegastrike_config.xml") # Save output in filedir
print("Will create output at: " + out_file)
search_strings = ["vs_config->g"]
config = {"bindings":[], "colors":[], "variables":[]}
pre_config = {"bindings":"", "colors":"""       <section name="absolute">
        <!-- absolute colors -->
            <color name="red"    r="1.0"  g="0.0"  b="0.0"  a="1.0"/>
            <color name="green"  r="0.0"  g="1.0"  b="0.0"  a="1.0"/>
            <color name="blue"   r="0.0"  g="0.0"  b="1.0"  a="1.0"/>
            <color name="cyan"   r="0.0"  g="1.0"  b="1.0"  a="1.0"/>
            <color name="yellow"     r="1.0"  g="1.0"  b="0.0"  a="1.0"/>
            <color name="brown"  r="0.6"  g="0.2"  b="0.0"  a="1.0"/>
            <color name="black"  r="0.0"  g="0.0"  b="0.0"  a="1.0"/>
            <color name="clear"  r="0.0"  g="0.0"  b="0.0"  a="0.0"/>
            <color name="white"  r="1.0"  g="1.0"  b="1.0"  a="1.0"/>
            <color name="grey"   r="0.5"  g="0.5"  b="0.5"  a="1.0"/>
            <color name="light-grey" r="0.8"  g="0.8"  b="0.8"  a="1.0"/>
            <color name="violet"     r="1.0"  g="0.0"  b="1.0"  a="1.0"/>
            <color name="light-blue" r="0.68" g="0.9"  b="1.0"  a="1.0"/>
            <color name="pink"   r="1.0"  g="0.47" b="0.64" a="1.0"/>
            <color name="dark-red"   r="0.1"  g="0.0"  b="0.0"  a="1.0"/>
            <color name="dark-blue"  r="0.0"  g="0.0"  b="0.2"  a="1.0"/>
            <color name="orange"     r="1.0"  g="0.4"  b="0.0"  a="1.0"/>
        </section>
""", "variables":""}
post_config = {"bindings":"", "colors":"", "variables":""}

# Search files for search_strings and put them in config
for dirpath, dirnames, filenames in os.walk(vegastrike_dir, topdown=True):
    if ".svn" in dirnames:
        dirnames.remove(".svn")
    if ".deps" in dirnames:
        dirnames.remove(".deps")
    reldir = (dirpath.replace(vegastrike_dir, "") + os.path.sep).lstrip("/")
    for f in filenames:
        if f.endswith(".cpp") or f.endswith(".h"):
            data = open(os.path.join(dirpath, f), 'rU')
            ln = 0
            line = data.readline()
            while line != "":
                ln += 1
                linebroken = []
                line = line.strip(" \t\n\r").replace("\n", " ")
                # Todo: Find commandMap stuff
#               if line.find("commandMap") >= 0:
#                   print reldir + f + ":" + str(ln) + " " + line
                for searched in search_strings:
                    vsc_loc = line.find(searched) # Location of the string or -1 if not found
                    if vsc_loc > 0:
                        found = searched
                        break
                if vsc_loc >= 0 and line.find("//", 0, vsc_loc) < 0: # If string found and line not commented before it
                    line = line[vsc_loc:] # Removes up to beginning of searched, i.e. "vs_config->g" + ...
                    open_p = line.find("(") # Find first (
                    while open_p < 0:
                        nextline = data.readline()
                        if nextline == "":
                            linebroken.append("End of file") # End of file, uhoh
                            break
                        line += " " + nextline.strip(" \t\n\r").replace("\n", " ")
                        open_p = line.find("(") # Find first (
                    method = line[:open_p].strip() # Gets part before (
                    method = method[method.find("->")+2:] # Gets the part after ->
                    line = line[open_p+1:]
                    num_par_op = 1
                    num_par_cl = 0
                    close_p = -1
                    while True:
                        close_pn = line.find(")", close_p + 1) # Find next )
                        if close_pn < 0: # Need more lines to find a )
                            nextline = data.readline() # Get another line
                            if nextline == "":
                                linebroken.append("End of file") # End of file, uhoh
                                break
                            line += " " + nextline.strip(" \t\n\r").replace("\n", " ")
                        else: # Found next )
                            num_par_op += line.count("(", close_p + 1, close_pn)
                            num_par_cl += 1
                            if (num_par_op - num_par_cl) <= 0:
                                line = line[:close_pn]
                                break # We've closed the original parenthesis
                            else: # Commas between () are not to be splitted, replace them to be restored after split.
                                open_pa =  line.rfind("(", 0, close_pn) #Find ( just before the latest )
                                line = line[:open_pa] + line[open_pa:close_pn].replace(",", "\n") + line[close_pn:]
                            close_p = close_pn
                    info = line.split(",") # Usually: info = [section, variable, value] or [section, subsection, variable, value]
                    for nb in range(len(info)): # Fix lines
                        if len(info[nb]) == 0:
                            continue
                        text = info[nb].strip(" \t")
                        text = text.replace("\n", ",") # Restore commas within ().
                        text = xml.sax.saxutils.escape(text) # Replace xml entities
                        text = text.replace(r'\"', '"') # Unescape quotes
                        text = text.replace(r"\'", "'") # Unescape and switch quotes
                         # Enforce different quotes at the extremities vs center
                        text = text[0].replace("'", '"') + text[1:len(text)-1].replace('"', "'") + text[len(text)-1].replace("'", '"')
                        info[nb] = text
                    info_dict = {}
                    def putValInDict(valname, valindex, info_dict=info_dict, info=info, linebroken=linebroken):
                        if len(info) > valindex: # If split returned a value for this index
                            val = info[valindex].strip()
                            info_dict[valname] = val
                            if not ((val[0] == '"' or val[0] == "'") and val[0] == val[len(val)-1]):
                                linebroken.append(valname + " not quoted")
                        else:
                            info_dict[valname] = ""
                            linebroken.append("no " + valname)
                    putValInDict("section", 0, info_dict, info, linebroken)
                    nb_subsection = len(info) - 3
                    if nb_subsection > 0:
                        putValInDict("subsection", 1, info_dict, info, linebroken)
                    else:
                        nb_subsection = 0
                        info_dict["subsection"] = ""
                    if nb_subsection > 2:
                        print(info[1]) # Todo: should add subsubsection support if you see some printed on execution.
                    putValInDict("variable", nb_subsection + 1, info_dict, info, linebroken)
                    putValInDict("value", nb_subsection + 2, info_dict, info, linebroken)
                    info_dict["method"] = method
                    info_dict["linebroken"] = linebroken
                    info_dict["reference"] = {reldir + f:str(ln)}
                    # Todo: add bindings option
                    if info_dict["method"].find("Color") > 0:
                        config["colors"].append(info_dict)
                    else:
                        config["variables"].append(info_dict)
                line = data.readline()
            data.close()
def sortListOfDict(list_to_sort, sortkeystuple=("section", "subsection", "variable", "value")):
    prepare_list = []
    for info in list_to_sort:
        info_list = []
        for key in sortkeystuple:
            info_list.append(info[key])
        info_list.append(info)
        prepare_list.append(info_list)
    prepare_list.sort()
    sorted_list = []
    for info_list in prepare_list:
        sorted_list.append(info_list[len(sortkeystuple)])
    return sorted_list
for metasec in config.keys():
    config[metasec] = sortListOfDict(config[metasec])

i = 0
while(True): # Merge lines with duplicate section/variable/value combination
    def mergeReference(list_to_merge, i, testkeystuple=("section", "subsection", "variable", "value")):
        if i <= len(list_to_merge) - 2:
            same = True
            while same and i <= len(list_to_merge) - 2:
                inf = list_to_merge[i]
                inf_next = list_to_merge[i+1]
                for key in testkeystuple:
                    same = same and inf[key] == inf_next[key]
                if same:
                    for f, ln in inf_next["reference"].items():
                        if f in inf["reference"]:
                            inf["reference"][f] += "," + ln
                        else:
                            inf["reference"][f] = ln
                    list_to_merge.pop(i+1)
    for metasec in config.keys():
        mergeReference(config[metasec], i)
    i += 1
    finished = True
    for metasec in config.keys():
        finished = finished and i > len(config[metasec]) - 2
    if finished:
        break

# Write config from the lists of dictionaries
data = open(out_file, 'wU') # Open file to send output to
data.write('<vegaconfig>\n')
sortedkeys = list(config.keys())
sortedkeys.sort()
for key in sortedkeys:
    data.write('\t<' + key + '>\n')
    data.write(pre_config[key])
    last_section = ""
    last_subsection = ""
    last_variable = ""
    broken_section = False
    broken_subsection = False
    for info in config[key]:
        method = info["method"]
        section = info["section"]
        subsection = info["subsection"]
        variable = info["variable"]
        value = info["value"]
        linebroken = info["linebroken"]
        ref = info["reference"] # dict i.e. {f:ln}
#Todo: Do subsubsection or a general method to print an arbitrary number of (sub)sections, if needed.
        if last_subsection != subsection and last_subsection != "": # If subsection changed and not on the first section
            if broken_subsection:
                data.write('<!-- ')
            data.write('\t\t\t</section>') # Close section
            if broken_subsection:
                data.write('\t-->')
            data.write('\n')
        if last_section != section: # When there's a section change
            if last_section != "": # If not on the first section
                if broken_section:
                    data.write('<!-- ')
                data.write('\t\t</section>') # Close section
                if broken_section:
                    data.write('\t-->')
                data.write('\n')
            broken_section = not ((section[0] == '"' or section[0] == "'") and section[0] == section[len(section)-1])
            if broken_section:
                data.write('<!-- ')
            data.write('\t\t<section name='+section+' >') # Open section
            if broken_section:
                data.write('\t-->')
            data.write('\n')
        if section == "": # If no section it's not broken
            broken_section = False
        if broken_section:
            linebroken.append("broken section")
        if last_subsection != subsection and subsection != "": # If section changed and new section
            broken_subsection = not ((subsection[0] == '"' or subsection[0] == "'") and subsection[0] == subsection[len(subsection)-1])
            if broken_subsection:
                data.write('<!-- ')
            data.write('\t\t\t<section name='+subsection+' >') # Open section
            if broken_subsection:
                data.write('\t-->')
            data.write('\n')
        if subsection == "": # If no subsection it's not broken
            broken_subsection = False
        if broken_subsection:
            linebroken.append("broken subsection")
        if last_variable == variable:
            linebroken.append("duplicate variable")
        if linebroken != []:
            data.write('<!-- ')
        if subsection != "":
            data.write('\t')
        if key == "colors": # Colors are defined by ref from the absolute section we add in pre_config
            data.write('\t\t\t<color name='+variable)
            data.write(' section="absolute"')
            data.write(' ref='+value+' />')
        elif key == "bindings":
            pass
#Output of variables in bindings would look like:
#<bind key="S" modifier="none" command="Cockpit::SkipMusicTrack" />
#<bind mouse="0" player="0" button="0" modifier="none" command="FireKey" />
#<axis name="x" mouse="0" axis="0" inverse="false" />
#<bind joystick="0" player="0" button="0" modifier="none" command="FireKey" />
#<axis name="throttle" joystick="0" axis="2"/>
#<axis name="z" joystick="0" axis="3"/>
#<axis name="hatswitch" nr="0" margin="0.15" joystick="0" axis="2">
#   <hatswitch value="-1.0"/>
#<bind hatswitch="0" button="2" modifier="none" command="Cockpit::SwitchLVDU" />
        elif key == "variables":
            data.write('\t\t\t<var name='+variable)
            data.write(' value='+value+' />')
        if linebroken != []:
            data.write(' -->')
        data.write('\t<!-- ')
        for file_name, line_number in ref.items():
            data.write(file_name+':'+str(line_number)+' ')
        if linebroken != []:
            data.write(str(linebroken)+' ')
        data.write('-->')
        data.write('\n')
        last_section = section
        last_subsection = subsection
        last_variable = variable
    if last_subsection != "":
        if broken_subsection :
            data.write('<!-- ')
        data.write('\t\t\t</section>')
        if broken_subsection :
            data.write('\t-->')
        data.write('\n')
    if last_section != "":
        if broken_section :
            data.write('<!-- ')
        data.write('\t\t</section>')
        if broken_section :
            data.write('\t-->')
        data.write('\n')
    data.write(post_config[key])
    data.write('\t</' + key + '>\n')
data.write('</vegaconfig>')
data.close()
