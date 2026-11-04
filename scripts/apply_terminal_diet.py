#!/usr/bin/env python3
import os
import re

def apply_terminal_diet():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(f"Base Directory: {base_dir}")

    # 1. RenewableVietNam/index.html
    idx_path = os.path.join(base_dir, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        t = f.read()

    t = t.replace(
        "Integrated visual telemetry tracking 107.5 GW generation pipelines, 168 eco-industrial parks, 22,055+ EV charging ports, and CPM statutory permitting.",
        "107.5 GW generation pipeline &middot; 168 Eco-IPs &middot; 22,055+ EV ports &middot; CPM statutory permitting."
    )
    t = t.replace(
        "Statutory framework orchestrating utility-scale generation expansion, ultra-high-voltage transmission corridors, competitive wholesale power markets, and green hydrogen power-to-X infrastructure across $134.7B in capital allocation through 2030. Click any pillar to inspect telemetry and direct gateway.",
        "PDP8 expansion &middot; UHV corridors &middot; $134.7B allocation &middot; Click pillar to navigate."
    )
    t = t.replace(
        "Quantitative models covering long-term net-zero trajectories, merit-order dispatch curves, capital expenditure allocations, grid voltage hierarchies, wholesale market clearing, and territorial power balance.",
        "10-module telemetry &middot; Dispatch, capex, voltage &amp; market models."
    )
    t = t.replace(
        "107.5 GW generation pipeline, offshore/onshore wind quotas, 500kV corridors &amp; provincial GIS telemetry.",
        "107.5 GW pipeline, wind quotas &amp; 500kV GIS telemetry."
    )
    t = t.replace(
        "168 Eco-IPs across 104.4K ha, clean utility sizing, rooftop solar viability &amp; Decree 35 ESG compliance.",
        "168 Eco-IPs, rooftop solar &amp; Decree 80 DPPA wheeling."
    )
    t = t.replace(
        "22,055+ verified EV charging ports, expressway fast-charging corridor telemetry &amp; CPO spatial density.",
        "22,055+ verified ports &amp; expressway fast corridors."
    )
    t = t.replace(
        "6-stage statutory CPM gate scheduling, Decree 80 DPPA wheeling, Land Law 2024 compliance &amp; M&amp;A due diligence.",
        "Statutory CPM scheduling &amp; M&amp;A legal due diligence."
    )

    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(t)
    print("Updated index.html")

    # 2. RenewableVietNam/industrial/index.html
    ind_path = os.path.join(base_dir, "industrial", "index.html")
    with open(ind_path, "r", encoding="utf-8") as f:
        t = f.read()

    t = t.replace(
        "Comprehensive institutional intelligence on Vietnam's Tier-1 eco-industrial parks: high-voltage substation interties (110kV/220kV), rooftop solar installations, DPPA bilateral wheeling readiness, and ESG certifications for multinational manufacturing siting.",
        "168 Tier-1 Eco-IPs &middot; 110kV/220kV interties &middot; Rooftop PV &amp; DPPA wheeling readiness."
    )
    t = t.replace(
        "Correlated analytics uniting 168 eco-industrial parks with the National Transmission Grid (1,915 substations and 2,877 circuits). Click any bar or slice to cross-filter the directory table.",
        "168 Eco-IPs &middot; 1,915 Substations &middot; Cross-filter active."
    )
    t = t.replace(
        "Institutional allocation intelligence modeling onsite rooftop PV self-generation, statutory DPPA bilateral grid wheeling, and EVN baseload firming across Vietnam's 168 prioritized eco-industrial parks.",
        "Rooftop PV, DPPA bilateral wheeling &amp; EVN baseload firming across 168 eco-IPs."
    )

    # Clean up card titles and heights
    ind_card_replacements = [
        ("Visual 02 &middot; Voltage Interties", "Voltage Interties (110kV/220kV)"),
        ("Visual 04 &middot; Substation Headroom", "Substation Headroom (MVA)"),
        ("Visual 06 &middot; 500kV/220kV Proximity", "500kV/220kV Proximity"),
        ("Visual 01 &middot; Regional Footprint", "Regional Siting Footprint"),
        ("Visual 03 &middot; DPPA Decree 80 Tiers", "Decree 80 DPPA Readiness"),
        ("Visual 08 &middot; Archetype Radar", "Archetype Demand Dimensions"),
        ("Visual 10 &middot; Net-Zero Path", "Net-Zero Trajectory (2025-2050)"),
        ("Visual 05 &middot; Clean Share Mix", "Clean Share Distribution"),
        ("Visual 07 &middot; Top 8 Flagships", "Top 8 Flagship Eco-IPs"),
        ("Visual 09 &middot; Province Density", "Top 10 Siting Provinces"),
    ]
    for old_title, new_title in ind_card_replacements:
        t = t.replace(old_title, new_title)

    # Increase canvas container heights
    t = t.replace('class="relative h-44 w-full">\n              <canvas id="indSubstationDoughnutChart"', 'class="relative h-56 w-full">\n              <canvas id="indSubstationDoughnutChart"')
    t = t.replace('class="relative h-52 w-full">\n              <canvas id="indGridHostingCapacityChart"', 'class="relative h-60 w-full">\n              <canvas id="indGridHostingCapacityChart"')
    t = t.replace('class="relative h-44 w-full">\n              <canvas id="indTransmissionDensityChart"', 'class="relative h-56 w-full">\n              <canvas id="indTransmissionDensityChart"')
    t = t.replace('class="relative h-52 w-full">\n              <canvas id="indRegionalSolarChart"', 'class="relative h-60 w-full">\n              <canvas id="indRegionalSolarChart"')
    t = t.replace('class="relative h-52 w-full">\n              <canvas id="indDppaTiersChart"', 'class="relative h-60 w-full">\n              <canvas id="indDppaTiersChart"')
    t = t.replace('class="relative h-56 w-full">\n              <canvas id="indArchetypeDemandRadarChart"', 'class="relative h-60 w-full">\n              <canvas id="indArchetypeDemandRadarChart"')
    t = t.replace('class="relative h-52 w-full">\n              <canvas id="indNetZeroTrajectoryChart"', 'class="relative h-60 w-full">\n              <canvas id="indNetZeroTrajectoryChart"')
    t = t.replace('class="relative h-52 w-full">\n              <canvas id="indCleanShareHistogramChart"', 'class="relative h-60 w-full">\n              <canvas id="indCleanShareHistogramChart"')
    t = t.replace('class="relative h-56 w-full">\n              <canvas id="indTopFlagshipHubsChart"', 'class="relative h-60 w-full">\n              <canvas id="indTopFlagshipHubsChart"')
    t = t.replace('class="relative h-52 w-full">\n              <canvas id="indProvinceDensityBarChart"', 'class="relative h-60 w-full">\n              <canvas id="indProvinceDensityBarChart"')

    with open(ind_path, "w", encoding="utf-8") as f:
        f.write(t)
    print("Updated industrial/index.html")

    # 3. RenewableVietNam/evcharging/index.html
    ev_path = os.path.join(base_dir, "evcharging", "index.html")
    with open(ev_path, "r", encoding="utf-8") as f:
        t = f.read()

    t = t.replace(
        "Authoritative registry of 22,055+ charging ports across Vietnam. Inspect DC fast charging hubs (up to 250 kW), AC destination points, and nationwide interprovincial highway corridors.",
        "22,055+ verified charging ports &middot; DC fast (up to 250 kW) &amp; expressway corridors."
    )
    t = t.replace(
        "Cross-referenced visual telemetry synthesizing 22,055 charging outlets across 63 provinces. Click any chart slice or bar to filter the directory table below.",
        "22,055 Outlets &middot; 63 Provinces &middot; Click to cross-filter."
    )
    t = t.replace(
        "High-power 180 kW and 250 kW CCS2 DC supercharging plazas stationed at 40-60 km intervals along core expressway corridors for continuous inter-city transit.",
        "180-250 kW CCS2 superchargers at 40-60 km intervals across core expressways."
    )
    t = t.replace(
        "Cao Bồ - Mai Sơn, Cam Lộ - La Sơn, Phan Thiết - Dầu Giây, Trung Lương - Mỹ Thuận plazas. Full coverage with 180kW/250kW dual-gun CCS2 superchargers.",
        "Cao Bồ - Mai Sơn, Cam Lộ - La Sơn, Phan Thiết - Dầu Giây, Trung Lương - Mỹ Thuận. 180kW/250kW dual-gun."
    )
    t = t.replace(
        "V52 Rest Stop and seaport logistics logistics charging plazas supporting heavy industrial EVs and passenger cross-gulf transit.",
        "V52 Rest Stop and seaport logistics charging plazas. 180kW fast charging."
    )
    t = t.replace(
        "Airport gateway corridor and maritime industrial ports with dense clusters of 250 kW liquid-cooled charging points.",
        "Airport gateway and seaport logistics corridor. 250 kW liquid-cooled points."
    )

    ev_card_replacements = [
        ("Visual 01 &middot; CPO Operator Mix", "CPO Operator Share"),
        ("Visual 02 &middot; Charging Power Velocity Mix", "Charging Power Velocity"),
        ("Visual 03 &middot; Top 10 Provinces by Plugs", "Top 10 Provinces by Outlets"),
        ("Visual 04 &middot; DC Fast Charging Density", "DC Fast Charging Density"),
        ("Visual 05 &middot; Connector Standard Distribution", "Connector Standards"),
        ("Visual 06 &middot; Grid Voltage Intertie Level", "Grid Voltage Interties"),
    ]
    for old_title, new_title in ev_card_replacements:
        t = t.replace(old_title, new_title)

    with open(ev_path, "w", encoding="utf-8") as f:
        f.write(t)
    print("Updated evcharging/index.html")

    # 4 & 5. RenewableVietNam/energy/index.html & projectenergy/index.html
    for energy_sub in ["energy", "projectenergy"]:
        en_path = os.path.join(base_dir, energy_sub, "index.html")
        with open(en_path, "r", encoding="utf-8") as f:
            t = f.read()

        t = t.replace(
            "National clean energy telemetry tracking 960 utility facilities against Decision 500/QĐ-TTg statutory mandates.",
            "960 utility facilities &middot; Decision 500/QĐ-TTg statutory targets."
        )
        t = t.replace(
            "Live geospatial topology visualizing North-South power wheeling corridors between Central/Southern renewable hubs and Northern load centers across 65,566 km of AC circuits and 1,915 substations.",
            "North-South 500kV wheeling &middot; 65,566 km circuits &middot; 1,915 substations."
        )
        t = t.replace(
            "Authoritative statutory fuel transition breakdown comparing Vietnam's active operational baseload against required pipeline capacity through 2030. Click any sector row or GIS action to filter corresponding spatial assets and dossier records in the cockpit below.",
            "PDP8 targets vs operational capacity &middot; Click row to filter GIS."
        )
        t = t.replace(
            "Simulated end-to-end power flow tracing primary energy supply transformation, transmission wheeling through the 500kV/220kV supergrid, and sectoral consumption sinks across Vietnam's phased decarbonization roadmap.",
            "Phased decarbonization power flow &middot; 500kV supergrid &middot; Sectoral sinks."
        )
        t = t.replace(
            "Real-time national dispatch balance telemetry, regional grid reserve margins, Vietnam Wholesale Electricity Market (VWEM) spot clearing rates, and Decree 80/2024 DPPA tariff schedules.",
            "VWEM spot clearing, reserve margins &middot; Decree 80 DPPA tariff schedules."
        )
        t = t.replace(
            "Interactive multi-fuel generation analytics across 960+ assets. Click any province bar or status slice to filter the table below.",
            "960+ utility assets &middot; Multi-fuel analytics &middot; Click to cross-filter."
        )
        t = t.replace("Click bar &rarr; Filter Table", "Operational &amp; Pipeline")
        t = t.replace("Click slice &rarr; Filter Table", "Decision 500 Milestones")

        with open(en_path, "w", encoding="utf-8") as f:
            f.write(t)
        print(f"Updated {energy_sub}/index.html")

    print("Terminal Diet successfully applied across all portals!")

if __name__ == "__main__":
    apply_terminal_diet()
