# Concurrent SNCF

ENSAI 2nd-year IT project.

We build an API for a new train company that uses the SNCF network.  
The goal is to help the commercial team offer train trips to customers.

Stations and travel times come from the [SNCF API](https://numerique.sncf.com/startup/api/).

**Tutor:** Kévin Leroy

## Contributors

- Salma Arraji
- Adam Ouattara
- Noé Sidobre
- Jonas Van Hecke
- Maxime Yvano

## What the API does

- User accounts (`CLIENT`, `COLLABORATEUR`, `ADMIN`)
- Operating lines between two stations
- Planned trips (date, time, seats, price)
- Search trips from a station to another
- One extra feature to stand out from SNCF (to be chosen later)

Optional later: booking trips and travel classes (standard / premium).

API documentation: `/docs` once the server is running.

## How to run

```bash
uv sync --project backend
uv run --project backend python backend/src/main.py
```
