""" Script to export items, encounters, etc as Markdown tables """
import sys
import os
import re
import json
import shutil
from os.path import join as joinp
from collections import namedtuple
from functools import cmp_to_key

DEBUG = True

# TODO: Add more here
TITLE_CASE_EXCEPTIONS = {

}

def TitleCase(s):
    """ Convert a string to Title Case """
    parts = re.split(r'[^\w]|[_-]', s)
    l = []
    for p in parts:
        if p in TITLE_CASE_EXCEPTIONS:
            l.append(p)
            continue
        elif p.startswith('TM'):
            l.append(p)
            continue
        else:
            p = p.lower().capitalize()
        p = TITLE_CASE_EXCEPTIONS.get(p, p)
        l.append(p)
    return ' '.join(l)

#WILD_ENCOUNTERS_REL_PATH = joinp('src', 'data', 'wild_encounters.json')
WILD_ENCOUNTERS_REL_PATH = 'wild_encounters.json'

MapDoc = namedtuple('MapDoc', ['name', 'land_mons', 'water_mons', 'rock_smash_mons', 'fishing_mons', 'hidden_mons'])

def parse_species_list(j):
    d = dict()
    for obj in j:
        species = obj.get('species', 'SPECIES_NONE')
        if species == 'SPECIES_NONE':
            continue
        species = species.replace('SPECIES_', '')
        d[species] = None
    l = [k for k in d]
    return l

def parse_map_encounters(obj):
    map_name = obj['map']
    land_mons = obj.get('land_mons', dict()).get('mons', [])
    water_mons = obj.get('water_mons', dict()).get('mons', [])
    rock_smash_mons = obj.get('rock_smash_mons', dict()).get('mons', [])
    fishing_mons = obj.get('fishing_mons', dict()).get('mons', [])
    hidden_mons = obj.get('hidden_mons', dict()).get('mons', [])
    # Construct tuple / doc
    #land_mons = parse_species_list(land_mons)
    #water_mons = parse_species_list(water_mons)
    #rock_smash_mons = parse_species_list(rock_smash_mons)
    #fishing_mons = parse_species_list(fishing_mons)
    #hidden_mons = parse_species_list(hidden_mons)
    tup = MapDoc(map_name, land_mons, water_mons, rock_smash_mons, fishing_mons, hidden_mons)
    return tup

def map_key(map_name) -> str:
    """ Generate a sortable key based on map name """
    route_m = re.search(r"ROUTE(\d+)", map_name, flags=re.IGNORECASE)
    # routes get a key == their #
    if route_m:
        route_num = route_m.group(1)
        # Mirage Spots get +1000
        if 'MIRAGE' in map_name:
            route_num = 'z' + route_num
        return route_num
    elif 'DESERT_UNDERPASS' in map_name:
        return 'y' + map_name
    elif 'MIRAGE' in map_name:
        return 'z' + map_name
    return map_name

def normalize_map_name(map_name):
    map_name = map_name.replace('MAP_', '')
    map_name = TitleCase(map_name)
    map_name = re.sub(r'Route(\d+)', r'Route \1', map_name)
    map_name = re.sub(r'(\d)f', r'\1F', map_name)
    map_name = re.sub(r'(\d)r', r'\1R', map_name)
    return map_name

def parse_wild_encounters(root=''):
    in_path = joinp(root, WILD_ENCOUNTERS_REL_PATH)
    with open(in_path, 'r') as f:
        data = json.load(f)
    encounters_data = data['wild_encounter_groups'][0]['encounters']
    docs = dict()
    for encounter in encounters_data:
        # skip cosmetic / cry-only areas
        if encounter.get('land_mons', dict()).get('encounter_rate', 1) == 0:
            continue
        doc = parse_map_encounters(encounter)
        if 'UNUSED' in doc.name:
            continue
        docs[doc.name] = doc
    # TODO: add some extra / notes
    return docs

# sort by location, then rate, then species name
def sort_table_rows(row1, row2):
    loc1 = re.split('"', ((re.split('"location=', row1)[0])))[5]
    loc2 = re.split('"', ((re.split('"location=', row2)[0])))[5]

    match loc1:
        case "grass":
            row1_score = 0
        case "surfing":
            row1_score = 1
        case "rock_smash":
            row1_score = 2
        case "old_rod":
            row1_score = 3
        case "good_rod":
            row1_score = 4
        case "super_rod":
            row1_score = 5
        case "hidden":
            row1_score = 6
    match loc2:
        case "grass":
            row2_score = 0
        case "surfing":
            row2_score = 1
        case "rock_smash":
            row2_score = 2
        case "old_rod":
            row2_score = 3
        case "good_rod":
            row2_score = 4
        case "super_rod":
            row2_score = 5
        case "hidden":
            row2_score = 6

    if row1_score < row2_score:
        return -1
    elif row1_score > row2_score:
        return 1
    else:
        # location was the same; sort by encounter rate
        rate1 = int(re.split('"', ((re.split('"rate=', row1)[0])))[9])
        rate2 = int(re.split('"', ((re.split('"rate=', row2)[0])))[9])
        if rate1 > rate2:
            return -1
        elif rate1 < rate2:
            return 1
        else:
            # encounter rate was the same; sort by species name
            species1_name = re.split('"', ((re.split('"species_name=', row1)[0])))[3]
            species2_name = re.split('"', ((re.split('"species_name=', row2)[0])))[3]
            names = [species1_name, species2_name]
            names.sort()

            if names.index(species1_name) == 0:
                return -1
            else:
                return 1

