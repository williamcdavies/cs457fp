from datetime        import datetime


from util.fire_area       import get_fire_areas, get_fire_area
from util.hms_fire        import get_hms_fires, get_hms_fire
from util.hms_smoke       import get_hms_smokes, get_hms_smoke
from util.lake_buffer     import get_lakes_buffers, get_lakes_buffer
from util.lake_point      import get_lakes_points, get_lakes_point
from util.lake_poly       import get_lakes_polys, get_lakes_poly
from util.lake            import get_lakes, get_lake
from util.log             import get_logs, get_log, post_log
from util.populated_place import get_populated_places, get_populated_place
from util.util            import intersects


def main():
    while True:
        print(
"""
usage: 
    \\q
    \\get_fire_areas       [offset]   [limit]
    \\get_fire_area        [year]     [id]
    \\get_hms_fires        [offset]   [limit]
    \\get_hms_fire         [year]     [id]
    \\get_hms_smokes       [offset]   [limit]
    \\get_hms_smoke        [year]     [id]
    \\get_lakes_buffers    [offset]   [limit]
    \\get_lakes_buffer     [hylak_id]
    \\get_lakes_points     [offset]   [limit]
    \\get_lakes_point      [hylak_id]
    \\get_lakes_polys      [offset]   [limit]
    \\get_lakes_polys      [hylak_id]
    \\get_lakes            [offset]   [limit]
    \\get_lake             [hylak_id]
    \\get_logs             [offset]   [limit]
    \\get_log              [id]
    \\get_populated_places [offset]   [limit]
    \\get_populated_place  [id]
    \\intersects           [path_a]   [col_a] [id_a] [path_b] [col_b] [id_b]
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
            
            elif cmd[0] == "\\get_hms_smokes":
                get_hms_smokes(cmd[1], cmd[2])
            elif cmd[0] == "\\get_hms_smoke":
                get_hms_smoke(cmd[1], cmd[2])
            
            elif cmd[0] == "\\get_lakes_buffers":
                get_lakes_buffers(cmd[1], cmd[2])
            elif cmd[0] == "\\get_lakes_buffer":
                get_lakes_buffer(cmd[1])

            elif cmd[0] == "\\get_lakes_points":
                get_lakes_points(cmd[1], cmd[2])
            elif cmd[0] == "\\get_lakes_point":
                get_lakes_point(cmd[1])

            elif cmd[0] == "\\get_lakes_polys":
                get_lakes_polys(cmd[1], cmd[2])
            elif cmd[0] == "\\get_lakes_poly":
                get_lakes_poly(cmd[1])

            elif cmd[0] == "\\get_lakes":
                get_lakes(cmd[1], cmd[2])
            elif cmd[0] == "\\get_lake":
                get_lake(cmd[1])

            elif cmd[0] == "\\get_logs":
                get_logs(cmd[1], cmd[2])
            elif cmd[0] == "\\get_log":
                get_log(cmd[1])

            elif cmd[0] == "\\get_populated_places":
                get_populated_places(cmd[1], cmd[2])
            elif cmd[0] == "\\get_populated_place":
                get_populated_place(cmd[1])

            elif cmd[0] == "\\intersects":
                intersects(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
            
            else:
                print(f"command not found: {cmd[0]}")

            post_log(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cmd[0])
        except IndexError:
            print("error: unexpected parameter(s)")

if __name__ == "__main__":
    main()