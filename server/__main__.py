from fastapi        import FastAPI
from server.routers import fire_area, hms_fire, hms_smoke, lake, lake_buffer, lake_point, lake_poly, log, populated_place


app = FastAPI()


app.include_router(fire_area.router)
app.include_router(hms_fire.router)
app.include_router(hms_smoke.router)
app.include_router(lake.router)
app.include_router(lake_buffer.router)
app.include_router(lake_point.router)
app.include_router(lake_poly.router)
app.include_router(log.router)
app.include_router(populated_place.router)