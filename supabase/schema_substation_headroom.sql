-- ==============================================================================
-- Vietnam National Substation Interconnection Headroom & DPPA Wheeling Schema
-- Platform: Renewable Viet Nam (renewablevietnam.com)
-- Target Database: Supabase PostgreSQL
-- ==============================================================================

-- 1. Substations & Interconnection Headroom Table
CREATE TABLE IF NOT EXISTS substations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    voltage_kv INT NOT NULL CHECK (voltage_kv IN (110, 220, 500)),
    province VARCHAR(100) NOT NULL,
    region VARCHAR(20) NOT NULL CHECK (region IN ('NORTH', 'CENTRAL', 'SOUTH')),
    latitude NUMERIC(10, 7) NOT NULL,
    longitude NUMERIC(10, 7) NOT NULL,
    transformer_mva NUMERIC(10, 2) NOT NULL,
    firm_capacity_mw NUMERIC(10, 2) NOT NULL,
    current_peak_mw NUMERIC(10, 2) NOT NULL,
    injection_headroom_mw NUMERIC(10, 2) NOT NULL,
    curtailment_risk_level VARCHAR(20) NOT NULL CHECK (curtailment_risk_level IN ('LOW', 'MODERATE', 'SEVERE')),
    dppa_clearance_status VARCHAR(30) NOT NULL CHECK (dppa_clearance_status IN ('OPEN_FOR_INJECTION', 'LIMITED_CAPACITY', 'CONGESTED')),
    evn_operator VARCHAR(50) NOT NULL, -- PTC1, PTC2, PTC3, PTC4, or Regional PC
    decision_500_upgrade_target VARCHAR(255),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indices for rapid geospatial & filter querying
CREATE INDEX IF NOT EXISTS idx_substations_voltage ON substations(voltage_kv);
CREATE INDEX IF NOT EXISTS idx_substations_region ON substations(region);
CREATE INDEX IF NOT EXISTS idx_substations_province ON substations(province);
CREATE INDEX IF NOT EXISTS idx_substations_clearance ON substations(dppa_clearance_status);

-- 2. DPPA Wheeling Corridors Table (Decree 80/2024 Implementation)
CREATE TABLE IF NOT EXISTS dppa_wheeling_corridors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    corridor_code VARCHAR(50) UNIQUE NOT NULL,
    corridor_name VARCHAR(255) NOT NULL,
    source_substation_id UUID REFERENCES substations(id) ON DELETE CASCADE,
    destination_substation_id UUID REFERENCES substations(id) ON DELETE CASCADE,
    source_region VARCHAR(20) NOT NULL,
    destination_region VARCHAR(20) NOT NULL,
    voltage_level_kv INT NOT NULL,
    transfer_capacity_mw NUMERIC(10, 2) NOT NULL,
    typical_losses_pct NUMERIC(4, 2) NOT NULL DEFAULT 2.50,
    evn_wheeling_fee_vnd_kwh NUMERIC(8, 2) NOT NULL,
    status VARCHAR(30) NOT NULL CHECK (status IN ('COMMISSIONED', 'EXPANDING_PDP8', 'PLANNED')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_corridors_source ON dppa_wheeling_corridors(source_substation_id);
CREATE INDEX IF NOT EXISTS idx_corridors_dest ON dppa_wheeling_corridors(destination_substation_id);

-- 3. Seed Reference Data for 500kV Supergrid Hubs
INSERT INTO substations (code, name, voltage_kv, province, region, latitude, longitude, transformer_mva, firm_capacity_mw, current_peak_mw, injection_headroom_mw, curtailment_risk_level, dppa_clearance_status, evn_operator, decision_500_upgrade_target)
VALUES
('SS-500-PHONOI', '500kV Phố Nối Substation', 500, 'Hưng Yên', 'NORTH', 20.9333, 106.0167, 1800.0, 1500.0, 1420.0, 80.0, 'MODERATE', 'LIMITED_CAPACITY', 'PTC1', 'Upgrade to 2x900MVA + 220kV intertie expansion'),
('SS-500-NHOQUAN', '500kV Nho Quan Substation', 500, 'Ninh Bình', 'NORTH', 20.3167, 105.7500, 1350.0, 1150.0, 980.0, 170.0, 'LOW', 'OPEN_FOR_INJECTION', 'PTC1', 'Circuit 3 terminal intertie commissioned 2024'),
('SS-500-PLEIKU', '500kV Pleiku Substation', 500, 'Gia Lai', 'CENTRAL', 13.9833, 108.0000, 1800.0, 1450.0, 1390.0, 60.0, 'SEVERE', 'CONGESTED', 'PTC3', 'Central Highlands renewable pooling bypass loop'),
('SS-500-DOCSOI', '500kV Dốc Sỏi Substation', 500, 'Quảng Ngãi', 'CENTRAL', 15.3167, 108.7000, 900.0, 750.0, 680.0, 70.0, 'MODERATE', 'LIMITED_CAPACITY', 'PTC2', 'Quảng Ngãi - Dung Quất industrial feed reinforcement'),
('SS-500-DILINH', '500kV Di Linh Substation', 500, 'Lâm Đồng', 'CENTRAL', 11.5333, 108.0500, 900.0, 750.0, 720.0, 30.0, 'SEVERE', 'CONGESTED', 'PTC3', 'South Central wind/solar evacuation node'),
('SS-500-TANDINH', '500kV Tân Định Substation', 500, 'Bình Dương', 'SOUTH', 11.1000, 106.6500, 1800.0, 1550.0, 1480.0, 70.0, 'MODERATE', 'LIMITED_CAPACITY', 'PTC4', 'Bình Dương industrial hub high-voltage absorption'),
('SS-500-CAUBONG', '500kV Cầu Bông Substation', 500, 'Hồ Chí Minh', 'SOUTH', 10.9667, 106.5167, 1800.0, 1600.0, 1350.0, 250.0, 'LOW', 'OPEN_FOR_INJECTION', 'PTC4', 'HCM City mega-load center primary gateway'),
('SS-500-THUANAU', '500kV Thuận Nam Substation', 500, 'Ninh Thuận', 'SOUTH', 11.4500, 108.9000, 1800.0, 1500.0, 1490.0, 10.0, 'SEVERE', 'CONGESTED', 'PTC3', 'Ninh Thuận concentrated solar/wind evacuation spine')
ON CONFLICT (code) DO NOTHING;
