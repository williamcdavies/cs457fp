from fire_area import get_fire_areas, get_fire_area
from hms_fire  import get_hms_fires, get_hms_fire

def main():
    while True:
        print(
"""
usage: 
    \\q
    \\get_fire_areas [offset] [limit]
    \\get_fire_area  [year]   [id]
    \\get_hms_fires  [offset] [limit]
    \\get_hms_fire   [year]   [id]
"""
        )
        cmd = input("> ").strip().split()
       
        if not cmd:
            continue
        
        try:
            if cmd[0] == "\\q":
                break
            elif cmd[0] == "\\get_fire_areas":
                get_fire_areas(cmd[1], cmd[2])
            elif cmd[0] == "\\get_fire_area":
                get_fire_area(cmd[1], cmd[2])
            elif cmd[0] == "\\get_hms_fires":
                get_hms_fires(cmd[1], cmd[2])
            elif cmd[0] == "\\get_hms_fire":
                get_hms_fire(cmd[1], cmd[2])
            else:
                print(f"command not found: {cmd[0]}")
        except IndexError:
            print("error: unexpected parameter(s)")

if __name__ == "__main__":
    main()