def create_table_rows(doc,type):
    encounters = dict()
    for i,mon in enumerate(eval("doc." + type)):
        # initialize encounter_rates and location data based on encounter type
        match type:
            case "land_mons":
                encounter_rates = [20,20,10,10,10,10,5,5,4,4,1,1]
                location = "grass"
            case "water_mons":
                encounter_rates = [60,30,5,4,1]
                location = "surfing"
            case "rock_smash_mons":
                encounter_rates = [60,30,5,4,1]
                location = "rock_smash"
            case "fishing_mons":
                encounter_rates = [70,30,60,20,20,40,40,15,4,1]
                if i in [0,1]:
                    location = "old_rod"
                if i in [2,3,4]:
                    location = "good_rod"
                if i in [5,6,7,8,9]:
                    location = "super_rod"
            case "hidden_mons":
                encounter_rates = [60,30,10]
                location = "hidden"

        species = mon.get('species', 'SPECIES_NONE')
        if species == 'SPECIES_NONE':
            continue
        species = species.replace('SPECIES_', '').lower()

        species_name = ' '.join(reversed(species.split('_')))
        # fix nidoran's name
        if species == "nidoran_f":
            species_name = "Nidoran♀"
        if species == "nidoran_m":
            species_name = "Nidoran♂"

        min_level = str(mon.get('min_level'))
        max_level = str(mon.get('max_level'))

        if species in encounters and location in encounters[species]:
            # update level and encounter rate
            if min_level < encounters[species][location]["min_level"]:
                encounters[species][location]["min_level"] = min_level
            if max_level > encounters[species][location]["max_level"]:
                encounters[species][location]["max_level"] = max_level
            encounters[species][location]["rate"] += encounter_rates[i]
        else:
            # intialize species entry
            if species not in encounters:
                encounters[species] = {}

            # create new encounter entry
            data = {"species_name": species_name, "min_level": min_level, "max_level": max_level, "rate": encounter_rates[i]}
            encounters[species][location] = data

    rows = []
    # iterate over encounters and create table entries for them
    for species,locations in encounters.items():
        for location in locations:
            # create level w/ range if needed
            if locations[location]['min_level'] == locations[location]['max_level']:
                level = str(locations[location]['min_level'])
            else:
                level = str(locations[location]['min_level']) + "-" + str(locations[location]['max_level'])

            # create table row
            row = f'{{% include encounter_entry.liquid species="{species}" species_name="{locations[location]['species_name']}" location="{location}" level="{level}" rate="{locations[location]['rate']}" %}}'
            rows.append(row)
        
    rows.sort(key=cmp_to_key(sort_table_rows))
    return rows

def get_map_table(doc):
    lines = []
    map_name = normalize_map_name(doc.name)
    lines.append(f'{{% include encounter_table_header.liquid map="{map_name}" %}}')
    for type in ["land_mons","water_mons","rock_smash_mons","hidden_mons","fishing_mons"]:
        rows = create_table_rows(doc,type)
        for row in rows:
            if row is not None:
                lines.append(row)
    lines.append(f'{{% include encounter_table_footer.liquid %}}')
    return lines

def copy_icons(docs, src, dest):
    """ Copy mon icons from src to dest, based on encounters """
    all_species = set()
    for doc in docs.values():
        all_species.update(doc.land_mons)
        all_species.update(doc.water_mons)
        all_species.update(doc.fishing_mons)
        all_species.update(doc.rock_smash_mons)
        all_species.update(doc.hidden_mons)
    for species in all_species:
        species = species.replace('SPECIES_', '').lower()
        src_path = joinp(src, f'{species}.png')
        dest_path = joinp(dest, f'{species}.png')
        src_path = src_path.replace('_alolan', '-alola')
        src_path = src_path.replace('_galarian', '-galar')
        src_path = src_path.replace('_f', '-f')
        src_path = src_path.replace('_m', '-m')
        try:
            shutil.copy(src_path, dest_path)
        except Exception as e:
            print(e, file=sys.stderr)

def export_wild_encounters(out_path, root=''):
    docs = parse_wild_encounters(root=root)
    # copy_icons(docs, 'icons', '.worktrees/pages/assets/images/icons')
    docs_sorted = [v for k, v in docs.items()]
    docs_sorted.sort(key=lambda d: map_key(d.name))
    if out_path == '-':
        f = sys.stdout
    else:
        f = open(out_path, 'w')
    fprint = lambda s: print(s, end='', file=f)
    # Export
    fprint("""---
title: Epsilon Emerald
layout: default
---

"""
    )
    fprint('{% include encounters_page_header.liquid %}')
    fprint('\n\n')
    for doc in docs_sorted:
        table_lines = get_map_table(doc)
        fprint('\n'.join(table_lines))
        fprint('\n\n')

def main(*args):
    args = list(args)
    export_wild_encounters('encounters.md')

if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
